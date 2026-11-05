#!/usr/bin/env python3
"""Archive closed agent run records out of the working tree (D-GOV-45).

Run records are history. A run folder (`<execution>/_Coordination/AgentRuns/<RUN>/`)
that no commit has touched for `--closed-days` is archived whole; in folders
still in use, binary evidence (traces, screenshots, archives, databases) that no
commit has touched for `--binary-days` is archived file by file. Archiving
removes the paths from the working tree only. Their exact bytes stay in Git
history at an immutable tag, and each AgentRuns directory carries
`ARCHIVE_INDEX.json`, which the governance tools use to resolve references
into archived records (tools/practitioner_harness/agent_runs_archive.py).

"Touched" means a commit on the checked-out history, by committer date, from
00:00 local time on the cutoff date, so the result depends only on `--as-of`.
Policy `containers` (e.g. Runtime's `AgentRuns/runtime/<runId>/`) hold one run
per child directory.

Paths listed in tools/agent_runs_archive_policy.json `keep` are never
archived: they are current governance inputs that happen to be filed in run
folders.

    python3 tools/archive_agent_runs.py                 # dry-run report
    python3 tools/archive_agent_runs.py --apply --tag archive/agent-runs-YYYY-MM-DD
    git show <tag>:<path>                               # read an archived file
    git restore --source=<tag> -- <path>                # bring a folder back
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path
import subprocess

REPO = Path(__file__).resolve().parents[1]
POLICY = REPO / 'tools' / 'agent_runs_archive_policy.json'
INDEX_NAME = 'ARCHIVE_INDEX.json'
INDEX_SCHEMA = 'chirality-agent-runs-archive-index/v1'


def git(*args: str) -> str:
    return subprocess.check_output(['git', '-C', str(REPO), *args], text=True)


def policy() -> dict:
    return json.loads(POLICY.read_text())


def touched_since(root: str, since: dt.date, ref: str) -> set[str]:
    out = git('log', ref, f'--since={since.isoformat()} 00:00:00', '--name-only', '--format=', '--', root)
    return {line for line in out.splitlines() if line}


def plan(as_of: dt.date, ref: str = 'HEAD') -> dict:
    rules = policy()
    keep = rules['keep']
    binary = tuple('.' + ext for ext in rules['binary_extensions'])
    runs, files = [], []
    for root in rules['roots']:
        tracked = [p for p in git('ls-tree', '-r', '--name-only', ref, '--', root).splitlines()]
        if not tracked:
            continue
        recent = touched_since(root, as_of - dt.timedelta(days=rules['closed_days']), ref)
        fresh_binaries = touched_since(root, as_of - dt.timedelta(days=rules['binary_days']), ref)
        by_run: dict[str, list[str]] = {}
        for path in tracked:
            parts = path[len(root) + 1:].split('/')
            depth = 2 if parts[0] in rules.get('containers', []) else 1
            if len(parts) > depth:  # files directly under AgentRuns or a container stay
                by_run.setdefault('/'.join([root, *parts[:depth]]), []).append(path)
        for run, paths in sorted(by_run.items()):
            kept = [p for p in paths if any(p == k or p.startswith(k.rstrip('/') + '/') for k in keep)]
            if not any(p in recent for p in paths) and not kept:
                runs.append(dict(path=run, files=len(paths)))
            else:
                files.extend(p for p in paths if p.endswith(binary) and p not in fresh_binaries and p not in kept)
    return dict(runs=runs, files=sorted(files))


def sizes(ref: str, paths: list[str]) -> int:
    total = 0
    for chunk in range(0, len(paths), 500):
        out = git('ls-tree', '-r', '-l', ref, '--', *paths[chunk:chunk + 500])
        total += sum(int(line.split()[3]) for line in out.splitlines() if line.split()[3] != '-')
    return total


def write_indexes(result: dict, tag: str, commit: str, as_of: dt.date) -> None:
    rules = policy()
    for root in rules['roots']:
        index_path = REPO / root / INDEX_NAME
        existing = json.loads(index_path.read_text()) if index_path.exists() else dict(
            schema=INDEX_SCHEMA, decision='D-GOV-45', tool='tools/archive_agent_runs.py', archives=[])
        runs = [r['path'] for r in result['runs'] if r['path'].startswith(root + '/')]
        files = [f for f in result['files'] if f.startswith(root + '/')]
        if not runs and not files:
            continue
        existing['archives'].append(dict(
            tag=tag, commit=commit, archived_on=as_of.isoformat(),
            rule=f"folders untouched {rules['closed_days']} days; binaries untouched {rules['binary_days']} days",
            runs=runs, files=files,
            restore=f'git restore --source={tag} -- <path>   |   git show {tag}:<path>'))
        index_path.parent.mkdir(parents=True, exist_ok=True)
        index_path.write_text(json.dumps(existing, indent=2) + '\n')
        write_readme(index_path.parent, existing)


def write_readme(directory: Path, index: dict) -> None:
    lines = ['# Archived run records', '',
             'Closed run records were moved out of the working tree under D-GOV-45',
             '(`docs/governance_harness/_DECISIONS/D-GOV-45_agent_run_record_archive.md`).',
             'Nothing was deleted: each archive tag holds the exact bytes, and',
             '`ARCHIVE_INDEX.json` lists every archived run folder and file.', '',
             'Read an archived file without restoring it:', '',
             '```bash', 'git show <tag>:<path>', '```', '',
             'Bring a run folder back temporarily for context (do not commit it unless the run is reopened):', '',
             '```bash', 'git restore --source=<tag> -- <path>', '```', '',
             '| Tag | Archived on | Run folders | Binary files |', '|---|---|---|---|']
    lines += [f"| `{a['tag']}` | {a['archived_on']} | {len(a['runs'])} | {len(a['files'])} |" for a in index['archives']]
    (directory / 'ARCHIVE.md').write_text('\n'.join(lines) + '\n')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--as-of', type=dt.date.fromisoformat, default=dt.date.today())
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('--tag', help='immutable tag holding the archived bytes (required with --apply)')
    args = parser.parse_args()
    result = plan(args.as_of)
    run_files = [p for r in result['runs'] for p in git('ls-files', '--', r['path']).splitlines()]
    report = dict(as_of=args.as_of.isoformat(), run_folders=len(result['runs']),
                  run_files=len(run_files), binary_files=len(result['files']),
                  mb=round(sizes('HEAD', run_files + result['files']) / 1e6, 1))
    print(json.dumps(report, indent=2))
    if not args.apply:
        return 0
    if not args.tag:
        parser.error('--apply requires --tag')
    commit = git('rev-parse', 'HEAD').strip()
    if git('status', '--porcelain', '--untracked-files=no').strip():
        parser.error('commit or stash tracked changes first: the tag must hold the exact archived bytes')
    subprocess.check_call(['git', '-C', str(REPO), 'tag', '-a', args.tag, commit, '-m',
                           f'Agent run records archived out of the working tree (D-GOV-45), as of {args.as_of}'])
    paths = [r['path'] for r in result['runs']] + result['files']
    for chunk in range(0, len(paths), 200):
        subprocess.check_call(['git', '-C', str(REPO), 'rm', '-r', '-q', '--', *paths[chunk:chunk + 200]])
    write_indexes(result, args.tag, commit, args.as_of)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

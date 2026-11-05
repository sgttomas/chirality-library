#!/usr/bin/env python3
"""Run the tools/ test suites affected by a change set.

Selection is delegated to the ratified selector
(tools/software_workflow/select_affected_checks.py) driven by the routing
profile tools/tools-test-routing.json: suites run when their inputs change;
unknown tool inputs conservatively run the full estate. The selection JSON (checks + per-check matched paths)
is printed before the run so every invocation records why each suite ran.

Change set = committed diff against --base (three-dot merge-base diff)
plus working-tree changes (staged, unstaged, untracked). If the base ref
cannot be resolved the script falls back to running everything — routing
must fail open, never silently skip.

Usage:
  python3 tools/run_affected_tests.py                 # vs origin/main
  python3 tools/run_affected_tests.py --base <ref>    # vs another ref
  python3 tools/run_affected_tests.py --all           # full estate
  python3 tools/run_affected_tests.py --dry-run       # selection only
  python3 tools/run_affected_tests.py --paths P [P..] # explicit change set
"""
from __future__ import annotations

import argparse
import json
import os
from fnmatch import fnmatchcase
import subprocess
import sys
from importlib.util import find_spec
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
PROFILE = REPO_ROOT / "tools" / "tools-test-routing.json"
SELECTOR = REPO_ROOT / "tools" / "software_workflow" / "select_affected_checks.py"


def _git(*args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(REPO_ROOT), *args],
        capture_output=True, text=True, check=True,
    ).stdout


def changed_paths(base: str) -> list[str] | None:
    """Committed + working-tree changed paths, or None if base is unusable."""
    try:
        # --no-renames: both halves of a rename select their suites, and Git
        # never reads deleted content for similarity (a blob-less CI clone
        # would otherwise download it, e.g. after a run-record archive).
        committed = _git("diff", "--name-only", "--no-renames", "-z", f"{base}...HEAD", "--")
    except subprocess.CalledProcessError:
        return None
    paths = set(filter(None, committed.split('\0')))
    paths.update(filter(None, _git('diff', '--name-only', '--no-renames', '-z', 'HEAD', '--').split('\0')))
    paths.update(filter(None, _git('ls-files', '--others', '--exclude-standard', '-z').split('\0')))
    return sorted(paths)


def load_profile() -> dict:
    return json.loads(PROFILE.read_text(encoding="utf-8"))


def select_checks(paths: list[str]) -> dict:
    profile = load_profile()
    if not paths:
        return {
            "schema": "chirality-affected-checks/v1",
            "paths": [],
            "checks": sorted(profile["always_checks"]),
            "reasons": {},
        }
    result = subprocess.run(
        [sys.executable, str(SELECTOR), str(PROFILE), "--paths-json-stdin"],
        input=json.dumps(paths), capture_output=True, text=True, check=True,
    )
    selected = json.loads(result.stdout)
    unknown = [p for p in paths if p.startswith('tools/') and not any(
        fnmatchcase(p, pattern) for rule in profile['path_rules'] for pattern in rule['paths'])]
    if unknown:
        selected['checks'] = sorted(profile['checks'])
        selected['reasons']['unknown-tool-inputs'] = unknown
    return selected


def pytest_dirs(check_ids: list[str]) -> list[str]:
    checks = load_profile()["checks"]
    dirs: list[str] = []
    for check_id in check_ids:
        dirs.extend(checks[check_id]["pytest_paths"])
    return sorted(set(dirs))


def run_pytest(dirs: list[str]) -> int:
    if not dirs:
        print('[run-affected] not selected: no tool inputs changed', flush=True)
        return 0
    cmd = [sys.executable, "-m", "pytest", "-q"]
    if find_spec("xdist") is not None:
        cmd += ["-n", "auto", "--dist", "loadscope"]
    cmd += dirs
    print(f"[run-affected] {' '.join(cmd)}", flush=True)
    return subprocess.run(cmd, cwd=REPO_ROOT).returncode


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--base", default="origin/main",
                        help="ref to diff against (default: origin/main)")
    parser.add_argument("--all", action="store_true",
                        help="run the full tools/ estate")
    parser.add_argument("--dry-run", action="store_true",
                        help="print the selection and exit without running")
    parser.add_argument("--paths", nargs="+", default=None,
                        help="explicit changed-path list (overrides git)")
    args = parser.parse_args()

    if args.all:
        selection = {"checks": sorted(load_profile()["checks"]),
                     "reasons": {"*": ["--all"]}, "paths": ["--all"]}
    else:
        paths = args.paths if args.paths is not None else changed_paths(args.base)
        if paths is None:
            print(f"[run-affected] base {args.base!r} not resolvable; "
                  "failing open to the full estate", flush=True)
            selection = {"checks": sorted(load_profile()["checks"]),
                         "reasons": {"*": ["base-unresolvable"]},
                         "paths": []}
        else:
            selection = select_checks(paths)

    print(json.dumps(selection, indent=2, sort_keys=True), flush=True)
    dirs = pytest_dirs(selection["checks"])
    skipped = sorted(set(load_profile()["checks"]) - set(selection["checks"]))
    print(f"[run-affected] running {len(selection['checks'])} suite(s); "
          f"skipping {len(skipped)}: {', '.join(skipped) or '(none)'}", flush=True)
    if os.getenv('GITHUB_OUTPUT'):
        with open(os.environ['GITHUB_OUTPUT'], 'a') as output:
            output.write(f"has_tests={'true' if dirs else 'false'}\n")
            instruction_inputs = any(p in ('--all','AGENTS.md','agents/registry.json') or p.startswith(('workflows/','agents/','tools/validation/')) for p in selection.get('paths', []))
            if selection.get('reasons', {}).get('*') == ['base-unresolvable']:
                instruction_inputs = True
            dependency_inputs = any(p == '--all' or p.endswith('/deliverable.yaml') or p.startswith('tools/deliverables/') or p == '.github/workflows/governance-harness.yml' for p in selection.get('paths', []))
            if selection.get('reasons', {}).get('*') == ['base-unresolvable']:
                dependency_inputs = True
            output.write(f"deliverables={'true' if dependency_inputs else 'false'}\n")
            output.write(f"instructions={'true' if instruction_inputs else 'false'}\n")
    if args.dry_run:
        return 0
    return run_pytest(dirs)


if __name__ == "__main__":
    raise SystemExit(main())

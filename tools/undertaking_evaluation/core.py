"""Inspect selected Git states and optional Codex response-usage observations.

No source is executed, no semantic outcome is inferred, and no network is used.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime
import hashlib
import html
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
from typing import Any

CASE_SCHEMA = "chirality-evaluation-case/v1"
REPORT_SCHEMA = "chirality-evaluation-report/v1"
COMPARISON_SCHEMA = "chirality-evaluation-comparison/v1"
TOKEN_FIELDS = ("input_tokens", "cached_input_tokens", "cache_write_input_tokens",
                "output_tokens", "reasoning_output_tokens", "total_tokens")
MAX_INPUT_BYTES = 256 * 1024 * 1024


class EvaluationError(ValueError):
    pass


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, ensure_ascii=False, allow_nan=False,
                      separators=(",", ":")).encode()


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise EvaluationError("Duplicate JSON keys are ambiguous")
        result[key] = value
    return result


def finite_float(value):
    number = float(value)
    if not math.isfinite(number):
        raise EvaluationError("Non-finite JSON values are unsupported")
    return number


def reject_constant(value):
    raise EvaluationError("Non-finite JSON values are unsupported")


def load_json(path: Path) -> tuple[dict, str]:
    try:
        if path.stat().st_size > MAX_INPUT_BYTES:
            raise EvaluationError("JSON input exceeds the supported size")
        raw = path.read_bytes()
        value = json.loads(raw, object_pairs_hook=unique_object, parse_constant=reject_constant, parse_float=finite_float)
        canonical(value)  # Reject unsupported Unicode/non-finite metadata before use.
    except (OSError, ValueError, UnicodeError, RecursionError) as exc:
        raise EvaluationError("Cannot read a valid JSON object from the selected input") from exc
    if not isinstance(value, dict):
        raise EvaluationError("Selected JSON input must be an object")
    return value, digest(raw)


def required_text(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise EvaluationError(f"{field} must be nonempty text")
    return value


def source_path(value: Any) -> str:
    value = required_text(value, "repository path")
    p = PurePosixPath(value)
    if p.is_absolute() or ".." in p.parts or "\\" in value or "\x00" in value:
        raise EvaluationError("Repository paths must be relative and contained")
    if value.startswith(":") or value.startswith("-"):
        raise EvaluationError("Repository path must be literal, not an option or pathspec")
    return p.as_posix()


def git_environment() -> dict:
    # The selected repository, not caller Git overrides or replacement objects,
    # supplies the immutable source. No network/authentication operation is used.
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    env.update(GIT_LITERAL_PATHSPECS="1", GIT_OPTIONAL_LOCKS="0", GIT_NO_REPLACE_OBJECTS="1")
    return env


def git(repo: Path, *args: str) -> bytes:
    env = git_environment()
    # Error bodies can contain private host paths or Git configuration: do not echo them.
    proc = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, env=env)
    if proc.returncode:
        raise EvaluationError("Selected Git source or operation is unavailable")
    return proc.stdout


def commit(repo: Path, ref: Any) -> str:
    ref = required_text(ref, "revision")
    if not re.fullmatch(r"[0-9a-fA-F]{40}|[0-9a-fA-F]{64}", ref):
        raise EvaluationError("Revisions must be full immutable Git commit IDs")
    return git(repo, "rev-parse", "--verify", "--end-of-options", ref + "^{commit}").decode().strip()


def tree_entries(repo: Path, rev: str, paths: list[str]) -> dict[str, dict]:
    raw = git(repo, "ls-tree", "-rz", "--full-tree", rev, "--", *paths)
    entries = {}
    try:
        for item in raw.split(b"\x00"):
            if not item:
                continue
            meta, name = item.split(b"\t", 1)
            mode, kind, oid = meta.decode("ascii").split()
            path = name.decode("utf-8")
            entries[path] = {"mode": mode, "kind": kind, "git_object": oid}
    except (ValueError, UnicodeError) as exc:
        raise EvaluationError("Unsupported Git tree representation or non-UTF-8 path") from exc
    return entries


def state_comparison(repo: Path, before: str, after: str, paths: list[str]) -> dict:
    a, b = tree_entries(repo, before, paths), tree_entries(repo, after, paths)
    for selected in paths:
        if not any(selected == "." or name == selected or name.startswith(selected + "/")
                   for name in set(a) | set(b)):
            raise EvaluationError("A selected path exists in neither repository state")
    changes = []
    for path in sorted(set(a) | set(b)):
        x, y = a.get(path), b.get(path)
        state = "added" if x is None else "removed" if y is None else "unchanged" if x == y else "modified"
        changes.append({"path": path, "change": state, "before": x, "after": y})
    return {"before_commit": before, "after_commit": after,
            "before_tree": git(repo, "rev-parse", before + "^{tree}").decode().strip(),
            "after_tree": git(repo, "rev-parse", after + "^{tree}").decode().strip(),
            "selected_paths": paths, "files": changes,
            "counts": dict(Counter(x["change"] for x in changes)),
            "coverage": "Committed selected paths only; working/untracked files and external state excluded. Renames appear as removal/addition.",
            "meaning": "Source object changes do not establish behavior, fulfillment, improvement or cause."}


def timestamp(value: Any) -> datetime:
    value = required_text(value, "event timestamp")
    try:
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if result.tzinfo is None:
            raise ValueError()
        return result
    except ValueError as exc:
        raise EvaluationError("Event timestamps must include a timezone") from exc


def codex_usage(path: Path, turn_ids: list[str]) -> dict:
    """Only per-response token_usage_record; never sum cumulative/token_count records."""
    if not isinstance(turn_ids, list) or not turn_ids or any(not isinstance(x, str) or not x for x in turn_ids):
        raise EvaluationError("Codex import requires explicit nonempty turn_ids")
    wanted = set(turn_ids)
    seen, found, problems, times = {}, set(), [], []
    ignored = duplicates = selected_rows = 0
    sha = hashlib.sha256()
    try:
        initial_stat = path.stat()
        if initial_stat.st_size > MAX_INPUT_BYTES:
            raise EvaluationError("Trace input exceeds the supported size")
        with path.open("rb") as stream:
            for number, raw in enumerate(stream, 1):
                sha.update(raw)
                try:
                    row = json.loads(raw, object_pairs_hook=unique_object, parse_constant=reject_constant, parse_float=finite_float)
                    if not isinstance(row, dict):
                        raise ValueError()
                except (ValueError, UnicodeError, RecursionError):
                    problems.append({"line": number, "issue": "unreadable record; scope and coverage unknown"})
                    continue
                if row.get("type") != "token_usage_record":
                    ignored += 1
                    continue
                p = row.get("payload")
                if not isinstance(p, dict):
                    problems.append({"line": number, "issue": "usage record has no readable payload; coverage unknown"})
                    continue
                if not isinstance(p.get("turn_id"), str):
                    problems.append({"line": number, "issue": "usage turn identity malformed; selection coverage unknown"})
                    continue
                if p.get("turn_id") not in wanted:
                    continue
                selected_rows += 1
                found.add(p["turn_id"])
                rid, usage = p.get("response_id"), p.get("usage")
                if not isinstance(rid, str) or not rid or not isinstance(usage, dict):
                    problems.append({"line": number, "issue": "selected usage lacks response identity or usage object"})
                    continue
                values = {}
                invalid = False
                for field in TOKEN_FIELDS:
                    value = usage.get(field)
                    if value is not None and (type(value) is not int or value < 0):
                        invalid = True
                    values[field] = value
                if invalid:
                    problems.append({"line": number, "issue": "selected usage has invalid token values"})
                    continue
                identity = (p["turn_id"], values)
                if rid in seen:
                    if seen[rid] != identity:
                        raise EvaluationError("Conflicting duplicate response usage; no aggregate produced")
                    duplicates += 1
                    continue
                seen[rid] = identity
                try:
                    times.append(timestamp(row.get("timestamp")))
                except EvaluationError:
                    problems.append({"line": number, "issue": "selected response timestamp unavailable"})
    except OSError as exc:
        raise EvaluationError("Selected trace is unreadable") from exc
    final_stat = path.stat()
    if (initial_stat.st_size, initial_stat.st_mtime_ns) != (final_stat.st_size, final_stat.st_mtime_ns):
        raise EvaluationError("Trace changed while being read; freeze a copy before inspection")
    metrics = {}
    for field in TOKEN_FIELDS:
        values = [u[field] for _, u in seen.values() if u[field] is not None]
        metrics[field] = {"observed_sum": sum(values) if values else None,
                          "records_with_value": len(values),
                          "complete_for_imported_responses": bool(seen) and len(values) == len(seen)}
    return {"adapter": "codex-jsonl-token-usage-record/v1", "source_sha256": sha.hexdigest(),
            "selection": {"turn_identity_sha256": [digest(x.encode()) for x in sorted(wanted)],
                          "requested_turns": len(wanted), "turns_with_usage": len(found)},
            "imported_responses": len(seen), "selected_usage_records": selected_rows,
            "duplicate_records_ignored": duplicates, "other_records_ignored": ignored,
            "observations": metrics, "issues": problems,
            "coverage": "Partial observation: only selected-turn per-response usage in this file; no guarantee of all responses, workers or attempts.",
            "missing_requested_turns": len(wanted - found),
            "observed_response_span_seconds": (max(times) - min(times)).total_seconds() if len(times) > 1 else None,
            "elapsed_work_seconds": None, "cost": None, "human_attention_seconds": None,
            "limits": ["Token categories retain host semantics and may overlap; cached/reasoning categories are not added to total_tokens.",
                       "Cumulative turn/thread counters and token_count events are ignored.",
                       "Response observation span is not active work or undertaking duration.",
                       "Retries, causal attribution and provider billing are not inferred. Raw messages/tool output are not copied."]}


def inspect_case(case_file: Path, repo: Path) -> tuple[dict, list[Path]]:
    case, case_hash = load_json(case_file)
    if case.get("schema") != CASE_SCHEMA:
        raise EvaluationError("Unsupported case schema")
    for key in ("case_id", "trial_id", "question", "examination_basis", "environment"):
        required_text(case.get(key), key)
    if case.get("hypothesis") is not None:
        required_text(case["hypothesis"], "hypothesis")
    if not isinstance(case.get("conditions"), list) or not case["conditions"] or any(not isinstance(x, str) or not x.strip() for x in case["conditions"]):
        raise EvaluationError("conditions must be a nonempty text list")
    if not isinstance(case.get("resource_budget"), dict) or not case["resource_budget"]:
        raise EvaluationError("resource_budget must explicitly declare resource conditions")
    if not isinstance(case.get("configuration", {}), dict):
        raise EvaluationError("configuration must be an object")
    paths = case.get("paths")
    if not isinstance(paths, list) or not paths:
        raise EvaluationError("paths must select at least one repository location")
    paths = sorted(set(source_path(x) for x in paths))
    repo = Path(git(repo, "rev-parse", "--show-toplevel").decode().strip()).resolve()
    before, after = commit(repo, case.get("before")), commit(repo, case.get("after"))
    outcome = case.get("outcome")
    if not isinstance(outcome, dict) or outcome.get("status") not in ("established", "not_established", "unknown"):
        raise EvaluationError("outcome requires an explicit supported status")
    required_text(outcome.get("summary"), "outcome.summary")
    evidence = outcome.get("evidence", [])
    if not isinstance(evidence, list) or (outcome["status"] != "unknown" and not evidence):
        raise EvaluationError("Non-unknown supplied outcomes require evidence bindings")
    protected = [case_file.resolve(), repo.resolve()]
    bound = []
    for item in evidence:
        if not isinstance(item, dict):
            raise EvaluationError("Each evidence binding must be an object")
        required_text(item.get("claim"), "evidence.claim")
        if item.get("kind") == "git":
            rev = commit(repo, item.get("revision")); path = source_path(item.get("path"))
            if git(repo, "cat-file", "-t", rev + ":" + path).strip() != b"blob":
                raise EvaluationError("Git evidence must identify a file blob")
            raw = git(repo, "show", rev + ":" + path)
            bound.append({"kind": "git", "revision": rev, "path": path, "sha256": digest(raw), "claim": item["claim"]})
        elif item.get("kind") == "file":
            path = (case_file.parent / required_text(item.get("path"), "evidence.path")).resolve()
            try:
                if path.stat().st_size > MAX_INPUT_BYTES:
                    raise EvaluationError("Evidence input exceeds supported size")
                raw = path.read_bytes()
            except OSError as exc:
                raise EvaluationError("Selected evidence is unavailable") from exc
            protected.append(path)
            bound.append({"kind": "file", "sha256": digest(raw), "claim": item["claim"]})
        else:
            raise EvaluationError("Evidence kind must be git or file")
    trace = None
    if case.get("codex_jsonl") is not None:
        spec = case["codex_jsonl"]
        if not isinstance(spec, dict):
            raise EvaluationError("codex_jsonl must be an object")
        path = (case_file.parent / required_text(spec.get("path"), "codex_jsonl.path")).resolve()
        protected.append(path)
        trace = codex_usage(path, spec.get("turn_ids"))
    basis = {"case_id": case["case_id"], "question": case["question"], "before_commit": before, "paths": paths,
             "conditions": case["conditions"], "examination_basis": case["examination_basis"],
             "environment": case["environment"], "resource_budget": case["resource_budget"]}
    report = {"schema": REPORT_SCHEMA, "case_source_sha256": case_hash,
              "case_id": case["case_id"], "trial_id": case["trial_id"],
              "question": case["question"], "hypothesis": case.get("hypothesis"),
              "conditions": case["conditions"], "configuration": case.get("configuration", {}),
              "comparison_basis": basis, "comparison_basis_sha256": digest(canonical(basis)),
              "repository": state_comparison(repo, before, after, paths),
              "supplied_assessment": {"status": outcome["status"], "summary": outcome["summary"], "evidence": bound,
                  "standing": "Supplied assessment; the tool bound evidence bytes, but did not verify its meaning or decide acceptance."},
              "effort": trace,
              "limits": ["Local/private analysis output; not cleared for publication.",
                         "Only explicit selected committed paths are observed; no automatic complete project state claim.",
                         "The tool does not judge whether the state change justifies effort or automatically adopt a method."]}
    return report, protected


def full_hash(value: Any, label: str, lengths=(40, 64)) -> str:
    if not isinstance(value, str) or len(value) not in lengths or not re.fullmatch(r"[0-9a-f]+", value):
        raise EvaluationError(f"Invalid {label} identity")
    return value


def nonnegative(value: Any, label: str) -> int:
    if type(value) is not int or value < 0:
        raise EvaluationError(f"Invalid {label} count")
    return value


def validate_report(item: dict) -> None:
    if item.get("schema") != REPORT_SCHEMA:
        raise EvaluationError("Comparison inputs must be inspect reports")
    for key in ("case_id", "trial_id", "question"):
        required_text(item.get(key), key)
    full_hash(item.get("case_source_sha256"), "case source", (64,))
    if item.get("hypothesis") is not None:
        required_text(item["hypothesis"], "hypothesis")
    if not isinstance(item.get("configuration"), dict):
        raise EvaluationError("Report configuration must be an object")
    basis = item.get("comparison_basis")
    keys = {"case_id", "question", "before_commit", "paths", "conditions", "examination_basis", "environment", "resource_budget"}
    if not isinstance(basis, dict) or set(basis) != keys:
        raise EvaluationError("Incomplete comparison basis")
    for key in ("case_id", "question", "examination_basis", "environment"):
        required_text(basis[key], key)
    for key in ("case_id", "question", "conditions"):
        if basis[key] != item.get(key):
            raise EvaluationError("Report and comparison basis disagree")
    if not isinstance(basis["conditions"], list) or not basis["conditions"]:
        raise EvaluationError("Comparison conditions must be a nonempty list")
    for condition in basis["conditions"]:
        required_text(condition, "condition")
    if not isinstance(basis["resource_budget"], dict) or not basis["resource_budget"]:
        raise EvaluationError("Resource conditions are missing")
    paths = basis["paths"]
    if not isinstance(paths, list) or not paths or paths != sorted(set(source_path(p) for p in paths)):
        raise EvaluationError("Comparison paths must be normalized, unique and ordered")
    full_hash(basis["before_commit"], "starting commit")
    if item.get("comparison_basis_sha256") != digest(canonical(basis)):
        raise EvaluationError("Comparison basis digest mismatch")
    repo = item.get("repository")
    if not isinstance(repo, dict) or repo.get("before_commit") != basis["before_commit"] or repo.get("selected_paths") != paths:
        raise EvaluationError("Repository observations disagree with comparison basis")
    for key in ("before_commit", "after_commit", "before_tree", "after_tree"):
        full_hash(repo.get(key), key)
    files = repo.get("files")
    if not isinstance(files, list):
        raise EvaluationError("Repository file observations missing")
    names, counts = set(), Counter()
    for f in files:
        if not isinstance(f, dict):
            raise EvaluationError("Invalid repository file observation")
        path = source_path(f.get("path"))
        if path in names or not any(p == "." or p == path or path.startswith(p + "/") for p in paths):
            raise EvaluationError("Duplicate or out-of-selection file observation")
        names.add(path)
        a, b = f.get("before"), f.get("after")
        for value in (a, b):
            if value is not None:
                if not isinstance(value, dict) or value.get("kind") not in ("blob", "commit") or not re.fullmatch(r"[0-7]{6}", str(value.get("mode", ""))):
                    raise EvaluationError("Invalid Git object observation")
                full_hash(value.get("git_object"), "Git object")
        if a is None and b is None:
            raise EvaluationError("File observation has neither state")
        change = "added" if a is None else "removed" if b is None else "unchanged" if a == b else "modified"
        if f.get("change") != change:
            raise EvaluationError("File change disagrees with object observations")
        counts[change] += 1
    if not isinstance(repo.get("counts"), dict):
        raise EvaluationError("Repository counts missing")
    for value in repo["counts"].values():
        nonnegative(value, "repository file")
    if dict(counts) != repo.get("counts"):
        raise EvaluationError("Repository counts disagree with file observations")
    outcome = item.get("supplied_assessment")
    if not isinstance(outcome, dict) or outcome.get("status") not in ("established", "not_established", "unknown"):
        raise EvaluationError("Supplied assessment missing or invalid")
    required_text(outcome.get("summary"), "assessment summary")
    evidence = outcome.get("evidence")
    if not isinstance(evidence, list) or (outcome["status"] != "unknown" and not evidence):
        raise EvaluationError("Assessment evidence bindings missing")
    for e in evidence:
        if not isinstance(e, dict) or e.get("kind") not in ("git", "file"):
            raise EvaluationError("Invalid evidence binding")
        full_hash(e.get("sha256"), "evidence", (64,));required_text(e.get("claim"), "evidence claim")
        if e["kind"] == "git":
            full_hash(e.get("revision"), "evidence commit");source_path(e.get("path"))
    effort = item.get("effort")
    if effort is not None:
        if not isinstance(effort, dict) or effort.get("adapter") != "codex-jsonl-token-usage-record/v1":
            raise EvaluationError("Unsupported effort observation")
        full_hash(effort.get("source_sha256"), "trace", (64,))
        n = nonnegative(effort.get("imported_responses"), "imported response")
        observations = effort.get("observations")
        if not isinstance(observations, dict) or set(observations) != set(TOKEN_FIELDS):
            raise EvaluationError("Effort field coverage is incomplete")
        for field, obs in observations.items():
            if not isinstance(obs, dict):
                raise EvaluationError("Invalid effort field")
            k = nonnegative(obs.get("records_with_value"), "field coverage")
            if k > n or type(obs.get("complete_for_imported_responses")) is not bool or obs["complete_for_imported_responses"] != (n > 0 and k == n):
                raise EvaluationError("Contradictory effort coverage")
            if k == 0:
                if obs.get("observed_sum") is not None:
                    raise EvaluationError("Missing observations cannot supply a sum")
            else:
                nonnegative(obs.get("observed_sum"), "observed usage")


def compare_reports(a_file: Path, b_file: Path) -> tuple[dict, list[Path]]:
    a, ah = load_json(a_file); b, bh = load_json(b_file)
    for item in (a, b):
        validate_report(item)
    mismatches = sorted(k for k in set(a["comparison_basis"]) | set(b["comparison_basis"])
                        if a["comparison_basis"].get(k) != b["comparison_basis"].get(k))
    if a.get("trial_id") == b.get("trial_id"):
        mismatches.append("distinct_trial_identity")
    deltas = {}
    ae, be = a.get("effort"), b.get("effort")
    if isinstance(ae, dict) and isinstance(be, dict):
        for key in TOKEN_FIELDS:
            av = ae.get("observations", {}).get(key, {}).get("observed_sum")
            bv = be.get("observations", {}).get(key, {}).get("observed_sum")
            deltas[key] = bv - av if type(av) is int and type(bv) is int else None
    return {"schema": COMPARISON_SCHEMA,
            "status": "declared_basis_matches" if not mismatches else "comparison_limited",
            "basis_differences": mismatches, "baseline_report_sha256": ah, "variant_report_sha256": bh,
            "baseline": a, "variant": b, "variant_minus_baseline_observed_tokens": deltas,
            "limits": ["Matching declared conditions are necessary metadata, not proof of experimental control or causation.",
                       "Token deltas compare partial observations only; differing trace coverage can invalidate their interpretation.",
                       "No automatic winner, quality score, statistical significance or acceptance is inferred."]}, [a_file.resolve(), b_file.resolve()]


def render_html(report: dict) -> str:
    # All case/source material is text, never executable markup or remote assets.
    esc = lambda x: html.escape(str(x), quote=True)
    title = "Repository change evaluation" if report["schema"] == REPORT_SCHEMA else "Evaluation comparison"
    rows = []
    if report["schema"] == REPORT_SCHEMA:
        rows = [f'<tr><td>{esc(x["path"])}</td><td>{esc(x["change"])}</td></tr>' for x in report["repository"]["files"]]
        main = f'<h2>{esc(report["question"])}</h2><p>{esc(report["hypothesis"] or "No intervention hypothesis selected")}</p><h2>Selected repository changes</h2><table><tr><th>Path</th><th>Observation</th></tr>{"".join(rows)}</table><h2>Supplied outcome assessment</h2><p>{esc(report["supplied_assessment"]["summary"])}</p><p>{esc(report["supplied_assessment"]["standing"])}</p>'
    else:
        main = f'<h2>{esc(report["status"])}</h2><p>Declared basis differences: {esc(", ".join(report["basis_differences"]) or "none")}</p>'
    return f'<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="Content-Security-Policy" content="default-src \'none\'; style-src \'unsafe-inline\'"><title>{title}</title><style>body{{font:18px/1.5 system-ui;margin:40px auto;max-width:1000px;padding:0 24px;color:#172015}}table{{border-collapse:collapse;width:100%}}td,th{{border-bottom:1px solid #aaa;text-align:left;padding:10px}}pre{{white-space:pre-wrap;overflow-wrap:anywhere;background:#f0f3ed;padding:20px}}small{{color:#485640}}</style><h1>{title}</h1><small>Local analysis · source observations and supplied assessments remain distinct</small>{main}<h2>Limits</h2><ul>{"".join("<li>"+esc(x)+"</li>" for x in report["limits"])}</ul><details><summary>Complete inspectable data</summary><pre>{esc(json.dumps(report,indent=2,ensure_ascii=False))}</pre></details></html>'


def write_report(output: Path, report: dict, protected: list[Path]) -> None:
    lexical = Path(os.path.abspath(output))
    if any(p.is_symlink() for p in [lexical, *lexical.parents]):
        raise EvaluationError("Output path must not traverse symlinks")
    target = lexical.resolve()
    for path in protected:
        path = path.resolve()
        if target == path or target in path.parents or (path.is_dir() and path in target.parents):
            raise EvaluationError("Output must be separate from source inputs and repository")
    if target.exists():
        raise EvaluationError("Output directory already exists; choose a new destination")
    if not target.parent.is_dir():
        raise EvaluationError("Output parent directory must already exist")
    inside = subprocess.run(["git", "-C", str(target.parent), "rev-parse", "--is-inside-work-tree"], capture_output=True, env=git_environment())
    if inside.returncode == 0 and inside.stdout.strip() == b"true":
        raise EvaluationError("Analysis outputs must stay outside Git working trees; publish only separately cleared material")
    # Informational discovery only. Never dereference these strings or turn them
    # into active links; the original input remains under the caller's custody.
    sources = [("case", protected[0], report["case_source_sha256"])] if report["schema"] == REPORT_SCHEMA else [
        ("baseline_report", protected[0], report["baseline_report_sha256"]),
        ("variant_report", protected[1], report["variant_report_sha256"])]
    report = {**report, "input_locators": [
        {"kind": kind, "relative_path": os.path.relpath(path, target), "sha256": source_hash,
         "relative_to": "Directory of the original report.json containing this locator; for embedded reports, open that original report first.",
         "standing": "Informational private input location, not a link, command or authorization."}
        for kind, path, source_hash in sources]}
    raw = json.dumps(report, indent=2, ensure_ascii=False, allow_nan=False) + "\n"
    markup = render_html(report)
    try:
        target.mkdir(mode=0o700)
        for name, contents in [("report.json", raw), ("report.html", markup)]:
            with (target / name).open("x", encoding="utf-8") as stream:
                stream.write(contents)
            (target / name).chmod(0o600)
    except OSError as exc:
        raise EvaluationError("Cannot complete report write; inspect the selected destination before retrying") from exc


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subs = parser.add_subparsers(dest="command", required=True)
    inspect = subs.add_parser("inspect")
    inspect.add_argument("--case", type=Path, required=True)
    inspect.add_argument("--repo", type=Path, required=True)
    inspect.add_argument("--output", type=Path, required=True)
    compare = subs.add_parser("compare")
    compare.add_argument("--baseline", type=Path, required=True)
    compare.add_argument("--variant", type=Path, required=True)
    compare.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        report, protected = inspect_case(args.case, args.repo) if args.command == "inspect" else compare_reports(args.baseline, args.variant)
        write_report(args.output, report, protected)
        print(json.dumps({"status": "written", "files": ["report.json", "report.html"], "schema": report["schema"]}))
        return 0
    except (EvaluationError, OSError) as exc:
        print(json.dumps({"status": "failed", "reason": str(exc) if isinstance(exc, EvaluationError) else "Local operation unavailable"}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

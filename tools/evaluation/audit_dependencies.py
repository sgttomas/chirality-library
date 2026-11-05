#!/usr/bin/env python3
"""Read-only native DEL dependency audit; observations do not establish readiness."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from audit_common import TOOLS, report_base, require_root, write_report


def audit(project):
    """Report the native check query without maintaining another dependency parser or graph."""
    project = require_root(project)
    result = report_base(project)
    result.update(schema_version=2, assessment="native DEL metadata structure and reference presence only")
    process = subprocess.run(
        [sys.executable, str(TOOLS / "deliverables/cli.py"), "--project", str(project), "check"],
        cwd=project, capture_output=True, text=True,
    )
    try:
        query = json.loads(process.stdout)
    except (json.JSONDecodeError, UnicodeError) as exc:
        raise ValueError("native deliverable check did not return JSON: " +
                         (process.stderr.strip() or str(exc))) from exc
    if not isinstance(query, dict) or not isinstance(query.get("errors"), list):
        raise ValueError("native deliverable check returned an invalid report")
    result["query"] = query
    result["issues"] = list(query["errors"])
    # Native check reports partial, structurally invalid metadata with a basis
    # and exit 2. Missing Git/HEAD/project inputs have no basis and are failed
    # observations; no fallback parser silently changes the query semantics.
    if process.returncode not in (0, 2) or "basis" not in query:
        result["run_status"] = "FAILED_INPUTS"
        if not result["issues"]:
            result["issues"].append(process.stderr.strip() or "native deliverable check could not establish its input basis")
        return result
    result["summary"] = {
        "deliverables": query["deliverables"],
        "needs": len(query["needs"]),
        "unknown_references": len(query["unknown"]),
        "native_cycle_components": len(query["cycles"]),
    }
    result["subject_status"] = "FAIL" if result["issues"] else "PASS" if query["deliverables"] else "NOT_ASSESSED"
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True, type=Path,
                        help="project root containing execution localities; document/evidence paths are relative to it")
    parser.add_argument("--output", required=True, help="JSON report path, or - for stdout")
    args = parser.parse_args(argv)
    try:
        report = audit(args.project)
    except (OSError, ValueError) as exc:
        report = report_base(args.project)
        report.update(schema_version=2, run_status="FAILED_INPUTS", issues=[str(exc)])
    try:
        write_report(report, args.output)
    except (OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    return 0 if report["run_status"] == "COMPLETE" else 2


if __name__ == "__main__":
    sys.exit(main())

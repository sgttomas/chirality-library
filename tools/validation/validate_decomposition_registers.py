#!/usr/bin/env python3
"""Read-only cross-check of decomposition companion registers (XRG).

Checks Deliverables.csv, ScopeLedger.csv and optional ContextBudgetQA.csv under
EXECUTION_ROOT/_Decomposition, or --registers-dir. Every scope item has one
Package home; supporting deliverables may belong to other Packages. Retains the
XRG check codes and scope/objective/context assertions. Dependency declarations,
locality layout and lifecycle are outside this validator: query consumer-local
needs with tools.deliverables. No input is modified.

Exit 0: no errors (or warnings with --strict); 1: findings; 2: unusable input.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
from pathlib import Path

ERROR = "ERROR"
WARNING = "WARNING"
FAMILIES = ("XRG",)

CHECKS: dict[str, tuple[str, str, str]] = {
    # code: (family, default severity, description)
    "XRG-001": ("XRG", ERROR, "ScopeLedger DeliverableIDs names a deliverable absent from Deliverables.csv"),
    "XRG-002": ("XRG", ERROR, "Deliverables CoversScopeItems names a scope item absent from ScopeLedger.csv"),
    "XRG-003": ("XRG", ERROR, "Scope-coverage link is non-reciprocal between ScopeLedger.csv and Deliverables.csv"),
    "XRG-004": ("XRG", WARNING, "Ledger item's home Package holds none of its linked deliverables (supporting deliverables in other Packages are allowed)"),
    "XRG-005": ("XRG", ERROR, "Scope item's ObjectiveIDs are not propagated to the covering deliverable's SupportsObjectives"),
    "XRG-006": ("XRG", WARNING, "IN-scope ledger item has no DeliverableIDs"),
    "XRG-007": ("XRG", ERROR, "Non-IN ledger item carries DeliverableIDs"),
    "XRG-008": ("XRG", WARNING, "Deliverables.csv row has a blank PhaseHint"),
    "XRG-009": ("XRG", ERROR, "ContextBudgetQA.csv and Deliverables.csv cover different deliverable sets"),
    "XRG-010": ("XRG", ERROR, "ContextEnvelope disagrees between ContextBudgetQA.csv and Deliverables.csv"),
    "XRG-011": ("XRG", ERROR, "IN-scope ledger item has no PackageID"),
    # XRG-012 (D-GOV-47: WARNING when an OUT/TBD item carried a PackageID) is
    # retired by D-GOV-48 and not reused; an OUT/TBD item with a PackageID now
    # conforms, and XRG-013 reports the opposite case.
    "XRG-013": ("XRG", WARNING, "OUT or TBD ledger item has no PackageID (D-GOV-48: every scope item has one Package home)"),
    "XRG-014": ("XRG", ERROR, "Ledger item names more than one PackageID (D-GOV-48: exactly one Package home)"),
    "XRG-015": ("XRG", WARNING, "Ledger item's PackageID names no Package found in Deliverables.csv"),
}

class OperationalError(Exception):
    """Input could not be read or the invocation is unusable."""


def split_list(value: str | None) -> list[str]:
    """Split a semicolon- or comma-delimited register cell into tokens."""
    return [token.strip() for token in re.split(r"[;,]", value or "") if token.strip()]


def read_register(path: Path) -> list[dict[str, str]]:
    try:
        with path.open(newline="", encoding="utf-8-sig") as handle:
            return [
                {(k or "").strip().lstrip("﻿"): (v or "") for k, v in row.items()}
                for row in csv.DictReader(handle)
            ]
    except FileNotFoundError as exc:
        raise OperationalError(f"register not found: {path}") from exc
    except (csv.Error, UnicodeDecodeError) as exc:
        raise OperationalError(f"register unreadable: {path}: {exc}") from exc
    except OSError as exc:
        # PermissionError, IsADirectoryError, and every other OS-level failure
        # are operational (exit 2), not register findings (exit 1).
        raise OperationalError(f"register unreadable: {path}: {exc}") from exc


class Finding:
    __slots__ = ("code", "family", "severity", "path", "line", "row_id", "row_class", "detail")

    def __init__(self, code, path, detail, line=None, row_id=None, row_class=None,
                 severity=None):
        family, default_severity, _ = CHECKS[code]
        self.code = code
        self.family = family
        self.severity = severity or default_severity
        self.path = path
        self.line = line
        self.row_id = row_id
        self.row_class = row_class
        self.detail = detail

    def as_dict(self) -> dict:
        return {
            "code": self.code,
            "family": self.family,
            "severity": self.severity,
            "path": self.path,
            "line": self.line,
            "row_id": self.row_id,
            "row_class": self.row_class,
            "detail": self.detail,
        }


def check_cross_register(
    deliverables: dict[str, dict[str, str]],
    ledger: list[dict[str, str]],
    context_qa: list[dict[str, str]] | None,
    paths: dict[str, str],
    findings: list[Finding],
) -> None:
    """XRG family — the companion registers against each other."""
    known_packages = {
        (record.get("PackageID") or "").strip()
        for record in deliverables.values()
        if (record.get("PackageID") or "").strip()
    }
    for item in ledger:
        item_id = (item.get("ScopeItemID") or "").strip()
        status = (item.get("InOutStatus") or "").strip().upper()
        linked = split_list(item.get("DeliverableIDs"))
        objectives = split_list(item.get("ObjectiveIDs"))
        ledger_pkg = (item.get("PackageID") or "").strip()

        if status == "IN" and not linked:
            findings.append(
                Finding("XRG-006", paths["ledger"],
                        f"IN-scope item {item_id} has no covering deliverable", row_id=item_id)
            )
        if status and status != "IN" and linked:
            findings.append(
                Finding("XRG-007", paths["ledger"],
                        f"{status} item {item_id} names deliverables {', '.join(linked)}",
                        row_id=item_id)
            )
        # Package home (D-GOV-48): every scope item, IN, OUT or TBD, has exactly
        # one Package. Only IN items map to Deliverables; an OUT or TBD item's
        # home is for accountability and traceability. A missing home is an
        # error on an IN item and a warning on an OUT or TBD item, since
        # decompositions adopted under D-GOV-47 left those blank. Checked only
        # when the ledger carries a PackageID column.
        if "PackageID" in item and not ledger_pkg:
            if status == "IN":
                findings.append(
                    Finding("XRG-011", paths["ledger"],
                            f"IN-scope item {item_id} has no PackageID", row_id=item_id)
                )
            elif status in ("OUT", "TBD"):
                findings.append(
                    Finding("XRG-013", paths["ledger"],
                            f"{status} item {item_id} has no PackageID; give it one "
                            f"Package home", row_id=item_id)
                )
        homes = split_list(ledger_pkg)
        if len(homes) > 1:
            findings.append(
                Finding("XRG-014", paths["ledger"],
                        f"{item_id} names {len(homes)} Packages ({', '.join(homes)}); "
                        f"give it exactly one Package home", row_id=item_id)
            )
        for home in homes:
            if known_packages and home not in known_packages:
                findings.append(
                    Finding("XRG-015", paths["ledger"],
                            f"{item_id} names Package {home!r}, which no deliverable in "
                            f"{paths['deliverables']} belongs to", row_id=item_id)
                )

        linked_packages: list[str] = []
        for deliverable_id in linked:
            record = deliverables.get(deliverable_id)
            if record is None:
                findings.append(
                    Finding("XRG-001", paths["ledger"],
                            f"{item_id} names deliverable {deliverable_id!r}, absent from "
                            f"{paths['deliverables']}", row_id=item_id)
                )
                continue
            covers = split_list(record.get("CoversScopeItems"))
            if item_id not in covers:
                findings.append(
                    Finding("XRG-003", paths["ledger"],
                            f"{item_id} names {deliverable_id}, but that deliverable's "
                            f"CoversScopeItems does not name {item_id}", row_id=item_id)
                )
            record_pkg = (record.get("PackageID") or "").strip()
            if record_pkg:
                linked_packages.append(record_pkg)
            supports = split_list(record.get("SupportsObjectives"))
            for objective in objectives:
                if objective not in supports:
                    findings.append(
                        Finding("XRG-005", paths["ledger"],
                                f"{item_id} maps to {objective}, but covering deliverable "
                                f"{deliverable_id} does not support it", row_id=item_id)
                    )
        # Home versus linked deliverables (D-GOV-48; management manual v7:
        # "Several Deliverables may contribute to an included obligation,
        # including supporting contributions from another Package"). A linked
        # deliverable in another Package is a supporting contribution, not a
        # defect. Warn once per item only when the home Package holds none of
        # the item's linked deliverables. With several homes, XRG-014 already
        # reports the item, so only a single home is compared.
        if len(homes) == 1 and linked_packages and homes[0] not in linked_packages:
            findings.append(
                Finding("XRG-004", paths["ledger"],
                        f"{item_id} declares home PackageID {homes[0]!r}, but none of its "
                        f"linked deliverables is in that Package (they are in "
                        f"{', '.join(sorted(set(linked_packages)))})", row_id=item_id)
            )

    ledger_index = {(row.get("ScopeItemID") or "").strip(): row for row in ledger}
    for deliverable_id, record in deliverables.items():
        if not (record.get("PhaseHint") or "").strip():
            findings.append(
                Finding("XRG-008", paths["deliverables"],
                        f"{deliverable_id} has a blank PhaseHint", row_id=deliverable_id)
            )
        for item_id in split_list(record.get("CoversScopeItems")):
            item = ledger_index.get(item_id)
            if item is None:
                findings.append(
                    Finding("XRG-002", paths["deliverables"],
                            f"{deliverable_id} covers {item_id!r}, absent from {paths['ledger']}",
                            row_id=deliverable_id)
                )
            elif deliverable_id not in split_list(item.get("DeliverableIDs")):
                findings.append(
                    Finding("XRG-003", paths["deliverables"],
                            f"{deliverable_id} covers {item_id}, but that ledger row's "
                            f"DeliverableIDs does not name {deliverable_id}", row_id=deliverable_id)
                )

    if context_qa is None:
        return
    qa_index = {(row.get("DeliverableID") or "").strip(): row for row in context_qa}
    for missing in sorted(set(deliverables) - set(qa_index)):
        findings.append(
            Finding("XRG-009", paths["context_qa"],
                    f"{missing} is in {paths['deliverables']} but has no ContextBudgetQA row",
                    row_id=missing)
        )
    for extra in sorted(set(qa_index) - set(deliverables)):
        findings.append(
            Finding("XRG-009", paths["context_qa"],
                    f"{extra} has a ContextBudgetQA row but is not in {paths['deliverables']}",
                    row_id=extra)
        )
    for deliverable_id in sorted(set(deliverables) & set(qa_index)):
        declared = (deliverables[deliverable_id].get("ContextEnvelope") or "").strip()
        measured = (qa_index[deliverable_id].get("ContextEnvelope") or "").strip()
        if declared != measured:
            findings.append(
                Finding("XRG-010", paths["context_qa"],
                        f"{deliverable_id} ContextEnvelope {measured!r} vs "
                        f"{paths['deliverables']} {declared!r}", row_id=deliverable_id)
            )


def run(
    execution_root: Path,
    families: tuple[str, ...] = FAMILIES,
    registers_dir: Path | None = None,
) -> dict:
    """Check only decomposition registers; never discover dependency files."""
    if not families or any(family != "XRG" for family in families):
        raise OperationalError("only the XRG decomposition family is supported")
    execution_root = Path(execution_root)
    if not execution_root.is_dir():
        raise OperationalError(f"EXECUTION_ROOT is not a directory: {execution_root}")
    if registers_dir is not None and not Path(registers_dir).is_dir():
        raise OperationalError(f"--registers-dir is not a directory: {registers_dir}")
    decomposition = Path(registers_dir) if registers_dir is not None else execution_root / "_Decomposition"
    deliverables_path = decomposition / "Deliverables.csv"
    ledger_path = decomposition / "ScopeLedger.csv"
    context_qa_path = decomposition / "ContextBudgetQA.csv"
    deliverables = {
        (row.get("DeliverableID") or "").strip(): row
        for row in read_register(deliverables_path)
        if (row.get("DeliverableID") or "").strip()
    } if deliverables_path.is_file() else {}
    findings: list[Finding] = []
    skipped: list[str] = []
    if deliverables_path.is_file() and ledger_path.is_file():
        context_qa = read_register(context_qa_path) if context_qa_path.is_file() else None
        if context_qa is None:
            skipped.append("XRG ContextBudgetQA checks (ContextBudgetQA.csv absent)")
        check_cross_register(
            deliverables, read_register(ledger_path), context_qa,
            {"deliverables": os.path.relpath(deliverables_path, execution_root),
             "ledger": os.path.relpath(ledger_path, execution_root),
             "context_qa": os.path.relpath(context_qa_path, execution_root)},
            findings,
        )
    else:
        skipped.append("XRG family (Deliverables.csv and/or ScopeLedger.csv absent)")
    by_code: dict[str, int] = {}
    for finding in findings:
        by_code[finding.code] = by_code.get(finding.code, 0) + 1
    return {
        "tool": "validate_decomposition_registers.py",
        "execution_root": str(execution_root), "registers_dir": str(decomposition),
        "families": list(families), "deliverables_declared": len(deliverables),
        "findings_by_code": dict(sorted(by_code.items())),
        "error_count": sum(f.severity == ERROR for f in findings),
        "warning_count": sum(f.severity == WARNING for f in findings),
        "skipped": skipped, "findings": [finding.as_dict() for finding in findings],
    }

def print_report(report: dict, max_per_code: int) -> None:
    print(f"Register validation — {report['execution_root']}")
    print(f"  Families: {', '.join(report['families'])}")
    print(f"  Deliverables declared: {report['deliverables_declared']}")
    for note in report["skipped"]:
        print(f"  SKIPPED: {note}")

    if report["findings"]:
        print("\nFindings")
        shown: dict[str, int] = {}
        for finding in report["findings"]:
            code = finding["code"]
            shown[code] = shown.get(code, 0) + 1
            if shown[code] > max_per_code:
                continue
            locator = finding["path"]
            if finding["line"] is not None:
                locator += f":{finding['line']}"
            ident = f" [{finding['row_id']}]" if finding["row_id"] else ""
            print(f"  {finding['severity']} {code} {locator}{ident} — {finding['detail']}")
        for code, count in sorted(report["findings_by_code"].items()):
            if count > max_per_code:
                print(f"  ... {code}: {count - max_per_code} further occurrence(s) suppressed "
                      f"(--max-per-code {max_per_code}; full list in --json)")

    print("\nSummary by check code")
    if report["findings_by_code"]:
        for code, count in sorted(report["findings_by_code"].items()):
            severity = CHECKS[code][1]
            print(f"  {severity:<7} {code}  {count:>5}  {CHECKS[code][2]}")
    else:
        print("  (none)")
    print(f"\n  ERROR findings:   {report['error_count']}")
    print(f"  WARNING findings: {report['warning_count']}")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("execution_root", nargs="?", help="Project execution root")
    parser.add_argument("--json", dest="json_out", help="Write the full report as JSON")
    parser.add_argument("--families", default="XRG", help="XRG (decomposition checks only)")
    parser.add_argument("--registers-dir", help="Companion register folder (default: EXECUTION_ROOT/_Decomposition)")
    parser.add_argument("--strict", action="store_true", help="Exit 1 on warnings as well as errors")
    parser.add_argument("--max-per-code", type=int, default=20, help="Human-readable finding cap per code")
    parser.add_argument("--list-checks", action="store_true", help="Print the check catalogue and exit")
    return parser.parse_args(argv)

def main(argv: list[str]) -> int:
    args = parse_args(argv)

    if args.list_checks:
        print(f"{'code':<10}{'family':<8}{'severity':<9}description")
        for code, (family, severity, description) in CHECKS.items():
            print(f"{code:<10}{family:<8}{severity:<9}{description}")
        return 0

    if not args.execution_root:
        print("ERROR: EXECUTION_ROOT is required (or use --list-checks)", file=sys.stderr)
        return 2

    families = tuple(f.strip().upper() for f in args.families.split(",") if f.strip())
    unknown = [f for f in families if f not in FAMILIES]
    if unknown:
        print(f"ERROR: unknown family/families: {', '.join(unknown)}", file=sys.stderr)
        return 2

    try:
        report = run(
            Path(args.execution_root),
            families=families,
            registers_dir=Path(args.registers_dir) if args.registers_dir else None,
        )
    except OperationalError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    print_report(report, args.max_per_code)

    if args.json_out:
        out_path = Path(args.json_out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(report, indent=2, sort_keys=False) + "\n", encoding="utf-8")
        print(f"\n  JSON report: {out_path}")

    if report["error_count"]:
        return 1
    if args.strict and report["warning_count"]:
        return 1
    return 0



if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

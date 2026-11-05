"""Synthetic read-only XRG decomposition checks; no live project corpus."""
from __future__ import annotations

import csv
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

VALIDATION_DIR = Path(__file__).resolve().parent
import validate_decomposition_registers as vdr

TOOL = VALIDATION_DIR / "validate_decomposition_registers.py"

DELIVERABLE_COLUMNS = [
    "DeliverableID", "PackageID", "Name", "Description", "Type", "ResponsibleParty",
    "AnticipatedArtifacts", "CoversScopeItems", "SupportsObjectives",
    "ContextEnvelope", "ContextEnvelopeNotes", "PhaseHint",
]
LEDGER_COLUMNS = [
    "ScopeItemID", "InOutStatus", "ScopeItemStatement", "SourceRef", "PackageID",
    "DeliverableIDs", "ObjectiveIDs", "DecisionRef", "OpenIssue", "Notes",
]
CONTEXT_QA_COLUMNS = [
    "DeliverableID", "PackageID", "ContextEnvelope", "Risk", "RecommendedAction", "Notes",
]


# --------------------------------------------------------------------------
# Fixture construction


def write_csv(path: Path, columns: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)



def build_workspace(
    root: Path,
    deliverables: list[dict[str, str]] | None = None,
    ledger: list[dict[str, str]] | None = None,
    context_qa: list[dict[str, str]] | None = None,
) -> Path:
    """Build a minimal, internally consistent two-deliverable execution root."""
    execution_root = root / "execution"
    decomposition = execution_root / "_Decomposition"

    deliverables = deliverables if deliverables is not None else [
        {
            "DeliverableID": "DEL-01-01", "PackageID": "PKG-01",
            "Name": "Record tier schema", "Description": "d", "Type": "CODE",
            "ResponsibleParty": "TBD", "AnticipatedArtifacts": "a",
            "CoversScopeItems": "SOW-001", "SupportsObjectives": "OBJ-001",
            "ContextEnvelope": "S", "ContextEnvelopeNotes": "", "PhaseHint": "P1",
        },
        {
            "DeliverableID": "DEL-02-01", "PackageID": "PKG-02",
            "Name": "Status parser", "Description": "d", "Type": "CODE",
            "ResponsibleParty": "TBD", "AnticipatedArtifacts": "a",
            "CoversScopeItems": "SOW-002", "SupportsObjectives": "OBJ-001",
            "ContextEnvelope": "M", "ContextEnvelopeNotes": "", "PhaseHint": "P1",
        },
    ]
    ledger = ledger if ledger is not None else [
        {
            "ScopeItemID": "SOW-001", "InOutStatus": "IN", "ScopeItemStatement": "s",
            "SourceRef": "§7.1", "PackageID": "PKG-01", "DeliverableIDs": "DEL-01-01",
            "ObjectiveIDs": "OBJ-001", "DecisionRef": "", "OpenIssue": "FALSE", "Notes": "",
        },
        {
            "ScopeItemID": "SOW-002", "InOutStatus": "IN", "ScopeItemStatement": "s",
            "SourceRef": "§7.2", "PackageID": "PKG-02", "DeliverableIDs": "DEL-02-01",
            "ObjectiveIDs": "OBJ-001", "DecisionRef": "", "OpenIssue": "FALSE", "Notes": "",
        },
    ]
    context_qa = context_qa if context_qa is not None else [
        {"DeliverableID": "DEL-01-01", "PackageID": "PKG-01", "ContextEnvelope": "S",
         "Risk": "LOW", "RecommendedAction": "None", "Notes": ""},
        {"DeliverableID": "DEL-02-01", "PackageID": "PKG-02", "ContextEnvelope": "M",
         "Risk": "LOW", "RecommendedAction": "None", "Notes": ""},
    ]

    write_csv(decomposition / "Deliverables.csv", DELIVERABLE_COLUMNS, deliverables)
    write_csv(decomposition / "ScopeLedger.csv", LEDGER_COLUMNS, ledger)
    write_csv(decomposition / "ContextBudgetQA.csv", CONTEXT_QA_COLUMNS, context_qa)

    return execution_root



def codes(report: dict) -> dict[str, int]:
    return report["findings_by_code"]



def ids_for(report: dict, code: str) -> list[str]:
    return [f["row_id"] for f in report["findings"] if f["code"] == code]



def test_non_reciprocal_scope_coverage_is_reported_from_both_sides(tmp_path: Path) -> None:
    execution_root = build_workspace(tmp_path)
    ledger_path = execution_root / "_Decomposition" / "ScopeLedger.csv"
    rows = list(csv.DictReader(ledger_path.open(encoding="utf-8-sig")))
    rows[0]["DeliverableIDs"] = "DEL-02-01"  # SOW-001 now points at the wrong deliverable
    write_csv(ledger_path, LEDGER_COLUMNS, rows)

    report = vdr.run(execution_root, families=("XRG",))

    assert codes(report)["XRG-003"] == 2  # once from the ledger, once from Deliverables
    assert codes(report)["XRG-004"] == 1  # home PKG-01 holds none of SOW-001's deliverables



def test_unknown_ids_objectives_and_context_budget_drift(tmp_path: Path) -> None:
    execution_root = build_workspace(tmp_path)
    decomposition = execution_root / "_Decomposition"

    ledger = list(csv.DictReader((decomposition / "ScopeLedger.csv").open(encoding="utf-8-sig")))
    ledger[0]["DeliverableIDs"] = "DEL-09-09"       # XRG-001
    ledger[1]["ObjectiveIDs"] = "OBJ-001;OBJ-007"   # XRG-005
    ledger.append({
        "ScopeItemID": "SOW-003", "InOutStatus": "IN", "ScopeItemStatement": "s",
        "SourceRef": "§7.3", "PackageID": "PKG-01", "DeliverableIDs": "",
        "ObjectiveIDs": "OBJ-001", "DecisionRef": "", "OpenIssue": "FALSE", "Notes": "",
    })                                              # XRG-006
    ledger.append({
        "ScopeItemID": "SOW-004", "InOutStatus": "OUT", "ScopeItemStatement": "s",
        "SourceRef": "§7.4", "PackageID": "PKG-01", "DeliverableIDs": "DEL-01-01",
        "ObjectiveIDs": "", "DecisionRef": "", "OpenIssue": "FALSE", "Notes": "",
    })                                              # XRG-007
    write_csv(decomposition / "ScopeLedger.csv", LEDGER_COLUMNS, ledger)

    deliverables = list(csv.DictReader((decomposition / "Deliverables.csv").open(encoding="utf-8-sig")))
    deliverables[0]["CoversScopeItems"] = "SOW-001;SOW-999"  # XRG-002
    deliverables[1]["PhaseHint"] = ""                        # XRG-008
    write_csv(decomposition / "Deliverables.csv", DELIVERABLE_COLUMNS, deliverables)

    context_qa = list(csv.DictReader((decomposition / "ContextBudgetQA.csv").open(encoding="utf-8-sig")))
    context_qa[0]["ContextEnvelope"] = "XL"                  # XRG-010
    context_qa.pop(1)                                        # XRG-009
    write_csv(decomposition / "ContextBudgetQA.csv", CONTEXT_QA_COLUMNS, context_qa)

    report = vdr.run(execution_root, families=("XRG",))
    found = codes(report)

    assert found["XRG-001"] == 1
    assert found["XRG-002"] == 1
    assert found["XRG-005"] == 1
    assert found["XRG-006"] == 1
    assert found["XRG-007"] == 1
    assert found["XRG-008"] == 1
    assert found["XRG-009"] == 1
    assert found["XRG-010"] == 1



def test_every_scope_item_has_a_package_home(tmp_path: Path) -> None:
    """D-GOV-48: every IN, OUT and TBD item has one Package; only IN items map to Deliverables.

    A missing home is XRG-011 (ERROR) on an IN item and XRG-013 (WARNING) on an
    OUT or TBD item. XRG-012 (D-GOV-47) is retired: an OUT or TBD item with a
    PackageID conforms.
    """
    execution_root = build_workspace(tmp_path)
    ledger_path = execution_root / "_Decomposition" / "ScopeLedger.csv"
    ledger = list(csv.DictReader(ledger_path.open(encoding="utf-8-sig")))
    blank = {"ScopeItemStatement": "s", "DeliverableIDs": "", "ObjectiveIDs": "",
             "DecisionRef": "", "OpenIssue": "FALSE", "Notes": ""}
    ledger.append({"ScopeItemID": "SOW-003", "InOutStatus": "OUT", "SourceRef": "§7.3",
                   "PackageID": "PKG-01", **blank})
    ledger.append({"ScopeItemID": "SOW-004", "InOutStatus": "TBD", "SourceRef": "§7.4",
                   "PackageID": "PKG-02", **blank})
    write_csv(ledger_path, LEDGER_COLUMNS, ledger)

    # OUT and TBD items with a Package home and no Deliverable mapping conform.
    assert vdr.run(execution_root, families=("XRG",))["findings"] == []

    ledger[0]["PackageID"] = ""  # IN item without a Package  -> XRG-011
    ledger[2]["PackageID"] = ""  # OUT item without a Package -> XRG-013
    ledger[3]["PackageID"] = ""  # TBD item without a Package -> XRG-013
    write_csv(ledger_path, LEDGER_COLUMNS, ledger)
    report = vdr.run(execution_root, families=("XRG",))

    assert codes(report) == {"XRG-011": 1, "XRG-013": 2}
    assert ids_for(report, "XRG-011") == ["SOW-001"]
    assert ids_for(report, "XRG-013") == ["SOW-003", "SOW-004"]
    assert report["error_count"] == 1  # XRG-013 is a WARNING
    assert "XRG-012" not in vdr.CHECKS  # retired by D-GOV-48, not reused



def test_package_home_is_exactly_one_known_package(tmp_path: Path) -> None:
    """D-GOV-48: a ledger item names exactly one Package, and that Package exists."""
    execution_root = build_workspace(tmp_path)
    ledger_path = execution_root / "_Decomposition" / "ScopeLedger.csv"
    ledger = list(csv.DictReader(ledger_path.open(encoding="utf-8-sig")))
    blank = {"ScopeItemStatement": "s", "DeliverableIDs": "", "ObjectiveIDs": "",
             "DecisionRef": "", "OpenIssue": "FALSE", "Notes": ""}
    ledger.append({"ScopeItemID": "SOW-003", "InOutStatus": "OUT", "SourceRef": "§7.3",
                   "PackageID": "PKG-99", **blank})
    ledger.append({"ScopeItemID": "SOW-004", "InOutStatus": "TBD", "SourceRef": "§7.4",
                   "PackageID": "PKG-01;PKG-02", **blank})
    write_csv(ledger_path, LEDGER_COLUMNS, ledger)
    report = vdr.run(execution_root, families=("XRG",))

    assert codes(report) == {"XRG-014": 1, "XRG-015": 1}
    assert ids_for(report, "XRG-014") == ["SOW-004"]
    assert ids_for(report, "XRG-015") == ["SOW-003"]



def test_single_home_is_compared_after_parsing(tmp_path: Path) -> None:
    """XRG-004 compares the parsed home, so a stray separator is not a mismatch."""
    execution_root = build_workspace(tmp_path)
    ledger_path = execution_root / "_Decomposition" / "ScopeLedger.csv"
    ledger = list(csv.DictReader(ledger_path.open(encoding="utf-8-sig")))
    ledger[0]["PackageID"] = "PKG-01; "
    write_csv(ledger_path, LEDGER_COLUMNS, ledger)
    assert "XRG-004" not in codes(vdr.run(execution_root, families=("XRG",)))

    ledger[0]["PackageID"] = "PKG-02;"
    write_csv(ledger_path, LEDGER_COLUMNS, ledger)
    assert codes(vdr.run(execution_root, families=("XRG",))).get("XRG-004") == 1



def test_supporting_deliverable_in_another_package_is_not_a_finding(tmp_path: Path) -> None:
    """XRG-004: a linked deliverable in another Package is a supporting contribution.

    Management manual v7: "Several Deliverables may contribute to an included
    obligation, including supporting contributions from another Package." No
    finding while the home Package holds at least one linked deliverable.
    """
    execution_root = build_workspace(tmp_path)
    decomposition = execution_root / "_Decomposition"
    ledger = list(csv.DictReader((decomposition / "ScopeLedger.csv").open(encoding="utf-8-sig")))
    ledger[0]["DeliverableIDs"] = "DEL-01-01;DEL-02-01"  # home PKG-01, support from PKG-02
    write_csv(decomposition / "ScopeLedger.csv", LEDGER_COLUMNS, ledger)
    deliverables = list(csv.DictReader((decomposition / "Deliverables.csv").open(encoding="utf-8-sig")))
    deliverables[1]["CoversScopeItems"] = "SOW-002;SOW-001"
    write_csv(decomposition / "Deliverables.csv", DELIVERABLE_COLUMNS, deliverables)

    report = vdr.run(execution_root, families=("XRG",))

    assert report["findings"] == []



def test_home_package_holding_no_linked_deliverable_is_a_warning(tmp_path: Path) -> None:
    """XRG-004 warns once per item when the home Package holds none of its deliverables."""
    execution_root = build_workspace(tmp_path)
    decomposition = execution_root / "_Decomposition"
    deliverables = list(csv.DictReader((decomposition / "Deliverables.csv").open(encoding="utf-8-sig")))
    deliverables.append({
        "DeliverableID": "DEL-02-02", "PackageID": "PKG-02",
        "Name": "Second parser", "Description": "d", "Type": "CODE",
        "ResponsibleParty": "TBD", "AnticipatedArtifacts": "a",
        "CoversScopeItems": "SOW-001", "SupportsObjectives": "OBJ-001",
        "ContextEnvelope": "S", "ContextEnvelopeNotes": "", "PhaseHint": "P1",
    })
    deliverables[1]["CoversScopeItems"] = "SOW-002;SOW-001"
    deliverables[0]["CoversScopeItems"] = ""
    write_csv(decomposition / "Deliverables.csv", DELIVERABLE_COLUMNS, deliverables)
    ledger = list(csv.DictReader((decomposition / "ScopeLedger.csv").open(encoding="utf-8-sig")))
    ledger[0]["DeliverableIDs"] = "DEL-02-01;DEL-02-02"  # home PKG-01 holds neither
    write_csv(decomposition / "ScopeLedger.csv", LEDGER_COLUMNS, ledger)
    context_qa = list(csv.DictReader((decomposition / "ContextBudgetQA.csv").open(encoding="utf-8-sig")))
    context_qa.append({"DeliverableID": "DEL-02-02", "PackageID": "PKG-02", "ContextEnvelope": "S",
                       "Risk": "LOW", "RecommendedAction": "None", "Notes": ""})
    write_csv(decomposition / "ContextBudgetQA.csv", CONTEXT_QA_COLUMNS, context_qa)

    report = vdr.run(execution_root, families=("XRG",))

    assert codes(report) == {"XRG-004": 1}  # one finding per item, not per link
    assert ids_for(report, "XRG-004") == ["SOW-001"]
    assert report["error_count"] == 0
    assert report["warning_count"] == 1
    assert vdr.CHECKS["XRG-004"][1] == vdr.WARNING



def test_xrg004_is_not_repeated_for_an_item_with_several_homes(tmp_path: Path) -> None:
    """With two homes, XRG-014 reports the item and XRG-004 stays silent."""
    execution_root = build_workspace(tmp_path)
    ledger_path = execution_root / "_Decomposition" / "ScopeLedger.csv"
    ledger = list(csv.DictReader(ledger_path.open(encoding="utf-8-sig")))
    ledger[0]["PackageID"] = "PKG-02;PKG-03"
    write_csv(ledger_path, LEDGER_COLUMNS, ledger)

    report = vdr.run(execution_root, families=("XRG",))

    assert "XRG-004" not in codes(report)
    assert codes(report)["XRG-014"] == 1



def test_registers_dir_reads_companion_registers_outside_decomposition(tmp_path: Path) -> None:
    """--registers-dir finds registers a project keeps outside _Decomposition/."""
    execution_root = build_workspace(tmp_path)
    registers = tmp_path / "docs" / "_Registers"
    registers.mkdir(parents=True)
    for name in ("Deliverables.csv", "ScopeLedger.csv", "ContextBudgetQA.csv"):
        (execution_root / "_Decomposition" / name).rename(registers / name)
    ledger = list(csv.DictReader((registers / "ScopeLedger.csv").open(encoding="utf-8-sig")))
    ledger[0]["PackageID"] = "PKG-01;PKG-02"  # XRG-014, visible only through the option
    write_csv(registers / "ScopeLedger.csv", LEDGER_COLUMNS, ledger)

    default = vdr.run(execution_root, families=("XRG",))
    assert default["skipped"] == ["XRG family (Deliverables.csv and/or ScopeLedger.csv absent)"]

    report = vdr.run(execution_root, families=("XRG",), registers_dir=registers)
    assert report["skipped"] == []
    assert codes(report) == {"XRG-014": 1}
    assert report["registers_dir"] == str(registers)

    cli = subprocess.run(
        [sys.executable, str(TOOL), str(execution_root), "--families", "XRG",
         "--registers-dir", str(registers)],
        capture_output=True, text=True,
    )
    assert cli.returncode == 1, cli.stdout + cli.stderr
    assert "XRG-014" in cli.stdout

    missing = subprocess.run(
        [sys.executable, str(TOOL), str(execution_root), "--registers-dir",
         str(tmp_path / "nope")],
        capture_output=True, text=True,
    )
    assert missing.returncode == 2



def test_unknown_package_check_needs_a_deliverable_package_column(tmp_path: Path) -> None:
    """XRG-015 is suppressed when Deliverables.csv carries no PackageID column."""
    execution_root = build_workspace(tmp_path)
    decomposition = execution_root / "_Decomposition"
    rows = list(csv.DictReader((decomposition / "Deliverables.csv").open(encoding="utf-8-sig")))
    columns = [c for c in DELIVERABLE_COLUMNS if c != "PackageID"]
    write_csv(decomposition / "Deliverables.csv", columns,
              [{k: v for k, v in row.items() if k != "PackageID"} for row in rows])

    assert "XRG-015" not in codes(vdr.run(execution_root, families=("XRG",)))



def test_package_home_checks_skip_a_ledger_without_a_package_column(tmp_path: Path) -> None:
    columns = [c for c in LEDGER_COLUMNS if c != "PackageID"]
    ledger = [
        {"ScopeItemID": "SOW-001", "InOutStatus": "IN", "ScopeItemStatement": "s",
         "SourceRef": "§7.1", "DeliverableIDs": "DEL-01-01", "ObjectiveIDs": "OBJ-001",
         "DecisionRef": "", "OpenIssue": "FALSE", "Notes": ""},
        {"ScopeItemID": "SOW-002", "InOutStatus": "IN", "ScopeItemStatement": "s",
         "SourceRef": "§7.2", "DeliverableIDs": "DEL-02-01", "ObjectiveIDs": "OBJ-001",
         "DecisionRef": "", "OpenIssue": "FALSE", "Notes": ""},
        {"ScopeItemID": "SOW-003", "InOutStatus": "OUT", "ScopeItemStatement": "s",
         "SourceRef": "§7.3", "DeliverableIDs": "", "ObjectiveIDs": "",
         "DecisionRef": "", "OpenIssue": "FALSE", "Notes": ""},
        {"ScopeItemID": "SOW-004", "InOutStatus": "TBD", "ScopeItemStatement": "s",
         "SourceRef": "§7.4", "DeliverableIDs": "", "ObjectiveIDs": "",
         "DecisionRef": "", "OpenIssue": "FALSE", "Notes": ""},
    ]
    execution_root = build_workspace(tmp_path)
    write_csv(execution_root / "_Decomposition" / "ScopeLedger.csv", columns, ledger)

    assert vdr.run(execution_root, families=("XRG",))["findings"] == []



def test_missing_companion_registers_are_skipped_not_errors(tmp_path: Path) -> None:
    execution_root = build_workspace(tmp_path)
    (execution_root / "_Decomposition" / "ScopeLedger.csv").unlink()

    report = vdr.run(execution_root, families=("XRG",))

    assert report["findings"] == []
    assert report["skipped"] == ["XRG family (Deliverables.csv and/or ScopeLedger.csv absent)"]


@pytest.mark.parametrize('phase', ['', '1_Working', '2_Checking', '3_Issued'])
def test_xrg_is_independent_of_locality_layout_and_dependency_storage(tmp_path, phase):
    execution_root = build_workspace(tmp_path)
    folder = execution_root/'PKG-01_Core'/phase/'DEL-01-01_Record_tier'
    folder.mkdir(parents=True)
    # Deliberately unusable dependency artifacts: XRG must not read any of them.
    (folder/'deliverable.yaml').write_text('invalid YAML for a different query: [\n')
    (folder/'Dependencies.csv').write_bytes(b'\xff\xfeinvalid historical bytes')
    (folder/'_DEPENDENCIES.md').write_text('retained original dependency notes')
    before = {path: path.read_bytes() for path in execution_root.rglob('*') if path.is_file()}
    report = vdr.run(execution_root)
    assert report['findings'] == []
    assert report['families'] == ['XRG']
    assert {path: path.read_bytes() for path in before} == before


def test_validator_preserves_sources_and_is_deterministic(tmp_path):
    execution_root = build_workspace(tmp_path)
    ledger_path = execution_root/'_Decomposition/ScopeLedger.csv'
    rows = list(csv.DictReader(ledger_path.open(encoding='utf-8-sig')))
    rows[0]['SourceRef'] = 'source version B, table 7: value 123.40 kg; case winter, pending acceptance'
    rows[0]['ObjectiveIDs'] = 'OBJ-001;OBJ-099'
    write_csv(ledger_path, LEDGER_COLUMNS, rows)
    before = {path: path.read_bytes() for path in execution_root.rglob('*.csv')}
    report = vdr.run(execution_root)
    assert report == vdr.run(execution_root)
    assert report['findings_by_code'] == {'XRG-005': 1}
    assert {path: path.read_bytes() for path in before} == before


def test_cli_exit_codes_json_strict_and_retained_check_catalogue(tmp_path):
    execution_root = build_workspace(tmp_path)
    report_path = tmp_path/'report.json'
    def cli(*args):
        return subprocess.run([sys.executable, str(TOOL), *map(str, args)], text=True, capture_output=True)
    clean = cli(execution_root, '--json', report_path)
    assert clean.returncode == 0, clean.stdout + clean.stderr
    assert json.loads(report_path.read_text())['findings'] == []
    ledger_path = execution_root/'_Decomposition/ScopeLedger.csv'
    rows = list(csv.DictReader(ledger_path.open(encoding='utf-8-sig')))
    rows[0]['ObjectiveIDs'] = 'OBJ-099'
    write_csv(ledger_path, LEDGER_COLUMNS, rows)
    assert cli(execution_root).returncode == 1
    rows[0]['ObjectiveIDs'] = 'OBJ-001'
    rows.append({'ScopeItemID': 'SOW-003', 'InOutStatus': 'OUT', 'PackageID': ''})
    write_csv(ledger_path, LEDGER_COLUMNS, rows)
    assert cli(execution_root).returncode == 0  # XRG-013 remains a warning.
    assert cli(execution_root, '--strict').returncode == 1
    assert cli(tmp_path/'absent').returncode == 2
    for removed_family in ('SCH', 'EVQ', 'DRB'):
        assert cli(execution_root, '--families', removed_family).returncode == 2
    listing = cli('--list-checks')
    assert listing.returncode == 0
    assert 'XRG-001' in listing.stdout and 'XRG-015' in listing.stdout
    assert 'EVQ-' not in listing.stdout and 'DRB-' not in listing.stdout


def test_operational_read_failures_are_not_scope_findings(tmp_path):
    directory = tmp_path/'register.csv'
    directory.mkdir()
    with pytest.raises(vdr.OperationalError, match='unreadable'):
        vdr.read_register(directory)
    source = tmp_path/'invalid.csv'
    source.write_bytes(b'\xff')
    with pytest.raises(vdr.OperationalError, match='unreadable'):
        vdr.read_register(source)


def test_extra_context_identity_and_optional_context_qa(tmp_path):
    execution_root = build_workspace(tmp_path)
    source = execution_root/'_Decomposition/ContextBudgetQA.csv'
    rows = list(csv.DictReader(source.open(encoding='utf-8-sig')))
    rows.append({'DeliverableID': 'DEL-99-99', 'ContextEnvelope': 'S'})
    write_csv(source, CONTEXT_QA_COLUMNS, rows)
    assert ids_for(vdr.run(execution_root), 'XRG-009') == ['DEL-99-99']
    source.unlink()
    report = vdr.run(execution_root)
    assert report['findings'] == []
    assert report['skipped'] == ['XRG ContextBudgetQA checks (ContextBudgetQA.csv absent)']

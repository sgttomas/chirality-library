#!/usr/bin/env python3
"""Tests for tools/validation/check_amendment_reopen.py (D-GOV-50, D-GOV-51).

Fixture amendment folders are built under tmp_path, read from the working
tree (unanchored) or committed to a fixture git repository and read at a
commit. The real-record tests read accepted PEC, Piping and Runtime records at
HEAD when they are present in the checkout.
"""
from __future__ import annotations

import csv
import hashlib
import importlib.util
import io
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPT = REPO_ROOT / "tools" / "validation" / "check_amendment_reopen.py"

_spec = importlib.util.spec_from_file_location("check_amendment_reopen", SCRIPT)
assert _spec and _spec.loader
mod = importlib.util.module_from_spec(_spec)
sys.modules["check_amendment_reopen"] = mod
_spec.loader.exec_module(mod)

BASE_COLUMNS = [
    "AmendmentID",
    "ActionSeq",
    "ActionType",
    "EntityType",
    "EntityID",
    "Description",
    "AffectedFiles",
    "DownstreamReruns",
    "SupersessionBindingPresent",
]
DEL_REL = "projects/fixture/execution/PKG-01_Fixture/1_Working/DEL-01-01_Fixture"
SC_REL = "projects/fixture/execution/_ScopeChange"


def _csv(columns, rows) -> str:
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=columns, lineterminator="\n")
    writer.writeheader()
    for row in rows:
        writer.writerow({c: row.get(c, "") for c in columns})
    return buffer.getvalue()


def row(action, entity="DEL-01-01", seq="1", entity_type="DELIVERABLE", scope=None, amendment="SCA-001"):
    data = {
        "AmendmentID": amendment,
        "ActionSeq": seq,
        "ActionType": action,
        "EntityType": entity_type,
        "EntityID": entity,
        "Description": "fixture",
        "SupersessionBindingPresent": "NO",
    }
    if scope is not None:
        data["ScopeChanging"] = scope
    return data


def build(
    project: Path,
    rows,
    *,
    amendment="SCA-001",
    scope_column=True,
    groups=("1", "2", "3"),
    group3_heading=None,
    register_name="Amendment_Actions.csv",
    bound_sha=None,
    extra_manifest_rows=(),
    manifest_path_override=None,
) -> dict:
    """Write a deliverable folder and one amendment's scope-change records."""
    deliverable = project / DEL_REL
    deliverable.mkdir(parents=True, exist_ok=True)
    (deliverable / "_STATUS.md").write_text("# Status: DEL-01-01\n\n**Current State:** ISSUED\n")
    root = project / SC_REL
    snapshot = root / f"{amendment}_2026-09-26_1200"
    snapshot.mkdir(parents=True, exist_ok=True)
    columns = BASE_COLUMNS + (["ScopeChanging"] if scope_column else [])
    register = snapshot / register_name
    register.write_text(_csv(columns, rows))
    sha = bound_sha or hashlib.sha256(register.read_bytes()).hexdigest()
    register_rel = manifest_path_override or register.relative_to(project).as_posix()
    snapshots = root / "checkpoint_snapshots"
    for group in groups:
        folder = snapshots / f"{amendment}_GROUP-{group}_2026-09-26"
        folder.mkdir(parents=True, exist_ok=True)
        heading = f"{amendment} checkpoint group {group} — accepted fixture"
        if group == "3" and group3_heading is not None:
            heading = group3_heading
        (folder / "DECISION.md").write_text(f"# {heading}\n\nFixture decision.\n")
        manifest_rows = [f"{snapshot.relative_to(project).as_posix()}/Propagation_Plan.md,{'0' * 64},plan,Accepted"]
        if group == "2":
            manifest_rows.append(f"{register_rel},{sha},exact final action register,Accepted")
            manifest_rows.extend(extra_manifest_rows)
        (folder / "ACCEPTED_MANIFEST.csv").write_text(
            "Path,SHA256,Role,AcceptanceBoundary\n" + "\n".join(manifest_rows) + "\n"
        )
    return {"deliverable": deliverable, "root": root, "snapshot": snapshot, "register": register}


def check(project: Path, deliverable, amendment="SCA-001", **kwargs):
    return mod.check_reopen(str(deliverable), amendment, project_root=project, cwd=project, **kwargs)


# ---------------------------------------------------------------------------
# Admitted paths
# ---------------------------------------------------------------------------


def test_modify_admitted(tmp_path):
    paths = build(tmp_path, [row("ADD", entity="DEL-01-02"), row("MODIFY", seq="2", scope="NO")])
    decision = check(tmp_path, paths["deliverable"])
    assert decision.admitted, decision
    assert decision.code == mod.ADMITTED
    assert decision.amendment_id == "SCA-001"
    assert decision.action_seq == "2"
    assert decision.action_type == "MODIFY"
    assert decision.scope_changing == "NO"
    assert decision.group3_decision == f"{SC_REL}/checkpoint_snapshots/SCA-001_GROUP-3_2026-09-26/DECISION.md"
    assert decision.register_sha256 == hashlib.sha256(paths["register"].read_bytes()).hexdigest()


def test_modify_admitted_in_legacy_register_without_scope_column(tmp_path):
    paths = build(tmp_path, [row("MODIFY")], scope_column=False)
    decision = check(tmp_path, paths["deliverable"])
    assert decision.admitted
    assert decision.scope_changing is None
    assert any("legacy register" in note for note in decision.notes)


def test_reclassify_scope_changing_yes_admitted(tmp_path):
    paths = build(tmp_path, [row("RECLASSIFY", scope="YES")])
    decision = check(tmp_path, paths["deliverable"])
    assert decision.admitted
    assert decision.action_type == "RECLASSIFY"
    assert decision.scope_changing == "YES"


def test_deliverable_id_and_labelled_entity_id(tmp_path):
    paths = build(tmp_path, [row("MODIFY", entity="DEL-01-01_Fixture", scope="YES")])
    assert check(tmp_path, "DEL-01-01", scope_change_root=paths["root"]).admitted
    assert check(tmp_path, paths["deliverable"]).admitted


def test_similar_deliverable_id_is_not_matched(tmp_path):
    paths = build(tmp_path, [row("MODIFY", entity="DEL-01-011", scope="NO")])
    decision = check(tmp_path, paths["deliverable"])
    assert decision.code == mod.NO_DELIVERABLE_ACTION


def test_group3_folder_and_decision_paths_admitted(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")])
    folder = paths["root"] / "checkpoint_snapshots" / "SCA-001_GROUP-3_2026-09-26"
    assert check(tmp_path, paths["deliverable"], amendment=str(folder)).admitted
    assert check(tmp_path, paths["deliverable"], amendment=f"{SC_REL}/checkpoint_snapshots/SCA-001_GROUP-3_2026-09-26/DECISION.md").admitted
    assert check(tmp_path, paths["deliverable"], amendment=str(paths["snapshot"])).admitted


def test_project_qualified_amendment_id(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO", amendment="SCA-APP-003")], amendment="SCA-APP-003")
    decision = check(tmp_path, paths["deliverable"], amendment="SCA-APP-003")
    assert decision.admitted, decision


def test_cp2_register_name_bound_in_group2_manifest(tmp_path):
    # A run whose group-1 snapshot bound Amendment_Actions.csv as intake writes
    # its group-2 register under a distinct name; the manifest names it.
    paths = build(tmp_path, [row("MODIFY", scope="NO")], register_name="Amendment_Actions_CP2.csv")
    (paths["snapshot"] / "Amendment_Actions.csv").write_text(_csv(BASE_COLUMNS, [row("ADD")]))
    decision = check(tmp_path, paths["deliverable"])
    assert decision.admitted
    assert decision.register_path.endswith("Amendment_Actions_CP2.csv")


def test_manifest_path_relative_to_project_folder_admitted(tmp_path):
    paths = build(
        tmp_path,
        [row("MODIFY", scope="NO")],
        manifest_path_override="execution/_ScopeChange/SCA-001_2026-09-26_1200/Amendment_Actions.csv",
    )
    decision = check(tmp_path, paths["deliverable"])
    assert decision.admitted, decision
    assert decision.register_path == f"{SC_REL}/SCA-001_2026-09-26_1200/Amendment_Actions.csv"


def test_role_disambiguates_two_bound_register_files(tmp_path):
    intake = f"{SC_REL}/SCA-001_2026-09-26_1200/Amendment_Actions.csv"
    paths = build(
        tmp_path,
        [row("MODIFY", scope="NO")],
        register_name="Amendment_Actions_CP2.csv",
        extra_manifest_rows=[f"{intake},{'1' * 64},intake context,Context"],
    )
    (paths["snapshot"] / "Amendment_Actions.csv").write_text("x\n")
    decision = check(tmp_path, paths["deliverable"])
    assert decision.admitted
    assert decision.register_path.endswith("Amendment_Actions_CP2.csv")


# ---------------------------------------------------------------------------
# Refusals: acceptance stage
# ---------------------------------------------------------------------------


def test_group2_only_refused(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")], groups=("1", "2"))
    decision = check(tmp_path, paths["deliverable"])
    assert not decision.admitted
    assert decision.code == mod.GROUP3_NOT_ACCEPTED
    assert "SCA-001_GROUP-2_2026-09-26" in decision.reason


def test_group1_only_refused(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")], groups=("1",))
    decision = check(tmp_path, paths["deliverable"])
    assert decision.code == mod.GROUP3_NOT_ACCEPTED


def test_candidate_snapshot_without_group3_refused(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")], groups=("1", "2"))
    decision = check(tmp_path, paths["deliverable"], amendment=str(paths["snapshot"]))
    assert decision.code == mod.GROUP3_NOT_ACCEPTED


def test_group2_decision_path_refused(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")])
    folder = paths["root"] / "checkpoint_snapshots" / "SCA-001_GROUP-2_2026-09-26"
    decision = check(tmp_path, paths["deliverable"], amendment=str(folder))
    assert decision.code == mod.GROUP3_NOT_ACCEPTED
    assert "group-2" in decision.reason


@pytest.mark.parametrize(
    "heading",
    [
        "SCA-001 checkpoint group 3 — returned to checkpoint 2",
        "SCA-001 checkpoint group 3 — not accepted",
        "SCA-002 checkpoint group 3 — accepted audited poststate",
        "Checkpoint group 3 notes",
    ],
)
def test_group3_heading_without_acceptance_refused(tmp_path, heading):
    paths = build(tmp_path, [row("MODIFY", scope="NO")], group3_heading=heading)
    decision = check(tmp_path, paths["deliverable"])
    assert decision.code == mod.GROUP3_NOT_ACCEPTED


@pytest.mark.parametrize(
    "heading",
    [
        "SCA-001 checkpoint group 3 — not yet accepted",
        "SCA-001 checkpoint group 3 — candidate, to be accepted",
        "SCA-001 checkpoint group 3 — declined; nothing accepted",
        "SCA-001 checkpoint group 3 — accepted: NO",
        "SCA-001 checkpoint group 3 — accepted? No: deferred",
        "SCA-001 checkpoint group 3 — NOT ACCEPTED",
        "SCA-001 checkpoint group 3 — unaccepted",
        "SCA-001 checkpoint group 3 — acceptance withheld (awaiting owner)",
        "SCA-001 checkpoint group 3 — acceptedly",
        "SCA-001 checkpoint group 30 — accepted",
        "SCA-001 checkpoint group 3 accepted",
    ],
)
def test_group3_heading_must_read_accepted_directly_after_the_dash(tmp_path, heading):
    paths = build(tmp_path, [row("MODIFY", scope="NO")], group3_heading=heading)
    assert check(tmp_path, paths["deliverable"]).code == mod.GROUP3_NOT_ACCEPTED


@pytest.mark.parametrize(
    "heading",
    [
        "SCA-001 checkpoint group 3 — accepted",
        "SCA-001 checkpoint group 3 — accepted.",
        "SCA-001 checkpoint group 3 — accepted audited poststate",  # PEC SCA-005 and SCA-006 wording
        "SCA-001 checkpoint group 3 - accepted, closure verdict COMPLETE",
        # Scope-change group 3 accepts or returns; a qualified acceptance is the
        # accepted outcome and its qualifications are decision text this check
        # does not interpret (scope-change contract, Deterministic Tool Contracts).
        "SCA-001 checkpoint group 3 — accepted with a limited basis",
    ],
)
def test_group3_heading_accepted_forms_admitted(tmp_path, heading):
    paths = build(tmp_path, [row("MODIFY", scope="NO")], group3_heading=heading)
    decision = check(tmp_path, paths["deliverable"])
    assert decision.admitted, decision


def test_group3_heading_must_be_the_first_line(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")])
    decision_md = paths["root"] / "checkpoint_snapshots" / "SCA-001_GROUP-3_2026-09-26" / "DECISION.md"
    decision_md.write_text("Status: RETURNED by owner.\n\n# SCA-001 checkpoint group 3 — accepted poststate\n")
    assert check(tmp_path, paths["deliverable"]).code == mod.GROUP3_NOT_ACCEPTED


@pytest.mark.parametrize(
    "name",
    [
        "SCA-001_GROUP-3_CANDIDATE_2026-09-27",
        "SCA-001_GROUP-3_2026-09-27_candidate",
        "SCA-001_GROUP-3_DRAFT",
    ],
)
def test_candidate_group3_folder_refused(tmp_path, name):
    paths = build(tmp_path, [row("MODIFY", scope="NO")], groups=("1", "2"))
    folder = paths["root"] / "checkpoint_snapshots" / name
    folder.mkdir()
    (folder / "DECISION.md").write_text("# SCA-001 checkpoint group 3 — accepted (candidate draft)\n")
    (folder / "ACCEPTED_MANIFEST.csv").write_text("Path,SHA256\n")
    decision = check(tmp_path, paths["deliverable"])
    assert decision.code == mod.GROUP3_NOT_ACCEPTED
    assert name in decision.reason
    pinned = check(tmp_path, paths["deliverable"], amendment=str(folder))
    assert pinned.code == mod.GROUP3_NOT_ACCEPTED


def test_group3_amendment_and_sequence_folder_names_admitted(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")], groups=("1", "2"))
    folder = paths["root"] / "checkpoint_snapshots" / "SCA-001_GROUP-3_AMENDMENT-1_2026-09-27_02"
    folder.mkdir()
    (folder / "DECISION.md").write_text("# SCA-001 checkpoint group 3 — accepted revised poststate\n")
    (folder / "ACCEPTED_MANIFEST.csv").write_text("Path,SHA256\n")
    decision = check(tmp_path, paths["deliverable"])
    assert decision.admitted, decision
    assert decision.group3_snapshot.endswith("SCA-001_GROUP-3_AMENDMENT-1_2026-09-27_02")


def test_group3_without_manifest_refused(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")])
    (paths["root"] / "checkpoint_snapshots" / "SCA-001_GROUP-3_2026-09-26" / "ACCEPTED_MANIFEST.csv").unlink()
    assert check(tmp_path, paths["deliverable"]).code == mod.GROUP3_NOT_ACCEPTED


def test_missing_group2_manifest_refused(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")])
    (paths["root"] / "checkpoint_snapshots" / "SCA-001_GROUP-2_2026-09-26" / "ACCEPTED_MANIFEST.csv").unlink()
    assert check(tmp_path, paths["deliverable"]).code == mod.GROUP2_MANIFEST_MISSING


# ---------------------------------------------------------------------------
# Refusals: register binding
# ---------------------------------------------------------------------------


def _rebind(paths, register_rows, folder_name, *, role="exact final action register", register_name="Amendment_Actions_R.csv"):
    """Write a revised register and a group-2 decision folder binding it."""
    register = paths["snapshot"] / register_name
    register.write_text(_csv(BASE_COLUMNS + ["ScopeChanging"], register_rows))
    project = paths["deliverable"].parents[len(Path(DEL_REL).parts) - 1]
    folder = paths["root"] / "checkpoint_snapshots" / folder_name
    folder.mkdir()
    (folder / "DECISION.md").write_text("# SCA-001 checkpoint group 2 — amendment: revised register\n")
    (folder / "ACCEPTED_MANIFEST.csv").write_text(
        "Path,SHA256,Role,AcceptanceBoundary\n"
        f"{register.relative_to(project).as_posix()},{hashlib.sha256(register.read_bytes()).hexdigest()},{role},Accepted\n"
    )
    return register


def test_latest_revised_group2_acceptance_governs(tmp_path):
    paths = build(tmp_path, [row("ADD", scope="NO")])
    _rebind(paths, [row("MODIFY", scope="NO")], "SCA-001_GROUP-2_AMENDMENT-1_2026-09-27")
    decision = check(tmp_path, paths["deliverable"])
    assert decision.admitted, decision
    assert decision.group2_manifest.endswith("SCA-001_GROUP-2_AMENDMENT-1_2026-09-27/ACCEPTED_MANIFEST.csv")
    assert decision.register_path.endswith("Amendment_Actions_R.csv")


def test_revised_group2_acceptance_can_withdraw_authorization(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")])
    _rebind(paths, [row("ADD", scope="NO")], "SCA-001_GROUP-2_AMENDMENT-1_2026-09-27")
    assert check(tmp_path, paths["deliverable"]).code == mod.ACTION_NOT_AUTHORIZING


def test_highest_amendment_number_governs_before_date(tmp_path):
    paths = build(tmp_path, [row("ADD", scope="NO")])
    _rebind(paths, [row("MODIFY", scope="NO")], "SCA-001_GROUP-2_AMENDMENT-2_2026-09-27", register_name="Amendment_Actions_R2.csv")
    _rebind(paths, [row("ADD", scope="NO")], "SCA-001_GROUP-2_AMENDMENT-1_2026-09-28", register_name="Amendment_Actions_R1.csv")
    decision = check(tmp_path, paths["deliverable"])
    assert decision.admitted, decision
    assert decision.register_path.endswith("Amendment_Actions_R2.csv")


def test_revised_group2_without_register_binding_keeps_earlier_binding(tmp_path):
    # PEC SCA-006 shape: GROUP-2_AMENDMENT-1 holds only DECISION.md.
    paths = build(tmp_path, [row("MODIFY", scope="NO")])
    folder = paths["root"] / "checkpoint_snapshots" / "SCA-001_GROUP-2_AMENDMENT-1_2026-09-27"
    folder.mkdir()
    (folder / "DECISION.md").write_text("# SCA-001 checkpoint group 2 — amendment 1: wording\n")
    assert check(tmp_path, paths["deliverable"]).admitted
    (folder / "ACCEPTED_MANIFEST.csv").write_text("Path,SHA256,Role\nsome/other.md," + "0" * 64 + ",context\n")
    decision = check(tmp_path, paths["deliverable"])
    assert decision.admitted
    assert decision.group2_manifest.endswith("SCA-001_GROUP-2_2026-09-26/ACCEPTED_MANIFEST.csv")


def test_register_hash_mismatch_refused(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")])
    with paths["register"].open("a") as handle:
        handle.write("SCA-001,9,MODIFY,DELIVERABLE,DEL-09-09,late edit,,,NO,NO\n")
    decision = check(tmp_path, paths["deliverable"])
    assert decision.code == mod.REGISTER_HASH_MISMATCH


def test_register_not_bound_refused(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")], register_name="Actions_Final.csv")
    assert check(tmp_path, paths["deliverable"]).code == mod.REGISTER_NOT_BOUND


def test_register_ambiguous_refused(tmp_path):
    other = f"{SC_REL}/SCA-001_2026-09-26_1200/Amendment_Actions_B.csv"
    paths = build(
        tmp_path,
        [row("MODIFY", scope="NO")],
        extra_manifest_rows=[f"{other},{'1' * 64},exact final action register,Accepted"],
    )
    assert check(tmp_path, paths["deliverable"]).code == mod.REGISTER_AMBIGUOUS


@pytest.mark.parametrize(
    "role",
    ["action register", "Action Register", "exact final action register (79 actions)"],
)
def test_role_matches_documented_values(tmp_path, role):
    intake = f"{SC_REL}/SCA-001_2026-09-26_1200/Amendment_Actions.csv"
    paths = build(
        tmp_path,
        [row("MODIFY", scope="NO")],
        register_name="Amendment_Actions_CP2.csv",
        extra_manifest_rows=[f"{intake},{'1' * 64},intake context,Context"],
    )
    manifest = paths["root"] / "checkpoint_snapshots" / "SCA-001_GROUP-2_2026-09-26" / "ACCEPTED_MANIFEST.csv"
    manifest.write_text(manifest.read_text().replace("exact final action register", role))
    decision = check(tmp_path, paths["deliverable"])
    assert decision.admitted, decision


@pytest.mark.parametrize(
    "decoy",
    ["NOT the action register (superseded)", "former action register", "action register draft", "action registers"],
)
def test_role_is_matched_as_a_whole_value(tmp_path, decoy):
    decoy_path = f"{SC_REL}/SCA-001_2026-09-26_1200/Amendment_Actions_EVIL.csv"
    paths = build(
        tmp_path,
        [row("REMOVE", scope="NO")],
        extra_manifest_rows=[f"{decoy_path},{'1' * 64},{decoy},Accepted"],
    )
    manifest = paths["root"] / "checkpoint_snapshots" / "SCA-001_GROUP-2_2026-09-26" / "ACCEPTED_MANIFEST.csv"
    # With the real row's Role changed, only the decoy mentions an action register.
    manifest.write_text(manifest.read_text().replace("exact final action register", "register copy"))
    assert check(tmp_path, paths["deliverable"]).code == mod.REGISTER_AMBIGUOUS


def test_bound_register_missing_refused(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")])
    paths["register"].unlink()
    assert check(tmp_path, paths["deliverable"]).code == mod.REGISTER_MISSING


# ---------------------------------------------------------------------------
# Refusals: action rows
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("action", ["ADD", "MERGE", "SPLIT"])
def test_other_actions_refused(tmp_path, action):
    paths = build(tmp_path, [row(action, scope="YES")])
    decision = check(tmp_path, paths["deliverable"])
    assert decision.code == mod.ACTION_NOT_AUTHORIZING
    assert action in decision.reason


@pytest.mark.parametrize("second", ["MODIFY", "RECLASSIFY"])
def test_remove_refused_even_with_another_authorizing_row(tmp_path, second):
    # PEC SCA-005 names DEL-07-02 with REMOVE (Seq 35) and MODIFY (Seq 66).
    paths = build(tmp_path, [row("REMOVE", scope="NO"), row(second, seq="2", scope="YES")])
    decision = check(tmp_path, paths["deliverable"])
    assert decision.code == mod.DELIVERABLE_REMOVED
    assert "ActionSeq 1" in decision.reason


def test_remove_of_a_labelled_entity_refused(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO"), row("REMOVE", entity="DEL-01-01_Fixture", seq="2", scope="NO")])
    assert check(tmp_path, paths["deliverable"]).code == mod.DELIVERABLE_REMOVED


def test_remove_of_another_deliverable_does_not_block(tmp_path):
    paths = build(tmp_path, [row("REMOVE", entity="DEL-01-02", scope="NO"), row("MODIFY", seq="2", scope="NO")])
    assert check(tmp_path, paths["deliverable"]).admitted


def test_reclassify_scope_changing_no_refused(tmp_path):
    paths = build(tmp_path, [row("RECLASSIFY", scope="NO")])
    assert check(tmp_path, paths["deliverable"]).code == mod.RECLASSIFY_NOT_SCOPE_CHANGING


def test_reclassify_scope_changing_blank_refused(tmp_path):
    paths = build(tmp_path, [row("RECLASSIFY", scope="")])
    assert check(tmp_path, paths["deliverable"]).code == mod.RECLASSIFY_NOT_SCOPE_CHANGING


def test_reclassify_in_legacy_register_refused(tmp_path):
    paths = build(tmp_path, [row("RECLASSIFY")], scope_column=False)
    decision = check(tmp_path, paths["deliverable"])
    assert decision.code == mod.RECLASSIFY_LEGACY_REGISTER
    assert "directly" in decision.reason


def test_non_deliverable_entity_refused(tmp_path):
    paths = build(tmp_path, [row("MODIFY", entity_type="OTHER", scope="NO")])
    assert check(tmp_path, paths["deliverable"]).code == mod.NO_DELIVERABLE_ACTION


def test_row_of_another_amendment_ignored(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO", amendment="SCA-009")])
    assert check(tmp_path, paths["deliverable"]).code == mod.NO_DELIVERABLE_ACTION


def test_blank_amendment_id_allowed(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO", amendment="")])
    assert check(tmp_path, paths["deliverable"]).admitted


def test_amendment_id_must_equal_exactly(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO", amendment="SCA-0010")])
    assert check(tmp_path, paths["deliverable"]).code == mod.NO_DELIVERABLE_ACTION


@pytest.mark.parametrize(
    "field,value",
    [
        ("entity", "DEL-01-01 "),
        ("entity", " DEL-01-01"),
        ("scope", "YES "),
        ("amendment", "SCA-001 "),
        ("action", "MODIFY "),
    ],
)
def test_stray_whitespace_in_register_values_refused(tmp_path, field, value):
    # No accepted register in the repository carries such whitespace (checked
    # 2026-09-26), so a padded value is a schema error, not a tolerated variant.
    kwargs = {"scope": "YES"}
    action = "RECLASSIFY"
    if field == "action":
        action = value
    elif field == "scope":
        kwargs["scope"] = value
    else:
        kwargs[field] = value
    paths = build(tmp_path, [row(action, **kwargs)])
    decision = check(tmp_path, paths["deliverable"])
    assert decision.code == mod.REGISTER_SCHEMA
    assert repr(value) in decision.reason


def test_stray_whitespace_in_register_column_name_refused(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")])
    text = paths["register"].read_text().replace("ScopeChanging", "ScopeChanging ", 1)
    paths["register"].write_text(text)
    sha = hashlib.sha256(paths["register"].read_bytes()).hexdigest()
    manifest = paths["root"] / "checkpoint_snapshots" / "SCA-001_GROUP-2_2026-09-26" / "ACCEPTED_MANIFEST.csv"
    lines = manifest.read_text().splitlines()
    lines[-1] = ",".join([lines[-1].split(",")[0], sha, *lines[-1].split(",")[2:]])
    manifest.write_text("\n".join(lines) + "\n")
    assert check(tmp_path, paths["deliverable"]).code == mod.REGISTER_SCHEMA


# ---------------------------------------------------------------------------
# Containment
# ---------------------------------------------------------------------------


def test_manifest_path_escape_refused(tmp_path):
    project = tmp_path / "project"
    outside = tmp_path / "outside"
    outside.mkdir()
    (outside / "Amendment_Actions.csv").write_text(_csv(BASE_COLUMNS, [row("MODIFY")]))
    paths = build(project, [row("MODIFY", scope="NO")], manifest_path_override="../outside/Amendment_Actions.csv")
    decision = check(project, paths["deliverable"])
    assert decision.code == mod.PATH_ESCAPE


def test_manifest_path_outside_scope_change_root_refused(tmp_path):
    other = tmp_path / "projects" / "other" / "Amendment_Actions.csv"
    other.parent.mkdir(parents=True)
    other.write_text(_csv(BASE_COLUMNS + ["ScopeChanging"], [row("MODIFY", scope="YES")]))
    paths = build(tmp_path, [row("MODIFY", scope="NO")], manifest_path_override="projects/other/Amendment_Actions.csv")
    assert check(tmp_path, paths["deliverable"]).code == mod.PATH_ESCAPE


def test_symlinked_register_escape_refused(tmp_path):
    project = tmp_path / "project"
    paths = build(project, [row("MODIFY", scope="NO")])
    outside = tmp_path / "outside.csv"
    outside.write_bytes(paths["register"].read_bytes())
    paths["register"].unlink()
    os.symlink(outside, paths["register"])
    assert check(project, paths["deliverable"]).code == mod.PATH_ESCAPE


def test_symlinked_checkpoint_snapshots_escape_refused(tmp_path):
    project = tmp_path / "project"
    paths = build(project, [row("MODIFY", scope="NO")])
    snapshots = paths["root"] / "checkpoint_snapshots"
    moved = tmp_path / "moved_snapshots"
    snapshots.rename(moved)
    os.symlink(moved, snapshots)
    assert check(project, paths["deliverable"]).code == mod.PATH_ESCAPE


def test_amendment_path_outside_project_refused(tmp_path):
    project = tmp_path / "project"
    paths = build(project, [row("MODIFY", scope="NO")])
    elsewhere = build(tmp_path / "elsewhere", [row("MODIFY", scope="NO")])
    decision = check(project, paths["deliverable"], amendment=str(elsewhere["snapshot"]))
    assert decision.code == mod.PATH_ESCAPE


def test_nested_scope_change_in_deliverable_folder_is_not_used(tmp_path):
    paths = build(tmp_path, [row("REMOVE", scope="NO")])
    nested = paths["deliverable"] / "_ScopeChange"
    shutil.copytree(paths["root"], nested)
    register = nested / "SCA-001_2026-09-26_1200" / "Amendment_Actions.csv"
    register.write_text(register.read_text().replace("REMOVE", "MODIFY"))
    manifest = nested / "checkpoint_snapshots" / "SCA-001_GROUP-2_2026-09-26" / "ACCEPTED_MANIFEST.csv"
    manifest.write_text(
        f"Path,SHA256,Role\n{register.relative_to(tmp_path).as_posix()},"
        f"{hashlib.sha256(register.read_bytes()).hexdigest()},exact final action register\n"
    )
    decision = check(tmp_path, paths["deliverable"])
    assert decision.scope_change_root == SC_REL
    assert decision.code == mod.DELIVERABLE_REMOVED
    pinned = check(tmp_path, paths["deliverable"], amendment=str(nested / "checkpoint_snapshots" / "SCA-001_GROUP-3_2026-09-26"))
    assert pinned.code == mod.AMENDMENT_OUTSIDE_DELIVERABLE_ROOT
    given = check(tmp_path, paths["deliverable"], scope_change_root=nested)
    assert given.code == mod.AMENDMENT_OUTSIDE_DELIVERABLE_ROOT


def test_nested_scope_change_in_package_folder_is_not_used(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")])
    package = paths["deliverable"].parent.parent
    (package / "_ScopeChange" / "checkpoint_snapshots").mkdir(parents=True)
    decision = check(tmp_path, paths["deliverable"])
    assert decision.admitted, decision
    assert decision.scope_change_root == SC_REL
    assert decision.execution_root == "projects/fixture/execution"


def test_adapter_must_imply_the_same_execution_root(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")])
    (tmp_path / "projects" / "fixture" / "_harness").mkdir()
    (tmp_path / "projects" / "fixture" / "_harness" / "adapter.yaml").write_text("schema: fixture\n")
    assert check(tmp_path, paths["deliverable"]).admitted
    package_adapter = paths["deliverable"].parent.parent / "_harness"
    package_adapter.mkdir()
    (package_adapter / "adapter.yaml").write_text("schema: fixture\n")
    assert check(tmp_path, paths["deliverable"]).code == mod.SCOPE_CHANGE_ROOT_NOT_FOUND


def test_deliverable_outside_an_execution_folder_needs_a_root(tmp_path):
    folder = tmp_path / "projects" / "loose" / "DEL-09-01_Loose"
    folder.mkdir(parents=True)
    assert check(tmp_path, folder).code == mod.SCOPE_CHANGE_ROOT_NOT_FOUND


def test_amendment_of_another_execution_root_refused(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")])
    other_root = tmp_path / "projects" / "other" / "execution" / "_ScopeChange"
    other_root.mkdir(parents=True)
    decision = check(tmp_path, paths["deliverable"], scope_change_root=other_root)
    assert decision.code == mod.AMENDMENT_OUTSIDE_DELIVERABLE_ROOT


def test_unresolvable_amendment_refused(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")])
    assert check(tmp_path, paths["deliverable"], amendment="no/such/path").code == mod.AMENDMENT_UNRESOLVED


def test_deliverable_id_without_root_refused(tmp_path):
    build(tmp_path, [row("MODIFY", scope="NO")])
    assert check(tmp_path, "DEL-01-01").code == mod.SCOPE_CHANGE_ROOT_NOT_FOUND


def test_prior_reopening_under_the_same_amendment_refused(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")])
    status = paths["deliverable"] / "_STATUS.md"
    status.write_text(
        status.read_text()
        + "\n## History\n- 2026-09-26 — State set to IN_PROGRESS (human) [reopened from ISSUED; amendment: SCA-001 "
        "(x); action: y ActionSeq 1 MODIFY; approval SHA: abc1234]\n"
    )
    decision = check(tmp_path, paths["deliverable"], status_file=status)
    assert decision.code == mod.AMENDMENT_ALREADY_USED
    assert check(tmp_path, paths["deliverable"]).admitted  # without the status file


def test_prior_reopening_under_another_amendment_does_not_block(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")])
    status = paths["deliverable"] / "_STATUS.md"
    status.write_text(
        status.read_text() + "- 2026-09-20 — State set to IN_PROGRESS (human) [reopened from ISSUED; amendment: SCA-0010 (x)]\n"
        "- 2026-09-21 — reopened from ISSUED; amendment: SCA-001-2 recorded elsewhere\n"
    )
    assert check(tmp_path, paths["deliverable"], status_file=status).admitted


def test_invalid_deliverable_is_usage_error(tmp_path):
    with pytest.raises(mod.UsageError):
        check(tmp_path, "not-a-deliverable")


# ---------------------------------------------------------------------------
# At-commit mode: every record is read from the commit (B1)
# ---------------------------------------------------------------------------


def git(project: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid", *args],
        cwd=project,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def commit_all(project: Path, message: str = "fixture") -> str:
    if not (project / ".git").exists():
        git(project, "init", "-q")
    git(project, "add", "-A")
    git(project, "commit", "-q", "--allow-empty", "-m", message)
    return git(project, "rev-parse", "HEAD")


def rebind_group2(project: Path, paths: dict) -> None:
    """Rewrite the group-2 manifest's register hash to the register's current bytes."""
    manifest = paths["root"] / "checkpoint_snapshots" / "SCA-001_GROUP-2_2026-09-26" / "ACCEPTED_MANIFEST.csv"
    register_rel = paths["register"].relative_to(project).as_posix()
    sha = hashlib.sha256(paths["register"].read_bytes()).hexdigest()
    lines = [
        ",".join([register_rel, sha, *line.split(",")[2:]]) if line.startswith(register_rel + ",") else line
        for line in manifest.read_text().splitlines()
    ]
    manifest.write_text("\n".join(lines) + "\n")


def test_at_commit_admitted_and_anchored(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")])
    head = commit_all(tmp_path)
    decision = check(tmp_path, paths["deliverable"], at_commit=head)
    assert decision.admitted, decision
    assert decision.anchored and decision.mode == "at-commit"
    assert decision.at_commit == head
    assert f"at commit {head}" in decision.reason
    assert mod.UNANCHORED_NOTE not in decision.notes
    short = check(tmp_path, paths["deliverable"], at_commit=head[:9])
    assert short.admitted and short.at_commit == head


def test_working_tree_mode_says_it_is_unanchored(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")])
    decision = check(tmp_path, paths["deliverable"])
    assert decision.admitted
    assert not decision.anchored and decision.mode == "working-tree" and decision.at_commit == ""
    assert mod.UNANCHORED_NOTE in decision.notes
    assert "unanchored" in decision.reason


def test_attack_a_uncommitted_register_and_manifest_edit_refused_at_commit(tmp_path):
    # Reviewer attack A: committed register says REMOVE; the working tree flips
    # it to MODIFY and rewrites the group-2 hash to match.
    paths = build(tmp_path, [row("REMOVE", scope="NO")])
    head = commit_all(tmp_path)
    paths["register"].write_text(paths["register"].read_text().replace("REMOVE", "MODIFY"))
    rebind_group2(tmp_path, paths)
    assert check(tmp_path, paths["deliverable"]).admitted  # the unanchored read is fooled
    decision = check(tmp_path, paths["deliverable"], at_commit=head)
    assert decision.code == mod.DELIVERABLE_REMOVED


def test_attack_a_uncommitted_register_edit_alone_refused_at_commit(tmp_path):
    paths = build(tmp_path, [row("ADD", scope="NO")])
    head = commit_all(tmp_path)
    paths["register"].write_text(paths["register"].read_text().replace("ADD", "MODIFY"))
    rebind_group2(tmp_path, paths)
    assert check(tmp_path, paths["deliverable"], at_commit=head).code == mod.ACTION_NOT_AUTHORIZING


def test_attack_b_uncommitted_heading_flip_refused_at_commit(tmp_path):
    # Reviewer attack B: the committed group-3 heading says returned; the
    # working tree says accepted.
    paths = build(tmp_path, [row("MODIFY", scope="NO")], group3_heading="SCA-001 checkpoint group 3 — returned by owner")
    head = commit_all(tmp_path)
    decision_md = paths["root"] / "checkpoint_snapshots" / "SCA-001_GROUP-3_2026-09-26" / "DECISION.md"
    decision_md.write_text("# SCA-001 checkpoint group 3 — accepted\n")
    assert check(tmp_path, paths["deliverable"]).admitted
    decision = check(tmp_path, paths["deliverable"], at_commit=head)
    assert decision.code == mod.GROUP3_NOT_ACCEPTED
    assert "returned by owner" in decision.reason


def test_git_replace_refs_do_not_change_what_is_read_at_commit(tmp_path):
    # Reviewer probe: `git replace` a committed REMOVE register (and its
    # manifest) with forged MODIFY copies. The at-commit read must ignore
    # local replace refs and still see the committed bytes.
    paths = build(tmp_path, [row("REMOVE", scope="NO")])
    head = commit_all(tmp_path)
    manifest = paths["root"] / "checkpoint_snapshots" / "SCA-001_GROUP-2_2026-09-26" / "ACCEPTED_MANIFEST.csv"
    register_rel = paths["register"].relative_to(tmp_path).as_posix()
    manifest_rel = manifest.relative_to(tmp_path).as_posix()
    old_register = git(tmp_path, "rev-parse", f"{head}:{register_rel}")
    old_manifest = git(tmp_path, "rev-parse", f"{head}:{manifest_rel}")
    paths["register"].write_text(paths["register"].read_text().replace("REMOVE", "MODIFY"))
    rebind_group2(tmp_path, paths)
    new_register = git(tmp_path, "hash-object", "-w", str(paths["register"]))
    new_manifest = git(tmp_path, "hash-object", "-w", str(manifest))
    git(tmp_path, "replace", old_register, new_register)
    git(tmp_path, "replace", old_manifest, new_manifest)
    git(tmp_path, "checkout", "-q", "--", ".")
    assert git(tmp_path, "cat-file", "-p", f"{head}:{register_rel}").count("MODIFY") >= 1  # replace is live
    decision = check(tmp_path, paths["deliverable"], at_commit=head)
    assert decision.code == mod.DELIVERABLE_REMOVED


def test_git_graft_does_not_make_a_side_commit_an_ancestor(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")], groups=("1", "2"))
    base = commit_all(tmp_path)
    git(tmp_path, "checkout", "-q", "-b", "side")
    group3 = paths["root"] / "checkpoint_snapshots" / "SCA-001_GROUP-3_2026-09-26"
    group3.mkdir()
    (group3 / "DECISION.md").write_text("# SCA-001 checkpoint group 3 — accepted\n")
    (group3 / "ACCEPTED_MANIFEST.csv").write_text("Path,SHA256\n")
    side = commit_all(tmp_path, "forged side")
    git(tmp_path, "checkout", "-q", "-")
    git(tmp_path, "replace", "--graft", "HEAD", base, side)
    decision = check(tmp_path, paths["deliverable"], at_commit=side)
    assert decision.code == mod.APPROVAL_SHA_NOT_ANCESTOR


def test_untracked_forged_group3_folder_does_not_count_at_commit(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")], groups=("1", "2"))
    head = commit_all(tmp_path)
    forged = paths["root"] / "checkpoint_snapshots" / "SCA-001_GROUP-3_2026-09-26"
    forged.mkdir()
    (forged / "DECISION.md").write_text("# SCA-001 checkpoint group 3 — accepted\n")
    (forged / "ACCEPTED_MANIFEST.csv").write_text("Path,SHA256\n")
    assert check(tmp_path, paths["deliverable"]).admitted
    decision = check(tmp_path, paths["deliverable"], at_commit=head)
    assert decision.code == mod.GROUP3_NOT_ACCEPTED
    assert "at the commit" in decision.reason
    pinned = check(tmp_path, paths["deliverable"], amendment=str(forged), at_commit=head)
    assert pinned.code == mod.AMENDMENT_UNRESOLVED


def test_uncommitted_revised_group2_binding_does_not_count_at_commit(tmp_path):
    paths = build(tmp_path, [row("ADD", scope="NO")])
    head = commit_all(tmp_path)
    _rebind(paths, [row("MODIFY", scope="NO")], "SCA-001_GROUP-2_AMENDMENT-1_2026-09-27")
    assert check(tmp_path, paths["deliverable"]).admitted
    assert check(tmp_path, paths["deliverable"], at_commit=head).code == mod.ACTION_NOT_AUTHORIZING


def test_side_branch_commit_refused(tmp_path):
    # Reviewer item 5: a forged group-3 committed on an unmerged side branch.
    paths = build(tmp_path, [row("MODIFY", scope="NO")], groups=("1", "2"))
    commit_all(tmp_path)
    git(tmp_path, "checkout", "-q", "-b", "side")
    forged = paths["root"] / "checkpoint_snapshots" / "SCA-001_GROUP-3_2026-09-26"
    forged.mkdir()
    (forged / "DECISION.md").write_text("# SCA-001 checkpoint group 3 — accepted\n")
    (forged / "ACCEPTED_MANIFEST.csv").write_text("Path,SHA256\n")
    side = commit_all(tmp_path, "forged")
    assert check(tmp_path, paths["deliverable"], at_commit=side).admitted  # on the side branch itself
    git(tmp_path, "checkout", "-q", "-")
    decision = check(tmp_path, paths["deliverable"], at_commit=side)
    assert decision.code == mod.APPROVAL_SHA_NOT_ANCESTOR


def test_unreachable_commit_refused(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")])
    commit_all(tmp_path)
    for value in ("deadbeefdeadbeefdeadbeefdeadbeefdeadbeef", "--output=x", ""):
        assert check(tmp_path, paths["deliverable"], at_commit=value).code == mod.APPROVAL_SHA_UNREACHABLE


def test_at_commit_needs_the_git_top_level(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")])
    head = commit_all(tmp_path)
    with pytest.raises(mod.UsageError):
        mod.check_reopen(str(paths["deliverable"]), "SCA-001", project_root=tmp_path / "projects", cwd=tmp_path, at_commit=head)


def test_at_commit_hash_mismatch_committed(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")])
    with paths["register"].open("a") as handle:
        handle.write("SCA-001,9,ADD,OTHER,X,late edit,,,NO,NO\n")
    head = commit_all(tmp_path)
    assert check(tmp_path, paths["deliverable"], at_commit=head).code == mod.REGISTER_HASH_MISMATCH


def test_at_commit_symlink_escape_in_tree_refused(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")])
    outside = tmp_path / "projects" / "fixture" / "Amendment_Actions.csv"
    outside.write_bytes(paths["register"].read_bytes())
    paths["register"].unlink()
    os.symlink("../../../Amendment_Actions.csv", paths["register"])  # leaves _ScopeChange, stays in the project
    head = commit_all(tmp_path)
    assert check(tmp_path, paths["deliverable"], at_commit=head).code == mod.PATH_ESCAPE


def test_at_commit_absolute_symlink_refused(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")])
    outside = tmp_path.parent / f"{tmp_path.name}_outside.csv"
    outside.write_bytes(paths["register"].read_bytes())
    paths["register"].unlink()
    os.symlink(outside, paths["register"])
    head = commit_all(tmp_path)
    assert check(tmp_path, paths["deliverable"], at_commit=head).code == mod.PATH_ESCAPE


def test_at_commit_symlinked_snapshots_escape_refused(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")])
    snapshots = paths["root"] / "checkpoint_snapshots"
    moved = tmp_path / "projects" / "fixture" / "moved_snapshots"
    snapshots.rename(moved)
    os.symlink("../../moved_snapshots", snapshots)
    head = commit_all(tmp_path)
    assert check(tmp_path, paths["deliverable"], at_commit=head).code == mod.PATH_ESCAPE


def test_at_commit_symlink_inside_root_followed(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")])
    real = paths["snapshot"] / "Amendment_Actions_real.csv"
    paths["register"].rename(real)
    os.symlink("Amendment_Actions_real.csv", paths["register"])
    head = commit_all(tmp_path)
    decision = check(tmp_path, paths["deliverable"], at_commit=head)
    assert decision.admitted, decision
    assert decision.register_path.endswith("Amendment_Actions_real.csv")


def test_at_commit_nested_scope_change_is_not_used(tmp_path):
    paths = build(tmp_path, [row("REMOVE", scope="NO")])
    nested = paths["deliverable"] / "_ScopeChange"
    shutil.copytree(paths["root"], nested)
    register = nested / "SCA-001_2026-09-26_1200" / "Amendment_Actions.csv"
    register.write_text(register.read_text().replace("REMOVE", "MODIFY"))
    manifest = nested / "checkpoint_snapshots" / "SCA-001_GROUP-2_2026-09-26" / "ACCEPTED_MANIFEST.csv"
    manifest.write_text(
        f"Path,SHA256,Role\n{register.relative_to(tmp_path).as_posix()},"
        f"{hashlib.sha256(register.read_bytes()).hexdigest()},exact final action register\n"
    )
    head = commit_all(tmp_path)
    assert check(tmp_path, paths["deliverable"], at_commit=head).code == mod.DELIVERABLE_REMOVED


def test_at_commit_amendment_path_resolved_in_the_tree(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")])
    head = commit_all(tmp_path)
    group3 = f"{SC_REL}/checkpoint_snapshots/SCA-001_GROUP-3_2026-09-26"
    assert check(tmp_path, paths["deliverable"], amendment=group3, at_commit=head).admitted
    assert check(tmp_path, paths["deliverable"], amendment=f"{group3}/DECISION.md", at_commit=head).admitted
    shutil.rmtree(tmp_path / group3)  # deleted from the working tree, still in the commit
    assert check(tmp_path, paths["deliverable"], amendment=group3, at_commit=head).admitted


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def run_cli(cwd: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(SCRIPT), *args], cwd=cwd, capture_output=True, text=True)


def test_cli_exit_codes_and_json(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")])
    ok = run_cli(tmp_path, "--deliverable", DEL_REL, "--amendment", "SCA-001", "--project-root", str(tmp_path), "--json")
    assert ok.returncode == 0, ok.stderr
    assert json.loads(ok.stdout)["code"] == "ADMITTED"

    refused = run_cli(tmp_path, "--deliverable", DEL_REL, "--amendment", "SCA-002", "--project-root", str(tmp_path))
    assert refused.returncode == 1
    assert refused.stderr.startswith("REFUSE GROUP3_NOT_ACCEPTED:")

    usage = run_cli(tmp_path, "--deliverable", "bogus", "--amendment", "SCA-001", "--project-root", str(tmp_path))
    assert usage.returncode == 2
    assert paths["deliverable"].is_dir()


def test_cli_modes_label_their_anchoring(tmp_path):
    build(tmp_path, [row("MODIFY", scope="NO")])
    head = commit_all(tmp_path)
    loose = run_cli(tmp_path, "--deliverable", DEL_REL, "--amendment", "SCA-001")
    assert loose.returncode == 0, loose.stderr
    assert loose.stdout.startswith("ADMIT (UNANCHORED working-tree read")
    anchored = run_cli(tmp_path, "--deliverable", DEL_REL, "--amendment", "SCA-001", "--at-commit", head, "--json")
    assert anchored.returncode == 0, anchored.stderr
    data = json.loads(anchored.stdout)
    assert data["anchored"] is True and data["at_commit"] == head and data["mode"] == "at-commit"
    refused = run_cli(tmp_path, "--deliverable", DEL_REL, "--amendment", "SCA-002")
    assert refused.returncode == 1
    assert refused.stderr.rstrip().endswith("[working tree, unanchored]")


def test_refusal_codes_are_listed():
    codes = {value for name, value in vars(mod).items() if name.isupper() and isinstance(value, str) and value == name}
    codes.discard(mod.ADMITTED)
    assert set(mod.REFUSAL_CODES) == codes
    assert len(mod.REFUSAL_CODES) == len(set(mod.REFUSAL_CODES)) == 20


# ---------------------------------------------------------------------------
# Real accepted amendment records, read at HEAD (skipped when absent)
# ---------------------------------------------------------------------------


PEC_EXEC = "projects/pec/execution"
PEC_DEL = f"{PEC_EXEC}/PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access"
PEC_GROUP3 = f"{PEC_EXEC}/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-3_2026-09-26"
PEC_SCA005_GROUP3 = f"{PEC_EXEC}/_ScopeChange/checkpoint_snapshots/SCA-005_GROUP-3_2026-09-25"


def real(deliverable, amendment, **kwargs):
    return mod.check_reopen(deliverable, amendment, project_root=REPO_ROOT, cwd=REPO_ROOT, at_commit="HEAD", **kwargs)


def _tracked(path: str) -> bool:
    out = subprocess.run(["git", "-C", str(REPO_ROOT), "ls-files", "--error-unmatch", path], capture_output=True)
    return out.returncode == 0


@pytest.mark.skipif(not _tracked(f"{PEC_GROUP3}/DECISION.md") or not (REPO_ROOT / PEC_DEL).is_dir(), reason="PEC records not in this checkout")
def test_real_pec_sca006_records():
    admitted = real(PEC_DEL, "SCA-006")
    assert admitted.admitted, admitted
    assert admitted.register_path.endswith("SCA-006_2026-09-25_1912/Amendment_Actions_CP2.csv")
    # GROUP-2_AMENDMENT-1 records no manifest, so the original binding governs.
    assert admitted.group2_manifest.endswith("SCA-006_GROUP-2_2026-09-25/ACCEPTED_MANIFEST.csv")
    assert admitted.action_type == "MODIFY"
    assert admitted.scope_changing is None  # accepted before the ScopeChanging column

    added = mod.check_reopen("DEL-08-06", PEC_GROUP3, project_root=REPO_ROOT, cwd=REPO_ROOT, at_commit="HEAD")
    assert added.code == mod.ACTION_NOT_AUTHORIZING  # ADD, not MODIFY


@pytest.mark.skipif(not _tracked(f"{PEC_SCA005_GROUP3}/DECISION.md"), reason="PEC records not in this checkout")
def test_real_pec_sca005_removed_deliverable_refused():
    # SCA-005 names DEL-07-02 with REMOVE (Seq 35) and MODIFY (Seq 66).
    decision = mod.check_reopen(
        "DEL-07-02", "SCA-005", scope_change_root=REPO_ROOT / PEC_EXEC / "_ScopeChange",
        project_root=REPO_ROOT, cwd=REPO_ROOT, at_commit="HEAD",
    )
    assert decision.code == mod.DELIVERABLE_REMOVED
    assert "35" in decision.reason


PIPING_ROOT = "projects/chirality-piping/execution/_ScopeChange"


@pytest.mark.skipif(not (REPO_ROOT / PIPING_ROOT / "checkpoint_snapshots").is_dir(), reason="Piping records not in this checkout")
def test_real_piping_group2_only_amendment_refused():
    decision = mod.check_reopen(
        "DEL-04-07", "SCA-011", scope_change_root=REPO_ROOT / PIPING_ROOT, project_root=REPO_ROOT, cwd=REPO_ROOT,
        at_commit="HEAD",
    )
    assert decision.code == mod.GROUP3_NOT_ACCEPTED


RUNTIME_ROOT = "projects/chirality-runtime/execution/_ScopeChange"


@pytest.mark.skipif(not (REPO_ROOT / RUNTIME_ROOT).is_dir(), reason="Runtime records not in this checkout")
def test_real_runtime_amendment_without_decision_snapshots_refused():
    decision = mod.check_reopen(
        "DEL-01-01", "SCA-001", scope_change_root=REPO_ROOT / RUNTIME_ROOT, project_root=REPO_ROOT, cwd=REPO_ROOT,
        at_commit="HEAD",
    )
    assert decision.code == mod.GROUP3_NOT_ACCEPTED

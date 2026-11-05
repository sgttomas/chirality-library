"""Tests for validate_scope_change_packet.py checkpoint-column naming."""

from __future__ import annotations

from pathlib import Path

import validate_scope_change_packet as vscp

ACTION_PREFIX = "PacketID,ActionSeq,ActionType,EntityType,EntityID,Description,AffectedDeliverables,AffectedFiles,EvidenceRefs"


def make_packet(root: Path, checkpoint_column: str | None) -> Path:
    packet = root / "PKT-001"
    packet.mkdir()
    for name in vscp.REQUIRED_FILES:
        if name.endswith(".md"):
            (packet / name).write_text("# stub\n", encoding="utf-8")
    (packet / "SCOPE_CHANGE_INIT.md").write_text(
        "Not valid until the human explicitly initiates scope-change.\n",
        encoding="utf-8",
    )
    columns = ACTION_PREFIX + (f",{checkpoint_column}" if checkpoint_column else "") + ",Status"
    row = "PKT-001,1,MODIFY,Deliverable,TBD,Example,TBD,TBD,EV-001"
    row += ",CHECKPOINT_GROUP_1" if checkpoint_column else ""
    row += ",PROPOSED"
    (packet / "Proposed_SCA_Actions.csv").write_text(f"{columns}\n{row}\n", encoding="utf-8")
    (packet / "Affected_Surfaces.csv").write_text(
        ",".join(vscp.SURFACE_COLUMNS) + "\n", encoding="utf-8"
    )
    (packet / "Evidence_Index.csv").write_text(
        ",".join(vscp.EVIDENCE_COLUMNS) + "\nEV-001,src.md,L1,DOC,1,\n",
        encoding="utf-8",
    )
    return packet


def test_current_checkpoint_column_passes(tmp_path: Path) -> None:
    packet = make_packet(tmp_path, "SCOPE_CHANGE_Checkpoint")
    assert vscp.validate_packet(packet) == []


def test_legacy_gate_column_is_accepted_on_read(tmp_path: Path) -> None:
    packet = make_packet(tmp_path, "SCOPE_CHANGE_Gate")
    assert vscp.validate_packet(packet) == []


def test_missing_checkpoint_column_names_current_column(tmp_path: Path) -> None:
    packet = make_packet(tmp_path, None)
    errors = vscp.validate_packet(packet)
    assert errors == ["Proposed_SCA_Actions.csv missing columns: SCOPE_CHANGE_Checkpoint"]

"""Tests for the shared surface classification and portability policy.

`validate_path_anchors.py` consumes `surface_roles.py`; these tests exercise
its classification and hash-bound exception ledger directly.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

from surface_roles import (
    SurfaceRole,
    classify_surface,
    load_project_policy,
    normalize_repo_relative_path,
)


PROJECT_REL = "projects/chirality-piping"
AGENTRUN = (
    "projects/chirality-piping/execution/_Coordination/AgentRuns/R10"
)
ABS = "/Users/fixture/worktree/projects/chirality-piping"


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _repo(tmp_path: Path) -> Path:
    repo = tmp_path / "repo"
    (repo / PROJECT_REL).mkdir(parents=True)
    return repo


def _policy(repo: Path, overrides=None, exceptions=None) -> Path:
    path = repo / PROJECT_REL / "validation" / "portability_policy.json"
    _write(path, json.dumps({
        "schema_version": 1,
        "project_root": PROJECT_REL,
        "historical_role_overrides": overrides or [],
        "control_path_exceptions": exceptions or [],
    }, indent=2) + "\n")
    return path


def _entry(repo: Path, rel: str, entry_type: str, role: str) -> dict[str, str]:
    return {
        "path": rel,
        "sha256": hashlib.sha256((repo / rel).read_bytes()).hexdigest(),
        "entry_type": entry_type,
        "role": role,
        "reason": "Immutable fixture migration record.",
        "authority": "Fixture owner approval.",
    }


def test_structural_roles_use_control_precedence_and_fail_closed():
    assert classify_surface(f"{AGENTRUN}/LAUNCH_BRIEF.md").role is SurfaceRole.CONTROL
    assert classify_surface(f"{AGENTRUN}/RETURN.md").role is SurfaceRole.EVIDENCE
    assert classify_surface(
        f"{AGENTRUN}/_run_records/LAUNCH_BRIEF.md").role is SurfaceRole.CONTROL
    unknown = classify_surface(f"{AGENTRUN}/CAPTURE.json")
    assert unknown.role is SurfaceRole.UNCLASSIFIED
    assert unknown.active is True
    assert classify_surface(f"{AGENTRUN}/PREFLIGHT_FINAL.json").role is (
        SurfaceRole.UNCLASSIFIED)
    assert classify_surface(f"{AGENTRUN}/RETURNED.md").role is (
        SurfaceRole.UNCLASSIFIED)
    assert classify_surface(f"{AGENTRUN}/LAUNCH_BRIEF.md.bak").role is (
        SurfaceRole.UNCLASSIFIED)
    assert classify_surface(
        "projects/example/execution/_Coordination/WorkGraphs/run-1/WORK_GRAPH.md"
    ).role is SurfaceRole.CONTROL


@pytest.mark.parametrize("name", [
    "NOT_A_RETURN.md",
    "RETURN_INSTRUCTIONS.md",
    "HANDOFF_INSTRUCTIONS.md",
    "SECRET_SUMMARY.md",
    "ARBITRARY_RESULT.json",
    "UNREGISTERED_MANIFEST.yaml",
])
def test_misleading_evidence_token_names_remain_unclassified(name: str):
    classification = classify_surface(f"{AGENTRUN}/{name}")
    assert classification.role is SurfaceRole.UNCLASSIFIED
    assert classification.active is True


@pytest.mark.parametrize("name", [
    "RETURN.md",
    "RETURN_V1.md",
    "RETURN_V12.md",
    "HANDOFF_STATE.md",
    "STATUS.json",
    "STATUS_V2.json",
    "RUN_RECORD.md",
    "INTERRUPTION_RECORD.md",
    "TOOL_ERROR_RECORD.md",
])
def test_exact_registered_evidence_records_are_evidence(name: str):
    assert classify_surface(f"{AGENTRUN}/{name}").role is SurfaceRole.EVIDENCE


@pytest.mark.parametrize("name", [
    "return.md",
    "Return.md",
    "status.json",
    "STATUS_V0.json",
    "STATUS_V01.json",
    "RETURN_V1.JSON",
    "RETURN_V1.json",
    "STATUS_V1.md",
    "RETURN.md.bak",
    "ARBITRARY.txt",
])
def test_case_near_matches_and_unknown_extensions_fail_closed(name: str):
    assert classify_surface(f"{AGENTRUN}/{name}").role is SurfaceRole.UNCLASSIFIED


@pytest.mark.parametrize("value", [
    "/projects/example/file.md",
    "projects/example/../file.md",
    "projects/example/./file.md",
    "projects//example/file.md",
    r"projects\example\file.md",
])
def test_path_normalization_rejects_noncanonical_values(value: str):
    with pytest.raises(ValueError):
        normalize_repo_relative_path(value)


def test_ledger_rejects_duplicate_missing_authority_and_stale_entry(tmp_path: Path):
    repo = _repo(tmp_path)
    rel = f"{AGENTRUN}/CAPTURE.json"
    _write(repo / rel, "portable capture\n")
    entry = _entry(repo, rel, "historical_role_override", "EVIDENCE")
    entry["authority"] = ""
    _policy(repo, [entry, dict(entry)])

    codes = {issue.code for issue in load_project_policy(
        repo, repo / PROJECT_REL).issues}

    assert "PORTABILITY_POLICY_SCHEMA" in codes
    assert "PORTABILITY_POLICY_DUPLICATE" in codes


def test_stale_override_and_non_normalized_path_are_rejected(tmp_path: Path):
    repo = _repo(tmp_path)
    rel = f"{AGENTRUN}/CAPTURE.json"
    _write(repo / rel, "portable capture\n")
    stale = _entry(repo, rel, "historical_role_override", "EVIDENCE")
    bad_path = dict(stale)
    bad_path["path"] = f"{PROJECT_REL}/validation/../CAPTURE.json"
    _policy(repo, [stale, bad_path])

    codes = {issue.code for issue in load_project_policy(
        repo, repo / PROJECT_REL).issues}

    assert "PORTABILITY_POLICY_STALE" in codes
    assert "PORTABILITY_POLICY_PATH" in codes


def test_missing_target_and_structural_role_mismatch_are_rejected(tmp_path: Path):
    repo = _repo(tmp_path)
    return_rel = f"{AGENTRUN}/RETURN.md"
    _write(repo / return_rel, f"Ran at {ABS}\n")
    wrong_role = _entry(
        repo, return_rel, "historical_role_override", "EVIDENCE")
    missing = {
        "path": f"{AGENTRUN}/MISSING.json",
        "sha256": "0" * 64,
        "entry_type": "historical_role_override",
        "role": "EVIDENCE",
        "reason": "Missing fixture target.",
        "authority": "Fixture owner approval.",
    }
    _policy(repo, [wrong_role, missing])

    codes = {issue.code for issue in load_project_policy(
        repo, repo / PROJECT_REL).issues}

    assert "PORTABILITY_POLICY_ROLE_MISMATCH" in codes
    assert "PORTABILITY_POLICY_TARGET_MISSING" in codes


def test_hash_bound_role_override_and_control_exception(tmp_path: Path):
    repo = _repo(tmp_path)
    capture_rel = f"{AGENTRUN}/CAPTURE.json"
    control_rel = f"{AGENTRUN}/ORCHESTRATION_PLAN.md"
    _write(repo / capture_rel, json.dumps({"cwd": ABS}) + "\n")
    _write(repo / control_rel, f"Historical root: {ABS}\n")
    _policy(
        repo,
        [_entry(repo, capture_rel, "historical_role_override", "EVIDENCE")],
        [_entry(repo, control_rel, "control_path_exception", "CONTROL")],
    )

    loaded = load_project_policy(repo, repo / PROJECT_REL)
    assert loaded.issues == ()

    _write(repo / capture_rel, json.dumps({"cwd": ABS, "drift": True}) + "\n")
    loaded = load_project_policy(repo, repo / PROJECT_REL)
    assert [issue.code for issue in loaded.issues] == [
        "PORTABILITY_POLICY_HASH_DRIFT"]

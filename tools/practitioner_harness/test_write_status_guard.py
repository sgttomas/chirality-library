#!/usr/bin/env python3
"""Tests for the write_status.sh precondition guard (tools/scaffolding/write_status.sh).

Subprocesses the zsh script inside tmp_path git repos with fixture adapter
manifests of both shapes (approval-SHA-declaring and not). Fixture manifests
are test material only — the live manifests under projects/*/_harness/ are
NOT read or written by these tests.
"""
from __future__ import annotations

import os
import subprocess
import importlib.util
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPT = REPO_ROOT / "tools" / "scaffolding" / "write_status.sh"
MANIFEST_SHA_DECLARING = """\
schema: practitioner-harness-adapter/v1
project: fixture-app
guard_requires_committed_ruling_path: true
guard_requires_approval_sha: true
guard_approval_sha_field: "Checking Approval SHA"
"""

MANIFEST_NO_SHA_SCHEMA = """\
schema: practitioner-harness-adapter/v1
project: fixture-piping
guard_requires_committed_ruling_path: true
guard_requires_approval_sha: false
guard_approval_sha_field: ""
"""

STATUS_TEMPLATE = """\
# Status: DEL-01-01

**Current State:** {state}
**Last Updated:** 2026-06-01

## History
- 2026-06-01 — State set to {state} (HUMAN)
"""

RULING_REL = "projects/fixture/docs/D-01_fixture_ruling.md"


def _git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        [
            "git",
            "-c",
            "user.name=Fixture",
            "-c",
            "user.email=fixture@example.invalid",
            *args,
        ],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def make_repo(tmp_path: Path, manifest: str, state: str = "IN_PROGRESS"):
    """Build a tmp git repo with a fixture project tree, adapter manifest,
    committed ruling record, and a _STATUS.md at `state`.

    Returns (repo, deldir, head_sha).
    """
    repo = tmp_path / "repo"
    proj = repo / "projects" / "fixture"
    deldir = proj / "execution" / "PKG-01" / "1_Working" / "DEL-01-01_Fixture"
    deldir.mkdir(parents=True)
    harness = proj / "_harness"
    harness.mkdir()
    (harness / "adapter.yaml").write_text(manifest)
    ruling = repo / RULING_REL
    ruling.parent.mkdir(parents=True)
    ruling.write_text("# D-01 — fixture ruling record (test material)\n")
    (deldir / "_STATUS.md").write_text(STATUS_TEMPLATE.format(state=state))
    _git(repo, "init", "-q")
    _git(repo, "add", "-A")
    _git(repo, "commit", "-q", "-m", "fixture")
    head = _git(repo, "rev-parse", "HEAD")
    return repo, deldir, head


def run_guard(cwd: Path, *args) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["zsh", str(SCRIPT), *[str(a) for a in args]],
        cwd=cwd,
        capture_output=True,
        text=True,
    )


def read_status(deldir: Path) -> str:
    return (deldir / "_STATUS.md").read_text()


# ---------------------------------------------------------------------------
# Committed-ruling precondition
# ---------------------------------------------------------------------------


def test_refuse_checking_without_ruling(tmp_path):
    repo, deldir, head = make_repo(tmp_path, MANIFEST_SHA_DECLARING)
    before = read_status(deldir)
    result = run_guard(repo, deldir, "CHECKING", "human", "--approval-sha", head)
    assert result.returncode == 1
    assert "RULING_REQUIRED" in result.stderr
    assert read_status(deldir) == before, "refusal must leave _STATUS.md byte-identical"


def test_refuse_uncommitted_ruling_path(tmp_path):
    repo, deldir, head = make_repo(tmp_path, MANIFEST_SHA_DECLARING)
    untracked = repo / "projects" / "fixture" / "docs" / "untracked_note.md"
    untracked.write_text("not committed\n")
    before = read_status(deldir)
    result = run_guard(
        repo,
        deldir,
        "CHECKING",
        "human",
        "--ruling",
        "projects/fixture/docs/untracked_note.md",
        "--approval-sha",
        head,
    )
    assert result.returncode == 1
    assert "RULING_NOT_COMMITTED" in result.stderr
    assert read_status(deldir) == before


def test_refuse_nonexistent_ruling_path(tmp_path):
    repo, deldir, head = make_repo(tmp_path, MANIFEST_SHA_DECLARING)
    before = read_status(deldir)
    result = run_guard(
        repo,
        deldir,
        "CHECKING",
        "human",
        "--ruling",
        "projects/fixture/docs/no_such_file.md",
        "--approval-sha",
        head,
    )
    assert result.returncode == 1
    assert "RULING_PATH_MISSING" in result.stderr
    assert read_status(deldir) == before


# ---------------------------------------------------------------------------
# Approval-SHA precondition (adapter-declared)
# ---------------------------------------------------------------------------


def test_refuse_missing_sha_on_sha_declaring_root(tmp_path):
    repo, deldir, _head = make_repo(tmp_path, MANIFEST_SHA_DECLARING)
    before = read_status(deldir)
    result = run_guard(repo, deldir, "CHECKING", "human", "--ruling", RULING_REL)
    assert result.returncode == 1
    assert "APPROVAL_SHA_REQUIRED" in result.stderr
    assert read_status(deldir) == before


def test_refuse_malformed_sha_on_sha_declaring_root(tmp_path):
    repo, deldir, _head = make_repo(tmp_path, MANIFEST_SHA_DECLARING)
    before = read_status(deldir)
    result = run_guard(
        repo,
        deldir,
        "CHECKING",
        "human",
        "--ruling",
        RULING_REL,
        "--approval-sha",
        "xyz-not-hex",
    )
    assert result.returncode == 1
    assert "INVALID_APPROVAL_SHA" in result.stderr
    assert read_status(deldir) == before


def test_refuse_unreachable_sha_on_sha_declaring_root(tmp_path):
    repo, deldir, _head = make_repo(tmp_path, MANIFEST_SHA_DECLARING)
    before = read_status(deldir)
    result = run_guard(
        repo,
        deldir,
        "CHECKING",
        "human",
        "--ruling",
        RULING_REL,
        "--approval-sha",
        "deadbeefdeadbeefdeadbeefdeadbeefdeadbeef",
    )
    assert result.returncode == 1
    assert "APPROVAL_SHA_UNREACHABLE" in result.stderr
    assert read_status(deldir) == before


def test_checking_success_on_sha_declaring_root_updates_fields(tmp_path):
    repo, deldir, head = make_repo(tmp_path, MANIFEST_SHA_DECLARING)
    result = run_guard(
        repo,
        deldir,
        "CHECKING",
        "human",
        "--ruling",
        RULING_REL,
        "--approval-sha",
        head,
    )
    assert result.returncode == 0, result.stderr
    text = read_status(deldir)
    assert "**Current State:** CHECKING" in text
    assert f"**Checking Approval SHA:** {head}" in text
    assert f"**Authorization Basis:** ruling: {RULING_REL}" in text
    assert "State set to CHECKING (human)" in text
    assert "Status: DEL-01-01" in result.stdout


def test_ruling_display_is_repo_relative_under_symlinked_cwd(tmp_path):
    repo, deldir, head = make_repo(tmp_path, MANIFEST_SHA_DECLARING)
    link = tmp_path / "linked-repo"
    link.symlink_to(repo, target_is_directory=True)
    result = subprocess.run(
        [
            "zsh",
            str(SCRIPT),
            str(link / deldir.relative_to(repo)),
            "CHECKING",
            "human",
            "--ruling",
            RULING_REL,
            "--approval-sha",
            head,
        ],
        cwd=link,
        env={**os.environ, "PWD": str(link)},
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    assert f"**Authorization Basis:** ruling: {RULING_REL}\n" in read_status(deldir)


def test_no_sha_schema_root_proceeds_with_review(tmp_path):
    repo, deldir, _head = make_repo(tmp_path, MANIFEST_NO_SHA_SCHEMA)
    result = run_guard(repo, deldir, "CHECKING", "human", "--ruling", RULING_REL)
    assert result.returncode == 0, result.stderr
    assert "REVIEW" in result.stderr
    assert "no approval-SHA schema" in result.stderr
    text = read_status(deldir)
    assert "**Current State:** CHECKING" in text
    assert "State set to CHECKING (human)" in text
    # No field updates on roots without a declared approval-SHA schema.
    assert "Checking Approval SHA" not in text
    assert "Authorization Basis" not in text


# ---------------------------------------------------------------------------
# State machine
# ---------------------------------------------------------------------------


def test_backward_transition_refused(tmp_path):
    repo, deldir, _head = make_repo(tmp_path, MANIFEST_SHA_DECLARING, state="IN_PROGRESS")
    before = read_status(deldir)
    result = run_guard(repo, deldir, "INITIALIZED", "human")
    assert result.returncode == 1
    assert "BACKWARD_TRANSITION" in result.stderr
    assert read_status(deldir) == before


# ---------------------------------------------------------------------------
# Human-ruled CHECKING -> IN_PROGRESS reversal (SPEC §3.3)
# ---------------------------------------------------------------------------


def test_checking_reversal_with_committed_ruling_records_reversal(tmp_path):
    repo, deldir, head = make_repo(tmp_path, MANIFEST_SHA_DECLARING, state="CHECKING")
    result = run_guard(
        repo,
        deldir,
        "IN_PROGRESS",
        "human",
        "--ruling",
        RULING_REL,
        "--approval-sha",
        head,
    )
    assert result.returncode == 0, result.stderr
    text = read_status(deldir)
    assert "**Current State:** IN_PROGRESS" in text
    assert (
        f"State set to IN_PROGRESS (human) [reversal from CHECKING; ruling: {RULING_REL}]\n"
        in text
    )
    assert "reversal from CHECKING" in result.stdout
    # The reversal never records a new checking approval.
    assert "Checking Approval SHA" not in text
    assert "Authorization Basis" not in text


def test_checking_reversal_on_no_sha_schema_root(tmp_path):
    repo, deldir, _head = make_repo(tmp_path, MANIFEST_NO_SHA_SCHEMA, state="CHECKING")
    result = run_guard(repo, deldir, "IN_PROGRESS", "HUMAN", "--ruling", RULING_REL)
    assert result.returncode == 0, result.stderr
    assert "REVIEW" in result.stderr
    text = read_status(deldir)
    assert "**Current State:** IN_PROGRESS" in text
    assert f"[reversal from CHECKING; ruling: {RULING_REL}]" in text


def test_checking_reversal_requires_ruling(tmp_path):
    repo, deldir, head = make_repo(tmp_path, MANIFEST_SHA_DECLARING, state="CHECKING")
    before = read_status(deldir)
    result = run_guard(repo, deldir, "IN_PROGRESS", "human", "--approval-sha", head)
    assert result.returncode == 1
    assert "RULING_REQUIRED" in result.stderr
    assert read_status(deldir) == before


def test_checking_reversal_requires_ruling_even_when_manifest_waives_it(tmp_path):
    manifest = MANIFEST_NO_SHA_SCHEMA.replace(
        "guard_requires_committed_ruling_path: true",
        "guard_requires_committed_ruling_path: false",
    )
    repo, deldir, _head = make_repo(tmp_path, manifest, state="CHECKING")
    before = read_status(deldir)
    result = run_guard(repo, deldir, "IN_PROGRESS", "human")
    assert result.returncode == 1
    assert "RULING_REQUIRED" in result.stderr
    assert read_status(deldir) == before


def test_checking_reversal_refuses_uncommitted_ruling(tmp_path):
    repo, deldir, head = make_repo(tmp_path, MANIFEST_SHA_DECLARING, state="CHECKING")
    untracked = repo / "projects" / "fixture" / "docs" / "untracked_reversal.md"
    untracked.write_text("not committed\n")
    before = read_status(deldir)
    result = run_guard(
        repo,
        deldir,
        "IN_PROGRESS",
        "human",
        "--ruling",
        "projects/fixture/docs/untracked_reversal.md",
        "--approval-sha",
        head,
    )
    assert result.returncode == 1
    assert "RULING_NOT_COMMITTED" in result.stderr
    assert read_status(deldir) == before


def test_checking_reversal_requires_sha_on_sha_declaring_root(tmp_path):
    repo, deldir, _head = make_repo(tmp_path, MANIFEST_SHA_DECLARING, state="CHECKING")
    before = read_status(deldir)
    result = run_guard(repo, deldir, "IN_PROGRESS", "human", "--ruling", RULING_REL)
    assert result.returncode == 1
    assert "APPROVAL_SHA_REQUIRED" in result.stderr
    assert read_status(deldir) == before


def test_checking_reversal_refuses_non_human_actor(tmp_path):
    repo, deldir, head = make_repo(tmp_path, MANIFEST_SHA_DECLARING, state="CHECKING")
    before = read_status(deldir)
    result = run_guard(
        repo,
        deldir,
        "IN_PROGRESS",
        "WORKING_ITEMS",
        "--ruling",
        RULING_REL,
        "--approval-sha",
        head,
    )
    assert result.returncode == 1
    assert "UNAUTHORIZED_ACTOR" in result.stderr
    assert "reversal" in result.stderr
    assert read_status(deldir) == before


@pytest.mark.parametrize(
    "current,target",
    [("CHECKING", "SEMANTIC_READY"), ("CHECKING", "INITIALIZED"), ("ISSUED", "CHECKING")],
)
def test_other_backward_moves_from_checking_or_issued_stay_blocked(tmp_path, current, target):
    repo, deldir, head = make_repo(tmp_path, MANIFEST_SHA_DECLARING, state=current)
    before = read_status(deldir)
    result = run_guard(
        repo, deldir, target, "human", "--ruling", RULING_REL, "--approval-sha", head
    )
    assert result.returncode == 1
    assert "BACKWARD_TRANSITION" in result.stderr
    assert read_status(deldir) == before


def test_issued_to_in_progress_stays_blocked_even_with_ruling(tmp_path):
    repo, deldir, head = make_repo(tmp_path, MANIFEST_SHA_DECLARING, state="ISSUED")
    before = read_status(deldir)
    result = run_guard(
        repo, deldir, "IN_PROGRESS", "human", "--ruling", RULING_REL, "--approval-sha", head
    )
    assert result.returncode == 1
    assert "BACKWARD_TRANSITION" in result.stderr
    assert "scope-change" in result.stderr
    assert read_status(deldir) == before


def test_override_cannot_waive_reversal_ruling(tmp_path):
    repo, deldir, head = make_repo(tmp_path, MANIFEST_SHA_DECLARING, state="CHECKING")
    before = read_status(deldir)
    result = run_guard(
        repo, deldir, "IN_PROGRESS", "human", "--approval-sha", head,
        "--force-human-override", "fixture reason",
    )
    assert result.returncode == 1
    assert "BLOCK RULING_REQUIRED" in result.stderr
    assert "not overridable" in result.stderr
    assert read_status(deldir) == before


def test_override_cannot_waive_uncommitted_reversal_ruling(tmp_path):
    repo, deldir, head = make_repo(tmp_path, MANIFEST_SHA_DECLARING, state="CHECKING")
    untracked = repo / "projects" / "fixture" / "docs" / "untracked_reversal.md"
    untracked.write_text("not committed\n")
    before = read_status(deldir)
    result = run_guard(
        repo, deldir, "IN_PROGRESS", "human",
        "--ruling", "projects/fixture/docs/untracked_reversal.md",
        "--approval-sha", head,
        "--force-human-override", "fixture reason",
    )
    assert result.returncode == 1
    assert "BLOCK RULING_NOT_COMMITTED" in result.stderr
    assert read_status(deldir) == before


def test_override_cannot_waive_issued_to_in_progress(tmp_path):
    repo, deldir, head = make_repo(tmp_path, MANIFEST_SHA_DECLARING, state="ISSUED")
    before = read_status(deldir)
    result = run_guard(
        repo, deldir, "IN_PROGRESS", "human", "--ruling", RULING_REL,
        "--approval-sha", head, "--force-human-override", "fixture reason",
    )
    assert result.returncode == 1
    assert "BLOCK BACKWARD_TRANSITION" in result.stderr
    assert "not overridable" in result.stderr
    assert read_status(deldir) == before


def test_checking_reversal_leaves_existing_approval_fields_as_history(tmp_path):
    repo, deldir, head = make_repo(tmp_path, MANIFEST_SHA_DECLARING, state="IN_PROGRESS")
    entry = run_guard(
        repo, deldir, "CHECKING", "human", "--ruling", RULING_REL, "--approval-sha", head
    )
    assert entry.returncode == 0, entry.stderr
    fields = [
        line
        for line in read_status(deldir).splitlines()
        if line.startswith(("**Checking Approval SHA:**", "**Authorization Basis:**"))
    ]
    assert len(fields) == 2
    result = run_guard(
        repo, deldir, "IN_PROGRESS", "human", "--ruling", RULING_REL, "--approval-sha", head
    )
    assert result.returncode == 0, result.stderr
    text = read_status(deldir)
    assert "**Current State:** IN_PROGRESS" in text
    for line in fields:
        assert text.count(line + "\n") == 1


def test_non_git_checking_reversal_requires_existing_ruling(tmp_path):
    deldir = _make_non_git_tree(tmp_path, "CHECKING")
    before = read_status(deldir)
    result = run_guard(tmp_path, deldir, "IN_PROGRESS", "human")
    assert result.returncode == 1
    assert "RULING_REQUIRED" in result.stderr
    assert read_status(deldir) == before
    ruling = tmp_path / "reversal_ruling.md"
    ruling.write_text("# fixture reversal ruling (test material)\n")
    result = run_guard(tmp_path, deldir, "IN_PROGRESS", "human", "--ruling", ruling)
    assert result.returncode == 0, result.stderr
    assert "REVIEW: not a git repository" in result.stderr
    text = read_status(deldir)
    assert "**Current State:** IN_PROGRESS" in text
    assert "[reversal from CHECKING; ruling: " in text


def test_skip_transition_refused(tmp_path):
    repo, deldir, head = make_repo(tmp_path, MANIFEST_SHA_DECLARING, state="OPEN")
    before = read_status(deldir)
    result = run_guard(
        repo,
        deldir,
        "CHECKING",
        "human",
        "--ruling",
        RULING_REL,
        "--approval-sha",
        head,
    )
    assert result.returncode == 1
    assert "TRANSITION_NOT_ALLOWED" in result.stderr
    assert read_status(deldir) == before


def test_non_human_actor_at_checking_refused(tmp_path):
    repo, deldir, head = make_repo(tmp_path, MANIFEST_SHA_DECLARING)
    before = read_status(deldir)
    result = run_guard(
        repo,
        deldir,
        "CHECKING",
        "PROJECT_SETUP",
        "--ruling",
        RULING_REL,
        "--approval-sha",
        head,
    )
    assert result.returncode == 1
    assert "UNAUTHORIZED_ACTOR" in result.stderr
    assert read_status(deldir) == before


def test_human_alias_actors_accepted_at_checking(tmp_path):
    for actor in ("USER", "operator", "Human (Ryan)"):
        repo, deldir, head = make_repo(
            tmp_path / actor.replace(" ", "_").replace("(", "").replace(")", ""),
            MANIFEST_SHA_DECLARING,
        )
        result = run_guard(
            repo,
            deldir,
            "CHECKING",
            actor,
            "--ruling",
            RULING_REL,
            "--approval-sha",
            head,
        )
        assert result.returncode == 0, f"{actor}: {result.stderr}"


def test_same_state_reassert_allowed_with_warn(tmp_path):
    repo, deldir, _head = make_repo(tmp_path, MANIFEST_SHA_DECLARING, state="IN_PROGRESS")
    result = run_guard(repo, deldir, "IN_PROGRESS", "TASK+working-items")
    assert result.returncode == 0, result.stderr
    assert "WARN" in result.stderr
    assert "same-state re-assert" in result.stderr
    text = read_status(deldir)
    assert text.count("State set to IN_PROGRESS") == 2
    assert "**Current State:** IN_PROGRESS" in text


def test_forward_step_allowed_for_scaffold_actor(tmp_path):
    repo, deldir, _head = make_repo(tmp_path, MANIFEST_SHA_DECLARING, state="OPEN")
    result = run_guard(repo, deldir, "INITIALIZED", "TASK+four-documents")
    assert result.returncode == 0, result.stderr
    assert "**Current State:** INITIALIZED" in read_status(deldir)


def test_invalid_state_is_usage_error(tmp_path):
    repo, deldir, _head = make_repo(tmp_path, MANIFEST_SHA_DECLARING)
    result = run_guard(repo, deldir, "NOT_A_STATE", "human")
    assert result.returncode == 2
    assert "Invalid state" in result.stderr


# ---------------------------------------------------------------------------
# New-file creation
# ---------------------------------------------------------------------------


def test_new_file_creation_at_open_allowed(tmp_path):
    repo, deldir, _head = make_repo(tmp_path, MANIFEST_SHA_DECLARING)
    fresh = deldir.parent / "DEL-01-02_Fresh"
    fresh.mkdir()
    result = run_guard(repo, fresh, "OPEN", "PREPARATION")
    assert result.returncode == 0, result.stderr
    text = read_status(fresh)
    assert "**Current State:** OPEN" in text
    assert "State set to OPEN (PREPARATION)" in text
    assert "Status: DEL-01-02" in result.stdout


def test_new_file_creation_at_checking_refused(tmp_path):
    repo, deldir, head = make_repo(tmp_path, MANIFEST_SHA_DECLARING)
    fresh = deldir.parent / "DEL-01-03_Fresh"
    fresh.mkdir()
    result = run_guard(
        repo,
        fresh,
        "CHECKING",
        "human",
        "--ruling",
        RULING_REL,
        "--approval-sha",
        head,
    )
    assert result.returncode == 1
    assert "NEW_FILE_NOT_OPEN" in result.stderr
    assert not (fresh / "_STATUS.md").exists()


# ---------------------------------------------------------------------------
# Human override
# ---------------------------------------------------------------------------


def test_force_human_override_records_reason(tmp_path):
    repo, deldir, _head = make_repo(tmp_path, MANIFEST_SHA_DECLARING, state="IN_PROGRESS")
    reason = "reverting after human review of fixture drift"
    result = run_guard(
        repo,
        deldir,
        "INITIALIZED",
        "human",
        "--force-human-override",
        reason,
    )
    assert result.returncode == 0, result.stderr
    assert "OVERRIDE recorded" in result.stderr
    assert "BACKWARD_TRANSITION" in result.stderr
    text = read_status(deldir)
    assert "**Current State:** INITIALIZED" in text
    assert f"[override: {reason}]" in text


def test_force_human_override_requires_human_actor(tmp_path):
    repo, deldir, _head = make_repo(tmp_path, MANIFEST_SHA_DECLARING, state="IN_PROGRESS")
    before = read_status(deldir)
    result = run_guard(
        repo,
        deldir,
        "INITIALIZED",
        "PROJECT_SETUP",
        "--force-human-override",
        "should not apply",
    )
    assert result.returncode == 1
    assert "BACKWARD_TRANSITION" in result.stderr
    assert "does not normalize to HUMAN" in result.stderr
    assert read_status(deldir) == before


def test_force_human_override_never_overrides_usage_errors(tmp_path):
    repo, deldir, _head = make_repo(tmp_path, MANIFEST_SHA_DECLARING)
    result = run_guard(
        repo,
        deldir,
        "NOT_A_STATE",
        "human",
        "--force-human-override",
        "irrelevant",
    )
    assert result.returncode == 2


# ---------------------------------------------------------------------------
# Outside a git repo (export/staging context)
# ---------------------------------------------------------------------------


def _make_non_git_tree(tmp_path: Path, state: str) -> Path:
    plain = tmp_path / "plain"
    deldir = plain / "PKG-01" / "1_Working" / "DEL-09-01_NoRepo"
    deldir.mkdir(parents=True)
    (deldir / "_STATUS.md").write_text(STATUS_TEMPLATE.format(state=state))
    return deldir


def test_non_git_dir_skips_git_checks_with_review(tmp_path):
    deldir = _make_non_git_tree(tmp_path, "IN_PROGRESS")
    result = run_guard(tmp_path, deldir, "CHECKING", "human")
    assert result.returncode == 0, result.stderr
    assert "REVIEW: not a git repository" in result.stderr
    assert "**Current State:** CHECKING" in read_status(deldir)


def test_non_git_dir_state_machine_still_enforced(tmp_path):
    deldir = _make_non_git_tree(tmp_path, "OPEN")
    before = read_status(deldir)
    result = run_guard(tmp_path, deldir, "CHECKING", "human")
    assert result.returncode == 1
    assert "TRANSITION_NOT_ALLOWED" in result.stderr
    assert read_status(deldir) == before


def test_non_git_dir_actor_gate_still_enforced(tmp_path):
    deldir = _make_non_git_tree(tmp_path, "IN_PROGRESS")
    before = read_status(deldir)
    result = run_guard(tmp_path, deldir, "CHECKING", "PROJECT_SETUP")
    assert result.returncode == 1
    assert "UNAUTHORIZED_ACTOR" in result.stderr
    assert read_status(deldir) == before


# ---------------------------------------------------------------------------
# Live export byte-identity
# ---------------------------------------------------------------------------



# ---------------------------------------------------------------------------
# Metacharacter safety + anchor fallback (adversarial-review findings)
# ---------------------------------------------------------------------------


MANIFEST_AMPERSAND_FIELD = """\
schema: practitioner-harness-adapter/v1
project: fixture-app
guard_requires_committed_ruling_path: true
guard_requires_approval_sha: true
guard_approval_sha_field: "R&D SHA"
"""


def test_ampersand_in_field_name_and_ruling_path_not_corrupted(tmp_path):
    """Regression: BSD sed '&' match-reference corrupted upsert lines."""
    repo, deldir, head = make_repo(tmp_path, MANIFEST_AMPERSAND_FIELD)
    ruling = repo / "projects" / "fixture" / "docs" / "D&X_ruling.md"
    ruling.write_text("# fixture ruling with ampersand (test material)\n")
    _git(repo, "add", "-A")
    _git(repo, "commit", "-q", "-m", "add ampersand ruling")
    head = _git(repo, "rev-parse", "HEAD")
    result = run_guard(
        repo, deldir, "CHECKING", "human",
        "--ruling", "projects/fixture/docs/D&X_ruling.md",
        "--approval-sha", head,
    )
    assert result.returncode == 0, result.stderr
    text = read_status(deldir)
    assert f"**R&D SHA:** {head}\n" in text
    assert "**Authorization Basis:** ruling: projects/fixture/docs/D&X_ruling.md\n" in text
    # exactly one occurrence each; no mangled duplication
    assert text.count("**R&D SHA:**") == 1
    assert text.count("**Authorization Basis:**") == 1
    # re-assert same state: replace branch, still exactly one line each
    result2 = run_guard(
        repo, deldir, "CHECKING", "human",
        "--ruling", "projects/fixture/docs/D&X_ruling.md",
        "--approval-sha", head,
    )
    assert result2.returncode == 0, result2.stderr
    text2 = read_status(deldir)
    assert text2.count("**R&D SHA:**") == 1
    assert text2.count("**Authorization Basis:**") == 1


def test_missing_last_updated_anchor_falls_back_to_current_state(tmp_path):
    """Regression: required fields were silently dropped (exit 0) when the
    status file had no '**Last Updated:**' line."""
    repo, deldir, head = make_repo(tmp_path, MANIFEST_SHA_DECLARING)
    status = deldir / "_STATUS.md"
    status.write_text(
        "# Status: DEL-01-01\n\n"
        "**Current State:** IN_PROGRESS\n\n"
        "## History\n"
        "- 2026-06-01 — State set to IN_PROGRESS (HUMAN)\n"
    )
    result = run_guard(
        repo, deldir, "CHECKING", "human",
        "--ruling", RULING_REL,
        "--approval-sha", head,
    )
    assert result.returncode == 0, result.stderr
    text = read_status(deldir)
    assert f"**Checking Approval SHA:** {head}\n" in text, (
        "required field silently dropped without Last Updated anchor"
    )
    assert "**Authorization Basis:**" in text


@pytest.mark.parametrize('state,override', [('OPEN', False), ('INITIALIZED', False), ('INITIALIZED', True)])
def test_root_governance_write_refused_before_override(tmp_path, state, override):
    repo, _, _ = make_repo(tmp_path, MANIFEST_NO_SHA_SCHEMA, 'OPEN')
    root_adapter = repo / 'execution/_harness/adapter.yaml'
    root_adapter.parent.mkdir(parents=True)
    root_adapter.write_text('schema: root-harness-adapter/v1\nmode: governance-only\n')
    target = repo / 'execution/PKG-01/1_Working/DEL-01-01_Fixture'
    target.mkdir(parents=True)
    if state != 'OPEN':
        (target / '_STATUS.md').write_text(STATUS_TEMPLATE.format(state='OPEN'))
    before = list(target.iterdir())
    previous = read_status(target) if before else None
    args = [target, state, 'human']
    if override: args += ['--force-human-override', 'fixture attempt']
    result = run_guard(repo, *args)
    assert result.returncode == 1
    assert 'Root source write refused' in result.stderr
    assert list(target.iterdir()) == before
    if before: assert read_status(target) == previous

@pytest.mark.parametrize('existing,override', [(False,False),(False,True),(True,False),(True,True)])
def test_root_governance_symlink_alias_cannot_create_or_activate(tmp_path,existing,override):
    repo,_,_=make_repo(tmp_path,MANIFEST_NO_SHA_SCHEMA,'OPEN')
    adapter=repo/'execution/_harness/adapter.yaml';adapter.parent.mkdir(parents=True)
    adapter.write_text('schema: root-harness-adapter/v1\nmode: governance-only\n')
    target=repo/'execution/PKG-01/1_Working/DEL-01-01_Alias';target.mkdir(parents=True)
    status=target/'_STATUS.md'
    if existing:status.write_text(STATUS_TEMPLATE.format(state='INITIALIZED'))
    before=status.read_bytes() if existing else None
    alias=repo/'alias';alias.symlink_to(target,target_is_directory=True)
    args=[alias,'IN_PROGRESS' if existing else 'OPEN','human']
    if override:args+=['--force-human-override','fixture bypass attempt']
    result=run_guard(repo,*args)
    assert result.returncode==1 and 'Root source write refused' in result.stderr
    assert (status.read_bytes() if status.exists() else None)==before


# ---------------------------------------------------------------------------
# Reopening ISSUED -> IN_PROGRESS under an accepted amendment (D-GOV-50/51)
# ---------------------------------------------------------------------------

AMENDMENT_ROOT_REL = "projects/fixture/execution/_ScopeChange"
REGISTER_HEADER = (
    "AmendmentID,ActionSeq,ActionType,EntityType,EntityID,Description,"
    "AffectedFiles,DownstreamReruns,SupersessionBindingPresent,ScopeChanging\n"
)


def add_amendment(
    repo: Path, action: str = "MODIFY", scope: str = "NO", groups=("1", "2", "3"), group3_heading: str | None = None
) -> str:
    """Commit fixture scope-change records naming DEL-01-01; return the new HEAD."""
    import hashlib

    root = repo / AMENDMENT_ROOT_REL
    snapshot = root / "SCA-001_2026-09-26_1200"
    snapshot.mkdir(parents=True)
    register = snapshot / "Amendment_Actions.csv"
    register.write_text(
        REGISTER_HEADER + f"SCA-001,1,{action},DELIVERABLE,DEL-01-01,fixture,,,NO,{scope}\n"
    )
    sha = hashlib.sha256(register.read_bytes()).hexdigest()
    for group in groups:
        folder = root / "checkpoint_snapshots" / f"SCA-001_GROUP-{group}_2026-09-26"
        folder.mkdir(parents=True)
        heading = f"SCA-001 checkpoint group {group} — accepted fixture"
        if group == "3" and group3_heading is not None:
            heading = group3_heading
        (folder / "DECISION.md").write_text(f"# {heading}\n")
        rows = "Path,SHA256,Role,AcceptanceBoundary\n"
        if group == "2":
            rows += f"{register.relative_to(repo).as_posix()},{sha},exact final action register,Accepted\n"
        (folder / "ACCEPTED_MANIFEST.csv").write_text(rows)
    _git(repo, "add", "-A")
    _git(repo, "commit", "-q", "-m", "fixture amendment")
    return _git(repo, "rev-parse", "HEAD")


def test_reopen_admitted_with_accepted_amendment(tmp_path):
    repo, deldir, _ = make_repo(tmp_path, MANIFEST_SHA_DECLARING, state="ISSUED")
    head = add_amendment(repo)
    result = run_guard(
        repo, deldir, "IN_PROGRESS", "human", "--amendment", "SCA-001", "--approval-sha", head
    )
    assert result.returncode == 0, result.stderr
    text = read_status(deldir)
    assert "**Current State:** IN_PROGRESS" in text
    history = text.strip().splitlines()[-1]
    assert "State set to IN_PROGRESS (human) [reopened from ISSUED; amendment: SCA-001 (" in history
    assert f"{AMENDMENT_ROOT_REL}/checkpoint_snapshots/SCA-001_GROUP-3_2026-09-26)" in history
    assert "ActionSeq 1 MODIFY" in history
    assert f"approval SHA: {head}]" in history
    assert "reopened from ISSUED under SCA-001" in result.stdout


def test_reopen_admitted_with_amendment_path_on_no_sha_schema_root(tmp_path):
    repo, deldir, _ = make_repo(tmp_path, MANIFEST_NO_SHA_SCHEMA, state="ISSUED")
    head = add_amendment(repo, action="RECLASSIFY", scope="YES")
    group3 = f"{AMENDMENT_ROOT_REL}/checkpoint_snapshots/SCA-001_GROUP-3_2026-09-26"
    result = run_guard(
        repo, deldir, "IN_PROGRESS", "Human", "--amendment", group3, "--approval-sha", head
    )
    assert result.returncode == 0, result.stderr
    assert "ActionSeq 1 RECLASSIFY" in read_status(deldir)


@pytest.mark.parametrize("manifest", [MANIFEST_SHA_DECLARING, MANIFEST_NO_SHA_SCHEMA])
def test_reopen_requires_approval_sha_on_every_root(tmp_path, manifest):
    repo, deldir, _ = make_repo(tmp_path, manifest, state="ISSUED")
    add_amendment(repo)
    before = read_status(deldir)
    result = run_guard(repo, deldir, "IN_PROGRESS", "human", "--amendment", "SCA-001")
    assert result.returncode == 1
    assert "BLOCK APPROVAL_SHA_REQUIRED" in result.stderr
    assert read_status(deldir) == before


def test_reopen_refuses_unreachable_approval_sha(tmp_path):
    repo, deldir, _ = make_repo(tmp_path, MANIFEST_SHA_DECLARING, state="ISSUED")
    add_amendment(repo)
    before = read_status(deldir)
    result = run_guard(
        repo, deldir, "IN_PROGRESS", "human", "--amendment", "SCA-001",
        "--approval-sha", "deadbeefdeadbeefdeadbeefdeadbeefdeadbeef",
    )
    assert result.returncode == 1
    assert "APPROVAL_SHA_UNREACHABLE" in result.stderr
    assert read_status(deldir) == before


def test_reopen_refuses_approval_sha_without_the_acceptance(tmp_path):
    # The records are read at the approval commit, which predates the amendment.
    repo, deldir, first = make_repo(tmp_path, MANIFEST_SHA_DECLARING, state="ISSUED")
    add_amendment(repo)
    before = read_status(deldir)
    result = run_guard(
        repo, deldir, "IN_PROGRESS", "human", "--amendment", "SCA-001", "--approval-sha", first
    )
    assert result.returncode == 1
    assert "BLOCK AMENDMENT_NOT_ADMITTED: SCOPE_CHANGE_ROOT_NOT_FOUND:" in result.stderr
    assert "at the commit" in result.stderr
    assert read_status(deldir) == before


def test_reopen_refuses_non_human_actor(tmp_path):
    repo, deldir, _ = make_repo(tmp_path, MANIFEST_SHA_DECLARING, state="ISSUED")
    head = add_amendment(repo)
    before = read_status(deldir)
    result = run_guard(
        repo, deldir, "IN_PROGRESS", "WORKING_ITEMS", "--amendment", "SCA-001", "--approval-sha", head
    )
    assert result.returncode == 1
    assert "BLOCK UNAUTHORIZED_ACTOR" in result.stderr
    assert read_status(deldir) == before


@pytest.mark.parametrize(
    "action,scope,groups,code",
    [
        ("ADD", "YES", ("1", "2", "3"), "ACTION_NOT_AUTHORIZING"),
        ("RECLASSIFY", "NO", ("1", "2", "3"), "RECLASSIFY_NOT_SCOPE_CHANGING"),
        ("MODIFY", "NO", ("1", "2"), "GROUP3_NOT_ACCEPTED"),
    ],
)
def test_reopen_refuses_when_checker_refuses(tmp_path, action, scope, groups, code):
    repo, deldir, _ = make_repo(tmp_path, MANIFEST_SHA_DECLARING, state="ISSUED")
    head = add_amendment(repo, action=action, scope=scope, groups=groups)
    before = read_status(deldir)
    result = run_guard(
        repo, deldir, "IN_PROGRESS", "human", "--amendment", "SCA-001", "--approval-sha", head
    )
    assert result.returncode == 1
    assert f"BLOCK AMENDMENT_NOT_ADMITTED: {code}:" in result.stderr
    assert read_status(deldir) == before


def test_reopen_refuses_hash_mismatch(tmp_path):
    repo, deldir, _ = make_repo(tmp_path, MANIFEST_SHA_DECLARING, state="ISSUED")
    add_amendment(repo)
    register = repo / AMENDMENT_ROOT_REL / "SCA-001_2026-09-26_1200" / "Amendment_Actions.csv"
    register.write_text(register.read_text() + "SCA-001,2,ADD,OTHER,X,late,,,NO,NO\n")
    _git(repo, "commit", "-qam", "register edited after binding")
    head = _git(repo, "rev-parse", "HEAD")
    before = read_status(deldir)
    result = run_guard(
        repo, deldir, "IN_PROGRESS", "human", "--amendment", "SCA-001", "--approval-sha", head
    )
    assert result.returncode == 1
    assert "REGISTER_HASH_MISMATCH" in result.stderr
    assert read_status(deldir) == before


def test_override_cannot_waive_reopening_preconditions(tmp_path):
    repo, deldir, _ = make_repo(tmp_path, MANIFEST_SHA_DECLARING, state="ISSUED")
    head = add_amendment(repo, action="ADD")
    before = read_status(deldir)
    result = run_guard(
        repo, deldir, "IN_PROGRESS", "human", "--amendment", "SCA-001", "--approval-sha", head,
        "--force-human-override", "fixture reason",
    )
    assert result.returncode == 1
    assert "BLOCK AMENDMENT_NOT_ADMITTED" in result.stderr
    assert "not overridable" in result.stderr
    assert read_status(deldir) == before


def test_amendment_argument_on_other_transitions_is_usage_error(tmp_path):
    repo, deldir, head = make_repo(tmp_path, MANIFEST_SHA_DECLARING, state="IN_PROGRESS")
    before = read_status(deldir)
    result = run_guard(
        repo, deldir, "CHECKING", "human", "--ruling", RULING_REL, "--approval-sha", head,
        "--amendment", "SCA-001",
    )
    assert result.returncode == 2
    assert "--amendment applies only to ISSUED -> IN_PROGRESS" in result.stderr
    assert read_status(deldir) == before


def test_non_git_reopen_refused(tmp_path):
    deldir = _make_non_git_tree(tmp_path, "ISSUED")
    before = read_status(deldir)
    result = run_guard(
        tmp_path, deldir, "IN_PROGRESS", "human", "--amendment", "SCA-001", "--approval-sha", "abc1234"
    )
    assert result.returncode == 1
    assert "REOPEN_REQUIRES_GIT" in result.stderr
    assert read_status(deldir) == before


# Review findings on the first version: the approval SHA must bind the content
# the check reads (B1), and each accepted amendment admits one tool-recorded
# reopening.


def _group2_manifest(repo: Path) -> Path:
    return repo / AMENDMENT_ROOT_REL / "checkpoint_snapshots" / "SCA-001_GROUP-2_2026-09-26" / "ACCEPTED_MANIFEST.csv"


def _flip_register_uncommitted(repo: Path, old: str, new: str) -> None:
    import hashlib

    register = repo / AMENDMENT_ROOT_REL / "SCA-001_2026-09-26_1200" / "Amendment_Actions.csv"
    register.write_text(register.read_text().replace(old, new))
    manifest = _group2_manifest(repo)
    lines = manifest.read_text().splitlines()
    path, _, *rest = lines[1].split(",")
    lines[1] = ",".join([path, hashlib.sha256(register.read_bytes()).hexdigest(), *rest])
    manifest.write_text("\n".join(lines) + "\n")


def _forge_group3(repo: Path) -> Path:
    folder = repo / AMENDMENT_ROOT_REL / "checkpoint_snapshots" / "SCA-001_GROUP-3_2026-09-26"
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "DECISION.md").write_text("# SCA-001 checkpoint group 3 — accepted\n")
    (folder / "ACCEPTED_MANIFEST.csv").write_text("Path,SHA256\n")
    return folder


def test_reopen_attack_a_uncommitted_register_and_manifest_edit_refused(tmp_path):
    repo, deldir, _ = make_repo(tmp_path, MANIFEST_SHA_DECLARING, state="ISSUED")
    head = add_amendment(repo, action="REMOVE")
    _flip_register_uncommitted(repo, "REMOVE", "MODIFY")
    before = read_status(deldir)
    result = run_guard(repo, deldir, "IN_PROGRESS", "human", "--amendment", "SCA-001", "--approval-sha", head)
    assert result.returncode == 1
    assert "BLOCK AMENDMENT_NOT_ADMITTED: DELIVERABLE_REMOVED:" in result.stderr
    assert read_status(deldir) == before


def test_reopen_attack_b_uncommitted_heading_flip_refused(tmp_path):
    repo, deldir, _ = make_repo(tmp_path, MANIFEST_SHA_DECLARING, state="ISSUED")
    head = add_amendment(repo, group3_heading="SCA-001 checkpoint group 3 — returned by owner")
    decision = repo / AMENDMENT_ROOT_REL / "checkpoint_snapshots" / "SCA-001_GROUP-3_2026-09-26" / "DECISION.md"
    decision.write_text("# SCA-001 checkpoint group 3 — accepted\n")
    before = read_status(deldir)
    result = run_guard(repo, deldir, "IN_PROGRESS", "human", "--amendment", "SCA-001", "--approval-sha", head)
    assert result.returncode == 1
    assert "BLOCK AMENDMENT_NOT_ADMITTED: GROUP3_NOT_ACCEPTED:" in result.stderr
    assert read_status(deldir) == before


def test_reopen_untracked_forged_group3_refused(tmp_path):
    repo, deldir, _ = make_repo(tmp_path, MANIFEST_SHA_DECLARING, state="ISSUED")
    head = add_amendment(repo, groups=("1", "2"))
    _forge_group3(repo)
    before = read_status(deldir)
    result = run_guard(repo, deldir, "IN_PROGRESS", "human", "--amendment", "SCA-001", "--approval-sha", head)
    assert result.returncode == 1
    assert "BLOCK AMENDMENT_NOT_ADMITTED: GROUP3_NOT_ACCEPTED:" in result.stderr
    assert read_status(deldir) == before


def test_reopen_side_branch_approval_sha_refused(tmp_path):
    repo, deldir, _ = make_repo(tmp_path, MANIFEST_SHA_DECLARING, state="ISSUED")
    add_amendment(repo, groups=("1", "2"))
    _git(repo, "checkout", "-q", "-b", "side")
    _forge_group3(repo)
    _git(repo, "add", "-A")
    _git(repo, "commit", "-q", "-m", "forged group 3")
    side = _git(repo, "rev-parse", "HEAD")
    _git(repo, "checkout", "-q", "-")
    _forge_group3(repo)  # the working tree copy is untracked on this branch
    before = read_status(deldir)
    result = run_guard(repo, deldir, "IN_PROGRESS", "human", "--amendment", "SCA-001", "--approval-sha", side)
    assert result.returncode == 1
    assert "BLOCK APPROVAL_SHA_NOT_ANCESTOR" in result.stderr
    assert "not overridable" in result.stderr
    assert read_status(deldir) == before


def test_reopen_nested_scope_change_in_deliverable_not_used(tmp_path):
    import hashlib
    import shutil

    repo, deldir, _ = make_repo(tmp_path, MANIFEST_SHA_DECLARING, state="ISSUED")
    add_amendment(repo, action="REMOVE")
    nested = deldir / "_ScopeChange"
    shutil.copytree(repo / AMENDMENT_ROOT_REL, nested)
    register = nested / "SCA-001_2026-09-26_1200" / "Amendment_Actions.csv"
    register.write_text(register.read_text().replace("REMOVE", "MODIFY"))
    (nested / "checkpoint_snapshots" / "SCA-001_GROUP-2_2026-09-26" / "ACCEPTED_MANIFEST.csv").write_text(
        f"Path,SHA256,Role\n{register.relative_to(repo).as_posix()},"
        f"{hashlib.sha256(register.read_bytes()).hexdigest()},exact final action register\n"
    )
    _git(repo, "add", "-A")
    _git(repo, "commit", "-q", "-m", "nested scope change")
    head = _git(repo, "rev-parse", "HEAD")
    before = read_status(deldir)
    result = run_guard(repo, deldir, "IN_PROGRESS", "human", "--amendment", "SCA-001", "--approval-sha", head)
    assert result.returncode == 1
    assert "DELIVERABLE_REMOVED" in result.stderr
    assert read_status(deldir) == before


def test_reopen_once_per_amendment(tmp_path):
    repo, deldir, _ = make_repo(tmp_path, MANIFEST_SHA_DECLARING, state="ISSUED")
    head = add_amendment(repo)
    first = run_guard(repo, deldir, "IN_PROGRESS", "human", "--amendment", "SCA-001", "--approval-sha", head)
    assert first.returncode == 0, first.stderr
    status = deldir / "_STATUS.md"
    status.write_text(
        status.read_text().replace("**Current State:** IN_PROGRESS", "**Current State:** ISSUED")
        + "- 2026-09-27 — State set to ISSUED (human)\n"
    )
    before = read_status(deldir)
    replay = run_guard(repo, deldir, "IN_PROGRESS", "human", "--amendment", "SCA-001", "--approval-sha", head)
    assert replay.returncode == 1
    assert "BLOCK AMENDMENT_NOT_ADMITTED: AMENDMENT_ALREADY_USED:" in replay.stderr
    assert read_status(deldir) == before

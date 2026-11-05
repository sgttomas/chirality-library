#!/usr/bin/env python3
"""LIVE-tree baseline tests (skippable with CHIRALITY_SKIP_LIVE_TESTS=1; the
retained _DomainEngines/ stale-surface fixtures were removed with that tree). Pins the ruled drift baseline (piping 0/101,
app-dev 0/54 — conscious pin update 2026-07-02: the original 92/101 class was
resolved by the owner's class-wide K-CONFLICT-1 ruling, header IN_PROGRESS
authoritative, recorded at projects/chirality-piping/execution/_Reconciliation/
LifecycleCorrection/LIFECYCLE_CORRECTION_2026-07-02_2050/Decision_Log.md),
the current aggregate self-check severity totals, the three deliberately
retained stale surfaces (owner ruling
2026-07-01; post-cleanup exact counts pinned per the D-T0 clean + backfill
owner ruling, 2026-07-02) that self-check MUST catch, the retired piping
reconciliation pointer (the GEN-7 pointer-currency check's first detection
target), the
GEN-8 25-file instruction-class abs-path baseline (a drift metric: it trends
DOWN as files are relativized when next touched, and a conscious pin update
accompanies each reduction), and the GEN-9 registry zero-drift state (its
first detection target, the AGENTS.md DELIVERABLE_TASK row, was removed at
owner direction 2026-07-01)."""

from __future__ import annotations

import os
from pathlib import Path

import pytest

import cmd_bridge_status
import cmd_self_check

LIVE_REPO = Path(__file__).resolve().parents[2]

# governance-harness CI sets CHIRALITY_REQUIRE_LIVE_TESTS=1: these tests are
# then the hosted self-check gate (no separate CLI step), so they must fail
# rather than skip when the live roots are unexpectedly absent.
live = pytest.mark.skipif(
    os.environ.get("CHIRALITY_REQUIRE_LIVE_TESTS") != "1"
    and os.environ.get("CHIRALITY_SKIP_LIVE_TESTS") == "1",
    reason="live tests disabled by env",
)


@pytest.fixture(scope="module")
def live_self_check():
    """One shared live self-check for every test in this module. The report is
    read-only and the tree cannot change mid-run, so per-test re-runs (each a
    full repo scan) would assert against byte-identical reports."""
    return cmd_self_check.run_self_check(LIVE_REPO)


@live
def test_live_self_check_abs_path_in_evidence_reports_are_pinned(live_self_check):
    report, _ = live_self_check
    hits = [f for f in report.findings if f.code == "ABS_PATH_IN_EVIDENCE"]
    # The one pinned owner-machine path was removed when the library moved to
    # its own repository; no absolute path remains in live evidence.
    assert hits == []




@live
def test_live_self_check_stale_open_issue_is_zero(live_self_check):
    # Post-cleanup live corpus: open_issues entries are annotated in place and
    # the D-T0-06 ruling condition carries its "[Condition met ...]" note.
    report, _ = live_self_check
    assert [f for f in report.findings if f.code == "STALE_OPEN_ISSUE"] == []


@live
def test_live_self_check_live_binding_gate_drift_is_detected(live_self_check):
    # Conscious pin inversion 2026-07-04: this test originally pinned the
    # HB-8 STALE_LIVE_BINDING_GATE finding at profile :145 (the line still
    # named the cleared tier-0-adoption and piping D-21 gates). The
    # owner-delegated tier-0 CHANGE
    # (CHANGE_PREP_2026-07-04_live_binding_gate_destale.md) rewrote the line
    # to the single genuinely open gate (app-dev F3), so the live corpus now
    # lawfully carries ZERO findings of this code. Detector behaviour on
    # synthetic stale input stays covered by the HB-8 fixture tests.
    report, _ = live_self_check
    hits = [f for f in report.findings if f.code == "STALE_LIVE_BINDING_GATE"]
    assert hits == []






@live
def test_live_gen8_semantic_portability_invariants(live_self_check):
    report, _ = live_self_check
    assert [f for f in report.findings if f.code in {
        "ABS_PATH_IN_PROJECT_SURFACE",
        "ABS_PATH_IN_UNCLASSIFIED_SURFACE",
    }] == []
    assert [f for f in report.findings
            if f.code.startswith("PORTABILITY_POLICY_")] == []


@live
def test_live_gen9_registry_currency_zero_drift(live_self_check):
    # Consistency-audit §4 item 3 was the check's first detection target: the
    # registry indexed DELIVERABLE_TASK as live (AGENTS.md:89 at 4e01db61e)
    # while the file existed only under the gitignored agents/.archive/. The
    # owner ruled the disposition REMOVE (directed 2026-07-01; applied in this
    # PR — the detection state is pinned by the prior commit, fcca5fedd), so
    # the live registry is pinned clean in BOTH directions. A regression in
    # either direction is a conscious pin update, never a silent one; the
    # detector itself is proven by test_agent_registry_fixtures.py.
    report, _ = live_self_check
    assert [f for f in report.findings
            if f.code == "REGISTRY_TARGET_MISSING"] == []
    assert [f for f in report.findings
            if f.code == "AGENT_FILE_UNINDEXED"] == []
    assert [f for f in report.findings
            if f.code == "REGISTRY_CHECK_NOT_APPLICABLE"] == []


@live
def test_live_self_check_reports_root_headers_and_exits_clean(live_self_check):
    # Equivalent to `harness.py self-check` exiting 0: no identity refusal
    # (exit 2) and no BLOCK finding (exit 1). This is the hosted gate.
    report, refusal = live_self_check
    assert refusal is None, refusal
    from harness_common import Severity, compute_exit_code
    assert compute_exit_code(report.findings) == 0
    assert not any(f.severity is Severity.BLOCK for f in report.findings)


@live
def test_archived_project_selection_refuses_with_recovery_pointer():
    import subprocess
    import sys
    proc = subprocess.run([sys.executable, str(LIVE_REPO / 'tools/practitioner_harness/harness.py'),
                           'status', '--project', 'app-dev', '--repo-root', str(LIVE_REPO)],
                          capture_output=True, text=True)
    assert proc.returncode == 2
    assert 'projects/FROZEN.md' in proc.stderr
    assert 'Traceback' not in proc.stderr


@live
def test_default_drift_skips_archived_project_roots():
    import subprocess
    import sys
    proc = subprocess.run([sys.executable, str(LIVE_REPO / 'tools/practitioner_harness/harness.py'),
                           'drift', '--all', '--repo-root', str(LIVE_REPO)],
                          capture_output=True, text=True)
    assert proc.returncode == 0, proc.stderr
    assert 'Project root absent' not in proc.stderr

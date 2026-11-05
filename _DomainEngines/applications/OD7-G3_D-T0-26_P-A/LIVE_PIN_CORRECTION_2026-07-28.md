# D-T0-26 Conscious Live-Pin Correction

**Date:** 2026-07-28
**PR:** `#395`
**Failed run:** `30368591914`
**Failed job:** `90306205022`
**Corrected surface:** `tools/practitioner_harness/test_live_baseline.py`
**Preimage SHA-256:** `8b1f2e170f58b3f21601e2d490c11d0e27046d78a42daee0cf6de26bccaa6d59`
**Corrected SHA-256:** `38314c98fe6ae1109e24286582d16e8555a21c7b3a11d4e74c75fc7c8a3fbaed`

## Owner provenance

Ryan Tufts, in-session, 2026-07-28:

> "Finish out your plan now (attaining your goal) with self merge of PRs and auto approve for owners rulings, which should still be recorded in the usual manner with your recommendation standing as what I approved."

The supervising Agent 0 recommended, and the direction therefore approves,
the bounded conscious live-pin correction recorded here.

## Failure and reason

The first PR run completed with 348 passing tests and one failure:

```text
tools/practitioner_harness/test_live_baseline.py:126
AssertionError: assert 'STALE' == 'ADOPTED'
```

The live-baseline test still pinned the superseded PEC profile posture
`ADOPTED` / `OPERATION_PROPOSAL`. D-T0-26 intentionally changes the current
profile to `STALE` / `MANUAL_BRIDGE`; the bridge-status parser reports its
current gate posture as `Gate 2 unknown`. The old Gate-2 adoption remains
historical authority but is no longer the live profile status.

## Exact diff

```diff
-def test_live_bridge_status_reports_pec_adopted_gate_closed():
-    # Conscious live-pin update (workplan step-4 convention): the owner adopted the
-    # PEC profile at Gate 2 on 2026-07-05 (D-T0-12 packet, dated adoption note), so
-    # the prior DRAFT / "Gate 2 open" pin is superseded in the same PR as the flip.
+def test_live_bridge_status_reports_pec_stale_profile():
+    # Conscious live-pin update: D-T0-26 preserves the historical Gate-2 adoption
+    # while classifying the current frozen profile STALE / MANUAL_BRIDGE.
     report = cmd_bridge_status.run_bridge_status(LIVE_REPO)
-    assert _fact(report, "bridge_status.profile.pec.profile_status").value == "ADOPTED"
+    assert _fact(report, "bridge_status.profile.pec.profile_status").value == "STALE"
     assert _fact(report, "bridge_status.profile.pec.gate_posture").value == (
-        "Gate 2 adopted"
+        "Gate 2 unknown"
     )
     md = report.render_markdown()
-    # integration level pin updated 2026-07-05: D-T0-18 O-A advanced pec to
-    # OPERATION_PROPOSAL (L3, imports scope) — conscious pin update, same PR.
-    assert "| `pec` | `ADOPTED` | Gate 2 adopted | `OPERATION_PROPOSAL` |" in md
+    assert "| `pec` | `STALE` | Gate 2 unknown | `MANUAL_BRIDGE` |" in md
```

## Boundary

Only this test pin changes. No validator production behavior, profile
semantics, product/runtime/implementation surface, migration, release,
compatibility, or reliance authority changes.

## Validation

- Focused corrected live-pin test: `1 passed`
- Complete practitioner-harness suite: `349 passed in 33.77s`
- `git diff --check`: pass

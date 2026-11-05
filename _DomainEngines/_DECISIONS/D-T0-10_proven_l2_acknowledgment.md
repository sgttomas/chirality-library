# D-T0-10 - RULING: proven-L2 acknowledgment (D-T0-08 precondition)

**Status:** RULED / ACKNOWLEDGED 2026-07-04.
**Date prepared:** 2026-07-04 (record added at acknowledgment per the register's staging note)
**Decision ID:** D-T0-10 (residual of D-T0-08 per the 2026-07-03 residual-work convention)
**Prepared by:** bridge work loop agent; the acknowledgment act is the owner's (K-AUTH-1; D-GOV-04).
**Staged packet:** `../bridge/CHANGE_PREP_2026-07-04_proven_l2_acknowledgment.md` (exact profile edits §3; evidence index §2; owner steps §4).
**Ruling SHA:** `2081d6daa` — the commit publishing this record and applying the staged CHANGE (backfilled same-branch per the D-APP-44 / D-31 precedent).

## Decision ruled

Acknowledge the **proven L2** — the D-T0-08 precondition for opening app-dev F3 —
on the DEC-064/TP-RUNNER-014 evidence, and apply the staged tier-0 CHANGE
(profile `headless_runner` impl/status lines + `profile_version` 0.3 -> 0.4).

## Evidence of record (commit-bound)

- PROVISIONAL entrypoint
  `projects/chirality-piping/core/runner/headless/src/bin/headless_preview_runner.rs`
  (DEC-064 / piping D-32 O-A; TP-RUNNER-014; code commit `035e25991`).
- Validated-kernel run through the entrypoint: exit 0, job `Completed`,
  `MECHANICS_SOLVED`, 822 result refs including the library-test golden signal
  `result:stress:pipe-P-120:end-j:torsional-shear`, two SHA-256 checksums;
  witness
  `projects/chirality-piping/validation/witness/generated/tp_runner_014_headless_entrypoint_preview_run.json`;
  run record `WORKING_ITEMS_RUN_2026-07-04_TP-RUNNER-014.md` in the DEL-10-05
  deliverable's `_run_records` directory (named with the same pointers in
  Receipt 23's executed-pointers line).
- DEC-025 five-surface sweep 5/5 bound to the tranche HEAD `98dfde1d1`;
  adversarial review reproduced the run byte-identical
  (`_DomainEngines/bridge/LOOP_RECEIPTS.md` Receipt 23).
- Landed on main at the PR #46 merge commit `f4169a282`.

## Human ruling

**Ruling recorded:** ACKNOWLEDGED — proven L2 on the cited evidence (owner,
Ryan Tufts, in-session 2026-07-04).

Owner direction, verbatim (this run's steer):

> Proceed accordingly: merge PR #46 → acknowledge D-T0-10 → rule D-APP-49 →
> rule D-APP-50 once the source-types tranche lands.

The acknowledgment applies the staged CHANGE prep §3 edits (same-commit,
owner-delegated by the direction above per the register row's decision text
"acknowledge ... and apply the staged profile edits").

## Scope not granted

No integration-level movement (`integration_level` stays `MANUAL_BRIDGE`;
L2->L3 movement stays per-operation risk-graded under D-T0-03), no live
binding (still gated by app-dev F3 per the profile's open_issues line), no
final CLI syntax claim (the entrypoint stays PROVISIONAL per DEC-064 rider 1),
no lifecycle, release, professional, certification, sealing, authentication,
or code-compliance claim.

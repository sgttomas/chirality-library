# D-T0-18 - PROPOSAL: advance PEC integration staging to L3 (OPERATION_PROPOSAL), scoped to the import-proposal seam

**Status:** AWAITING_RULING.
**Date prepared:** 2026-07-05
**Decision ID:** D-T0-18 (residual of `D-T0-13`, 2026-07-03 residual-row convention)
**Prepared by:** PEC work loop agent. The ruling act is the owner's (K-AUTH-1; D-GOV-04).

Structure precedent: the residual-row packets `D-T0-10`/`D-T0-17` and the
option-slate shape of `D-T0-13_pec_integration_staging.md`.

## Why this row exists now

D-T0-13 O-A ruled **L2 as the destination with L3 future-only**, expressly
"pending a pec proposal-shaped API". Both preconditions named by the ruled
path have since been discharged:

1. **The proposal-shaped API exists.** The D-PEC-08 O-A tranche (PR #82,
   merged 2026-07-05) implemented `import_proposal` records with the profile's
   `operation_proposal_contract` lifecycle (draft → ready_for_review →
   accepted → rejected/applied), hash+version-bound human acceptance,
   staleness refusal, and transaction-atomic human-only apply.
2. **The evidence precondition is met.** D-PEC-05 O-B deferred L3 "until
   after D-PEC-01 pilot evidence"; evidence 01–04 exists and the owner's
   Gate-2 adoption (2026-07-05, D-T0-12 adoption note) judged it sufficient
   for profile adoption.

Owner direction opening this preparation (2026-07-05, in-session, verbatim):
"I want to get to L3."

## Decision to rule

Whether to advance PEC's ruled staging destination from L2 to L3 —
`integration_level: OPERATION_PROPOSAL` in the schema's vocabulary — scoped
initially to the §16 import-contract family through the `import_proposal`
seam, with semantics fixed by the companion pec-local packet `D-PEC-12`.

## What L3 changes (and what it does not)

Changes: the loop/embedded agent may **author and file** import proposals
(the propose + dry-run acts) as first-class operation proposals; the profile
`integration_level` moves `MANUAL_BRIDGE` → `OPERATION_PROPOSAL`; an L3
evidence capture convention starts (mirroring the L1/L2 conventions).

Does NOT change: accept and apply remain human-only in-app acts forever
(K-AUTH-1 analogue; profile `accepted_or_applied_requires`); `force` is never
agent-set; D-T0-14 residency stays CLOSED — the agent proposes from
owner-provided files and does not read instance content beyond what a
D-PEC-01-style basis ruling enumerates; no other write operation family is
opened; no pilot-readiness or go-live implication.

## Options

| ID | Option | Consequence |
|---|---|---|
| O-A | Advance to L3 scoped to the import-proposal seam, semantics per D-PEC-12. | Agent may propose; humans accept/apply; profile level flips with validator + live-pin updates riding the execution PR; first L3 evidence run follows on a demo/scratch or owner-provided basis. |
| O-B | Keep the L2 destination; treat the upload-agent pathway as L2 tooling only. | No level change; agents file proposals only under per-run owner confirmation as today. |
| O-C | Defer. | Status quo; the D-PEC-05 deferral effectively continues without a named successor gate. |

## Recommendation (non-binding)

O-A. The seam was built precisely to make agent proposing safe: every
authority-bearing act stays human, hash-bound, and audited; scoping to the
import family keeps the profile's "L3 semantics overlap native lifecycles"
open issue contained (D-PEC-12 resolves it for imports only).

## On ruling (mechanism)

O-A: record the ruling verbatim here and in D-PEC-12; execute in one PR —
profile `integration_level` + open-issue annotations + validator report,
DOMAIN_ENGINE_INDEX row, conscious live-pin updates
(`test_live_baseline.py` bridge-status pins), registers, receipt; then the
first L3 evidence capture (`PEC_<date>_L3-evidence-01/`) on the basis the
owner names. O-B/O-C: row closes with the ruling recorded; no execution.

## Human ruling

**Ruling:** O-A affirmed by owner (Ryan Tufts), 2026-07-05.

Owner ruling of record (verbatim, in-session):

> 1. O-A advance.
> 2. The agent should have full agency, don't try to use semantics as a replacement
> for proper governance harnesses (more than just semantics) so focus on making a
> useful agent for now.
> Merge the PR first and then proceed accordingly.

Item 2 rules the companion `D-PEC-12` (recorded there). PR #84 was merged first
as directed (`45ff3e6a7`); execution proceeds in the PR carrying this note.

**Ruling SHA:** backfilled in the execution PR (see the PEC loop Receipt 28).

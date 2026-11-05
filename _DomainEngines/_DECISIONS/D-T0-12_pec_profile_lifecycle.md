# D-T0-12 - PROPOSAL: PEC profile lifecycle and Gate 2

**Status:** RULED / O-A affirmed by owner; published by PR #51 merge commit `57307cac1`.
**Date prepared:** 2026-07-04  
**Decision ID:** D-T0-12  
**Prepared by:** PEC work loop agent under the standing plan. The ruling act is the owner's (K-AUTH-1; D-GOV-04).

## Decision to rule

Confirm the lifecycle for the PEC domain-engine profile: DRAFT profile,
deterministic validator evidence for schema validity, and owner Gate 2 for any
VALIDATED-to-ADOPTED transition.

## Verified facts

| Fact | Source |
|---|---|
| The validator deterministically checks required fields, enums, deterministic tool declarations, operation proposal contract shape, and professional-boundary structure. | `tools/validation/validate_domain_engine_profile.py:4-8` |
| The validator writes a report under `_DomainEngines/` and never marks a profile VALIDATED or ADOPTED. | `tools/validation/validate_domain_engine_profile.py:22-37` |
| PEC's profile is staged as DRAFT at `_DomainEngines/pec/profile/pec.DRAFT.yaml`. | `_DomainEngines/pec/profile/pec.DRAFT.yaml` |
| PEC's own app has controlled record lifecycles and RBAC around approvals, decisions, checks, and issue events. | `projects/pec/docs/SPEC.md:50-85`, `projects/pec/docs/SPEC.md:151-164` |

## Options

| ID | Option | Consequence |
|---|---|---|
| O-A | Use the existing lifecycle: DRAFT authored by agent, VALID evidence from the validator, owner Gate 2 for adoption. | Matches the existing tier-0 profile lifecycle and keeps adoption human-only. |
| O-B | Keep the profile DRAFT until the harness tranche is authorized and executed. | More conservative, but delays even validator-supported profile readiness. |
| O-C | Defer profile lifecycle ruling. | Leaves profile status and future movement ambiguous. |

## Recommendation

Recommend O-A: accept validator evidence as the schema-validity prerequisite,
while keeping ADOPTED strictly owner-ruled.

## If O-A is ruled

The agent may keep regenerating the validation report as evidence. The owner may
later rule Gate 2 adoption on the evidence, but no agent may self-adopt or move
PEC to ADOPTED.

## Human ruling

**Ruling:** O-A affirmed by owner (Ryan Tufts), 2026-07-04.

**Publication:** Published by PR #51 merge commit `57307cac1` (2026-07-04).

Owner ruling excerpt:

> This is just reusing the exact lifecycle `open_pipe_stress` already went
> through (validator evidence -> owner Gate 2), and the validator ran VALID
> with zero findings. Ruling O-A also resolves the one coupling I flagged
> earlier: PR #51's live-baseline pin on the validation report becomes
> consistent by construction.

This ruling confirms the lifecycle and validator evidence path. It does not
itself adopt the PEC profile; Gate 2 remains open and owner-only.

## Gate-2 adoption ruling (2026-07-05, appended note — the O-A ruling text above is unchanged)

**Ruling:** PEC profile ADOPTED by owner (Ryan Tufts), 2026-07-05.

Owner ruling of record (verbatim, in-session):

> merge PR #82 now, then I adopt the pec profile for Gate 2, you may execute
> as you see fit.  We will not start the pilot DB this time.  Another time.

Basis: validator evidence current and VALID; D-PEC-01 pilot rehearsal evidence
01-04 exists (the D-PEC-04 O-B "until pilot evidence" deferral is thereby
discharged by the owner's own judgment). Executed: profile
`_DomainEngines/profiles/pec.yaml` status DRAFT -> ADOPTED, registry row and
banner updated, live-baseline pin consciously updated in the same PR, PEC-local
pointer row D-PEC-11 opened RULED. Adoption is a governance act only: no pec
source change, no pilot start (owner deferred it in the same ruling), no
professional or go-live claim (APEGA ceiling, K-AUTH-1).

**Adoption SHA:** recorded in the PEC loop receipt for this PR (Receipt 26).

Structure precedent (this appended note): the dated-corrigendum/adoption-note
convention of the D-PEC-07 packet and the D-T0-06 Gate-2 adoption record; the
ruled text above is unchanged. Note: the ruled text's reference to the
DRAFT-era staged profile path is historical — the profile has lived at
`_DomainEngines/profiles/pec.yaml` since the D-T0-16 tranche.

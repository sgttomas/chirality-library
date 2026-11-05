# D-T0-17 - RULING: PEC L1 accepted as proven (D-T0-13 staging step)

**Status:** RULED / ACCEPTED 2026-07-04.
**Date prepared:** 2026-07-04 (record added at acceptance per the D-T0-10 precedent)
**Decision ID:** D-T0-17 (residual of D-T0-13 per the 2026-07-03 residual-work convention)
**Prepared by:** PEC work loop agent; the acceptance act is the owner's (K-AUTH-1; D-GOV-04).
**Ruling SHA:** `0164d944f` — the commit publishing this record (backfilled same-branch per the D-T0-10 / D-APP-44 precedent).

## Decision ruled

Accept the **read-only L1 evidence rung** of the D-T0-13 O-A staging as proven,
on the two published evidence snapshots. Owner ruling of record (2026-07-04,
in-session, Ryan Tufts): **"I accept L1 as proven."**

## Evidence of record (commit-bound)

- `_DomainEngines/pec/PEC_2026-07-04_L1-evidence-01/` (PR #57, merge
  `8e42b126c`): deterministic-check seam — typecheck/test/build/drill all
  exit 0 at `090cd4efb`; 161 tests (core 72, server 89); drill 17/17 on a
  scratch DB; manifest with fixture SHA-256s.
- `_DomainEngines/pec/PEC_2026-07-04_L1-evidence-02/` (PR #58, merge
  `fa0cdf3b8`): owner-provisioned demo-basis API seam — authenticated session
  (ADR-007) as `admin@aurora.dev`, all 11 §15/§16 register exports, sponsor
  brief + package pack renders, revision-gate Explain payloads, plan view; 18
  artifacts SHA-256'd in the manifest; scratch DB deleted after capture;
  D-T0-14 CLOSED respected throughout (demo seed content only).

## What this acceptance unlocks — and what it does not

- **Unlocks:** the per-operation L2 stage of the ruled D-T0-13 O-A path.
  Sequence per the ruling: `backup.create` first; imports only with an
  explicit data/ruling basis; scratch-only seed/drill. Every L2 act remains
  human-confirmed per the profile's `requires_human_confirmation` flags, at
  demo/scratch basis unless and until D-PEC-01 rules a real-data case.
- **Does not change:** D-T0-14 residency (CLOSED default stands; real-data
  basis arrives only via D-PEC-01); profile status (DRAFT; Gate 2 adoption
  remains owner-only, D-T0-12); fences F-PEC-1..4; L3 remains future-only
  pending a pec proposal-shaped API.
- Demo-scope caveat carried forward from the evidence manifests: L1 was proven
  at admin visibility over seeded demo content; scoped-persona visibility
  capture remains an optional later snapshot and is not a precondition the
  owner set for this acceptance.

## Human ruling

**Ruling:** ACCEPTED — owner (Ryan Tufts), 2026-07-04, in-session:
"I accept L1 as proven." Recorded verbatim in `_DomainEngines/pec/LOOP_RECEIPTS.md`
Receipt 7 with the handoff direction that accompanied it.

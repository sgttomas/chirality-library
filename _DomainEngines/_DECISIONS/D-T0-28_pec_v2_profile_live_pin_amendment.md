# D-T0-28 — D-T0-27 live-baseline pin amendment

**Status:** `RULED O-A / APPLIED / EFFECTIVE SUPPORTING AMENDMENT`

**Date presented:** 2026-08-02

**Decision ID:** D-T0-28

**Packet:**
`../bridge/PEC_V2_PROFILE_LIVE_PIN_AMENDMENT_D-T0-28_2026-08-02/PACKET.md`

**Exact test preimage SHA-256:**
`80823ee8dea253f91145302f37e618bdf8feb753f032a741d0aa0e4f0df1e70c`

**Exact proposed postimage SHA-256:**
`7a4e8aa0fdb28cacdfedb62a307a260bd090136362102b48673ea2a9842d7638`

## Named precedent

The exact Tier-0 precedent is the D-T0-26 conscious live-pin correction at
`_DomainEngines/applications/OD7-G3_D-T0-26_P-A/LIVE_PIN_CORRECTION_2026-07-28.md`.
That record updates this same live-baseline test path through explicit
preimage/postimage hashes, owner provenance, a production-behavior non-effect,
focused/full test evidence, and `git diff --check`. D-T0-28 follows that
pattern for the D-T0-27 successor-profile observations; it does not broaden it.

## Question and options

Authorize the exact one-path conscious pin amendment needed to complete the
required D-T0-27 checks?

- **O-A — authorize exact patch (recommended).** Only
  `tools/practitioner_harness/test_live_baseline.py` changes, from the exact
  preimage to exact postimage, followed by all packet checks.
- **O-B — defer.** Test unchanged; D-T0-27 remains materialized but not
  effective and D-T0-26 remains the effective durable posture.
- **O-C — amend or decline.** Requires a revised exact packet before any act.

## Authority fence

The ruled application changes only the conscious test pins described by the
exact packet. It changes no production behavior, profile, project, source,
ScopeOfWork, lifecycle, Task Management, accepted artifact, runtime, release,
reliance, D-PEC-75 state, or cross-loop duty. It is an effective supporting
amendment through PR #459 merge
`d9dc65804a0719fdf869af1ef60d53dc8cb0a895`.

## Owner ruling

Ryan Tufts, in-session, 2026-08-02 (verbatim):

> APPROVE:
>
> 1. D-T0-28: O-A.
>
> 2. DEL-01-06 REVIEW Gate 1 — select SELF_CHECK and authorize
>    review from INITIALIZED under D-PEC-75.
>
>    Use the deterministic six-item SOW checklist, AC-001 through
>    AC-006, bound to ScopeOfWork.md SHA-256
>    7dfa008b44d7425ab7e4fc47260d089c3d739416d666f52657d7093492ecf38a.
>
>    This opens mechanical contract-fitness review only. It does not
>    accept the repaired SOW, satisfy the future-production acceptance
>    criteria, advance lifecycle, make D-T0-27 effective, open source
>    production, authorize another P1 node, release, or professional
>    reliance.

Only item 1 is executed by this Tier-0 application. Item 2 remains with the
PEC loop and is neither implemented nor narrowed here.

## Application result

The exact test preimage was verified and `TEST_PIN_PATCH.diff` produced exact
postimage SHA-256
`7a4e8aa0fdb28cacdfedb62a307a260bd090136362102b48673ea2a9842d7638`.
The targeted suite passed 18/18, profile-validator tests passed 8/8,
bridge-status completed with no findings, self-check completed at the recorded
baseline, protected PEC hashes remained exact, and both candidate manifests
reproduced. Exact evidence is in the packet's `APPLICATION_EVIDENCE.md`.

Exact source `0e47c218c26830a4efeb29eb2d2f3ea99142b987` was published by PR
#459 merge `d9dc65804a0719fdf869af1ef60d53dc8cb0a895`. D-T0-28 is applied and
effective as a supporting amendment; its non-effects remain unchanged.

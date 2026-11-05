# D-T0-29 — Exact whitespace attribute for D-T0-28 patch evidence

**Status:** `RULED O-A / APPLIED / EFFECTIVE SUPPORTING AMENDMENT`

**Date presented:** 2026-08-02

**Decision ID:** D-T0-29

**Packet:**
`../bridge/D-T0-29_D-T0-28_PATCH_WHITESPACE_ATTRIBUTE_2026-08-02/PACKET.md`

**Exact `.gitattributes` preimage SHA-256:**
`7dece5526cb8dd98264bab5c96be95235cd482b1b1da4e623b63489dae1e1fe2`

**Exact proposed postimage SHA-256:**
`c0d9e5b7e3bbca1f41087959d6095e75d578fef172123050da7145f52fb9d89f`

## Named convention

Root `.gitattributes` already applies `-whitespace` to
`execution/_ScopeChange/**/*.diff` because unified-diff artifacts carry
format-mandated single-space blank context lines. D-T0-29 proposes the same
convention for exactly the ruled D-T0-28 patch path and no other file.

## Question and options

Authorize the exact one-line attribute without changing the ruled D-T0-28
patch or test bytes?

- **O-A — authorize exact attribute (recommended).** Only `.gitattributes`
  changes from the exact preimage to exact postimage, followed by every packet
  check.
- **O-B — defer.** Preserve all bytes and keep candidate-whitespace blocked.
- **O-C — amend or decline.** Requires a revised exact packet before any act.

## Authority fence

The ruled application changes only the exact Git whitespace attribute. It
changes no validator behavior, patch, test, profile, project, PEC path, source,
ScopeOfWork, lifecycle, Task Management, runtime, release, reliance,
D-PEC-75 state, or cross-loop duty. It is an effective supporting amendment
through PR #459 merge `d9dc65804a0719fdf869af1ef60d53dc8cb0a895`.

## Owner ruling

Ryan Tufts, in-session, 2026-08-02 (verbatim):

> APPROVE:
>
> 1. D-T0-29: O-A.
>
> 2. DEL-01-06 REVIEW Gate 5 — HOLD.
>
>    Retain DEL-01-06 at INITIALIZED. The SELF_CHECK populated
>    AC-001 through AC-006 as PENDING FUTURE PRODUCTION, recorded
>    zero findings, and recommends no lifecycle transition.
>
> 3. DEL-01-06 ScopeOfWork contract fitness — ACCEPT.
>
>    I accept ScopeOfWork.md at SHA-256
>    7dfa008b44d7425ab7e4fc47260d089c3d739416d666f52657d7093492ecf38a
>    as the production contract for DEL-01-06.
>
>    AC-001 through AC-006 remain future-production obligations and
>    are not satisfied by this act. This acceptance does not advance
>    lifecycle, make D-T0-27 effective, independently open source,
>    authorize another P1 node, release, or professional reliance.

Only item 1 is executed by this Tier-0 application. Items 2 and 3 belong to
the PEC loop and are neither executed nor narrowed here.

## Application result

The exact `.gitattributes` preimage was verified and
`GITATTRIBUTES_PATCH.diff` produced exact postimage SHA-256
`c0d9e5b7e3bbca1f41087959d6095e75d578fef172123050da7145f52fb9d89f`.
Git reports the exact D-T0-28 patch path's `whitespace` attribute as `unset`.
The D-T0-28 patch remains exact SHA-256
`db807bef647db3ef6cd7f4208e5bb5ac5e8ee2775b6a8a19eaeb70434476a499`
and the applied test postimage remains exact SHA-256
`7a4e8aa0fdb28cacdfedb62a307a260bd090136362102b48673ea2a9842d7638`.

The targeted suite passed 18/18, profile-validator tests passed 8/8,
bridge-status completed with no findings, self-check completed at the recorded
baseline, candidate-whitespace passed against `origin/main`, protected PEC
hashes remained exact, and the manifest chain was regenerated. Exact evidence
is in the packet's `APPLICATION_EVIDENCE.md`.

Exact source `0e47c218c26830a4efeb29eb2d2f3ea99142b987` was published by PR
#459 merge `d9dc65804a0719fdf869af1ef60d53dc8cb0a895`. D-T0-29 is applied and
effective as a supporting amendment; its non-effects remain unchanged.

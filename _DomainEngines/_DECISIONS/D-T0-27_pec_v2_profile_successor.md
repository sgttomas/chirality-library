# D-T0-27 — PEC v2 Domain Engine Profile successor

**Status:** `RULED O-A / EFFECTIVE / ADOPTED / READ_ONLY`

**Date presented:** 2026-08-02

**Decision ID:** D-T0-27

**Candidate packet:**
`../bridge/PEC_V2_PROFILE_SUCCESSOR_D-T0-27_2026-08-02/PACKET.md`

**Exact candidate profile SHA-256:**
`be3044d3b3d402d3c3268332d4386f76ddadd67f9e8bb258ba7aabee6d0cdc1d`

## Named precedents

- `_DomainEngines/_DECISIONS/D-T0-12_pec_profile_lifecycle.md` owns the
  validator-evidence-to-owner-Gate-2 lifecycle for PEC profile adoption.
- D-PEC-11 in
  `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md` is the
  project-local pointer-row precedent and creates no second adoption ruling.
- `_DomainEngines/_DECISIONS/D-T0-26_pec_profile_stale_demotion.md` is the live
  demotion and separately adopted PEC v2 successor requirement this row
  discharges only if ruled and effectively applied.

## Question

Adopt the exact newly authored PEC v2 profile at `READ_ONLY` as the separately
adopted successor required by D-T0-26, or keep the current frozen-v0.4 profile
`STALE / DENY_ALL`?

## Options

- **O-A — adopt now (recommended).** Owner Gate 2 approves the exact candidate
  and its application plan, effective only after exact application merge;
  D-PEC-76 is the local pointer row and no second ruling.
- **O-B — defer.** Keep the exact candidate as validated preparation; leave
  the live profile unchanged; keep both D-PEC-75 executable options held
  before source activation while allowing only separately owner-ruled bounded
  SOW-currency work.

## Recommendation

Recommend O-A. Accepted PEC v2 contract bytes support a narrow read-only
profile now. It declares no runtime or mutating operation, and adopting it
before adapter code avoids a deadline-driven boundary decision.

## Current authority fence

The exact application preserves the prior live profile at SHA-256
`0d6e1505003cffeba0393bdebaa48f19f27e2b1de8964e2c2bd262331f9ccca6`
under the packet and installs candidate SHA-256
`be3044d3b3d402d3c3268332d4386f76ddadd67f9e8bb258ba7aabee6d0cdc1d`
at `ADOPTED / READ_ONLY`. D-T0-28 O-A corrected the two conscious
live-baseline pins at exact postimage SHA-256
`7a4e8aa0fdb28cacdfedb62a307a260bd090136362102b48673ea2a9842d7638`;
all application checks pass. PR #459 published exact source
`0e47c218c26830a4efeb29eb2d2f3ea99142b987` through merge
`d9dc65804a0719fdf869af1ef60d53dc8cb0a895`, whose second parent is that
source. D-T0-27 is effective at that merge; current main
`556ae59a34ac2f06ef924d367843a72ea00d1f37` descends from it.

This ruling and application create no PEC source/SOW/software-workflow,
lifecycle, artifact-fitness, Task-Management, release, professional-reliance,
or cross-loop act and declare no runtime, adapter-client, mutation, proposal,
or external-result tool.

## Owner ruling

Ryan Tufts, in-session, 2026-08-02 (verbatim):

> APPROVE:
>
> 1. Merge PR #458 at source SHA
>    5ea7c116d32aa8f133536a1a1de6c7c1cb4a9f88.
>
> 2. D-T0-27: O-A.
>
> 3. D-PEC-75: O-A.

D-T0-27 O-A adopts the exact candidate and authorizes only the bounded
`APPLICATION_PLAN.md`. PR #458 is merged at
`23d15899fd0acf5d1d0513f3fe396438375c9e25`. Exact application source
`0e47c218c26830a4efeb29eb2d2f3ea99142b987` was published by PR #459 merge
`d9dc65804a0719fdf869af1ef60d53dc8cb0a895`; D-T0-27 is therefore effective
at `ADOPTED / READ_ONLY`. D-PEC-75 disposition and execution remain governed
by the PEC loop and are not performed by this row.

## Effectiveness identity

| Identity | Git SHA |
|---|---|
| PublicationSHA | `0e47c218c26830a4efeb29eb2d2f3ea99142b987` |
| EffectiveSHA | `d9dc65804a0719fdf869af1ef60d53dc8cb0a895` |
| Current descendant basis | `556ae59a34ac2f06ef924d367843a72ea00d1f37` |

The effective merge has the exact publication SHA as its second parent. The
live profile remains exact SHA-256
`be3044d3b3d402d3c3268332d4386f76ddadd67f9e8bb258ba7aabee6d0cdc1d`;
its portable validation remains `VALID`, `ADOPTED`, with zero findings. The
effective profile grants only the declared `READ_ONLY` boundary. It creates no
profile-mediated invocation by itself and no source, lifecycle, release, or
professional-reliance authority.

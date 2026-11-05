# D-T0-15 - PROPOSAL: PEC standing loop goal and fences

**Status:** RULED / O-A affirmed by owner; published by PR #51 merge commit `57307cac1`.
**Date prepared:** 2026-07-04  
**Decision ID:** D-T0-15  
**Prepared by:** PEC work loop agent under the standing plan. The ruling act is the owner's (K-AUTH-1; D-GOV-04).

## Decision to rule

Adopt the standing PEC loop goal and fences F-PEC-1..4 after the registration
package is reviewed.

## Verified facts

| Fact | Source |
|---|---|
| The PEC loop goal currently implements `plans/pec_bridge_integration_plan_2026-07-04.md` and says the later standing goal takes over only if the owner adopts it. | `_DomainEngines/pec/WORKPLAN_2026-07-04_pec_loop.md` |
| The live launcher is already present and ACTIVE in `init/init-prompt.md`, ahead of the older plan expectation that it would be STAGED. | `init/init-prompt.md` §4 |
| PEC's own status file says remaining pilot work is human and pilot-feedback driven. | `projects/pec/docs/STATUS.md:82-92` |
| PEC runtime state changes are controlled by app RBAC/lifecycles, not file edits. | `projects/pec/docs/SPEC.md:50-85`, `projects/pec/docs/SPEC.md:151-164` |

## Proposed standing goal

Keep the PEC project surface governably aligned with the framework and move the
PEC standing plan forward as far as live authority permits.

## Proposed fences

| Fence | Boundary |
|---|---|
| F-PEC-1 | No writes under `projects/pec/**` except `execution/_Coordination/**`, `AGENTS.md`, and the one-time `projects/pec/docs/STATUS.md` pointer edit; never `pec.db*`, `backups/**`, source trees, fixtures, tools, or manifests; never run the server or a mutating CLI against a non-scratch DB. |
| F-PEC-2 | No invention or file-level mutation of PEC record states; approvals, checks, decisions, holds, issues, and comments exist only as app-created RBAC records or cited owner statements. |
| F-PEC-3 | No `npm publish`, release, packaging act, new PEC runtime dependency, or PEC instance-content egress absent the D-T0-14 ruling. |
| F-PEC-4 | Tier-0 writes only under `_DomainEngines/pec/**` and `_DomainEngines/proposals/pec/**`, plus this registration package's enumerated tier-0 edits; no integration advance past L0 without D-T0-13 and no harness code changes without D-T0-16. |

## Options

| ID | Option | Consequence |
|---|---|---|
| O-A | Adopt the standing goal and fences above; treat the already-ACTIVE launcher as Receipt-0 owner-directed scaffolding, not as profile adoption. | Establishes the standing PEC loop boundary. |
| O-B | Adopt the fences but require a different owner-spoken goal. | Keeps the safety boundary while letting the owner choose wording. |
| O-C | Defer the standing loop. | PEC remains in registration-only mode. |

## Recommendation

Recommend O-A.

## Human ruling

**Ruling:** O-A affirmed by owner (Ryan Tufts), 2026-07-04.

**Publication:** Published by PR #51 merge commit `57307cac1` (2026-07-04).

Owner ruling excerpt:

> The goal wording is the one from the workplan you directed; the fence table
> matches F-PEC-1..4 as authored (I diffed the packet wording against the
> workplan -- same boundaries, with F-PEC-4 sensibly adding "this registration
> package's enumerated tier-0 edits"). The "launcher is Receipt-0 scaffolding,
> not adoption" clause is exactly the right disambiguation of the
> ACTIVE-ahead-of-plan delta.

This ruling adopts the standing goal and fences after the registration package
is published. It does not convert the already-ACTIVE launcher into profile
adoption.

## Fence-scope grant note (dated — no fence rewrite)

2026-07-06, by the owner's D-T0-19 O-1A ruling (verbatim in
`D-T0-19_pec_appdev_bridge_lane.md`): the F-PEC-4 fence set gains the
enumerated app-dev **decision/coordination packet** paths —
`projects/chirality-app-dev/execution/_Coordination/_DECISIONS/**` rows
authored as PROPOSALs by the pec work loop; app-dev **source** stays behind
D-APP rulings. Deconfliction with the app-dev↔piping loop is recorded as a
dated grant note in the app-dev register preamble (same date); D-APP IDs are
minted from the live app-dev register at authoring time. Twin notes: the
D-T0-19 packet and the pec workplan's F-PEC-4 bullet.

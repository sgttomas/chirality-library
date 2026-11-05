# D-T0-13 - PROPOSAL: PEC integration level and staging

**Status:** RULED / O-A affirmed by owner; published by PR #51 merge commit `57307cac1`.
**Date prepared:** 2026-07-04  
**Decision ID:** D-T0-13  
**Prepared by:** PEC work loop agent under the standing plan. The ruling act is the owner's (K-AUTH-1; D-GOV-04).

## Decision to rule

Choose PEC's integration destination and staging sequence across L0, read-only
evidence, domain-controlled writes, and any future proposal-shaped API path.

## Verified facts

| Fact | Source |
|---|---|
| PEC health scripts are `typecheck`, `test`, `build`, and `drill`; `drill` uses a scratch DB. | `projects/pec/package.json:12-25`, `projects/pec/tools/pilot-drill.ts:1-21`, `projects/pec/tools/pilot-drill.ts:87-95` |
| PEC server defaults to the `PEC_DB` environment value or its local database path; running the server opens that database. | `projects/pec/server/src/index.ts:16-22` |
| Backup/restore can write backup files and replace the configured database path. | `projects/pec/tools/backup.ts:1-20`, `projects/pec/tools/backup.ts:71-130` |
| PEC importers seed/update controlled records and use row-level accept/reject/conflict reports. | `projects/pec/server/src/import/index.ts:1-31`, `projects/pec/docs/SPEC.md:376-380` |
| L3-style proposal apply would overlap PEC's native approval, decision, check, and issue lifecycles. | `projects/pec/docs/SPEC.md:130-146`, `projects/pec/docs/SPEC.md:461-471` |

## Options

| ID | Option | Consequence |
|---|---|---|
| O-A | L0 now; L2 destination staged through L1 read-only evidence (tests, exports, reports, explain, drill) and then per-operation L2 (backup/create first; imports only with explicit data/ruling basis; scratch seed/drill only). L3 future-only until PEC exposes a proposal-shaped API. | Advances safely without pretending PEC has the same apply seam as piping. |
| O-B | L1 only, no L2 target. | Simplest boundary, but underuses PEC's existing deterministic drill/backup/import seams. |
| O-C | Declare L3 destination now. | Premature; PEC lacks a proposal-shaped API distinct from native lifecycle acts. |
| O-D | Defer integration staging. | Keeps the standing loop at L0 only. |

## Recommendation

Recommend O-A.

Any L1/L2 evidence that affects project reasoning should be captured in new
immutable snapshot folders under `_DomainEngines/pec/` with a manifest naming
source refs, actor/visibility basis, output paths, warnings, and limitations.
Generated outputs are derivative packages, not substitute authority.

## Human ruling

**Ruling:** O-A affirmed by owner (Ryan Tufts), 2026-07-04.

**Publication:** Published by PR #51 merge commit `57307cac1` (2026-07-04).

Owner ruling excerpt:

> PEC has no proposal-shaped apply seam -- its "writes" are native RBAC
> lifecycle acts, so declaring L3 now (O-C) would pretend an API exists that
> doesn't, and L1-only (O-B) wastes the genuinely deterministic seams PEC does
> have (drill on scratch DB, VACUUM-INTO backup, row-level import reports).

Owner sequencing note:

> Ruling O-A here does not by itself unlock any instance-content capture --
> every L1 evidence act touching real data still routes through D-T0-14.

This ruling authorizes the stated L0-now/L2-destination staging model. It does
not grant residency authority or permit agent-visible capture of PEC instance
content.

# D-T0-14 - PROPOSAL: PEC data residency and instance-content visibility

**Status:** RULED / deferred with O-A CLOSED default; published by PR #51 merge commit `57307cac1`.
**Date prepared:** 2026-07-04  
**Decision ID:** D-T0-14  
**Prepared by:** PEC work loop agent under the standing plan. The ruling act is the owner's (K-AUTH-1; D-GOV-04).

## Decision to rule

Decide whether and under what conditions agents may view or capture PEC
instance content, including pilot DB content, register exports, reports, and
visibility-filtered logs.

## Verified facts

| Fact | Source |
|---|---|
| PEC log visibility is role-filtered and title/detail-bearing rows are redacted outside the actor's visible logs. | `projects/pec/docs/SPEC.md:80-85`, `projects/pec/docs/SPEC.md:468-471` |
| Register, report, import/export, plan, schedule, and lookahead routes expose project data through API/read surfaces. | `projects/pec/docs/SPEC.md:355-372`, `projects/pec/docs/SPEC.md:513-533` |
| Real pilot work remains human and may involve real MDL/RAIL/decision/risk data. | `projects/pec/docs/STATUS.md:82-87` |
| The server and backup tools use configurable database and backup paths. | `projects/pec/server/src/index.ts:16-22`, `projects/pec/tools/backup.ts:18-32` |

## Options

| ID | Option | Consequence |
|---|---|---|
| O-A | CLOSED/TBD for now: agents read committed repo files only; no instance-content capture or egress unless separately authorized. | Gate-safe default and no privacy surprise. |
| O-B | Owner-approved exported artifacts only, with an actor/visibility basis and immutable capture manifest. | Enables bounded L1/L2 evidence while preserving traceability. |
| O-C | Open residency for PEC instance content. | Broadest access; requires explicit owner comfort with real project-controls data exposure. |
| O-D | Custom residency rule. | Owner supplies provider/location/visibility constraints. |

## Recommendation

Frame only. If deferred, use O-A as the gate-safe default. For any future
capture of instance data, require a declared actor/visibility basis and write a
manifest with source refs, command refs, output paths, and limitations.

## Human ruling

**Ruling:** Deferred by owner (Ryan Tufts), 2026-07-04, with O-A CLOSED default
kept in force for now.

**Publication:** Published by PR #51 merge commit `57307cac1` (2026-07-04).

Owner ruling excerpt:

> I'd still defer: under O-A CLOSED the L1 lane remains usable against
> committed fixtures and scratch/demo DBs, which covers everything until real
> MDL/RAIL data enters -- and that moment already has a home as D-PEC-01 in
> the pec register. Let D-PEC-01 preparation force the O-B ruling with a
> concrete data case in front of you, rather than pre-authorizing egress in the
> abstract.

The current rule remains repo-file-only plus committed fixtures and scratch/demo
DB evidence. O-B is not pre-authorized; a future D-PEC-01 packet should present
the concrete owner-approved export case if real PEC instance content becomes
necessary.

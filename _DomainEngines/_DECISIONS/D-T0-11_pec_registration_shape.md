# D-T0-11 - PROPOSAL: PEC registration shape

**Status:** RULED / O-A affirmed by owner; published by PR #51 merge commit `57307cac1`.
**Date prepared:** 2026-07-04  
**Decision ID:** D-T0-11  
**Prepared by:** PEC work loop agent under the standing plan. The ruling act is the owner's (K-AUTH-1; D-GOV-04).

## Decision to rule

Select the PEC tier-0 registration shape: loop directory, profile id,
proposal directory, profile staging location, `_LATEST.md` convention,
one-time `projects/pec/docs/STATUS.md` pointer edit, and the PEC-local
decision-ID scheme.

## Verified facts

| Fact | Source |
|---|---|
| The live tree already has a PEC loop launcher pointing to `_DomainEngines/pec/LOOP_INIT.md`; it is labeled ACTIVE. | `init/init-prompt.md` §4 |
| `projects/pec` is a workspace named `pec`; health scripts live in the root package manifest. | `projects/pec/package.json:1-25` |
| PEC's status file makes `projects/pec/docs/STATUS.md` the first read and persistent handoff surface. | `projects/pec/docs/STATUS.md:1-7`, `projects/pec/docs/STATUS.md:31-40` |
| The staged profile is not placed in `_DomainEngines/profiles/` because the live adapter observes `profiles/*.yaml` as a single mutable observation. | `tools/practitioner_harness/adapter_domain_engines.py:103-131` |
| Existing bridge-status awareness is hardcoded to app-dev, piping, and the tier-0 register. | `tools/practitioner_harness/cmd_bridge_status.py:73-104` |

## Options

| ID | Option | Consequence |
|---|---|---|
| O-A | Approve the authored shape: `_DomainEngines/pec/`, profile id `pec`, `_DomainEngines/proposals/pec/`, staged `_DomainEngines/pec/profile/pec.DRAFT.yaml`, `_LATEST.md` remains bridge-pointed, one STATUS pointer edit, and PEC-local `D-PEC-XX` rows. | Minimal naming, no conflict with bridge loop, and no multi-profile adapter breakage. |
| O-B | Use `pec-bridge` and/or profile id `pec_execution_control`. | More descriptive, but longer and less aligned with package/profile naming. |
| O-C | Defer registration shape. | Leaves PEC outside the tier-0 index and prevents the rest of the slate from settling. |

## Recommendation

Recommend O-A.

## If O-A is ruled

The owner ruling should treat this registration package as the accepted shape
for subsequent PEC-loop work. It does not adopt the profile, authorize
instance-data egress, move the profile into `_DomainEngines/profiles/`, or
execute the harness tranche.

## Human ruling

**Ruling:** O-A affirmed by owner (Ryan Tufts), 2026-07-04.

**Publication:** Published by PR #51 merge commit `57307cac1` (2026-07-04).

Owner ruling excerpt:

> `pec` as id matches the workspace/package name; loop dir, proposals dir, and
> `D-PEC-XX` are the sibling convention you already chose during planning.
> O-B (`pec_execution_control`) buys nothing -- the INDEX row carries the
> descriptive name. Keeping `_LATEST.md` bridge-pointed is right; pec
> discoverability is handled by the INDEX read-order edit instead.

This ruling accepts the authored registration shape only. It does not adopt the
profile, authorize instance-data egress, move the profile into
`_DomainEngines/profiles/`, or execute the harness tranche.

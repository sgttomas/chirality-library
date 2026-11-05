# D-T0-24 — Flow-A and Root runtime compatibility identity separation

**Status:** `RULED_EFFECTIVE`
**Date prepared:** 2026-07-27
**Decision ID:** D-T0-24
**Prepared by:** DOMAIN_ENGINE (Agent 1)
**Accepted repository basis:** `9fa2f82ac4b9e55873bcd7cd99ca042a4456fea2`
**AcceptedCandidateSHA256:** `6a42c2c7c3d9cd86eb10168d4589de7ed0ede0972f00ef4f356ffd4ed972bd45`
**DecisionSetManifestSHA256:** `a81aa66e73b8aa3812b6242343ca542c3cc77dc42163ce1b66dfa73ef582979e`
**PublicationSHA:** `aed9ef5ea1df7e128739fb6363218f0cc237e248`
**EffectiveSHA:** `4ac8348e0c15795f33bf2192b2964ee1347aca59`

## Owner ruling

Ryan Tufts, in-session, 2026-07-27:

> SELECT D-T0-24 CS-A exact candidate
> 6a42c2c7c3d9cd86eb10168d4589de7ed0ede0972f00ef4f356ffd4ed972bd45
> with candidate set
> a81aa66e73b8aa3812b6242343ca542c3cc77dc42163ce1b66dfa73ef582979e.
> Authorize final closeout preparation only.

This record is a closeout candidate. The quotation identifies the selected
semantic subject and authorizes preparation; it does not authorize this file's
application or Git closeout.

## Decision question

How does the existing Tier-0 Flow-A contract identity relate to the future,
separately governed Root runtime compatibility identity?

## Verified basis

1. D-T0-07 rules a Tier-0-owned Flow-A version scheme that references the
   relevant App version sources without transferring ownership to App.
2. D-T0-09 rules the current Flow-A value
   `flow-a.contract.v0.1.0`.
3. D-T0-23 coordinates App and PEC as clients of one Root shared runtime while
   preserving project and domain authority.
4. D-GOV-28 adopts Root PRD O-11: Root owns continuing stewardship of generic
   runtime semantics and their future versioned-contract evidence.
5. No selected accepted source in the bounded negative-search scope recorded
   by `CONSUMER_REFERENCE_SCAN.json` names a Root runtime compatibility
   identity or establishes a mapping, equivalence, range, or supersession
   relationship between it and Flow-A.
6. D-APP-48 and Piping D-30 record Flow-A consumption. Their pin currency and
   internal concordance are separate evidence questions and are not validated
   or repaired by this decision.

## Ruling — CONTINUE-SEPARATE

If exactly accepted by the owner:

1. The Flow-A contract identity remains the Tier-0-owned identity governed by
   D-T0-07 and D-T0-09. Its current value remains
   `flow-a.contract.v0.1.0`.
2. The future Root runtime compatibility identity is a distinct Root-owned
   identity. This ruling does not select its value, grammar, declaration
   point, comparison behavior, compatibility epoch, or binding record.
3. Neither identity implies or aliases the other. Equality of route names,
   package versions, source commits, release identities, fingerprints,
   transport success, or any other version-like label cannot establish a
   relationship between them.
4. Consumers must identify which governed identity they rely on. A Flow-A
   consumer does not thereby become a consumer of the Root compatibility
   identity, and a Root runtime client does not thereby become a Flow-A
   consumer.
5. Any later mapping requires a separate human ruling backed by exact
   direction, covered semantics, consumer inventory, source and effective
   interval, invalidation criteria, and evidence sufficient to establish the
   claimed relationship.
6. Any later retirement or supersession of Flow-A requires a separate human
   ruling backed by an exact successor, effective boundary, relied-semantic
   coverage, affected-consumer inventory, migration and rollback posture, and
   routed client evidence.
7. D-T0-07, D-T0-09, and D-T0-23 remain in force. Historical interpretation
   is unchanged.

## Scope limits

This candidate ruling does not:

- name or reserve the Root runtime compatibility identity;
- amend any Root runtime contract or authorize DEL-02-06 work;
- validate or repin D-APP-48, Piping D-30, or any consumer record;
- change Flow-A source, package, event, tool, SDK, or release bytes;
- authorize a mapping, retirement, supersession, migration, or compatibility
  claim;
- change App, Piping, PEC, Root, runtime, or domain scope;
- authorize implementation, lifecycle transition, release, or professional
  reliance.

## Closeout history

The semantic subject is the byte-identified candidate selected by the owner.
The record and register row were published by commit
`aed9ef5ea1df7e128739fb6363218f0cc237e248` and became effective through PR #380 at merge commit
`4ac8348e0c15795f33bf2192b2964ee1347aca59`. This bounded backfill records those identities without
changing the ruling clauses.

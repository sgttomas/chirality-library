# D-T0-26 — PEC profile stale demotion

**Status:** `RULED_EFFECTIVE`
**Date:** 2026-07-28
**PublicationSHA:** `7948eef43fe27eacd482688d9249a1ad2b92471c`
**EffectiveSHA:** `dc89356eb4db715bfe8357b25d8831c752cb822e`
**Effective-state closeout:** `../applications/OD7-G3_D-T0-25_D-T0-26_EFFECTIVE_CLOSEOUT_2026-07-28/D-T0-26_EFFECTIVE_STATE_CLOSEOUT.md`
**Accepted preparation input:** OD7-G3 `P-A` gate identity `f0714f38b902bbee074e5588da0b84a6e49661aaf0211a7360a457fad39797db`
**Accepted exact semantic input:** `95263e4fa5c72840a5053a91da904ea76acbef7050dae344e4e1e94cf4a22152`
**Accepted candidate-set identity:** `79ce291ec7ec5247543b05ea19078e2e06be7a5f99be0fae91363159e8198bc1`
**Accepted rebuilt planning package:** artifact `7940a9bd8f26497c8e3050b8a31cf6d89c09dbd2934c8e8ead04f1b016ab14d2`; P-A tranche `8913d5b6654128da60e889822833b84bee477129fe291201ed98605d00195c22`
**Application basis:** `2c8e4168220b49f1e83a45aa916a6eb29856f0b4`

## Decision

Approve the supervising Agent 0's P-A recommendation:

- demote the frozen PEC Domain Engine profile from version `0.2`,
  `ADOPTED` / `OPERATION_PROPOSAL`, to version `0.3`,
  `STALE` / `MANUAL_BRIDGE`;
- set
  `execution_policy: "DENY_ALL_PROFILE_MEDIATED_INVOCATIONS"` and
  `historical_binding_only: true`;
- retain its deterministic-tool, proposal-lifecycle, path, visibility, and
  data-residency declarations only as frozen-instance lineage;
- make the profile ineligible for governed profile-mediated invocation while
  continuing to permit static citation and schema validation;
- grant no live read, egress, mutation, or project authority and make no claim
  that an ungoverned machine consumer is mechanically unable to ignore the
  status or deny field; and
- require a new profile to be prepared and separately adopted against accepted
  PEC v2 contracts before any PEC v2 profile-mediated integration, and no
  later than activation of the first accepted PEC v2
  adapter/runtime-client deliverable.

The accepted semantic input is preserved byte-for-byte at
`../applications/OD7-G3_D-T0-26_P-A/accepted_candidate/ACCEPTED_INPUT.md`.

## Dependencies and identifiers

D-T0-25 is durable on `main` at merge
`2c8e4168220b49f1e83a45aa916a6eb29856f0b4`. The execution-time scan found
D-T0-26 and its application archive absent, established D-T0-26 as the next
free Tier-0 identifier, and established Receipt 30 as the next free bridge
receipt.

## Owner ruling

Ryan Tufts, in-session, 2026-07-28:

> "Finish out your plan now (attaining your goal) with self merge of PRs and auto approve for owners rulings, which should still be recorded in the usual manner with your recommendation standing as what I approved."

Under that direction, the supervising Agent 0's exact P-A recommendation
stated in the Decision section is the approved owner ruling for D-T0-26.

## Authority boundary

This ruling changes only the Tier-0 classification of the frozen PEC profile
and the records needed to make that classification durable. It grants no
profile-mediated invocation, successor-profile design, product or project
scope, PEC v2 work, runtime or implementation work, migration, compatibility,
release, or professional-reliance authority. Project-local PEC files,
PRDs, decompositions, ScopeOfWork contracts, notices, and pointers remain
unchanged.

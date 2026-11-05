# D-T0-26 / OD7-G3 P-A — Exact Application Tranche

**Status:** APPLICATION CANDIDATE ONLY — NO LIVE APPLY
**Owner application gate:** OPEN
**Frozen basis:** `4ac8348e0c15795f33bf2192b2964ee1347aca59`
**Accepted gate identity:** `f0714f38b902bbee074e5588da0b84a6e49661aaf0211a7360a457fad39797db`
**Accepted package identities:** candidate set `79ce291ec7ec5247543b05ea19078e2e06be7a5f99be0fae91363159e8198bc1`;
artifact set `b26af678b9e1f1f9f56327289874bd6dc4791046ac39be6386c397799138303e`

## Owning workflow

DOMAIN_ENGINE owns profile lifecycle preparation/validation; HELP_HUMAN presents; CHANGE owns later Git closeout.

## Exact effect

Apply profile 0.3 STALE/MANUAL_BRIDGE/deny-all and the integrated index update; retain historical declarations as lineage.

## Exact write surfaces if later approved

- `_DomainEngines/_DECISIONS/_REGISTER.md`
- `_DomainEngines/_DECISIONS/D-T0-26_pec_profile_stale_demotion.md`
- `_DomainEngines/profiles/pec.yaml`
- `_DomainEngines/DOMAIN_ENGINE_INDEX.md`
- `_DomainEngines/applications/OD7-G3_D-T0-26_P-A/`
- `_DomainEngines/profiles/_validation/pec.validation.json`

The application-package directory preserves the exact input, decision body,
manifests, validation, and future verbatim `OWNER_RULING.md`. No receipt,
pointer, notice, SCA, implementation, or Git surface is implicit.
Any additional surface returns as a new exact gate.

## Preimages and candidate bytes

`APPLICATION_MANIFEST.csv` records every preimage and candidate identity.
Load-bearing candidate identities:

- `ACCEPTED_INPUT.md` — SHA-256 `95263e4fa5c72840a5053a91da904ea76acbef7050dae344e4e1e94cf4a22152` (accepted exact semantic input)
- `DECISION_RECORD_CANDIDATE.md` — SHA-256 `0bd1b024643455a3a1b6c25dbe6fbc3363a932146e3b6666ace8f9d4016bcb8f` (pre-ruling decision body)
- `candidate_live/pec.yaml` — SHA-256 `db36664d9fbd3dc3c348e51dc5367d52753faf0eff10c13d36340f6cc019b8ae` (exact live profile candidate)
- `candidate_live/DOMAIN_ENGINE_INDEX.md` — SHA-256 `777cc1400c5aef17a3e4c3aa40f8de4d533b1228fbeb88d76ab3a4ca1bdcb690` (R-A + P-A serialized index candidate)
- `candidate_live/REGISTER.md` — SHA-256 `ab0f75ee11524cf6797e8b5a008eb628cf080a699a0cd1bc4efeb365d3501a5e` (serialized exact register candidate)

New decision and application-package paths have preimage state `ABSENT`.
Tier-0 register candidates use the exact D-T0-24 post-application bytes as
their declared predecessor and place D-T0-24, D-T0-25, and D-T0-26 in
numeric order before the terminal `Per-decision records` paragraph.

## Dependencies

The exact D-T0-25 R-A application is the required predecessor for both the
Tier-0 register (SHA-256 `8ad1787633179ea82984b3738cb2427b48a304247b4673657e85c938f6450656`) and shared
`DOMAIN_ENGINE_INDEX.md`. If R-A is not applied exactly, regenerate P-A.

## Validation required before live application

1. Reproduce the accepted package and per-gate hashes.
2. Reproduce current main, the durable D-T0-24 register identity, and the exact
   serialized predecessor declared by this successor before checking later ID
   reservations.
3. Reproduce every preimage hash in `APPLICATION_MANIFEST.csv`.
4. Verify exact candidate bytes or exact diff application.
5. Verify the only write paths are the enumerated surfaces.
6. Transcribe the future owner application ruling verbatim into
   `OWNER_RULING.md`; absence of that file blocks application.
7. Run tranche-specific postconditions recorded in `VALIDATION_PLAN.md`.

## Rollback

Before Git closeout, rollback restores each existing surface to its exact
preimage and removes only newly created tranche surfaces. After a published
Git closeout, never rewrite the decision history: use a separately approved
revert/supersession tranche. Profile, PRD, ScopeOfWork, and hold-state reversal
always requires its owning workflow and a new owner gate.

## Owner application gate

The owner must identify this packet's SHA-256 and its `TRANCHE_HASHES.sha256`
identity, approve the exact listed writes, and authorize no more than this
tranche. Acceptance of application planning alone is insufficient.

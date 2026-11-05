# D-T0-27 exact application plan

**State:** `PROPOSED / OWNER-GATED / NOT APPLIED`

## Preconditions

Application is lawful only when all are true:

1. the owner rules D-T0-27 O-A over candidate SHA-256
   `be3044d3b3d402d3c3268332d4386f76ddadd67f9e8bb258ba7aabee6d0cdc1d`;
2. PEC-local pointer row D-PEC-76 exists, cites the exact D-T0-27 candidate
   and application, and creates no duplicate adoption authority;
3. live `_DomainEngines/profiles/pec.yaml` still has preimage SHA-256
   `0d6e1505003cffeba0393bdebaa48f19f27e2b1de8964e2c2bd262331f9ccca6`;
4. the candidate validator result is `VALID`, `profile_status == ADOPTED`,
   and zero findings; and
5. the application write list and resulting postimage hashes are frozen before
   CHANGE publication.

## Allowed application acts

The later application tranche may only:

1. preserve the exact live preimage under this packet at
   accepted_preimage/pec_v0.4_profile_v0.3.yaml;
2. install the exact candidate bytes at `_DomainEngines/profiles/pec.yaml`;
3. regenerate `_DomainEngines/profiles/_validation/pec.validation.json`;
4. update `_DomainEngines/DOMAIN_ENGINE_INDEX.md` and `_DomainEngines/_LATEST.md`
   from the stale v0.4 statement to the exact v2 `ADOPTED / READ_ONLY` posture;
5. record the owner ruling/effective identity in D-T0-27, the Tier-0 register,
   and the ordinary bridge receipt;
6. perform only the D-T0-27-bounded local pointer corrections recorded by
   D-PEC-76 in
   `projects/pec/AGENTS.md`, `projects/pec/docs/STATUS.md`, and the PEC decision
   register/record; and
7. create an exact application manifest and handoff state under this packet.

`projects/pec/chirality.project.json` remains byte-identical because it already
points to the canonical `_DomainEngines/profiles/pec.yaml` path.

## Required checks

- exact preimage and candidate SHA checks;
- `python3 tools/validation/validate_domain_engine_profile.py` against the
  candidate before application and the live postimage after application;
- `pytest -q test_validate_domain_engine_profile.py` from
  `tools/validation/`;
- `python3 tools/practitioner_harness/harness.py bridge-status`;
- `python3 tools/practitioner_harness/harness.py self-check`;
- targeted practitioner-harness live-baseline and domain-engine adapter tests;
- D-PEC-74 accepted API schema/test/fixture hashes unchanged;
- `projects/pec/software-workflow.json` unchanged unless separately opened by
  a source-production packet;
- exact changed-path containment, manifest reproduction, committed-range
  `coord-check`, and `git diff --check`.

## Rollback and failure behavior

Before publication, any failed precondition or check restores the exact live
preimage, its validation report, index/pointer prose, and only the coordinated
local pointer files changed by this application. The candidate packet remains
as failed/deferred evidence. No source or lifecycle file is touched.

After publication, correction is forward-only through a successor decision;
the preserved preimage and Git history remain recovery evidence. A failed
profile adoption blocks profile-mediated PEC v2 integration and both D-PEC-75
executable options before source activation because O-A is unambiguously
adapter-shaped and O-B's mandatory DDL makes the trigger at least ambiguous.
It does not block file-native governed work or a separately owner-ruled bounded
SOW-currency phase.

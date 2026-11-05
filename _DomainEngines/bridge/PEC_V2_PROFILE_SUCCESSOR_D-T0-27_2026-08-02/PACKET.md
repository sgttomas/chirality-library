# D-T0-27 candidate — PEC v2 Domain Engine Profile successor

**State:** `AWAITING_RULING / VALIDATED CANDIDATE / LIVE PROFILE UNCHANGED`

**Prepared:** 2026-08-02

**Action classification:** `PROFILE_ADOPTION` + `BOUNDARY_AUDIT`

**Proposed integration level:** `READ_ONLY`

**Candidate profile:** `candidate/pec.yaml`, SHA-256
`be3044d3b3d402d3c3268332d4386f76ddadd67f9e8bb258ba7aabee6d0cdc1d`

## 1. Decision requested

Should the owner separately adopt the exact PEC v2 profile candidate as the
successor to the live frozen-v0.4 profile?

The live `_DomainEngines/profiles/pec.yaml` remains version `0.3`, `STALE`,
`MANUAL_BRIDGE`, and `DENY_ALL_PROFILE_MEDIATED_INVOCATIONS`; its current
SHA-256 is
`0d6e1505003cffeba0393bdebaa48f19f27e2b1de8964e2c2bd262331f9ccca6`.
This packet does not edit, promote, or adopt those bytes.

## 2. Why the decision is ripe

D-T0-26 requires a newly prepared and separately adopted successor against
accepted PEC v2 contracts before any PEC v2 profile-mediated integration and
no later than activation of the first accepted PEC v2 adapter/runtime-client
deliverable. PEC v2 now has accepted, exact contract bytes:

- API schema SHA-256
  `0a4e42737e628be604bd163e8c6f835cda488f7978ae9e973cff03d1f8695c67`;
- ADR SHA-256
  `f63ecc2725b26e0e78be993a7902ad5b901cdfbb2e7921a19fc3442c9d785db5`;
- SPEC SHA-256
  `8b25a0d1f7ec7451ed3d19839904ee0c5f9a69b94df50f2122d9065c59a02315`;
- PRD v2.2 SHA-256
  `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba`;
  and
- software-workflow profile SHA-256
  `46f8495444de922d5f85bd71ee473d8ff980fac0b8c30392d7ddf76fee4fff82`.

DEL-08-02 is `CHECKING`, its five acceptance items have zero findings, and
the owner accepted the schema/test/fixture bytes recorded in the D-PEC-74
handoff. That is enough accepted implementation shape to design a narrow
read-only boundary. No runtime tool, store, service, transport, adapter client,
or proposal operation is needed for this adoption.

### Named governance precedents

- Gate-2 lifecycle and Tier-0 profile-adoption ownership:
  `_DomainEngines/_DECISIONS/D-T0-12_pec_profile_lifecycle.md`.
- PEC-local pointer-row precedent: D-PEC-11 in
  `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md`; it locates
  D-T0-12 without creating a second semantic ruling.
- The live stale demotion and exact successor condition:
  `_DomainEngines/_DECISIONS/D-T0-26_pec_profile_stale_demotion.md`.

## 3. Trigger interpretation

- D-PEC-75 O-A / DEL-01-06 is unambiguously trigger-reaching: its local
  configuration reader is a filesystem adapter under ADR-PEC-V2-001. Selection
  may open only its bounded SOW-currency phase; source activation must wait
  until this successor is adopted and effective.
- DEL-08-03 is likewise trigger-reaching when activated: serialization is a
  presentation adapter under the same ADR.
- D-PEC-75 O-B / DEL-01-01 is not named as an adapter/runtime-client
  deliverable, but its mandatory DDL/store-persistence output sits on the
  accepted ADR's explicit core-versus-persistence-adapter seam. The trigger is
  therefore at least ambiguous and must not be narrowed by inference. The safe
  sequence holds its source activation until this successor is adopted and
  effective; its bounded owner-ruled SOW-currency phase may proceed separately.

Preparing this profile now avoids making the next packet depend on a narrow
reading and makes the boundary explicit before adapter code exists.

## 4. Proposed boundary

The candidate is a new v2 profile authored from current accepted contracts,
not a status promotion of the frozen profile. It retains stable profile id
`pec` and the canonical live path so `projects/pec/chirality.project.json`
does not need a path migration. At application time the exact stale preimage
is preserved in this immutable packet, outside `profiles/*.yaml`, before the
candidate replaces the canonical live path.

The candidate declares:

- `profile_status: ADOPTED`, effective only after the owner Gate-2 ruling and
  the exact application merge;
- `integration_level: READ_ONLY` and a declared-read/summary-only execution
  policy;
- the accepted PEC-owned API schema as the sole current authoritative domain
  artifact, explicitly not authority over file-native governance facts;
- bounded readable accepted contracts and development-check evidence;
- protected source, workflow, project-manifest, governance, lifecycle, and
  profile paths;
- agent writes only to bounded integration evidence/coordination surfaces;
- only the registered software checks and practitioner-harness self-check;
- no operation-proposal lane, runtime operation, mutating tool, adapter-client
  invocation, external-result state, instance-content capture, or network
  egress; and
- explicit graceful-absence, file-native-authority, content-minimality,
  no-second-loop, no-ruling-write, other-loop autonomy, release, and
  professional-boundary notices.

`projects/pec/software-workflow.json` remains a separate WORKING_ITEMS check
registry. The candidate may cite its allowlisted checks; it neither replaces
that file nor turns the file into profile or source authority.

## 5. Options

### O-A — Adopt the exact v2 successor now (recommended)

Approve the exact candidate SHA above for Gate 2 and authorize its later
application only through `APPLICATION_PLAN.md`. PEC-local pointer row D-PEC-76
records and locates this Tier-0 ruling without duplicating it. The live profile becomes the new
`ADOPTED / READ_ONLY` v2 profile only when that application is merged.

This clears the D-T0-26 successor-profile prerequisite while granting only the
two declared non-mutating/evidence tools. It does not activate D-PEC-75,
authorize profile-mediated runtime integration, or accept any later artifact.

### O-B — Keep the candidate validated but do not adopt

Retain the live `STALE / DENY_ALL` profile and this candidate as preparation
evidence only. Both D-PEC-75 executable options remain held before source
activation, while a separately owner-ruled bounded SOW-currency phase may
proceed. DEL-08-03 and every other adapter/runtime-client activation likewise
remain blocked on a later successor-profile ruling.

## 6. Recommendation

Recommend **O-A**. The narrow read-only profile is supported by accepted bytes
today, removes the stale-profile deadline from the critical path, and grants
no runtime or mutation capability. Deferral preserves safety but adds a hard
sequencing dependency immediately before the first filesystem or presentation
adapter.

The owner may rule:

```text
D-T0-27: O-A.
D-T0-27: O-B.
```

Amendment or decline remains lawful; a consequential amendment requires a
revised exact candidate and fresh validation before application.

## 7. Effects and non-effects

An O-A ruling approves only the exact candidate and coordinated application
mechanism. It does not by itself modify the live profile. Effective adoption
requires the application preconditions, exact-byte verification, presence of
the D-PEC-76 pointer row, and merge described in `APPLICATION_PLAN.md`.

Neither option authorizes PEC source production, a ScopeOfWork edit, lifecycle
movement, Task Management mutation, another P1 node, a service, store,
transport, runtime client, adapter invocation, proposal/apply operation,
instance-content egress, ruling write, release, professional reliance, or any
duty on App, Root, Task Management, Piping, Bridge, or another loop.

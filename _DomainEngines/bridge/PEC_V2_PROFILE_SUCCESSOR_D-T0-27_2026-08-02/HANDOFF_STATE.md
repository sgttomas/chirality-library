# D-T0-27 application handoff state

| Field | Value |
|---|---|
| RunStatus | `EFFECTIVE / CLOSEOUT RECORD READY FOR CHANGE` |
| ApplicationBasis | PR #458 merge `23d15899fd0acf5d1d0513f3fe396438375c9e25`; PR #459 source `0e47c218c26830a4efeb29eb2d2f3ea99142b987` |
| EffectiveIdentity | PR #459 merge `d9dc65804a0719fdf869af1ef60d53dc8cb0a895`; current descendant basis `556ae59a34ac2f06ef924d367843a72ea00d1f37` |
| DomainEngineID | `pec` |
| ProfileStatus | `ADOPTED / EFFECTIVE` |
| IntegrationLevel | `READ_ONLY` |
| LiveProfileSHA256 | `be3044d3b3d402d3c3268332d4386f76ddadd67f9e8bb258ba7aabee6d0cdc1d` |
| PreservedPreimageSHA256 | `0d6e1505003cffeba0393bdebaa48f19f27e2b1de8964e2c2bd262331f9ccca6` |
| Validation | `VALID`; `profile_status == ADOPTED`; zero findings; portable live report |
| HumanApprovals | D-T0-27 O-A, owner 2026-08-02; verbatim ruling in decision record and bridge Receipt 33 |
| ProtectedPathsTouched | exact live profile plus the application plan's enumerated Tier-0 and D-PEC-76 pointer surfaces only |
| NextOwningWorkflow | `CHANGE` — publish this effectiveness closeout record; PEC manager fan-in remains separate |

## Applied result

The exact candidate at SHA-256
`be3044d3b3d402d3c3268332d4386f76ddadd67f9e8bb258ba7aabee6d0cdc1d`
is installed byte-for-byte at `_DomainEngines/profiles/pec.yaml`. The exact
stale preimage is preserved at
`accepted_preimage/pec_v0.4_profile_v0.3.yaml`. Portable live validation
evidence is at `_DomainEngines/profiles/_validation/pec.validation.json`.

D-T0-27 O-A clears the D-T0-26 successor-profile prerequisite at PR #459
merge `d9dc65804a0719fdf869af1ef60d53dc8cb0a895`.
D-T0-28 O-A corrected the two conscious live-baseline pins at exact SHA-256
`7a4e8aa0fdb28cacdfedb62a307a260bd090136362102b48673ea2a9842d7638`;
the merged application checks pass. D-T0-28 and D-T0-29 are effective
supporting amendments on the same merge identity.
The adopted profile declares only the registered software checks and harness
self-check; it declares no runtime, adapter-client, mutating, proposal,
external-result, instance-content, or cross-loop lane.

## D-PEC-76 coordination result

D-PEC-76 points to the ruled D-T0-27 application without creating duplicate
adoption authority. Only present-tense pointer/status prose in
`projects/pec/AGENTS.md`, `projects/pec/docs/STATUS.md`, the PEC register, and
the existing D-PEC-75 record's profile-prerequisite section was aligned.
D-PEC-75 disposition and execution belong to the PEC loop. This closeout
updates only its D-PEC-76-bounded profile-prerequisite pointer state.

## Remaining gates and reruns

- CHANGE must publish this closeout record. The effectiveness identity itself
  is already durable at PR #459 merge `d9dc65804...`.
- D-PEC-75 source activation, lifecycle, artifact acceptance, release, and
  professional reliance remain separately gated and require owning-manager
  fan-in.

No PEC source, `software-workflow.json`, ScopeOfWork, lifecycle, Task
Management, decomposition, accepted artifact, adapter invocation, release,
professional reliance, or other-loop act is included.

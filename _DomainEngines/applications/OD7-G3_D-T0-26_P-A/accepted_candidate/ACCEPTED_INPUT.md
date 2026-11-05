# OD7-G3 P-A — PEC Profile Demotion Candidate

**Status:** EXACT CANDIDATE — NOT ACCEPTED
**Candidate gate:** `OD7-G3-P-A`
**Exact profile candidate:** `../candidate_tree/_DomainEngines/profiles/pec.yaml`
**Exact diff:** `../diffs/PEC_PROFILE_0_2_TO_0_3_STALE.diff`
**Exact index candidate:** `../candidate_tree/P-A/_DomainEngines/DOMAIN_ENGINE_INDEX.md`
**Exact index diff:** `../diffs/P-A_DOMAIN_ENGINE_INDEX.diff`

## Exact candidate decision

Demote the PEC Domain Engine profile from version `0.2`,
`ADOPTED` / `OPERATION_PROPOSAL`, to version `0.3`,
`STALE` / `MANUAL_BRIDGE`, with:

```yaml
execution_policy: "DENY_ALL_PROFILE_MEDIATED_INVOCATIONS"
historical_binding_only: true
```

The old deterministic-tool, proposal-lifecycle, path, visibility, and data
residency declarations remain in the file solely as frozen-instance lineage.
Under `AGENT_DOMAIN_ENGINE.md`, the `STALE` profile is ineligible for governed
profile-mediated invocation. It grants no governed live read, egress,
mutation, or project authority. Static citation and schema validation remain
permitted. This candidate does not claim that an ungoverned machine consumer
is mechanically incapable of ignoring the profile status or deny field.

The successor trigger is binding if this candidate is later accepted:
before any PEC v2 profile-mediated integration, and no later than activation
of the first accepted PEC v2 adapter/runtime-client deliverable, a new profile
must be prepared and separately adopted against accepted v2 contracts. This
stale profile cannot be promoted by inference or by editing only its status.

## Deterministic behavior

The candidate remains structurally valid under the Git-pinned profile
validator, which the package validator reruns.
The package's semantic validator additionally requires all four facts:

- `profile_version == "0.3"`;
- `profile_status == "STALE"`;
- `integration_level == "MANUAL_BRIDGE"`; and
- `execution_policy == "DENY_ALL_PROFILE_MEDIATED_INVOCATIONS"`.

Any failed semantic assertion blocks the candidate even if the generic schema
validator returns `VALID`.

## Conditional write surfaces

- `_DomainEngines/profiles/pec.yaml`
- `_DomainEngines/profiles/_validation/pec.validation.json`
- `_DomainEngines/DOMAIN_ENGINE_INDEX.md` only through the exact P-A diff
- the accepted Tier-0 decision/receipt/pointer surfaces that record the
  profile lifecycle change
- non-binding notices to the PEC loop

No project-local PEC file is directly written by this gate.

## Acceptance boundary

This candidate requires exact owner acceptance separate from `R-A`. It
authorizes no profile-mediated invocation and no successor profile design.

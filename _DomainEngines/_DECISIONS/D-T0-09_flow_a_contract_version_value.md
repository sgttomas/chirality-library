# D-T0-09 - RULING: Flow-A contract version value

**Status:** RULED / Option A selected 2026-07-04.
**Date prepared:** 2026-07-04
**Decision ID:** D-T0-09
**Prepared by:** bridge work loop agent, at owner direction to prepare the ruling packet.

This packet prepares the owner ruling for the concrete Flow-A contract version
value. It does not edit the adopted profile, app-dev package source, piping
source, publication state, live binding, lifecycle state, or any protected path.

## Decision to rule

Set the concrete value that replaces
`FLOW_A_CONTRACT_VERSION = 'TBD_BY_TIER_0'` under the tier-0-owned scheme ruled
in D-T0-07.

## Verified basis

| Fact | Source |
|---|---|
| D-T0-07 ruled a tier-0-owned Flow-A contract version scheme that references both app-dev version constants and confirms DEC-041 as decision-of-record. | `_DomainEngines/_DECISIONS/D-T0-07_contract_versioning.md` |
| App-dev D-APP-45 confirmed the wiring but left the concrete Flow-A value as `TBD_BY_TIER_0`. | `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-45_RULING_2026-07-02.md` |
| D-APP-46 extracted the internal package with `FLOW_A_CONTRACT_VERSION = 'TBD_BY_TIER_0'`. | `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-46_RULING_2026-07-02.md`; `projects/chirality-app-dev/frontend/packages/harness-contract/src/sdk-version.ts` |
| Current referenced constants are `CLAUDE_AGENT_SDK_PACKAGE_VERSION = '0.3.150'` and `HARNESS_TOOL_REGISTRY_VERSION = 'harness-tools.v6.mutating-mcp'`. | `projects/chirality-app-dev/frontend/packages/harness-contract/src/sdk-version.ts`; `projects/chirality-app-dev/frontend/packages/harness-contract/src/tool-descriptor.ts` |
| DEC-055 binds future event-vocabulary pins to the live `event-schema.ts` enumeration at the commit being pinned, not to stale DEC-041 prose. | `projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md` DEC-055 |

## Options

| ID | Option | Consequence |
|---|---|---|
| **O-A** | **Set `FLOW_A_CONTRACT_VERSION` to `flow-a.contract.v0.1.0`.** Treat this as the first governed Flow-A contract value. The decision record, not the string alone, binds the referenced SDK version, tool-registry version, event-vocabulary source, package path, and eventual SHA pin. | Stable, human-readable, and not falsely tied to the private npm package version. Allows package/source SHAs to change under new evidence while this version remains the first contract generation. |
| **O-B** | **Set a date-bearing value such as `flow-a.contract.2026-07-04.1`.** | Makes ruling date visible in the value. Less semantic and more likely to need churn if the implementing SHA changes after ruling. |
| **O-C** | **Defer until D-APP-48 and D-30 implementation commits exist.** | Avoids choosing before final implementation SHA exists, but keeps app-dev and piping consumption blocked by `TBD_BY_TIER_0`. |
| **O-D** | **Custom owner value.** | Owner supplies a different concrete string and any associated naming convention. |

## Recommendation

Recommend **O-A**: `flow-a.contract.v0.1.0`.

This keeps ownership tier-0, references the app-dev constants through the
decision record as D-T0-07 required, and avoids pretending that the private
package version `0.0.0-private` is the cross-repo contract value.

## If O-A is ruled

The follow-on implementation should:

- update the app-dev package constant from `TBD_BY_TIER_0` to
  `flow-a.contract.v0.1.0`;
- record the exact app-dev commit SHA/package path/export manifest in the
  D-APP-48/D-30 consumption mechanism;
- keep DEC-041 immutable history and use DEC-055 for event-vocabulary count
  interpretation;
- make no profile, publication, F3, or live-binding claim unless separately
  ruled.

## Human ruling

**Ruling recorded:** O-A approved by owner (Ryan Tufts), 2026-07-04.

Concrete value: `flow-a.contract.v0.1.0`.

Owner ruling, verbatim:

> D-T0-09: O-A, value flow-a.contract.v0.1.0

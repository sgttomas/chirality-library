# D-T0-07 — Contract versioning / pinning + DEC-041 confirmation  (RULED 2026-06-21)

**Decision:** Where does the cross-repo flow-A contract package version live and how is it pinned — and confirm DEC-041 as decision-of-record.

**Structural precedent:** Same-directory tier-0 decision/ruling summary pattern used by D-T0-04 through D-T0-06.

**Why the owner's:** cross-repo version governance is a maintainer decision; DEC-041's status needs confirmation.

**Verified facts:** `CLAUDE_AGENT_SDK_PACKAGE_VERSION='0.3.150'`
(`projects/chirality-app-dev/frontend/packages/harness-contract/src/sdk-version.ts`);
`HARNESS_TOOL_REGISTRY_VERSION`
(`projects/chirality-app-dev/frontend/packages/harness-contract/src/tool-descriptor.ts`).
These constants moved to the direct package source when D-APP-47 retired the
frontend harness shims. **DEC-041 EXISTS** at piping
`projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md:611`
(harness-as-versioned-packages; gated behind D-21 + an automation condition;
2026-06-18) — **refutes** app-dev's "no written DEC-041 text"; it was simply
invisible from app-dev's tree.

**Options:** (a) tier-0-owned scheme that *references* both app-dev versions; (b) extend `CLAUDE_AGENT_SDK_PACKAGE_VERSION`; (c) extend `HARNESS_TOOL_REGISTRY_VERSION`.

**Recommendation:** (a) — neither repo's version owns the cross-repo contract; cross-reference DEC-041 (SHA-pinned) into app-dev so its Flow-A boundary is decision-backed, not import-graph-derived.

**Unblocks:** app-dev open-Q5; the DEC-041 consumable-package-pull automation condition. **Forecloses:** decision-unbacked package boundaries.

---
**HumanRuling:** **(a) tier-0-owned scheme** — a flow-A contract version that *references* both `CLAUDE_AGENT_SDK_PACKAGE_VERSION` + `HARNESS_TOOL_REGISTRY_VERSION`. **DEC-041 confirmed** as decision-of-record (piping `SOFTWARE_DECOMP.md:611`); cross-reference it (SHA-pinned) into app-dev.   **RuledBy:** owner (in-session)   **Ruling SHA:** 6e70b5aace4a3a7c4ebb20490a3bf57bfd912f45 (publication commit, 2026-06-21; backfilled 2026-07-02 per owner ruling)   **Date:** 2026-06-21

# D-T0-08 — Fence-3 opening sequence (sub-decision)  (RULED 2026-06-21)

**Decision:** The order and preconditions for opening app-dev fence **F3** — (a) standing up `DomainEngineProfile`/`OperationProposal` **source types** in `frontend/src`, and (b) adding **domain MCP tools** (e.g. `piping_propose_operation`).

**Why the owner's:** F3 gates R7 domain-engine implementation; opening it is consequential scope expansion (app-dev autonomous posture explicitly stops at F3 for a ruling).

**Verified facts:** F3 = "R7 domain-engine impl; PKG-10 stays future-boundary/doc-only" (`projects/chirality-app-dev/.../D-APP-39_RULING_2026-06-20.md:26`). Editing the doc contracts is permitted; standing up source types crosses F3; an OperationProposal-as-MCP-tool is R7 implementation. Both are GATED today.

**Options:** (a) sequential — source types first, then MCP tools; (b) parallel; (c) keep both held until L2 (validated-kernel runs) is proven.

**Recommendation:** (a) sequential, and not before D-T0-01 (single canon) is ruled and L2 is demonstrated. The MCP tool surface consumes the type contract, so types must settle first. Each step is its own PROPOSAL packet (never self-ruled).

**Unblocks:** the R7 build lane. **Forecloses:** standing up MCP tools against an unsettled type contract.

---
**HumanRuling:** **(a) Sequential** — source types first, then domain MCP tools; not before D-T0-01 (ruled) + a proven L2. Each step its own PROPOSAL packet.   **RuledBy:** owner (in-session)   **Ruling SHA:** 6e70b5aace4a3a7c4ebb20490a3bf57bfd912f45 (publication commit, 2026-06-21; backfilled 2026-07-02 per owner ruling)   **Date:** 2026-06-21

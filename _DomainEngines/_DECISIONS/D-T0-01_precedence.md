# D-T0-01 — Contract precedence  (RULED 2026-06-21)

**Decision:** Which authoring is canonical for the `DomainEngineProfile`/`OperationProposal` contract — framework-root `agents/AGENT_DOMAIN_ENGINE.md`, or app-dev `docs/TYPES.md §11`/PKG-10?

**Why the owner's:** selecting canonical governance authoring is a Type-0/maintainer act; neither project loop may pre-rule it.

**Verified facts:** two-layer rule `docs/PLAN.md:17`, `docs/CONTRACT.md:9`, K-AGENTS-1 `:123`. `AGENT_DOMAIN_ENGINE.md` absent from DEL-10-01/03 `_REFERENCES.md` (root cause). Root CONTRACT has no K-DOMAIN; app-dev `docs/CONTRACT.md:131-138` has K-DOMAIN-1..4; app-dev `docs/TYPES.md:499-545` = §11.

**Options:** (a) framework-root persona canonical; (b) app-dev `TYPES §11`/PKG-10 canonical; (c) co-equal.

**Counter-position (recorded per persona `:76`):** the two-layer rule (`docs/CONTRACT.md:9`) already lets app-dev's working-root K-DOMAIN-1..4 be authoritative *within app-dev*, so "leave the contract working-root-local, no promotion" is defensible. I recommend against it: the contract governs all future domain engines, not just app-dev. Choose explicitly whether FM-02 **establishes new framework policy** (recommended) or **ratifies/elevates** app-dev's existing invariants — either keeps app-dev's IDs stable and citing the root family.

**Recommendation:** (a), reconciled as a two-way merge landing at root (CONTRACT_DIRECTION §1): app-dev conforms DOWN on the 19-row table; promote K-DOMAIN UP (FM-02); merge app-dev's richer OperationProposal UP (FM-04).

**SHA-pin sequencing:** after this ruling and after FM-01..04 are applied, DOMAIN_ENGINE pins the *ruled* SHA of `agents/AGENT_DOMAIN_ENGINE.md` into app-dev DEL-10-01/03 `_REFERENCES.md` (and the piping working root where it cites the persona). Tier-0's citations in this package are already lawful; the pin gates the app-dev-side conformance work.

**Unblocks:** single-canon PKG-10 re-draft; FM-02. **Forecloses:** independent corpus drift.

---
**HumanRuling:** **(a) Framework-root persona canonical** — FM-02 promotes K-DOMAIN to root as **new framework policy**; app-dev conforms DOWN (19-row table) and its richer OperationProposal merges UP (FM-04).   **RuledBy:** owner (in-session)   **Ruling SHA:** 6e70b5aace4a3a7c4ebb20490a3bf57bfd912f45 (publication commit, 2026-06-21; backfilled 2026-07-02 per owner ruling)   **Date:** 2026-06-21

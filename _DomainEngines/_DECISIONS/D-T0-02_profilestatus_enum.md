# D-T0-02 — ProfileStatus INVALID/UNKNOWN  (RULED 2026-06-21)

**Decision:** Reconcile the persona's `ProfileStatus` self-inconsistency.

**Why the owner's:** edits the canonical persona enum (framework maintenance; not self-ruled).

**Verified facts:** `UNKNOWN` at `AGENT_DOMAIN_ENGINE.md:197`; `INVALID` at `:657` and `:378`; free field at `:830`. Epistemic Gap-vs-resolved-negative distinction `docs/TYPES.md` §10.

**Options:** (a) keep both — `NONE|DRAFT|VALIDATED|ADOPTED|STALE|INVALID|UNKNOWN`; (b) `INVALID` only (app-dev default); (c) `UNKNOWN` only.

**Recommendation:** (a). **Interpretation (this proposal's, not a TYPES.md citation):** map `UNKNOWN`≈Gap (not yet determined at intake); `INVALID`≈resolved-negative (malformed). `docs/TYPES.md` §10 defines Gap vs resolved-negative as distinct primitives but does not prescribe the enum mapping; the mapping is the working rationale offered for this ruling. Collapsing the two tokens would erase a distinction the ontology motivates. Exact diff: FM-01.

**Unblocks:** clean enum across profile + Handoff State. **Forecloses:** intake-vs-validation ambiguity.

---
**HumanRuling:** **(a) Keep both** — 7-token enum `NONE|DRAFT|VALIDATED|ADOPTED|STALE|INVALID|UNKNOWN` (apply FM-01).   **RuledBy:** owner (in-session)   **Ruling SHA:** 6e70b5aace4a3a7c4ebb20490a3bf57bfd912f45 (publication commit, 2026-06-21; backfilled 2026-07-02 per owner ruling)   **Date:** 2026-06-21

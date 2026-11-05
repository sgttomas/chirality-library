# FM-02 — Promote a K-DOMAIN-* family to root `docs/CONTRACT.md` (APPLIED draft; pending approval)

**Target (canonical):** `docs/CONTRACT.md` (root). **Resolves:** D-T0-01 flow (ii). **Gate:** framework-maintenance (human-gated). **Status: APPLIED and PUBLISHED at `77a327727` (committed + pushed to origin/main; owner-directed 2026-06-21).**
**Application record:** Applied by HELPS_HUMANS framework-maintenance pass on 2026-06-22. Applying SHA: `77a327727`. Draft base HEAD observed: `16e723f45813`.

**Why:** Before application, root `docs/CONTRACT.md` had **23 K-*** and **no K-DOMAIN family**; the domain-engine invariants lived only as persona prose (`AGENT_DOMAIN_ENGINE.md:80-95`) and as a working-root specialization in app-dev (`projects/chirality-app-dev/docs/CONTRACT.md:131-138`, K-DOMAIN-1..4). Per the two-layer rule a working root may *extend but not weaken*; an invariant that governs **all** domain engines belongs at the framework altitude. Promote it; app-dev's K-DOMAIN-1..4 then conform to (cite) the root family rather than being its only home. K-* IDs are stable and never-reused **within a catalog**: these are **new to the framework-root catalog** — app-dev's existing K-DOMAIN-1..4 stay stable within the app-dev working root and will cite (not duplicate) the root definitions per the two-layer rule. (This is flow (ii) of D-T0-01; see also the counter-position recorded there and in `D-T0-01_precedence.md`.)

> Root `docs/CONTRACT.md` is itself **DRAFT pending ratification**; this addition rides that ratification.

> **Citation authorization.** This proposal cites `agents/AGENT_DOMAIN_ENGINE.md` line numbers. That is lawful here because tier-0 authors at the framework root and the persona is its own canon — it is *not* a Type-2 deliverable bounded by a `_REFERENCES.md`. The separate prerequisite (for the **app-dev-side** conformance, where `AGENT_DOMAIN_ENGINE.md` is absent from DEL-10-01/03 `_REFERENCES.md`) is the SHA-pin recommended in `D-T0-01` — it gates app-dev acting on these diffs, not this package authoring them.

---

### Edit 1 — add to the K-* Invariant Index (`docs/CONTRACT.md` §1, after the K-AGENTS-1 row)

```diff
 | K-AGENTS-1 | 1.11 | Agent Index and Governance Surface |
+| K-DOMAIN-1 | 1.12 | Domain Engine Integration |
+| K-DOMAIN-2 | 1.12 | Domain Engine Integration |
+| K-DOMAIN-3 | 1.12 | Domain Engine Integration |
+| K-DOMAIN-4 | 1.12 | Domain Engine Integration |
```
(and update the count line "There are **23 stable invariants** across 11 subsections" → "There are **27 stable invariants** across 12 subsections".)

### Edit 2 — new subsection `### 1.12 Domain Engine Integration` (after §1.11)

```markdown
### 1.12 Domain Engine Integration

| ID | Invariant | Enforcement |
|---|---|---|
| **K-DOMAIN-1** | **Domain engines own authoritative domain truth.** Canonical model files, model states, analysis runs, comparisons, solver outputs, and handoff internals are owned by the domain engine. Chirality governs the work around it (profiles, manifests, proposals, review notes, gates); it is not the solver and is never the source of accepted engineering truth. | DOMAIN_ENGINE persona; profile `protected_write_paths`; human review |
| **K-DOMAIN-2** | **Protected domain paths are write-quarantined.** Agents must not directly write protected domain artifacts. Domain-controlled writes occur only through declared deterministic tools under the active profile. | DOMAIN_ENGINE; TASK ScopePath/AllowedWriteTargets; profile; human review |
| **K-DOMAIN-3** | **Domain operations require an OperationProposal record and explicit human acceptance.** A proposal is `proposal_only` until validated by a declared deterministic tool AND accepted by a human; application occurs only through a domain-engine-controlled apply. | DOMAIN_ENGINE Gate 5; profile; K-AUTH-1/K-AUTH-2; human review |
| **K-DOMAIN-4** | **Domain-engine outputs must not be represented as professional approval.** A green validation/PASS is structural evidence only — never code-compliance, certification, sealing, authentication, or external-prover validation absent a cited human authoritative record (APEGA ceiling). Validation-passed is necessary, not sufficient, for engineering correctness. | DOMAIN_ENGINE professional_boundary; K-CLAIM-1; K-AUTH-1; AUDIT_GOVERNANCE; human review |
```

### Edit 3 — working-root note (so app-dev conforms, not competes)

Add to app-dev's `docs/CONTRACT.md` §1.10 (a working-root edit — **app-dev's** maintenance, not tier-0's): annotate K-DOMAIN-1..4 as "specializes framework `docs/CONTRACT.md` §1.12 K-DOMAIN-*; MUST NOT weaken." (Flagged here; performed by the app-dev loop, not tier-0.)

**Provenance:** persona invariants `AGENT_DOMAIN_ENGINE.md:80-95`; app-dev family `projects/chirality-app-dev/docs/CONTRACT.md:131-138`; two-layer rule `docs/PLAN.md:17`, `docs/CONTRACT.md:9`, K-AGENTS-1 `:123`.

# CONTRACT_DIRECTION — DomainEngineProfile / OperationProposal (PROPOSE, do not rule)

Maps app-dev's reconciliation table and piping's six trust requirements onto **one** contract direction. Everything here is a recommendation for D-T0-01 and the framework-maintenance gate (FM-01..04). No canon is edited.

---

## 1. Precedence = framework-canonical, reconciled by a two-way merge landing at root

The framework's own two-layer rule (`docs/PLAN.md:17`; `docs/CONTRACT.md:9`; K-AGENTS-1 `:123`) makes the framework-root persona canonical. But "canonical" ≠ "frozen": three flows reconcile the corpora.

**(i) app-dev conforms DOWN** on the drift table (below): add the missing fields and align the casing as a *derived view*.

**(ii) Promote a K-DOMAIN-* family UP to root** `docs/CONTRACT.md` (derived from the persona's prose invariants `:80-95` + app-dev's K-DOMAIN-1..4). Root currently has **none**; app-dev has four. The invariants belong at the altitude that governs *all* domain engines. → FM-02.

**(iii) Merge app-dev's richer `OperationProposal` UP** into the canonical contract. app-dev's field list + lifecycle is better than the persona's bare `proposal_only` + prose; absorb it. → FM-04.

### 1a. DomainEngineProfile reconciliation (DEL-10-01 ⇄ persona) — verified

| Concept | Verdict | app-dev (`TYPES §11.1`) | persona (canonical) | Reconcile to |
|---|---|---|---|---|
| Field naming/casing | DRIFT | camelCase TS | snake_case YAML (`:671-707`) | TS = derived view; annotate snake_case mapping |
| `engine_type` | MISSING | absent | required (`:676`) | add (MUST) |
| `schema_version`/`profile_version` | MISSING | only `engineVersion?` | required (`:673,:677`) | add both; don't conflate with engine version |
| `domain_root_patterns` | MISSING | absent | required (`:679`) | add |
| Path taxonomy | DRIFT | 2 classes | 4 classes (`:682-692`) | expand to authoritative/readable/protected/agent_writable |
| `artifactTypes` | DRIFT | flat `string[]` | role-classed path sets | model by ownership role |
| operations vs `deterministic_tools` | DRIFT (false gap) | `operations`, "TBD" | concrete `deterministic_tools` (`:694`) | adopt `deterministic_tools{id,mode,requires_human_confirmation,schema}` |
| `manifestRules` | DRIFT | `unknown`, "TBD" | not a profile field | drop or mark Chirality-extension |
| `professional_boundary` | DRIFT | scalar string | structured `agent_must_not_claim` (`:699-707`) | upgrade to structured object |
| `ProfileStatus` | DRIFT | none | 7-token (D-T0-02) | add; fix `INVALID`/`UNKNOWN` (FM-01) |
| `IntegrationLevel` | MISSING | absent | L0-L4 (`:162-172`) | add 5-token enum |

### 1b. OperationProposal reconciliation (DEL-10-03 ⇄ persona) — verified

| Concept | Verdict | app-dev | persona (`:393-404`) | Reconcile to |
|---|---|---|---|---|
| Contract form | DRIFT | typed field-list | 8 prose criteria | map each criterion to a field (merge up) |
| status | DRIFT | draft\|ready_for_review\|accepted\|rejected\|applied | `proposal_only` | `proposal_only` = {draft, ready_for_review}; accepted/applied human-gated + SHA |
| cite evidence | AGREE | inputRefs/checks/expectedOutputRefs | manifests/run/comparison IDs | ensure refs admit run/comparison IDs |
| assumptions + blockers | MISSING | only `risks` | MUST list (`:401`) | add field distinct from risks |
| boundary language in-record | TBD | checklist only | record MUST contain (`:402`) | add boundary-notice field |
| under agent-writable path | TBD | standalone | MUST live under profile path (`:403`) | bind storage to `agent_writable_paths` |
| names base state | TBD | none | SHOULD (`:398`) | add optional `baseState` ref |
| Human Agency Map | AGREE | propose-before-apply | humans accept/reject (`:406-417`) | map status transitions onto rows |

### 1c. Reconciliation tally (resolves Appendix-A "12 vs 19")

The app-dev table holds **19 rows = 9 DRIFT + 5 MISSING + 3 TBD + 2 AGREE → 17 action items.** The "~12" figure undercounts by omitting the 5 MISSING + 2 AGREE; "~19" is the total row count. **Genuine** gaps remaining even after precedence is ruled (not "false gaps"): `requiredHumanGate ↔ approval-SHA` semantics, the adapter **validate/apply result schema**, the **deterministic-check result schema** — all resolvable by cross-referencing piping (`AnalysisStatus` + K-AUTH-2 + `rule_check_runner` result shape).

**Ownership of the 3 genuine gaps:** they are **contract-authoring** tasks (not TOOLMAKER), owned by the **DOMAIN_ENGINE** framework-maintenance pass, **gated on D-T0-01** (precedence ruled) + your acceptance of this CONTRACT_DIRECTION. They close by reading the verified piping result shapes into the merged OperationProposal (FM-04) — no new code, just cross-reference. Tracked here; they do not need a separate register.

---

## 2. ProfileStatus (7 tokens) — see FM-01

`NONE | DRAFT | VALIDATED | ADOPTED | STALE | INVALID | UNKNOWN`. Fix `:197 / :378 / :657 / :830` consistently.

---

## 3. Piping's six trust requirements → contract homes (with the GENERIC guard)

| Piping requirement (§) | Contract home | Generic form (guards against piping-shape leak) |
|---|---|---|
| 1 Green ≠ assured | K-CLAIM-1 + persona `professional_boundary` + profile invariant | "validation-passed is structural, never engineering, assurance" |
| 2 Operation risk-classing | **new generic field** on OperationProposal/profile | **engine-checkable vs engine-silent** (not the piping `change_kind` list) |
| 3 Provenance on judgment values | K-PROV-1 + a profile rule, **kept distinct from DEC-043** | "provenance required on engine-silent values" |
| 4 Premise-audit obligation | results-interpretation operation requirement | "what premises does this PASS depend on?" |
| 5 Reserved human acts | K-AUTH-1 + K-AUTH-2 | engine-lifecycle terminal transition (instance: `HUMAN_APPROVED_FOR_PROJECT`) |
| 6 Risk-graded staging | PLAN staging (subordinate to D-T0-03) | per-operation, not wholesale |

**Corrections carried (challenge-not-adopt):**
- "Operation risk-classing" and "physics-grounding" are **proposals, not engine truth** today (`model_operation.schema.json` has no `risk_class`; `professional_boundary` uniform).
- **DEC-043** is a **corpus-reliability** constraint (extracted equations not authoritative; routed to piping `AGENTS.md`), **not** an operation-level provenance gate. Keep it distinct from requirement 3.
- The cited "Invented allowable stress" is a **test fixture** (`completeness_checker/src/lib.rs:586`); the substantive refusal-to-invent / no-code-defaults behavior is real (`:1-6`).

---

## 4. The one item ruled here (shared-root-internal working call — labeled as such)

**The generic contract stays generic.** `AnalysisStatus`, allowable-stress/SIF/material vocabulary, the `change_kind` taxonomy, and `project.ops.yaml` are **OpenPipeStress instance bindings**, never the generic schema. The generic contract carries only the generalized axes (engine-checkable/engine-silent risk class; provenance-on-judgment-values; premise-audit; bind-to-engine-lifecycle). The OpenPipeStress profile is where the instance specifics bind. This is a working call within my shared-root authority, **not** an owner ruling.

**Genericness verification (closes the circular-provenance risk).** FM-04 promotes app-dev's `OperationProposal` UP as the canonical generic form — so it must itself be free of piping shape. Verified against `projects/chirality-app-dev/docs/TYPES.md:517-533`: its fields are `proposalId, profileId, operationName, createdAt, createdBy, inputRefs, intendedChanges, deterministicChecks, expectedOutputRefs, risks, requiredHumanGate, status` — **none** is piping vocabulary (no `AnalysisStatus`, no `allowable`/`SIF`, no `change_kind`). The single field this proposal *adds* (`operation_risk_class`) is the generalized engine-checkable/engine-silent axis, not Class-A/Class-B piping examples. Conclusion: app-dev's OperationProposal is generic-shaped; the merge is safe. (If a *future* domain engine — cost, scheduling — surfaces a field app-dev's shape cannot express, that is the trigger to revisit, not a blocker now.)

# FM-03 — Re-author the OpenPipeStress Example Binding (APPLIED draft; pending approval)

**Target (canonical):** `agents/AGENT_DOMAIN_ENGINE.md`, "OpenPipeStress Example Binding" (≈ lines 709-718).
**Gate:** framework-maintenance (human-gated). **Status: APPLIED and PUBLISHED at `77a327727` (committed + pushed to origin/main; owner-directed 2026-06-21).**
**Application record:** Applied by HELPS_HUMANS framework-maintenance pass on 2026-06-22. Applying SHA: `77a327727`. Draft base HEAD observed: `16e723f45813`.

**Why:** Before application, the example binding was **aspirational and diverged from the verified piping layout** (no `project.ops.yaml`; no top-level `states/`/`runs/`/`comparisons/` directory tree; no `Model_Manifest`/`RUN-*`/`CMP-*` artifacts). `core/handoff/**` *does* exist — but as engine handoff/export adapters, not as the analysis-result storage tree the persona's `handoff/**` implied. Piping is schema-driven + persistence-abstracted. Since OpenPipeStress is the *example*, not the ontology, the binding should reflect reality so the example does not mislead future profile authors.

---

### Before (current `:709-718`, paraphrased table)

| Class | Example paths/artifacts |
|---|---|
| Authoritative | `OpenPipeStress/project.ops.yaml`, `OpenPipeStress/states/**`, `.../runs/**`, `.../comparisons/**`, `.../handoff/**` |
| Chirality-readable | `Model_Manifest.{md,yaml}`, `RUN-*_summary.md`, `CMP-*_summary.md`, `CMP-*_delta_table.csv`, `Handoff_Manifest.md`, warnings, assumptions, TBD registers |
| Protected | canonical model files, accepted model states, analysis result records, comparison records, handoff internals, solver outputs, professional acceptance records |
| Agent-writable | operation proposals, review notes, TBD registers, scope notes, handoff checklists, draft report sections, dependency notes, reconciliation notes |

### After (proposed — bound to verified reality)

| Class | Real paths/artifacts (verified 2026-06-21) |
|---|---|
| Authoritative | `projects/chirality-piping/core/**` (engine/solver/model-operations); `schemas/**` (contracts); the engine **project store** per `schemas/project_persistence.schema.yaml` (model states / analysis runs / comparisons — SQLite-backed, **not** a static dir tree); `core/handoff/**` |
| Chirality-readable | records per `schemas/{analysis_run,model_state,comparison_mapping,handoff_package}.schema.*` (schemas present; **instances produced on demand — TBD**); on-demand exports under `core/handoff/*` (native_json / stress_neutral / review_geometry); professional-boundary notices from `operation_applier` & `rule_check_runner` |
| Protected | `core/**`, `schemas/**`, the project store, `core/handoff/**`, solver outputs, accepted model states |
| Agent-writable | `_DomainEngines/proposals/open_pipe_stress/**` (OperationProposals); `_DomainEngines/bridge/**` (review notes, TBD registers, checklists) |

Add an explicit note: *"OpenPipeStress persists model/state/run/comparison records in an engine-owned store (SQLite per `project_persistence.schema.yaml`) and emits readable artifacts on demand; there is no `project.ops.yaml` or static `states/`/`runs/` directory tree. The engineering lifecycle is `AnalysisStatus` (`schemas/model.schema.yaml:22-32`)."*

**Provenance:** ARTIFACT_INVENTORY.md (this snapshot); workflow `tier0-cold-verify` slice "piping-profile-binding" (REFUTED `project.ops.yaml`, REFUTED `states/runs/comparisons` dirs, NOT_FOUND manifests).

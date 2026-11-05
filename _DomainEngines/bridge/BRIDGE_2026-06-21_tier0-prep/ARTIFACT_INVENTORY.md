# ARTIFACT_INVENTORY — OpenPipeStress (verified layout vs persona example binding)

Role-labeled inventory of the **real** piping engine surfaces, verified by read-only inspection 2026-06-21. This **supersedes** the persona's aspirational OpenPipeStress Example Binding (`AGENT_DOMAIN_ENGINE.md:709-718`); see FM-03 for the proposed persona re-author.

## Authoritative domain artifacts (engine-owned; protected)

| Artifact | Real location | Note |
|---|---|---|
| Mutation kernel | `core/model_operations/operation_applier/` (Rust, JSON-in/out) | Single validate/apply kernel; `apps/desktop/src/services/operationService.ts:8-16` is the GUI-independent entry |
| Rule kernels | `core/rules/{completeness_checker,rule_check_runner}/` | completeness + rule-check evidence |
| Solver / runner | `core/{solver,runner/headless}/` | headless is lib-only (`core/runner/headless/src/lib.rs:655`) — needs thin CLI |
| Contract schemas | `schemas/*.{yaml,json}` | model, model_state, analysis_run, comparison_*, handoff_package, external_prover_metadata, … |
| Model/state/run/comparison records | engine project store (`project_persistence.schema.yaml`) | **SQLite-backed; not a static `states/`/`runs/`/`comparisons/` dir tree** |
| Handoff internals + export adapters | `core/handoff/**` | caepipe_*, native_json, stress_neutral, review_geometry, pcf, target_mapping, … |

## Chirality-readable artifacts

| Artifact | Status |
|---|---|
| `analysis_run` record (`schemas/analysis_run.schema.json`, DEL-14-02) | schema present; **instances TBD** (produced on demand) |
| `model_state` record (`schemas/model_state.schema.json`) | schema present; instances TBD |
| `comparison` record (`schemas/comparison_mapping.schema.json`) | schema present; instances TBD |
| `handoff_package` (`schemas/handoff_package.schema.json`) | schema present; `external_prover_status = not_declared_by_handoff_package` |
| On-demand exports (native_json / stress_neutral / review_geometry) | produced by `core/handoff/*` |
| Professional-boundary notices | emitted by `operation_applier` (lib.rs:1134-1141) and `rule_check_runner` (lib.rs:78-80) |

## Engineering lifecycle (the human gate binds here, not to a new scheme)

`AnalysisStatus` (`schemas/model.schema.yaml:22-32`, `schemas/analysis_status.schema.yaml:94-105`), 7 states:
`MODEL_INCOMPLETE → MECHANICS_SOLVED → RULE_INPUTS_INCOMPLETE → USER_RULE_CHECKED / USER_RULE_FAILED → HUMAN_REVIEW_REQUIRED → HUMAN_APPROVED_FOR_PROJECT`.
Software emits only the first six (`AutomaticAnalysisStatus`); `HUMAN_APPROVED_FOR_PROJECT` is an **external, hash-bound** acceptance record only (`USER_RULE_PASSED` intentionally absent).

## Divergences from the persona example binding (→ FM-03)

| Persona claims (`:709-718`) | Reality |
|---|---|
| `OpenPipeStress/project.ops.yaml` | **does not exist**; canonical model = persistence store |
| `states/**`, `runs/**`, `comparisons/**` dirs | **no such top-level tree**; records live in the SQLite engine store |
| `handoff/**` dir | exists as **`core/handoff/**`** — engine handoff/export adapters, not analysis-result storage |
| `Model_Manifest`, `RUN-*_summary`, `CMP-*_summary`, `Handoff_Manifest` | **NOT_FOUND**; schemas exist, instances produced on demand |

## Missing / TBD

- No deterministic profile-schema validator (TOOLMAKER).
- No materialized readable run/state/comparison instances yet.
- `operation_risk_class` field not in `model_operation.schema.json`.
- Headless CLI entrypoint not built.

# PROFILE_STATUS — open_pipe_stress

| Field | Value |
|---|---|
| Active profile | `open_pipe_stress.DRAFT.yaml` (as of this 2026-06-21 snapshot; renamed to `_DomainEngines/profiles/open_pipe_stress.yaml` 2026-07-01 per D-GOV-06) |
| ProfileStatus | **ADOPTED** (validated + human Gate 2 adopted by owner 2026-06-21; governed-authoritative) |
| Integration level (current, not yet ruled) | MANUAL_BRIDGE (L0) |
| Validator | `tools/validation/validate_domain_engine_profile.py` (built, 8/8 tests pass) — report: `_DomainEngines/profiles/_validation/open_pipe_stress.validation.json` (VALID) |

## Boundary summary (ADOPTED — governed-authoritative 2026-06-21)

- **Authoritative (engine-owned, protected):** `core/**`, `schemas/**`, the engine project store (model states / analysis runs / comparisons per `project_persistence.schema.yaml`), `core/handoff/**`, solver outputs.
- **Chirality-readable:** analysis-run / model-state / comparison records (schema-defined; instances TBD), handoff package manifest (no private payload), on-demand exports, engine professional-boundary notices.
- **Agent-writable:** `_DomainEngines/proposals/open_pipe_stress/**`, `_DomainEngines/bridge/**` (review notes, TBD registers).
- **Declared tools:** `operation_applier` (validate/apply), `completeness_checker`, `rule_check_runner` (all Rust, verified), `headless_runner` (lib-only; entrypoint TBD).

## Human gates (Gate 2 ADOPTED 2026-06-21; Gates 3–5 pending as work reaches them)

profile adoption · protected-write policy · mutating tool calls (`operation_applier.apply`) · operation-proposal application · external-prover interpretation · professional reliance.

## Open profile issues

1. ~~Not validated~~ → **VALIDATED** 2026-06-21 (validator built + passed). Now gated only on human Gate 2 (ADOPTED).
2. Readable run/state/comparison **instances** are TBD (schemas exist; produced on demand).
3. `operation_risk_class` is proposed, not implemented in the engine.
4. The persona's example binding diverges from this verified binding (FM-03).
5. Live binding (L2–L3) gated ×4 (tier-0 adoption · app-dev F3 · piping D-21 · DEC-041 automation condition).

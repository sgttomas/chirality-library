# Domain Engine Integration — Control Area Index

**Owner persona:** DOMAIN_ENGINE (`agents/AGENT_DOMAIN_ENGINE.md`), Type-1 manager subordinate to Type-0 `AGENT_HELPS_HUMANS`.
**Control root:** `{REPO_ROOT}/_DomainEngines/` (persona default `DOMAIN_CONTROL_ROOT`; created 2026-06-21 with explicit owner approval).
**Scope:** shared-root (tier-0) governance authoring only. Nothing here is project-runtime truth, and nothing here edits the registered project subtrees (`projects/chirality-app-dev/**`, `projects/chirality-piping/**`, `projects/pec/**`) except where a governed registration packet explicitly permits a project-local coordination pointer.

> **Status:** the `open_pipe_stress` profile is **`ADOPTED`** (validated + owner Gate-2 ruling 2026-06-21; D-T0-06) and the original 8 tier-0 decisions are **RULED** (2026-06-21; `_DECISIONS/_REGISTER.md`). PEC registration rows D-T0-11..16 were ruled and published in PR #51, then the D-T0-16 harness tranche moved the PEC profile into `profiles/`, and the owner adopted it at Gate 2 on 2026-07-05 (**ADOPTED**; D-T0-12 adoption note). No professional status is claimed (APEGA ceiling, K-AUTH-1). Publication is handed to CHANGE; DOMAIN_ENGINE does not commit. *(Banner reauthored per D-GOV-06, ruled 2026-07-01 — it previously denied both the adoption and the rulings.)*

---

## Registered domain engines

| DOMAIN_ENGINE_ID | Engine | Profile | ProfileStatus | Integration level (today) |
|---|---|---|---|---|
| `open_pipe_stress` | OpenPipeStress piping-stress engine (`projects/chirality-piping/`) | `profiles/open_pipe_stress.yaml` | **ADOPTED** (validated + Gate-2 adopted 2026-06-21) | `MANUAL_BRIDGE` (L0) |
| `pec` | PEC engineering execution-control engine (`projects/pec/`) | `profiles/pec.yaml` | **ADOPTED** (validated + owner Gate-2 ruling 2026-07-05; D-T0-12 adoption note) | `OPERATION_PROPOSAL` (L3, imports scope; D-T0-18 O-A 2026-07-05) |

## Layout

```
_DomainEngines/
  DOMAIN_ENGINE_INDEX.md          ← this file
  _LATEST.md                      ← pointer to the latest accepted snapshot
  RULINGS_PUBLISHED.md            ← the 8 owner rulings (2026-06-21) + RES-RECONCILE; the green-light signal
  NEXT_INSTANCE_PROMPT.md         ← sequencing: how owner rulings flow to action
  profiles/
    open_pipe_stress.yaml         ← ADOPTED generic-shape profile, bound to the real piping layout
    pec.yaml                      ← ADOPTED PEC profile (owner Gate-2 ruling 2026-07-05)
  bridge/
    BRIDGE_2026-06-21_tier0-prep/ ← immutable snapshot for this prep run (see its RUN_SUMMARY.md)
      framework_maintenance/      ← FM-01..04 gated canon diffs (NOT applied)
      TOOLMAKER_BRIEF-*.md        ← profile-schema validator; headless CLI entrypoint
  pec/
    LOOP_INIT.md                   ← PEC work-loop entrypoint
    WORKPLAN_2026-07-04_pec_loop.md
    LOOP_RECEIPTS.md
    PEC_2026-07-04_tier0-prep/     ← immutable registration prep snapshot
  proposals/
    open_pipe_stress/             ← (empty; no OperationProposals authored — L3 not reached)
    pec/                          ← import-proposal mirrors (L3 imports scope; D-T0-18 O-A 2026-07-05)
  _DECISIONS/
    _REGISTER.md                  ← tier-0 decision register, including ruled PEC registration rows
    D-T0-01..10_*.md              ← ruled / acknowledged historical records
    D-T0-11..16_*.md              ← PEC registration rows, HumanRuling published by PR #51
```

## Read order for a human or successor agent

1. `bridge/BRIDGE_2026-06-21_tier0-prep/RUN_SUMMARY.md` — what this run did + the readiness verdict.
2. `_DECISIONS/_REGISTER.md` — the tier-0 decision register, including any open residual rows.
3. `bridge/.../CONTRACT_DIRECTION.md`, `BRIEF_human_decisions.md`, `PLAN_cross_tier.md` — the OpenPipeStress bridge substance.
4. `pec/PEC_2026-07-04_tier0-prep/BRIEF_human_decisions.md` — the PEC registration slate.
5. `bridge/.../framework_maintenance/FM-0{1..4}_*.md` — reviewable canon diffs (gated, **not applied**).

## Shared runtime convergence

D-T0-23 remains immutable historical authority for shared-runtime convergence.
D-PEC-58 later retired the old PEC product and did not carry its deterministic-
acts/RBAC/reporting/data-boundary adapter allocation into PEC v2. The current
boundary preserves Root ownership of generic runtime semantics, distinct
project/domain authority, checkout-contained evidence, no production dual
execution loop, human-only-act restrictions, and fail-closed runtime-client
behavior without making file-native governed work depend on PEC.

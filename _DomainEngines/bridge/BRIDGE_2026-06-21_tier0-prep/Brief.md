# Brief — Tier-0 Bridge Prep (BRIDGE_2026-06-21_tier0-prep)

| Field | Value |
|---|---|
| **Human request** | Author the tier-0 bridge **prep** plan + decision-framing brief + reconciled contract direction integrating the chirality-app-dev generalist harness with chirality-piping / OpenPipeStress under the Domain Engine Framework. |
| **Normalized action type** | `FRAMEWORK_EXTENSION` + `PROFILE_ADOPTION` (prep) + `BOUNDARY_AUDIT` |
| **Run nature** | Root-governance authoring (scope override; supervised by Type-0 `AGENT_HELPS_HUMANS`). NOT project-runtime work. |
| **WORKING_ROOT** | `{REPO_ROOT}` (resolved via `git rev-parse --show-toplevel`) |
| **DOMAIN_ENGINE_ID** | `open_pipe_stress` |
| **Profile** | `_DomainEngines/profiles/open_pipe_stress.DRAFT.yaml` (status DRAFT) |
| **Integration level** | MANUAL_BRIDGE (L0) today; staging owner-ruled |
| **Tools invoked** | None (read-only verification only; no domain tool invoked, no mutation) |
| **Write scope this run** | `{REPO_ROOT}/_DomainEngines/**` only (owner-approved). No writes to `projects/**`, `agents/**`, root `docs/**`. |
| **Permissions** | doc-only PROPOSAL authoring; no canon edits applied; no git; no professional-status claims |
| **Expected outputs** | BRIEF (7 framed decisions), PLAN (4-gate + staging + tier map), CONTRACT_DIRECTION (precedence + ProfileStatus + merge), readiness verdict, 4 gated canon diffs, 7 decision-record stubs |

## Inputs read (provenance)

- **Governing core (first-hand):** `agents/AGENT_DOMAIN_ENGINE.md`, `AGENT_HELPS_HUMANS.md`, `AGENT_EQUATION_AUDIT.md`, `PROFESSIONAL_ENGINEERING.md`, `AGENTS.md`, root `docs/{CONTRACT,TYPES,SPEC,DIRECTIVE,PLAN}.md`, `plans/monorepo_*.md`.
- **Both repos + decision records + root second-pass:** 8-agent read-only verification (workflow `tier0-cold-verify`, 2026-06-21).
- **Cross-checks (challenge-not-adopt):** `projects/chirality-app-dev/plans/artifacts/bridge_appdev_contribution_for_tier0_2026-06-21.md`; `projects/chirality-piping/plans/artifacts/bridge_piping_contribution_for_tier0_2026-06-21.md`.
- **Coordination prompts:** `execution/_Coordination/NEXT_INSTANCE_PROMPT-{piping,app-dev}.md`.

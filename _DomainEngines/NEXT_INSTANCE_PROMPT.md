# NEXT_INSTANCE_PROMPT — Tier-0 Bridge sequencing (how rulings flow to action)

This is the handoff/sequencing contract for the tier-0 bridge prep snapshot `bridge/BRIDGE_2026-06-21_tier0-prep/`. It specifies how owner rulings become action. Nothing here is ruled.

## Sequence

1. **HUMAN rules** the decisions in `_DECISIONS/D-T0-01..08_*.md`: set `HumanRuling: <choice>` + `Ruling SHA: <commit>` + `Date:` in each stub. (Precedence D-T0-01 and data-residency D-T0-04 are load-bearing; D-T0-04 has a gate-safe DEFAULT if deferred.)
2. **DOMAIN_ENGINE reads** the ruled stubs and:
   - if D-T0-01 ⇒ framework-canonical and FM-01..04 approved: routes the canon edits to a **HELPS_HUMANS / framework-maintenance** pass (the diffs are in `bridge/.../framework_maintenance/`); CHANGE publishes them.
   - updates `profiles/open_pipe_stress.yaml` (e.g. ProfileStatus enum per D-T0-02; integration level per D-T0-03). *[Renamed from `open_pipe_stress.DRAFT.yaml` 2026-07-01 per D-GOV-06.]*
   - emits the TOOLMAKER briefs (`bridge/.../TOOLMAKER_BRIEF-*.md`) to the owner-chosen owning workflow.
   - writes a new immutable snapshot recording the post-ruling state and updates `_LATEST.md`.
3. **DOMAIN_ENGINE signals the green light** by writing `_DomainEngines/RULINGS_PUBLISHED.md` (pointer to the ruled SHAs + which decisions are now actionable). This is the artifact app-dev and piping watch for.
4. **app-dev and piping each author their OWN execution slices** (PLAN_cross_tier "Who-does-what"), reading `RULINGS_PUBLISHED.md` — tier-0 never writes their slices. app-dev's PKG-10 re-draft is blocked until D-T0-01; piping prep is DEC-042-sanctioned and D-21-held.
5. **CHANGE publishes** each tier's work behind its own gates.

## Invariants carried

- No step marks a profile `ADOPTED` or a deliverable `ISSUED` without the human gate (K-AUTH-1, F4).
- No live binding (L2–L3) until all four asymmetric conditions clear (PLAN §Live build).
- Tier-0 stays doc-only and shared-root-only; canon edits are gated diffs, never self-applied.

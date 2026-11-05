# RULINGS_PUBLISHED — Tier-0 Bridge (2026-06-21)

The owner ruled all 8 tier-0 decisions in-session on 2026-06-21. This file is the **green-light signal** the project loops watch (per `NEXT_INSTANCE_PROMPT.md`). Canonical per-decision records: `_DECISIONS/D-T0-01..08_*.md` + `_DECISIONS/_REGISTER.md`. **Rulings are SHA-bound at the publication commit `6e70b5aace4a3a7c4ebb20490a3bf57bfd912f45`** (2026-06-21; K-AUTH-2); the per-record Ruling SHA fields were backfilled 2026-07-02 per owner ruling *(the bind-at-publish/TBD conditional formerly stated here was stale after publication)*.

## The rulings

| ID | Ruling |
|---|---|
| D-T0-01 | **Framework-root persona canonical**, as **new framework policy**. Two-way merge to root: app-dev conforms DOWN; OperationProposal merges UP. |
| D-T0-02 | **Keep both** → 7-token `ProfileStatus` (FM-01). |
| D-T0-03 | **L3 is the destination**, reached **risk-graded per-operation**; L0→L1→L2→L3; L4 future-only. |
| D-T0-04 | **OPEN RESIDENCY** — agent may see the private model + Class-B inputs; the app does not enforce privacy; any provider (local/Anthropic/other). **L3 not residency-blocked.** |
| D-T0-05 | **Confirmed** G1–G5. |
| D-T0-06 | **Persona cadence**; `VALIDATED` gated on the TOOLMAKER profile-schema validator. |
| D-T0-07 | **tier-0-owned versioning** referencing both versions; **DEC-041 confirmed**. |
| D-T0-08 | **Sequential** Fence-3: source types → MCP tools, after D-T0-01 + proven L2. |

## What is now actionable, by owner — STILL GATED

**Tier-0 (DOMAIN_ENGINE → human-gated framework-maintenance pass → CHANGE):** FM-01..04 are now **authorized in direction** but remain **gated diffs to be applied by a HELPS_HUMANS/framework-maintenance pass and published by CHANGE** — not self-applied. Update the DRAFT profile per rulings.

**Tier-1 (app-dev loop):** may begin (1) PKG-10 re-draft to the ruled canon; (2) SHA-pin `AGENT_DOMAIN_ENGINE.md` into DEL-10-01/03 `_REFERENCES.md`; (3) flow-A tier-0 versioning; (4) ProfileStatus/OperationProposal conformance. **Subject to its own fences + the RES-RECONCILE item below.** Tier-0 does not author this slice.

**Tier-2 (piping loop):** DEC-042-sanctioned prep only (validate-only trust-probe, surface-reconciliation, headless CLI entrypoint). **D-21 still held.**

## `RES-RECONCILE` — RESOLVED 2026-06-21 (both halves published + tier-0-verified)

The open-residency ruling required two working-root fences to be reconciled by their own loops (tier-0 cannot edit them). Both are now done, published, and verified cold against their committed diffs:

- **app-dev fence F1** → **`D-APP-44` @ `d83e63b95`**: F1 amended from a categorical hard-deny to an **owner-permitted, default-closed** provider/residency configuration (egress only under explicit owner config; harness never auto-egresses). F2/F3/F4 + K-AUTH intact; scope clean.
- **piping `OPS-K-PRIV-1` / SPEC §4.4 / `IP_AND_DATA_BOUNDARY`** → **`DEC-051` @ `9db0eef27`**: provider-channel residency relaxed; **`OPS-K-IP-1/2/3` + `IP_AND_DATA_BOUNDARY` + telemetry-off preserved** (verified: IP rows untouched, boundary doc additions-only, `PROFESSIONAL_BOUNDARY.md` not touched).

**Net posture (owner-confirmed 2026-06-21): keep default-closed.** OPEN residency; the harness (which owns the egress layer) is default-closed and egresses only under an explicit owner provider/residency config; the engine adds no independent guard or indicator; telemetry stays off. The two repos' wordings differ but are complementary — the harness config is the single control point. The K-CONFLICT-1 conflict-on-record is **cleared**; residency is no longer a live-build blocker.

## Still gating the LIVE build (unchanged by these rulings)

The 4 asymmetric conditions still hold: **tier-0 adoption** (in progress) · **app-dev F3** · **piping D-21** · **DEC-041 automation condition**. Residency is no longer a 5th blocker.

## Next

HELPS_HUMANS framework-maintenance pass applied FM-01..04 and **published them at commit
`77a327727`** (committed + pushed to origin/main, owner-directed 2026-06-21): canon
`agents/AGENT_DOMAIN_ENGINE.md` + root `docs/CONTRACT.md`, the FM records, and the release
note. Tier-0 cold-verified the live canon against all four diffs (clean). Root
`docs/CONTRACT.md` remains DRAFT-pending-ratification per its own header; the K-DOMAIN
family rides that broader ratification.

The profile-schema validator (TOOLMAKER) is **built** and the profile **passed** → `VALIDATED`; the owner
then **ruled Gate 2 (`VALIDATED → ADOPTED`) on 2026-06-21** → ProfileStatus **ADOPTED**. **Tier-0 adoption
is complete** — 1 of the 4 live-build conditions cleared; remaining: **app-dev F3 · piping D-21 · DEC-041**.

App-dev loop (now actionable — canon is published): annotate app-dev K-DOMAIN-1..4 as
specializing framework `docs/CONTRACT.md` §1.12 without weakening it, and SHA-pin the ruled
`agents/AGENT_DOMAIN_ENGINE.md` revision (`77a327727`) into DEL-10-01/03 `_REFERENCES.md`.

*(A stale closing line — "Profile remains DRAFT … and not ADOPTED" — contradicted the adoption paragraph above and was deleted per D-GOV-06, ruled 2026-07-01.)*

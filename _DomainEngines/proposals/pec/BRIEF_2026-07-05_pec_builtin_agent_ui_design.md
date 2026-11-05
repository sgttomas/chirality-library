# BRIEF (ADOPTED): the built-in agent UI in pec — design

**Status:** ADOPTED — adopted by the owner's D-PEC-16 O-A ruling with runtime
**RT-B (local sidecar)** (2026-07-06, verbatim in
`../../../projects/pec/execution/_Coordination/_DECISIONS/D-PEC-16_builtin_agent_ui.md`).
Adoption authorizes no implementation; the source tranche is `D-PEC-17`
(opened NOT_PREPARED at ruling). Companions: tier-0 `D-T0-19`/`D-T0-20` (both
RULED 2026-07-06); sibling brief
`BRIEF_2026-07-05_pec_appdev_bridge_design.md` (ADOPTED same direction —
shared seam, actor model, and human-act boundary).
**Date:** 2026-07-05
**Prepared by:** PEC work loop agent (K-AUTH-1; D-GOV-04).

Structure precedent: `BRIEF_2026-07-05_embedded_upload_agent_design.md`
(adopted 2026-07-05). This brief extends that design — same proposal seam,
same lifecycle — from "upload → proposal" to a full in-app agent surface; its
RV-12 rider and RV-13..21 deferred obligations bind any tranche this design
feeds.

## 1. What the owner asked for

Direction of record (2026-07-05, verbatim): "a fully functioning bridge, with
a built-in agent UI in pec." The workflow it serves is ruled (D-PEC-10 O-A,
owner intent verbatim in that packet): five weekly source documents; updates
"by having the agent intake and triage the information therein to the correct
database assignments"; "the interface will also allow the human to make targeted
changes within the current screen and what it shows"; "the agent is the
primary means of making updates."

Today pec's web UI (React 18 + Vite, `projects/pec/web/src/`) has no agent,
chat, or LLM surface (verified 2026-07-05); agent acts have only run from
external clients (loop scripts — D-PEC-10 rehearsal-01) over the HTTP API.

## 2. Design at a glance

A persistent **agent panel** in the pec web shell (dockable alongside any
page), backed by an agent runtime that acts on pec **exclusively through the
same RBAC'd HTTP API as any client**, authenticated as the provisioned agent
person (`is_admin=0`). The human keeps the existing screens — including the
Admin "Proposed imports" accept/apply buttons — and the panel adds: drop a
file, watch the agent propose and report, ask it to triage, ask questions
about what the current screen shows. Every agent act lands in pec's
append-only history under the agent's own person; every accept/apply stays a
human click under `import.accept` (admin-only). K-DOMAIN-3 is enforced by
RBAC, not by prompt text.

## 3. Runtime options (the D-PEC-16 decision)

| ID | Runtime | Shape | Trade |
|---|---|---|---|
| RT-A | In-server, zero-dep | Hand-rolled `node:https` Anthropic API client inside the pec server; SSE streaming to the panel; tool loop implemented in pec. | ADR-002 intact by construction; single process; but re-implements what the Agent SDK provides (sessions, tool dispatch, streaming, retries) — slowest to useful, largest new test surface. |
| RT-B | Local sidecar (**recommended**) | A separate local Node process hosting the agent (free to use `@anthropic-ai/claude-agent-sdk` and the app-dev `harness-contract` packages); it logs into pec as the agent person and drives the API; the web panel reaches it via the pec server proxying a narrow `/api/agent/*` surface (or a configured local port). Dev story: one script starts server + sidecar. | Richest agent soonest; pec server package keeps zero runtime deps (the SDK dependency lives in the sidecar's own package); the sidecar holds no special power — it is just another RBAC-bounded client; packaging/lifecycle is the main tranche-level design item. |
| RT-C | App-dev-hosted only | No pec-side runtime; the app-dev harness UI (bridge brief) is the sole agent surface. | Zero pec work, but does not satisfy "built-in agent UI in pec"; kept for completeness. |

Whichever runtime rules, the **engine-side contract is identical** (§4) — the
runtime choice never changes what the agent may do to pec.

## 4. The agent client contract (shared with the bridge)

- **Actor:** owner-provisioned agent person; `is_admin=0`; coordinator-class
  grant (`import.propose`, `intake.triage`); never `import.accept`.
- **Acts:** propose / refresh / withdraw-own proposals; open-triage and
  disposition intake items (converted/parked/duplicate/rejected, grounds in
  note; ungroundable items left for the owner); read per the residency bound.
- **Never:** accept, apply, reject-of-others, `force`, approval/decision/check
  outcomes or any reserved human act (profile `professional_boundary`);
  conversion never creates approval records (D-PEC-10 rider).
- **Failure semantics:** `409 STALE_PROPOSAL` → refresh → human re-accepts
  (normal flow); RBAC `403` → report, never escalate.
- **Weekly cycle:** exactly FILE_DROP_RUNBOOK v1.2 (serial proposes, owner
  screen acts between, post-disposition re-import boundary per D-PEC-15 once
  ruled).

## 5. UI composition (v1)

1. **Agent panel** (shell-level, per-project): conversation thread; file-drop
   zone (routes to the adopted upload seam once its tranche lands — until
   then, proposals are filed from pasted/dropped CSV exactly like the Admin
   flow); live status of the agent's open proposals with lifecycle badges;
   triage queue summary.
2. **Screen-context grounding:** the panel is told which page/records the
   human is viewing (client-side route + visible record ids only) so "update
   this one" resolves; it reads records through the API under the agent
   person's visibility, never by scraping the DOM.
3. **Human-act affordances stay native:** accept/apply/reject buttons remain
   the existing Admin components under the human's own session; the panel
   deep-links to them and shows their outcomes; it never renders an
   accept/apply control of its own.
4. **Attribution:** every panel-initiated act renders with the agent person's
   name, exactly as history records it (WF-8 separation).

## 6. Constraints the design must satisfy

- **ADR-002:** zero runtime dependencies in the pec server package — RT-B
  isolates the SDK in the sidecar package; RT-A hand-rolls; either way `npm
  run typecheck && npm test && npm run build && npm run drill` stays green
  with no server-package dependency additions.
- **Residency (`D-T0-20`):** under CLOSED, LLM features run on synthetic/demo
  bases or degrade to the deterministic mapper (adopted-brief RV-12 rider);
  under an O-B ruling, the enumerated surface is the panel's read bound.
- **RBAC (RV-16 analog):** the tranche defines the panel's permission naming
  (who may open the panel, who may direct the agent) rather than inheriting
  `config.manage` silently.
- **Deferred obligations RV-13..21** of the adopted upload brief bind the
  tranche wherever the surfaces overlap (hash binding, CSV-only v1,
  history-vs-audit, permission naming, dry-run contract, report-field
  completeness, upload-store lifecycle, precedent note, CSRF posture).
- **No new authority:** the panel adds capability, never permission — anything
  the agent cannot do via the raw API it cannot do via the panel.

## 7. Out of scope (v1)

Auto-apply or any agent-side accept; `force` in any form; agent-initiated
imports without an owner-dropped basis; SSO/identity-provider work;
non-import write families (each needs its own row per D-PEC-12 §2);
multi-agent orchestration; mobile.

## 8. Path to execution

D-PEC-16 rules the design + runtime → a source-tranche row (D-PEC-17-to-be)
with an exact file fence under `projects/pec/{server,web,core}/**` (+ sidecar
package location if RT-B), tests, rollback/verification plan (D-PEC-08
precedent) → owner authorizes → implementation → rehearsal with the owner at
the screen (D-PEC-10 gate precedent) → weekly use.

## Adoption

Adoption is the owner's act (via D-PEC-16) and authorizes no implementation.
Owner riders land here as dated notes.

**Adoption note (2026-07-06):** adopted by the owner's D-PEC-16 ruling — "I
rule O-A — adopt the UI brief with runtime RT-B (local sidecar). Adoption
authorizes no implementation; open the source-tranche row (D-PEC-17)
NOT_PREPARED per the mechanism" (in-session steer, Ryan Tufts; full ruling
verbatim in the D-PEC-16 packet). Runtime of record: **RT-B** (§3). The
residency bound is now the `D-T0-20` O-B enumerated surface (§6's O-B
branch). Session environment constraint of record (owner, 2026-07-06): no
`ANTHROPIC_API_KEY` exists or will be provided this session — the tranche
builds the LLM seam behind a config-driven engine port with a deterministic
stub, key-droppable later without source change.

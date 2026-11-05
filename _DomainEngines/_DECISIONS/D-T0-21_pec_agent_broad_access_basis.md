# D-T0-21 - PROPOSAL: pec agent broad-access basis (designer testing mode alongside the D-T0-20 enumeration)

**Status:** RULED 2026-07-06 (execution deferred to the next session).
**Execution note (dated):** the companion `D-PEC-20` tranche was executed
2026-07-06 in the deferred-to session; evidence
`_DomainEngines/pec/PEC_2026-07-06_DPEC20-evidence-01/`; recorded in
`_DomainEngines/pec/LOOP_RECEIPTS.md` Receipt 46.
**Date prepared:** 2026-07-06
**Decision ID:** D-T0-21 (residual-work row convention, owner-ruled 2026-07-03: D-T0-20's ruled row stays immutable; this residue gets its own row)
**Prepared by:** PEC work loop agent under the standing PEC loop. The ruling act
is the owner's (K-AUTH-1; D-GOV-04). This packet changes no ruling and
authorizes no implementation; the companion source tranche is pec-local
`D-PEC-20`, rulable only if this row opens the basis it implements.

## Why this row exists

D-T0-20 O-B (RULED 2026-07-06) gave LLM-hosted agents an enumerated OPEN
surface — (i) intake items, (ii) `import_proposal` records/reports, (iii) the
profile's `chirality_readable_artifacts`, (iv) owner-dropped files — under the
agent person's RBAC, `is_admin=0`. The D-PEC-17 sidecar implements it as a
hard clamp: under `model-provider` egress, reads outside the enumeration
throw `OUTSIDE_ENUMERATION`, never silently narrowed
(`projects/pec/agent-sidecar/src/acts.ts:36-60`, test-pinned).

At the first live SDK-engine session (2026-07-06, the owner at the screen,
demo basis `pec-demo.db`), the clamp behaved exactly as ruled — and the owner
found it too narrow for the next phase. Owner direction of record
(2026-07-06, in-session, Ryan Tufts, verbatim):

> I want to expand the agent functionality and data access broadly.  We can
> keep the narrow controls in place too.  Both have their place.  But now, as
> the system designer and sole user I need to expand the agent functionality
> to push the limits and test out functionality.

D-T0-20 residency expansion is excluded from agent-side acts (Receipt 32
exclusions; the D-T0-20 packet's own scoping), so the expansion needs this
tier-0 row and the owner's ruling.

## Verified current state

| Fact | Source |
|---|---|
| The clamp keys on the ENGINE's egress class: `model-provider` ⇒ enumerated reads only; `none` (stub) ⇒ every RBAC-visible read passes. | `projects/pec/agent-sidecar/src/acts.ts:53-60` |
| The pec server already exposes the whole read surface as RBAC'd project-scoped GET routes (overview, packages, deliverables, plan, my-week, log, holds, approval-register, decisions, risks, tracker, interfaces, intake, history, explain, reports, import-proposals). | `projects/pec/server/src/api.ts` GET routes |
| The agent person is its own identity, `is_admin=0`, coordinator-class grant; accept/apply are structurally out of the sidecar (no method, URL denylist, payload guard, pec RBAC 403 — test-pinned). | `projects/pec/agent-sidecar/README.md`; D-PEC-17 packet + evidence |
| Screen context is route + record ids only, never page content (rider 5); v1 publishes ids on two detail routes only. | `projects/pec/web/src/agent/context.tsx` |
| The live basis in use is the owner's demo instance (`pec-demo.db`, project AUR); the real/non-scratch mutation basis remains its own future row. | Receipt 43; D-T0-20 packet clarity sentence |

## Decision to rule

Whether LLM-hosted (model-provider egress) pec agents gain a second,
**config-selected access basis** — broad RBAC-visibility reads for
designer/sole-user testing — alongside (not replacing) the D-T0-20 O-B
enumeration.

## Options

- **O-A — status quo.** Enumerated surface only. No change.
- **O-B (recommended) — dual basis, owner-selected per launch.** Add
  `PEC_AGENT_ACCESS=enumerated|broad` to the sidecar config; **default
  `enumerated`** (the D-T0-20 clamp exactly as today). `broad` widens
  model-provider **reads** to everything the agent person's own RBAC already
  shows over the existing GET routes. Guardrails that do NOT move with the
  switch (excluded regardless of basis): accept/apply/reject-of-others/
  `force` (K-DOMAIN-3; structural); creating approval/decision/check outcomes
  or any conversion-shaped disposition (GOV MAJOR-1); people/config/project
  mutation; instance-admin identity. Disclosure: `/agent/health` and the
  panel badge state the active basis; evidence packs must name it.
- **O-C — remove the clamp entirely.** Not recommended: erases the
  enumerated posture the owner said should remain available ("both have
  their place"), and removes the machinery future rows will want.

## Recommendation

**O-B.** It implements the owner's direction literally — broad access for the
designer, narrow controls kept in place — as a launch-time owner act (env
flip), with the human-only acts unchanged and structurally enforced. Egress
consequence stated plainly: under `broad`, any RBAC-visible record the model
reads may reach the model provider; the owner, as sole user on his own demo
basis, is the one who flips it.

## On-ruling mechanism

Record the ruling verbatim in this packet's Human-ruling section + register
row; pec-local `D-PEC-20` (companion source tranche) becomes rulable; the
loop executes only under that tranche's fence. No profile edit is required by
this row itself (`data_residency` remains the D-T0-20 O-B text for the
default basis; the packet note records the broad testing basis as
owner-selected per launch).

## Human ruling

**RULED — 2026-07-06** (owner in-session, Ryan Tufts, verbatim):

> I want to make the ruling here to give approval to proceed with this work.
> But I want to defer implementation of the work until the next session.

Recorded interpretation (agent, per the presented slate): O-B (dual basis, owner-selected per launch, default `enumerated`) affirmed as
presented (the recommended option). Implementation is DEFERRED by the same
ruling: no source change this session; the ruled-but-unexecuted tranche is
live authority for the next session (LOOP_INIT S5 adopted-brief posture),
executed inside the D-PEC-20 fence with the packet's verification plan.

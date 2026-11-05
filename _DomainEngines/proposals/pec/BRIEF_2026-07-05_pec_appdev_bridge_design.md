# BRIEF (ADOPTED): pec ↔ chirality-app-dev harness bridge — design

**Status:** ADOPTED — adopted by the owner's D-T0-19 ruling (O-1A + O-2A +
O-3A, 2026-07-06, verbatim in
`../../_DECISIONS/D-T0-19_pec_appdev_bridge_lane.md`) as the design basis for
the P1/P2 app-dev packets. Adoption authorizes no implementation in either
project — every source tranche carries its own D-APP/D-PEC ruling. Companion
decision packets: tier-0 `D-T0-19` (lane, transport, mapping — RULED), `D-T0-20`
(residency — RULED O-B 2026-07-06), pec-local `D-PEC-16` (built-in agent UI,
sibling brief — RULED O-A/RT-B 2026-07-06).
**Date:** 2026-07-05
**Prepared by:** PEC work loop agent (K-AUTH-1; D-GOV-04).

Structure precedent: `BRIEF_2026-07-05_embedded_upload_agent_design.md`
(adopted 2026-07-05; its RV-12 rider and RV-13..21 deferred obligations bind
any pec-side tranche this design later feeds).

## 1. Purpose and shape

One engine-side seam, two harness hosts. pec's `import_proposal` API (D-PEC-08
tranche; L3 per D-T0-18/D-PEC-12) is the single seam through which any agent
acts on pec. This brief designs the **app-dev host**: the Claude-Agent-SDK
harness in `projects/chirality-app-dev` reaching pec through its domain MCP
tools. The sibling brief designs the **in-pec host** (built-in agent UI). Both
hosts share the actor model, the transport, and the human-act boundary defined
here, so the engine cannot tell the hosts apart and the governance story is
checked once.

All facts below were verified against the live tree 2026-07-05 (HEAD
`e2e30abfa`).

## 2. The engine-side seam (as shipped)

Routes (`projects/pec/server/src/api.ts`, D-PEC-08 block):

| Act | Route | Permission | Notes |
|---|---|---|---|
| propose | `POST /api/projects/:pid/import-proposals` | `import.propose` | dry-run computed at propose |
| list / get | `GET .../import-proposals[/:id]` | `import.propose` | read |
| refresh | `POST .../import-proposals/:id/refresh` | `import.propose` | recomputes dry-run; **voids prior acceptance** |
| accept | `POST .../import-proposals/:id/accept` | `import.accept` (admin-only) | requires version echo + SHA-256 echo (RV-13) + watermark match; stale ⇒ `409 STALE_PROPOSAL` |
| reject | `POST .../import-proposals/:id/reject` | own: `import.propose`; others: `import.accept` | reason recorded |
| apply | `POST .../import-proposals/:id/apply` | `import.accept` (admin-only) | watermark re-check; contract import + lifecycle change in one transaction (RV-17); `force` is a human-supplied argument, never agent-set |

Auth is cookie/session only: `POST /api/auth/login` → httpOnly `pec_session`
cookie (7-day TTL), DB-backed, person-bound; **no API-token / bearer / service
mechanism exists** (`projects/pec/server/src/auth.ts`; grep-verified). The
five import-proposal mutation routes carry a same-origin guard that fires only
when an `Origin` header is present (`requireSameOrigin` in
`projects/pec/server/src/services/proposals.ts`, RV-21); other mutations
(intake triage, login) carry no origin guard; a header-less programmatic
client passes. Server: `node:http`, port `PEC_PORT` (default
4810), DB `PEC_DB`; ADR-002 zero server runtime dependencies.

## 3. Transport design (D-T0-19 sub-item 2, recommendation O-2A)

- **Endpoint:** `http://127.0.0.1:<port>` only; port from harness-side local
  config (default 4810). The client refuses non-loopback hosts by
  construction.
- **Identity:** an owner-provisioned agent person (D-PEC-10 actor model: own
  person record, `is_admin=0`, coordinator-class grant carrying
  `import.propose` + `intake.triage`, never `import.accept`). Credentials
  (email/password) come from the harness host's local environment, are never
  committed, never echoed into tool results, and never shown to the model.
- **Session:** login at bridge-session start; hold the `pec_session` cookie in
  memory; re-login on `401`. No cookie persistence to disk.
- **Server lifecycle:** the harness never starts, stops, or owns the owner's
  pec server or DB. Hermetic tests inside an executing tranche may spawn a
  scratch-DB server (O-2B-style) under the same client and actor model.
- **Error taxonomy** surfaced to the model as tool results: `401`
  (re-auth), `403` (RBAC/origin refusal — report, never escalate), `400`
  (contract/echo mismatch, e.g. sha256 echo), `409 STALE_PROPOSAL` (watermark
  moved — the ruled recovery is refresh → owner re-accepts; rehearsal-01
  evidenced this loop), `5xx`/network (report; no retry storms).
- **Why not child-process/sidecar as primary:** D-APP-50's framing fit
  piping's Rust binaries. pec is a stateful HTTP server whose RBAC, audit
  attribution, and staleness guards *are* the governance mechanism — the
  transport must reach the owner's running instance, not a private copy.
- **Future engine-side options (not in scope, each its own D-PEC row if ever
  wanted):** an API-token/service-identity mechanism; origin-guard hardening
  for cookie-bearing non-browser clients; CSRF-posture changes (RV-21).

## 4. Tool surface mapping (D-T0-19 sub-item 3, recommendation O-3A)

The app-dev registry (`harness-tools.v8.domain-mcp-read-live`) already
registers the names; today `domain_propose_operation` /
`domain_proposal_validate` are descriptor-only and the read tools are gated to
`open_pipe_stress` by a singleton check in
`frontend/src/lib/harness/mcp/read-tools.ts`.

| Tool | Grade | pec binding (all under `profileId: 'pec'`) |
|---|---|---|
| `domain_completeness_check` | read | unchanged semantics over `_DomainEngines/profiles/pec.yaml` once the multi-engine registry (P1) lands |
| `domain_rule_check_run` | read | same |
| `domain_propose_operation` | workspace-write | inputs: `contract` (one of the five §16 contracts), CSV payload or owner-dropped file reference, optional `proposalId` + `mode: refresh`. Maps to propose / refresh. Output: proposal id, lifecycle state, dry-run report (visibility per §6). |
| `domain_proposal_validate` | read | input: `proposalId`. Maps to get-proposal + dry-run report. Read-only; never recomputes (refresh mutates, so it rides the write tool — the grade point D-T0-19 settles). |
| accept / apply / reject-of-others / `force` | — | **never registered as tool names** (D-APP-50 rider-2 precedent; K-DOMAIN-3; `import.accept` admin-only). The owner performs them in pec's Admin UI. |

Envelope: results reuse the D-APP-50 evidence-envelope pattern (transport
facts + engine response verbatim + no domain verdict claim). The harness never
interprets a green dry-run as acceptance — K-DOMAIN-4 wording rides the
descriptor text.

## 5. Phased tranche plan (D-T0-19 sub-item 1; no source change under this brief)

- **P1 — app-dev future PROPOSAL (provisionally `D-APP-51`, renumbered from
  the live app-dev register at authoring time):** replace the singleton
  profile gate with a small registry (id → profile path, engine kind,
  transport binding); expose the two read tools for `profileId: 'pec'`. No pec
  writes; no new live tools beyond the read pair.
- **P2 — app-dev future PROPOSAL (provisionally `D-APP-52`, same renumber
  rule):** the localhost HTTP client + session identity per §3; first live
  exposure of `domain_propose_operation` + `domain_proposal_validate`, scoped
  to pec; hermetic scratch-basis rehearsal + committed bridge evidence (§7).
  Real-data **visibility** additionally gated by `D-T0-20`; real/non-scratch
  DB **operation** by its own future basis row (the D-PEC-10 scratch/demo
  rider and the deferred pilot-DB basis stand).
- **P3 — pec `D-PEC-16` → later source-tranche row:** built-in agent UI
  (sibling brief); engine-side source changes, if any, ride that lane — the
  bridge itself requires **zero pec source change**.
- **P4 — end-to-end weekly-workflow rehearsal** through the harness UI: owner
  at the screen for every accept/apply, agent driving propose/refresh/triage,
  captured per §7 and the FILE_DROP_RUNBOOK v1.2 cycle — on the mutation basis
  then ruled (scratch until the pilot-DB/real-basis row rules).

Cross-loop fences: app-dev source executes only under D-APP-* rulings in the
app-dev register; this lane never writes `_DomainEngines/bridge/**`,
`_DomainEngines/proposals/open_pipe_stress/**`, or piping surfaces; pec source
stays behind F-PEC-1 and pec-local rulings.

## 6. Residency enforcement points (depends on `D-T0-20`)

What the model sees is exactly what tool results carry. Under the current
CLOSED default: synthetic/demo/scratch bases freely; owner-dropped file
content and count-level + dropped-row-error reports per D-PEC-12 §4; nothing
else without a per-run owner enumeration. If `D-T0-20` rules O-B, the
enumerated surface (intake items, proposal records/reports, the profile's
`chirality_readable_artifacts` set, dropped files) becomes the standing bound,
and for the v1 endpoint set the transport client enforces it structurally: the
client binds only the §4-mapped endpoints — it has no generic "GET any pec
URL" tool. Any later tool that reaches other enumerated surfaces (register
exports, Explain payloads) needs its own D-APP row and re-check against this
bound. Capture limits
for what may be *committed* remain governed by the D-PEC-01/RV-11 conventions
regardless of the visibility ruling.

## 7. Evidence convention

Each governed bridge rung captures an immutable
`_DomainEngines/pec/PEC_<date>_BRIDGE-evidence-NN/` snapshot (D-T0-13
convention): tool-call transcripts (envelopes verbatim), proposal mirrors
under `_DomainEngines/proposals/pec/`, dry-run/apply reports, export-and-
compare results (RV-10), scratch-DB lifecycle notes. Routine weekly cycles log
through pec's own append-only history (person-attributed), not through
evidence dirs (FILE_DROP_RUNBOOK v1.2 convention).

## 8. Risks and open points (named, not silently resolved)

1. **Registry design (P1)** — the profile registry must not weaken the
   open_pipe_stress gate semantics; per-engine transport binding keeps pec's
   HTTP client from ever being reachable under another profileId.
2. **Secret handling** — pec has no token mechanism; password-in-env is the
   v1 cost of zero engine changes. If the owner wants better, that is an
   engine-side D-PEC row (§3 future options), not a harness workaround.
3. **Watermark movement under concurrency** — owner screen acts move the
   watermark while the agent holds proposals; `409 STALE_PROPOSAL` → refresh →
   human re-accept is the ruled loop, and the harness must surface it as
   normal flow, not an error to retry around.
4. **Origin-guard posture** — the guard passes header-less clients today;
   whether cookie-bearing non-browser clients should be further constrained is
   RV-21 territory for a future pec row.
5. **Grade semantics** — `domain_proposal_validate` stays read-grade only if
   it never triggers recompute; the tranche's tests must pin that.

## Adoption

Adoption is the owner's act and authorizes no implementation; the D-APP-51/52
packets and any pec-side tranche carry their own rulings. Owner riders land
here as dated notes.

**Adoption note (2026-07-06):** adopted by the owner's D-T0-19 ruling —
"The bridge design brief moves CANDIDATE → ADOPTED as the design basis for
the P1/P2 packets." (in-session steer, Ryan Tufts; full ruling verbatim in
the D-T0-19 packet). The companion rulings landed the same direction:
`D-T0-20` O-B (enumerated OPEN visibility surface — §6's O-B branch is now
the standing bound; mutation basis unchanged, scratch/demo only) and
`D-PEC-16` O-A with runtime RT-B (sibling brief adopted). No implementation
is authorized by this adoption.

## 2026-07-22 shared-runtime migration note

D-T0-23/D-PEC-56 replace the historical two-host runtime ownership with one
shared daemon. This brief’s deterministic PEC API/RBAC seam remains an adapter
input; app-dev and embedded PEC are clients of the same runtime. The legacy
PEC endpoint may proxy for one migration cycle, never as a second production
loop.

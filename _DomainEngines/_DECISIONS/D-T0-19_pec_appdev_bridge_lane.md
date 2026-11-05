# D-T0-19 - PROPOSAL: the pec ↔ chirality-app-dev harness bridge lane — scope, transport, and tool mapping

**Status:** RULED — O-1A, O-2A, O-3A affirmed by owner 2026-07-06 (verbatim below).
**Date prepared:** 2026-07-05
**Decision ID:** D-T0-19 (new coupling row — no prior row in any register claims the
pec ↔ app-dev pair; verified 2026-07-05 against the tier-0, pec-local, app-dev,
and piping registers)
**Prepared by:** PEC work loop agent. The ruling act is the owner's (K-AUTH-1; D-GOV-04).

Structure precedent: the bundled registration-shape packet
`D-T0-11_pec_registration_shape.md` (several sub-items under one row) and the
option-slate shape of `D-T0-18_pec_l3_operation_proposal_advance.md`.

## Why this row exists now

Owner direction of record (2026-07-05, in-session, Ryan Tufts, verbatim):

> the pec ↔ chirality-app-dev bridge is my top priority for both projects: a
> fully functioning bridge, with a built-in agent UI in pec. This session is
> detailed planning ONLY — prepare the tier-0 decision packet(s) and the
> design brief(s) for the lane and stop at every gate; no source tranche in
> either project this run.

The two halves of the bridge pattern are separately proven but nowhere joined:

1. **Harness side (app-dev).** The D-APP-49/D-APP-50 tranches (after
   D-T0-08/D-T0-10) landed the domain MCP tool family: `domain_completeness_check`
   and `domain_rule_check_run` live read-side; `domain_propose_operation` and
   `domain_proposal_validate` registered **descriptor-only**; no apply tool
   registered (registry `harness-tools.v8.domain-mcp-read-live`,
   `projects/chirality-app-dev/frontend/packages/harness-contract/src/tool-descriptor.ts`).
   The domain seam is hard-gated to a single engine: the runtime check in
   `projects/chirality-app-dev/frontend/src/lib/harness/mcp/read-tools.ts`
   accepts only `profileId === 'open_pipe_stress'` and hard-codes that profile's
   path; no registry or second-engine mechanism exists, and no file under the
   app-dev frontend references pec (verified 2026-07-05).
2. **Engine side (pec).** D-T0-18 O-A + D-PEC-12 advanced pec to L3
   (`OPERATION_PROPOSAL`, imports scope) on the D-PEC-08 `import_proposal` seam:
   agent-propose / human-accept-apply, hash+version-bound acceptance, staleness
   refusal, transaction-atomic apply. The D-PEC-10 O-A rehearsal
   (`_DomainEngines/pec/PEC_2026-07-05_DPEC10-rehearsal-01/`) evidenced the full
   seam driven by an **external client authenticated as a provisioned agent
   person** (`is_admin=0`, coordinator) over the live localhost HTTP API, with
   every accept/apply the owner's screen act.

Joining them — the app-dev harness agent (and later the built-in pec agent UI)
driving pec's proposal seam — is a cross-project coupling with no register home
until this row. The companion rows are `D-T0-20` (residency residual of
`D-T0-14`, rules the instance-content-visibility question this lane raises) and
pec-local `D-PEC-16` (the built-in agent UI design gate). The lane's design
detail lives in the CANDIDATE brief
`_DomainEngines/proposals/pec/BRIEF_2026-07-05_pec_appdev_bridge_design.md`.

## Decision to rule

Three sub-items, rulable together or severally:

1. **Lane authorization and cross-loop sequencing** — whether the bridge lane
   exists as a goal of record, and which loop authors the app-dev-side
   decision packets.
2. **Transport** — how a harness-hosted agent reaches an HTTP-API-shaped
   engine. pec is a long-running stateful server (`node:http`, default port
   4810, DB-backed cookie sessions, no API-token mechanism — verified
   2026-07-05 in `projects/pec/server/src/{index.ts,auth.ts}`); the D-APP-50
   transport open point was framed for piping's Rust binaries as
   **child-process vs sidecar** and never contemplated an HTTP engine, so the
   shape question is genuinely open at tier-0.
3. **Tool mapping** — how pec's proposal acts map onto the registered domain
   MCP tool names, preserving K-DOMAIN-3 ("a proposal is `proposal_only` until
   validated by a declared deterministic tool and accepted by a human;
   application occurs only through a domain-engine-controlled apply",
   `docs/CONTRACT.md` §1.12).

## What this lane changes (and what it does not)

Changes (once ruled and later executed under D-APP-* tranches): the app-dev
domain seam gains a second registered engine (`profileId: 'pec'`); the reserved
descriptor-only names `domain_propose_operation` / `domain_proposal_validate`
acquire their first live, pec-scoped handlers; a bridge evidence convention
starts.

Does NOT change: accept, apply, reject-of-others, and `force` remain human
in-app acts in pec (`import.accept` is admin-only in
`projects/pec/core/src/permissions.ts`; the harness registers **no** apply
tool — D-APP-50 rider-2 precedent stands); D-T0-14 residency stays as ruled
until `D-T0-20` rules; no app-dev or pec source changes under THIS row — every
source tranche needs its own D-APP-* (app-dev) or D-PEC-* (pec) ruling; the
app-dev ↔ piping bridge loop and its surfaces (`_DomainEngines/bridge/**`,
`_DomainEngines/proposals/open_pipe_stress/**`) are untouched by this lane; no
pilot-readiness, go-live, or professional claim (K-DOMAIN-4).

## Sub-item 1 — lane authorization and sequencing

Proposed phase order (detail in the bridge design brief):

- **P1 (app-dev, future row — provisionally `D-APP-51`, renumbered from the
  live app-dev register at authoring time):** multi-engine profile registry
  replacing the singleton gate in `read-tools.ts`; read-side tools accept
  `profileId: 'pec'`. No pec writes.
- **P2 (app-dev, future row — provisionally `D-APP-52`, same renumber rule):**
  pec HTTP transport client + live exposure of `domain_propose_operation` /
  `domain_proposal_validate` scoped to pec; hermetic scratch-basis bridge
  rehearsal evidence. Real-data **visibility** additionally gated by
  `D-T0-20`; real/non-scratch DB **operation** by its own future basis row
  (below).
- **P3 (pec, `D-PEC-16` → its own later source-tranche row):** the built-in
  agent UI.
- **P4:** end-to-end weekly-workflow rehearsal through the harness UI (owner
  at the screen for every accept/apply), captured under the L3 evidence
  convention.

| ID | Option | Consequence |
|---|---|---|
| O-1A | Single lane, run by the pec loop, with an explicit owner-granted authoring scope for app-dev **decision/coordination packets only** (`projects/chirality-app-dev/execution/_Coordination/_DECISIONS/**` rows authored as PROPOSALs by this loop; app-dev source tranches execute only under those D-APP rulings). | One accountable lane and receipt trail; the F-PEC-4 fence set gains the enumerated app-dev coordination paths by this ruling (dated note, no fence rewrite). Disclosed overlap: the app-dev register file is also the concurrent app-dev↔piping loop's write surface and both loops would mint from the same `D-APP-*` sequence — the grant therefore includes a recorded deconfliction act (dated grant note in the app-dev register preamble at ruling time; IDs minted from the live register at authoring time; receipt cross-references in both ledgers). That loop's own lanes are otherwise untouched, and app-dev source stays behind its own register's rulings. |
| O-1B | Split lanes: this loop prepares only pec/tier-0-side artifacts; a separate app-dev-side loop authors and executes the D-APP packets. | Cleaner fence story, but two loops must coordinate sequencing through receipts; the owner carries the cross-loop scheduling. |
| O-1C | Defer. | The bridge stays unplanned; the built-in-UI lane (D-PEC-16) can still proceed engine-side. |

**Recommendation (non-binding):** O-1A. The owner already gates every PR and
every D-APP ruling; a decision-packet-only authoring grant keeps one receipt
trail for the owner's stated top priority without weakening any source fence.

## Sub-item 2 — transport

| ID | Option | Consequence |
|---|---|---|
| O-2A | **Localhost HTTP + person-bound service identity.** The harness client talks to the owner-run pec server (`127.0.0.1`, configured port, default 4810); authenticates via `POST /api/auth/login` as an owner-provisioned agent person (`is_admin=0`, coordinator-class grant — the D-PEC-10 actor model); holds the `pec_session` cookie in memory for the session; credentials come from local environment, never committed. No pec source change needed for v1 (evidenced by rehearsal-01). Rehearsal/evidence runs use scratch DBs; operation against the owner's real/non-scratch DB is **not** granted here — it additionally needs `D-T0-20` (visibility) **and** its own future basis row lifting the D-PEC-10 scratch/demo-basis rider (the deferred pilot-DB basis; owner 2026-07-05: "Another time"). | The transport matches the engine's shape: RBAC, audit attribution, hash/staleness guards all come from the engine itself, and both agent hosts (harness and built-in UI) share one seam. |
| O-2B | Child-process/sidecar per the D-APP-50 framing: app-dev spawns the pec server against a scratch DB and drives the same API. | Hermetic for tests, but wrong as the primary transport — the weekly workflow is intended (pending its future basis row) to target the owner's live server and DB, which the harness must never spawn or own; reduces to O-2A plus lifecycle management. |
| O-2C | Defer transport to the executing D-APP tranche (D-APP-50 precedent). | Keeps tier-0 clean but re-opens at app-dev a question that is cross-project here: the transport fixes the *actor model* (provisioned person vs process identity), which is an engine-governance fact, not an app-dev implementation detail. |

**Recommendation (non-binding):** O-2A as the ruled transport, with the
executing tranche free to use an O-2B-style scratch spawn **for hermetic tests
only** under the same client and actor model.

## Sub-item 3 — tool mapping

Proposed mapping (detail, schemas, and error taxonomy in the bridge design
brief):

| Harness tool | Grade | pec act |
|---|---|---|
| `domain_propose_operation` | workspace-write | `POST /api/projects/:pid/import-proposals` (propose; dry-run computed at propose) and `POST .../import-proposals/:id/refresh` (recompute dry-run; voids any prior acceptance — a proposal-record write) |
| `domain_proposal_validate` | read | `GET .../import-proposals/:id` (+ dry-run report): read-only inspection of the proposal record and its report |
| — (never registered) | — | accept, apply, reject-of-others, `force`: human in-app acts (`import.accept` admin-only; K-DOMAIN-3; D-APP-50 rider-2 exclusion precedent) |
| `domain_completeness_check`, `domain_rule_check_run` | read | accept `profileId: 'pec'` once the P1 registry lands (profile-evidence reads, unchanged semantics) |

Note the grade point this mapping settles: pec's `refresh` **mutates** (it
rewrites the dry-run and voids acceptance — `projects/pec/server/src/services/proposals.ts`),
so it cannot ride `domain_proposal_validate`, which D-APP-50's executed tranche
corrected to read-grade. Refresh therefore rides the write-graded
`domain_propose_operation`.

| ID | Option | Consequence |
|---|---|---|
| O-3A | Adopt the mapping above. | K-DOMAIN-3 alignment is structural: the write tool can only create/refresh proposals; acceptance and application stay behind pec's admin-only RBAC and are not tool-reachable. |
| O-3B | Map refresh under `domain_proposal_validate` and re-rule that tool's grade to write for pec. | One tool per lifecycle verb reads cleanly, but it re-opens a ruled D-APP-50 correction and makes "validate" a mutating act — misleading against K-DOMAIN-3's "validated by a declared deterministic tool" language. |
| O-3C | Defer the mapping to the executing tranche. | The tranche would fix cross-project semantics without a tier-0 record; the mapping IS the K-DOMAIN-3 alignment story, so it belongs here. |

**Recommendation (non-binding):** O-3A.

## On ruling (mechanism)

Record the ruling verbatim here and in the register row. O-1A additionally:
append a dated fence-scope note to this packet, to the `D-T0-15` fence record,
and to the pec workplan's F-PEC-4 bullet (dated grant pointers, no fence text
rewrite — the same note may, at the owner's word, also ratify explicitly the
precedent-only tier-0 packet-authoring carve-out this loop has used since
D-T0-11); place the deconfliction grant note in the app-dev register preamble
at ruling time so the app-dev↔piping loop discovers the grant at its own
step-0; the next loop iteration then authors the P1/P2 PROPOSAL packets in the
app-dev register (IDs minted from the live register) and stops at their
rulings. A ruling affirming O-1A/O-2A/O-3A together also moves the bridge
design brief CANDIDATE → ADOPTED as the design basis for those packets
(adoption authorizes no implementation); a partial ruling leaves it CANDIDATE
with the ruled sub-items recorded in it. O-2A/O-3A: the ruled transport and
mapping bind the future D-APP tranches; no execution under this row. The
companion `D-T0-20` rules separately; nothing in this row moves residency or
any mutation basis. O-1B: this loop stops after tier-0/pec-side artifacts and
the owner routes the D-APP packets. Any O-*C: the row closes with the ruling
recorded; no execution.

## Human ruling

**Ruling:** O-1A, O-2A, O-3A. Owner ruling of record (2026-07-06, in-session
steer, Ryan Tufts, verbatim):

> D-T0-19: I rule O-1A, O-2A, and O-3A. The bridge design brief moves
> CANDIDATE → ADOPTED as the design basis for the P1/P2 packets. Apply the
> O-1A mechanism as written: dated fence-scope grant notes (this packet,
> D-T0-15, the workplan's F-PEC-4 bullet) and the deconfliction grant note in
> the app-dev register preamble. The grant is decision/coordination packets
> only — app-dev source stays behind D-APP rulings (which item 4 below lets
> this session make).

("item 4 below" is item 4 of the same owner direction — the session-scoped
conditional standing pre-ruling, quoted verbatim in
`_DomainEngines/pec/LOOP_RECEIPTS.md` Receipt 32.)

**Ruling SHA:** received with `main` at `4c636e53e` (tag
`pre-bridge-session-2026-07-06`); published by this packet's PR.

## Fence-scope grant note (dated, per the O-1A mechanism — no fence rewrite)

2026-07-06, by the D-T0-19 O-1A ruling above: the F-PEC-4 fence set gains the
enumerated app-dev **decision/coordination packet** paths —
`projects/chirality-app-dev/execution/_Coordination/_DECISIONS/**` rows
authored as PROPOSALs by the pec work loop. App-dev **source** tranches
execute only under those D-APP rulings. The deconfliction act of record is the
dated grant note in the app-dev register preamble (same date), with receipt
cross-references in both loop ledgers (`_DomainEngines/pec/LOOP_RECEIPTS.md`
Receipt 32; `_DomainEngines/bridge/LOOP_RECEIPTS.md` cross-loop note
2026-07-06). D-APP IDs are minted from the live app-dev register at authoring
time. Twin notes: the `D-T0-15` packet and the pec workplan's F-PEC-4 bullet.

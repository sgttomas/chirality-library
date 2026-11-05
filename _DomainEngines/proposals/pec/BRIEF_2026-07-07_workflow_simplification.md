# ADOPTED brief — PEC workflow simplification (under the 2026-07-07 owner priority)

> **Epistemic status: ADOPTED brief (per-item, 2026-07-07 — see the Human
> ruling section); prepared as CANDIDATE. Adoption was the owner's act
> (K-AUTH-1; D-GOV-04).** Prepared 2026-07-07 by the PEC work loop under
> the standing plan's 2026-07-07 owner-intent addendum (owner verbatim,
> `_DomainEngines/pec/LOOP_RECEIPTS.md` Receipt 51): *"My intention now is to
> simplify workflows and reinforce only reporting on what is factual and has a
> clear basis."* Interface and import refinement are indefinitely postponed
> (D-PEC-14/15/19, ruled 2026-07-07) — nothing below reopens them. Every
> factual claim cites the live tree at authoring; sources govern on any
> disagreement. Adoption authorizes ONLY the enumerated doc-only edits below;
> no pec source, test, manifest, profile, or import-behavior change rides this
> brief under any reading.

## Why this brief exists

Receipt 51 directed that the loop's next work re-derive under the
simplification addendum, "prepared as CANDIDATE briefs to the gate." This
brief converts the addendum into three small, separable doc-only items. Each
stands on facts in the live tree; each can be adopted or declined
independently. Declining everything is a fine outcome — the workflows keep
working exactly as they do today.

## B-1 — One-page launch runbook for the owner's demo launches

**Facts (live tree at authoring):**

- One root script starts all three processes: `projects/pec/package.json:16`
  (`dev` = server & agent-sidecar & web). No workspace script sets any
  environment variable.
- The per-launch environment surface the owner assembles by hand spans four
  read sites: sidecar `agent-sidecar/src/config.ts` (`PEC_AGENT_ENGINE` :72,
  `PEC_AGENT_ACCESS` :76, `PEC_AGENT_SESSION` :80, `PEC_BASE_URL` :81,
  `PEC_AGENT_PORT` :83, `PEC_AGENT_EMAIL` :87, `PEC_AGENT_PASSWORD` :88); SDK
  engine `agent-sidecar/src/engine/sdk.ts` (`PEC_AGENT_MODEL` :296,
  `PEC_AGENT_MAX_ACTS` :61, `ANTHROPIC_API_KEY` :326); server proxy
  `server/src/agent-proxy.ts` (`PEC_AGENT_MESSAGE_TIMEOUT_MS` :29,
  `PEC_AGENT_URL` :43); server core `server/src/index.ts` (`PEC_DB` :17,
  `PEC_PORT` :18).
- The root `README.md:33-36` documents the basic demo launch (including
  `export PEC_DB=...`) but its `npm run dev` line names only the server
  (:4810) and web (:4811) — not the sidecar the same script starts. The only
  operator documentation for the agent-path variables is
  `agent-sidecar/README.md` (they otherwise appear in ruled decision packets,
  not launch docs); nothing under `projects/pec/docs/` mentions the sidecar or
  the agent launch path.
- The by-hand assembly has failed live once on record: the first
  `PEC_AGENT_SESSION=open` launch attempt ran without `PEC_DB`, the server
  came up on the non-demo `pec.db`, and the sidecar failed clean at login
  (401) — relaunch corrected with `PEC_DB` set (Receipt 50, owner-provided
  account).

**Proposal:** one page,
`projects/pec/execution/_Coordination/LAUNCH_RUNBOOK.md`, giving each launch
shape the owner actually uses as a single copy-paste block — (a) demo stub,
(b) demo SDK hermetic/enumerated, (c) demo SDK broad, (d) demo SDK broad+open
— each block listing exactly the variables that shape needs, the one `npm run
dev` command, and the post-launch check: `curl :4812/agent/health` with the
expected disclosure fields (`engine`, `access`, `session`, `configured` —
`agent-sidecar/src/http.ts:115-128`). Doc-only. No script and no manifest row
(root manifests are fenced, F-PEC-1); no default changes; secrets referenced
by name only, never by value.

**Basis in the owner priority:** removes the error-prone by-hand step from a
workflow the owner runs at his screen; the Receipt-50 mishap is the clear
basis.

## B-2 — FILE_DROP_RUNBOOK v1.3 consolidation

**Facts (live tree at authoring):**

- `projects/pec/execution/_Coordination/IMPORT_TEMPLATES/FILE_DROP_RUNBOOK.md`
  (96 lines) carries two procedures side by side: the v1.1 per-drop loop
  (5 steps, lines 24-41) and the v1.2 weekly agent intake+triage cycle
  (6 steps, lines 68-96).
- Its standing-rules block still states **"Never re-import a full RAIL file"**
  (lines 47-49), which v1.2 step 5 itself supersedes in-file ("supersedes the
  v1.1 'never re-import a full RAIL file' rule", lines 87-93).
- Step 5's operative rule is conditioned on a ruling that has now been made:
  "until D-PEC-15 rules a convention, drop dispositioned `item_id`s from the
  weekly export or expect and triage the re-landed rows" (line 92) —
  D-PEC-15 was ruled 2026-07-07 (indefinitely postponed; effect matches O-D;
  register: "runbook v1.2 step 5 interim rule stands"; Receipt 51: "runbook
  v1.2 step 5 stands"). No convention was chosen; the interim rule is what
  stands.

**Proposal:** issue v1.3 with two parts, one mechanical and one an explicit
owner choice:

1. *(mechanical)* Remove the standing-rules text "Never re-import a full RAIL
   file" (lines 47-49) — superseded in-file by step 5's own words (lines
   87-88) — leaving a dated supersession note; and replace step 5's discharged
   "until D-PEC-15 rules a convention" condition with a dated pointer to the
   2026-07-07 ruling, keeping the rule's operative instruction (drop
   dispositioned `item_id`s from the weekly export or expect and triage the
   re-landed rows) word-for-word.
2. *(owner's explicit choice at adoption)* Whether to also retire the v1.1
   per-drop loop (lines 24-41) into a dated note, leaving the v1.2 weekly
   cycle as the single procedure. No source calls the v1.1 loop superseded —
   it is the ad-hoc per-file-drop procedure and carries the RV-7-corrected
   approval-sequence text — so retiring it is a fresh owner act, not a
   cleanup. Adopting B-2 without naming this part executes part 1 only.

No import behavior changes under either part; the document describes the same
acts it describes today.

**Basis in the owner priority:** one procedure instead of two overlapping
ones, and no live rule left pointing at a postponed decision — simplification
of the workflow document the weekly cycle actually runs on.

## B-3 (optional) — REPORT_BASIS.md, the clear-basis reporting reference

**Facts (live tree at authoring):**

- Every reporting surface is server-computed; the web renders payload fields.
  The on-plan KPI is computed in `core/src/status.ts:547-549` (rule
  KPI-ONPLAN, invoked server-side via `projectStatus`), assembled into the
  payload at `server/src/services/views.ts:90`, and rendered untransformed at
  `web/src/pages/Overview.tsx:93`.
- The reporting surfaces are: overview (`server/src/api.ts:118`), revision
  explain (`api.ts:178-181`), register CSV exports (`api.ts:327-332`; the
  register list is the `exportRegister` switch in
  `server/src/import/index.ts`), sponsor brief (`api.ts:333-336`), package
  pack (`api.ts:337-340`).

**Proposal:** one page,
`projects/pec/execution/_Coordination/REPORT_BASIS.md`, enumerating each
reporting surface with its basis — what records it derives from and where it
is computed — so any report, and any agent answer about project state, can
name its basis by pointer. Explicitly NOT a code or prompt change: Receipt 51
closed the KPI-basis lane with none directed, and this item does not reopen
it; it only writes the bases down.

**Basis in the owner priority:** the direct documentary form of "reinforce
only reporting on what is factual and has a clear basis." Offered as optional
because it adds a page rather than removing one — decline it if it reads as
more surface, not less.

## What this brief deliberately does NOT propose

- No import-semantics, matcher, or contract change (D-PEC-14/15 postponed;
  import refinement postponed by the addendum).
- No web/interface change of any kind (interface refinement postponed;
  D-PEC-19 postponed — tracker stays import-owned/read-only).
- No pec source, test, manifest, or profile edit; no new env var, script, or
  dependency; no KPI or agent-prompt change (Receipt 51 closed that lane).
- No edit to any ruled packet or dated map (receipts rule 4); the stale
  five-contract line in the D-PEC-10 packet stays as history — the six-contract
  fact lives in `server/src/services/proposals.ts:22` and Receipt 39.

## Non-binding recommendation

Adopt B-1 and B-2 part 1; take or decline B-2 part 2 and B-3 at preference.
B-1 addresses the one launch failure on record; B-2 part 1 removes the only
live rule text still pointing at a postponed decision. Both shrink workflow
surface without touching behavior.

## On-adoption mechanism

On an owner adoption naming the adopted item(s), the loop executes them as
doc-only edits: branch-first + PR; write scope exactly the named files (all
inside F-PEC-1's `execution/_Coordination/**` grant) plus this brief's status
flip to ADOPTED with the ruling verbatim; checks per the docs-only precedent
(repo self-check, coord-check on the range, `git diff --check`; pec
belt-and-braces not triggered — no pec source touched). Silence or decline
parks the item(s) with nothing to undo.

## Human ruling (2026-07-07)

Owner ruling of record (verbatim, 2026-07-07, in-session, Ryan Tufts):

> B-1: approved.
> B-2, part-1: approved.
> B-2, part-2: no keep the per-drop loop.
> B-3: approved.

Recorded interpretation: B-1, B-2 part 1, and B-3 ADOPTED and executed
doc-only per the on-adoption mechanism above
(`projects/pec/execution/_Coordination/LAUNCH_RUNBOOK.md`;
`FILE_DROP_RUNBOOK.md` v1.3 with the v1.1 per-drop loop retained;
`projects/pec/execution/_Coordination/REPORT_BASIS.md`). B-2 part 2
DECLINED — the v1.1 per-drop loop stays current. Nothing else was authorized
by this ruling.

# Chirality Task Management — PRD Candidate

| Field | Value |
|---|---|
| Date | 2026-07-31 |
| Revision | 2 |
| Status | `NON_AUTHORITATIVE_PRD_CANDIDATE` |
| Candidate project name | Chirality Task Management |
| Candidate project slug | `projects/chirality-task-management/` |
| Authoring session | Fresh Agent 0 (HELP_HUMAN) PRD inquiry, 2026-07-31, per parent basis §12.1 |
| Parent basis | `plans/chirality-task-management/PRD_AUTHORING_BASIS_2026-07-28.md` |
| Addendum input | `plans/chirality-task-management/PRD_AUTHORING_BASIS_ADDENDUM_01_capture_architecture_2026-07-28.md` |
| Architecture review | `plans/chirality_task_management_architecture_review_2026-07-31.html` (this session; frozen basis main@`a7371ed94`) |
| Source corpus | `plans/chirality-task-management/SOURCE_MANIFEST.md` — all three SHA-256 hashes re-verified 2026-07-31 before use |
| Intended next use | Owner review and iteration; adoption only by a separate owner act (§23) |

## Revision log

| Rev | Date | Change |
|---|---|---|
| 1 | 2026-07-31 | Initial candidate from parent basis, addendum, source corpus, and boundary concordance; adversarial findings AF-1..AF-8 |
| 2 | 2026-07-31 | Restructured after the four-lens architecture review and deterministic dry-run (review §07 amendment list, items 1–12), and after two owner directions of record given 2026-07-31. Principal changes: registers move from a four-tier model to per-loop registers bound into loop-entry instruments; no new tool root is minted; the scanner is re-scoped to structured closure-capable surfaces; the return-contract amendment is withdrawn; identifiers change from `AI-` to `TM-`; the schema gains SHA binding, notice/SCA references, and a single-authoritative-file rule; K-TM-4 is re-scoped to permit loop-adopted duties; Stage A shrinks to one loop and zero agent-file changes. Review findings F-1..F-30 dispositioned in §20 |

## 0. Fence and provenance labels

This is a PRD candidate. It grants no scope, adopts no bytes, creates no
project tree, amends no agent instruction or loop instrument, and mints no
directory. Every normative-sounding statement below is a candidate until the
owner's separate adoption act.

| Label | Meaning |
|---|---|
| `[OWNER]` | Owner direction of record (parent basis §2, addendum §2, or the 2026-07-31 session) |
| `[CORPUS]` | The three-document professional-framework source corpus |
| `[GOVERNED]` | Accepted governed record, cited by path |
| `[MEASURED]` | Deterministic dry-run or counted live-state evidence at main@`a7371ed94` (review §02) |
| `[SYNTHESIS]` | Agent synthesis proposed for owner ruling; not settled |
| `[FINDING]` | Adversarial finding (AF-* from the Rev-1 inquiry; F-* / RF-* from the architecture review) — dispositions in §20 |
| `[OPEN]` | Explicitly not decided here; deferred with a named trigger |

## 1. Problem and thesis

`[OWNER]` "Without this, I can't expect that issues that arise during
development will be dealt with." (parent basis §2)

`[OWNER, 2026-07-31]` "The task manager shouldn't be dispatching tasks for
working in deliverables. Those should be discovered via the development loop.
But as matters arise during the course of those development loops that can't
or shouldn't be resolved in that session need to have a means of being
identified and worked on later."

`[OWNER, 2026-07-31]` "Matters get resolved directly or by updating the
content of the deliverables and the appropriate surfaces the development loop
touches."

`[CORPUS]` Projects stall on coordination failures: someone doesn't know
their priorities, can't find the right information, or doesn't know what was
decided. The Nine Domains framework is a simultaneous scanning discipline —
the project's mise en place — surfacing HOLDs before they stop progress,
without micromanaging or creating bureaucracy.

`[MEASURED]` The failure is real but class-specific, not general. Concerns
that enter a decision-register row or a loop receipt's parked-lanes field get
dispositioned — 269 of 275 decision-register rows are ruled, usually with a
verbatim owner token and a bound SHA. Concerns that enter a standalone CSV
register or the routed-notice ledger essentially never close: 29 of 30
notices `TRACKED_OPEN`; 0/12 in a purpose-built disposition register after 58
days; 13/15 research open questions frozen since June; one TBD register that
cannot record closure because it has no status column. The instruction layer
explains it: across 22 concern-generating mechanisms, emission is enforced
and consumption is not (review §03); and because governed outputs are
immutable snapshots, their status fields can never advance in place.

`[GOVERNED]` The ratified contract already names the missing instrument:
K-STALE-2's declared enforcement point is a "Human triage queue"
(`docs/CONTRACT.md:100`) that exists nowhere in `docs/SPEC.md` or
`docs/TYPES.md`. This product is that instrument, built to the shape the
evidence says closes items.

**Thesis.** `[SYNTHESIS, owner-aligned]` Chirality Task Management is a
non-agentic standard plus deterministic tooling for **per-loop, git-tracked
Action Item registers**: durable disposition ledgers for matters that arise
during development-loop work and cannot or should not be resolved in that
session. Loops discover their own work and resolve matters on their own
surfaces; the register guarantees only that what a session could not absorb
survives to a later one and receives explicit disposition. Compressed:

> Capture is deterministic and in-place; promotion is judgment and
> in-register; reading is bound to loop entry by the loop's own ruling; the
> service owns the scan and the views, never the truth.

The service is code. It contains no agent, no LLM, no judgment, and no second
execution loop (parent basis §6.1). `[FINDING F-21]` The register differs
from the failed notice-ledger experiment in exactly one load-bearing way: it
is read because the adopting loop's own entry instrument names it, not
because a duty was asserted at large.

## 2. What Task Management is not

| Must not become | Because |
|---|---|
| A work-discovery or dispatch queue for deliverable production | `[OWNER, 2026-07-31]` work is discovered via the development loop; loop surfaces (`## Remaining`, work graphs, slates) remain the work surfaces. A register view is a disposition ledger, never a backlog the loop pulls deliverable work from |
| A resolution surface | `[OWNER, 2026-07-31]` matters resolve directly or on the loop's own surfaces; the register records existence and disposition only |
| General coordination plane | PEC (`projects/pec/docs/PRD.md` §1.1); seam in §12.2 |
| Agent orchestration / runtime / session service | D-GOV-20; `{EXECUTION_ROOT}/_Coordination/AgentRuns/` (`docs/SPEC.md` §9.8) |
| Authoritative dependency graph | K-DEP-1 (`docs/CONTRACT.md:86`) |
| Deliverable lifecycle authority | REVIEW gates and owning workflows |
| Project-controls / resource-governance service | Human-owned schedule basis; §12.4 exclusions |
| The reusable program work surface | A-B-012 remains deliberately unfilled; §12.8 |
| Universal issue dump | Promotion contract §7 with explicit NOTs |
| A second escalation channel | Escalation reuses the parent-ward notice flow (§8.3) |
| The notice ledger rebuilt | `[FINDING F-21]` a register with no bound reader reproduces 29/30; §13–§14 are the difference, and if they fail, §19 fires |
| A task database in the practitioner-harness sense | `tools/practitioner_harness/README.md`; boundary §12.6 |

## 3. Ontology and vocabulary (Q4, Q18)

### 3.1 Object distinctions (Q4)

| Term | Definition | Where it lives | Owner |
|---|---|---|---|
| task (ordinary word) | A bounded action toward a result; most are never durably tracked | Nowhere durable, by design | The actor |
| work | Actual execution | Deliverable folders, run records | Humans, agents, tools |
| observation | A concern noticed outside the observing agent's brief, returned upward with evidence | Parent-ward returns; loop receipts (§5.2) | The parent, then the loop |
| candidate | A machine-harvested pointer to a possible Action Item | Derived candidate inventory (rebuildable, non-authoritative) | Service, as projection only |
| Action Item | A durable concern that arose during loop work and could not or should not be resolved in that session; the only new authoritative object | The owning loop's register (§6) | The loop's triage owner |
| issue / open question | Existing conventions; remain where they are; scannable | Their existing surfaces | Their workflows |
| risk | A change under consideration with no decision, or a HOLD not yet materialized | Register (with trigger) or owning risk surface | Register owner |
| HOLD | A stoppage of progress or imminent risk of one; the promotion rubric's center | A condition cited by rows, not an object | — |
| dependency | K-DEP-1/-2 deliverable-local rows; never migrated; citable as evidence only at HOLD risk | `_DEPENDENCIES.md` / `Dependencies.csv` | The deliverable |
| remaining work / blocker | `HANDOFF_STATE.md` and `## Remaining` content; scannable; authoritative where they live | Handoffs, status files | The emitting workflow / loop |

An Action Item exists outside deliverable folder structure; association with
a deliverable does not make it deliverable scope (`[OWNER]`, parent basis
§5.2). Resolution may change deliverable documentation, Root governance, an
App/PEC/Piping improvement, a decision or approval, checking evidence,
received information — or nothing. Closure cites the loop-side evidence or
an explicit no-artifact disposition.

### 3.2 Name separation (Q18) and identifiers

1. **"task"** is never the name of a tracked object; the object is **Action
   Item**. No register field, file, or view is named "task".
2. **`TASK`** (the Agent 2 shell) is always code-styled; never shorthand for
   the product.
3. **Task Management** is the product; tooling namespace `taskmgmt`
   (`[FINDING F-26]` collision-free).
4. `[FINDING F-25]` Identifiers use the **`TM-`** prefix, not `AI-` — the
   `AI-` prefix collides with `AI-Reliance`, a governed KnowledgeType
   identifier with 1,093 in-tree occurrences. Row IDs are
   `TM-<LOOP>-<seq>` (e.g. `TM-ROOT-0007`, `TM-PIP-0002`), program-unique by
   loop namespace — `[FINDING, review §02]` bare per-level sequences
   reproduce the live `OI-013` collision, where one ID names three unrelated
   concerns. The inline marker grammar is `TM-CANDIDATE:` (§5.2).

`[OWNER]` (addendum §2, agreed #5): the corpus-consistent spelling is
**praxiology**.

## 4. The Nine Domains, normatively stated

`[CORPUS]` The nine domains — Action Item, Assignment, Prioritization,
Deliverables, Work, Planning, Approval, Checking, Decisions — are a 3×3
scanning matrix: a mnemonic and diagnostic lens for asking, concurrently,
what is missing, unresolved, misaligned, or approaching a HOLD.

`[OWNER]` "the nine domains are scanning lenses for agents to coordinate
their work on, not any kind of sequence or specific workflow." Not a
sequence, lifecycle, state machine, nine agents, nine queues, a replacement
for the development loop, or a source of authority (parent basis §4).

| Domain | Authoritative owner today | Task Management's relation |
|---|---|---|
| Action Item | **Task Management registers (new, §6)** | Owns |
| Assignment | Activations, briefs, RASCI adaptation (§8) | Records assignment facts on rows; A is human-only |
| Prioritization | Human/manager judgment, owner direction | Records stated priority + basis; computes nothing (§16) |
| Deliverables | Accepted decomposition and deliverable state | Cites |
| Work | Loop work; governed agent workflows; run records | Reads run records as scan input |
| Planning | Human-owned schedule basis; workplans; dependencies | Cites; never schedules |
| Approval | Human approval instruments (K-AUTH-1) | Cites; never approves |
| Checking | Validators, reviewers, audits | Cites statuses |
| Decisions | `_DECISIONS/` registers | Cites decision IDs; federates with the residual-row convention (§12.5) |

## 5. Capture architecture

### 5.1 Layer 1 — structured, closure-capable surfaces; the scanner meets them where they are

`[FINDING F-10/F-11, RF-B]` Rev 1 proposed free-text signatures. The
dry-run and adversarial review killed that: `TBD` is the *mandated lawful
token* for unknowns under K-INVENT-1 (19,365 files contain it; 41,679
post-exclusion hits), and the supposed "tight" signatures yield ~1 live row
each because their high counts came from one-off derivative artifacts. Layer
1 is therefore **structured surfaces only** — files whose schema carries an
open/closed state or an explicit concern field:

| Candidate source | Signature | Live load `[MEASURED]` |
|---|---|---|
| Decision registers — non-ruled rows | `_DECISIONS/_REGISTER.md` rows not `RULED` | 6 across 5 registers (e.g. piping D-45 `AWAITING_RULING`, 14 days) |
| Notice files vs. ledger | `NOTICE_*.md` under any `_Coordination/`; ledger rows `TRACKED_OPEN`; **notice present but absent from ledger** | 29 open + 3 unregistered |
| Evaluation findings | `FINDINGS.csv` under `_Evaluation/` trees; open `Disposition`/`Status` values | 33 files; 0/9 horizon rows closed |
| Review findings | `Review_Findings.csv`; `Status` OPEN/DEFERRED or `HumanDisposition=TBD` | 407 registers deployed; 1 known open (PKG16-DEL1604) |
| HOLD registers | `APP_HOLD_REGISTER.csv`, `ACTIVE_RELIANCE_HOLDS.csv` open rows | live instruments |
| Handoff blockers | `HANDOFF_STATE.md` remaining-blocker / coverage-gap content | 35 files with blocker language |
| Packet fields | `Open_Questions.csv`, `Amendment_Candidates.csv`, `Conflicts.csv` (`HumanRuling=TBD`) — immutable at source, harvested as candidates | 23 open questions; 1 open conflict |
| TBD registers | `*TBD_Register.csv` rows | 21 rows (structurally uncloseable at source) |
| Slates and review reports | `*_NEXT_WORK_SLATE_*.md` items; ranked actions and held-open questions in `plans/` review reports (`[FINDING F-23/F-24]` — currently tracked nowhere, and archived plans leave the tracked tree) | 4 slates; 07-28 review §08/§09 |
| Receipt parked lanes | `Parked lanes:` fields in `LOOP_RECEIPTS.md` | uneven: pec 68 mentions, app-dev 1 |
| Run-record escalations | `NEEDS_HUMAN_RULING:` / `MISSING:` in `_run_records/` and managed-run returns — the most-produced, least-read concern artifact (review §03 M3) | present; unindexed |

Free-text token scanning (`TBD`, `TBC`, `ASSUMPTION`) survives only as an
explicit **per-document mode** (`taskmgmt scan --doc <path>`), never as a
tree-wide candidate source. In structured files, `TBD` is a signal only in
disposition-bearing columns (`HumanRuling`, `HumanDisposition`), where the
schema itself says a judgment is outstanding.

### 5.2 Layer 2 — capture at the loop boundary, without touching runtime contracts

`[FINDING F-28]` Rev 1's "amend the RETURN.md contract" is withdrawn: no
such contract exists — returns are free text by typed runtime contract
(`runtime/packages/contracts/src/protocol.ts`), runtime-owned under
D-GOV-20/D-GOV-28, and any standardization is DEL-02-06 work behind an
unactivated carrier. The governed capture paths are instead:

1. **The loop receipt.** Receipts are already contractual per loop
   (`tools/validation/validate_*_loop_receipts.py`) and their
   `Parked lanes:` discipline is the program's proven carry-forward
   mechanism `[MEASURED]`. A loop that adopts a register commits, in its own
   receipt contract, to record session residue either as a register row or a
   parked-lane entry — a loop-owned, loop-ruled change.
2. **The inline marker.** `TM-CANDIDATE: <concern> | <evidence-ref>` may be
   written anywhere governed prose is written (run records, returns, notes).
   It is grammar, not contract: no instruction file must change for it to be
   scannable, and adopting it into instruction text happens only as files
   are touched under `docs/WORKFLOW_COMPONENT_STANDARD.md` §15 lifecycle
   maintenance (`[FINDING AF-1]` — §15, not R15).

The marker designates a candidate; it is not the Action Item and carries no
lifecycle state.

### 5.3 Layer 3 — the register is the only new authoritative object

Promotion is a judgment act of the owning loop's triage owner that writes a
git-tracked row (§6). Lifecycle state lives in the register, never in the
tag or the source surface. The service proper is: scanner + candidate
inventory (derived, rebuildable) + register views + staleness and
closure-echo checks (§6.5, §9).

### 5.4 Why not a central mandatory write-target

Unchanged from Rev 1, confirmed by review:

1. `docs/DIRECTIVE.md` §2.1/§2.2 — authoritative state lives in git-tracked
   files.
2. Instruction-text enforcement is soft (`docs/thesis/08_implementation.md`
   §8.6.2); a dual-write obligation fails silently.
3. A required write path fails Q16; the governed posture is graceful absence
   (§13, PEC-K-01 precedent).
4. Agent-suite rewrite violates parent basis §7.
5. D-GOV-01 — any database is a rebuildable, gitignored projection; Task
   Management is not a domain engine and claims no engine-store exemption.

### 5.5 Disposition of every existing capture surface, by name

`[FINDING F-22]` extended beyond Rev 1's seven rows:

| Surface | Disposition |
|---|---|
| TBD registers | Left in place; scanned. Promoted items cite the row |
| Conflict Tables | Left in place; scanned via `HumanRuling=TBD`. Ruling still happens in the table (K-CONFLICT-1); the row tracks that it is outstanding |
| Open-question / amendment-candidate packet fields | Left in place (immutable); harvested as candidates. The register is where their status can finally advance — the packet never learns, the register does (§6.5 closure echo shows the divergence) |
| Coordination notices + ledger | Left in place; scanned. `TRACKED_OPEN` presented as open concern, never gating; notice-not-in-ledger reported |
| Evaluation `FINDINGS.csv` | Left in place (immutable snapshots); open rows harvested. Disposition happens in-register, citing the finding ID |
| `Review_Findings.csv` | Left in place — it is the proven deliverable-scope action-item shape; only rows left OPEN/DEFERRED/TBD after their review session closes are harvested |
| HOLD registers | Left in place — they are live instruments with their own release rules; scanned for open holds as concerns, never duplicated or released from the register |
| Run records / returns | Left in place (immutable); `NEEDS_HUMAN_RULING:`/`MISSING:`/`TM-CANDIDATE:` content harvested |
| `HANDOFF_STATE.md` | Left in place; blockers harvested |
| Decision registers | Left in place; federated. Non-ruled rows are displayed as their own class; the D-T0 residual-row convention remains the ruled mechanism for governance residue, and Tier-0 keeps it (§12.5) |
| `## Remaining` / slates / work graphs | **Fenced, not scanned into candidates.** These are the loop's work-discovery surfaces `[OWNER, 2026-07-31]`; the register never harvests ordinary planned work. Slate *held-open decision items* (not work options) may be cited by rows |
| Review reports in `plans/` | One-time backfill at Stage A seeding (§17); thereafter, new review reports' ranked actions and held-open questions are a scan source |
| Dependency registers | Fenced (K-DEP-1); citable as evidence only at HOLD risk; never aggregated into a central graph view |

Neither dump nor fragmentation: every surface keeps its owner; the register
adds the one thing none of them has — a mutable, closure-capable disposition
lifecycle with a named triage owner and a bound reader.

## 6. Registers (Q2, Q3, Q6, Q7)

### 6.1 Per-loop registers, no new roots

`[FINDING F-1/F-3/F-4/F-27]` Rev 1's four-tier model assumed standing
occupants that do not exist and a tool root that cannot lawfully be minted
as specified. Rev 2: **one register per development loop**, living inside
the loop's existing coordination surface, owned by the loop's owner and
instruments:

| Loop | Register home (working shape) | Triage owner and cadence instrument |
|---|---|---|
| Root governance loop (= program register) | `execution/_Coordination/_TaskManagement/` | Owner, at root loop entry (`LOOP_INIT.md` — which already requires enumerating parked lanes) |
| App-dev loop | `projects/chirality-app-dev/execution/_Coordination/_TaskManagement/` | Loop owner + instruments, on adoption by loop ruling (F-APP-5) |
| Piping loop | `projects/chirality-piping/execution/_Coordination/_TaskManagement/` | Same (F-PIP-5) |
| PEC loop | with the loop's standing surfaces (see below) | DOMAIN_ENGINE-supervised loop + owner |
| Tier-0 / bridge | not registered — Tier-0 keeps its ruled residual-row convention (§12.5) | — |

- `[FINDING F-3]` Where a loop's standing surfaces and execution tree
  diverge (PEC: loop in `_DomainEngines/pec/`, tree in
  `projects/pec/execution/`), the register lives **with the loop's standing
  surfaces** — the loop reads its own directory every session; that is the
  binding that makes registers work.
- No `_TaskManagement/` enters `docs/SPEC.md` §1.2: these are subdirectories
  of existing `_Coordination/` surfaces (as `AgentRuns/` already is), not
  new workspace tool roots. No SPEC amendment, no G0/G2 change, no
  tool-root-writer audit issue. `[FINDING F-27 dispositioned]`
- No package or deliverable registers. Deliverable/package association is a
  row field. `[FINDING F-1]`
- The program register is the root loop's register. Cross-loop and
  program-scope items live there; OBJ-6 is honored because this PRD is
  itself the "new product function" act OBJ-6 requires, and says so
  (`docs/PRD_ROOT.md` OBJ-6; §23).

### 6.2 Escalation between registers (Q7)

An Action Item's register *is* its escalation position. `[FINDING F-5]`
Elevation is **linked rows, not a move**: the lower register's owner sets
the row `ELEVATED` with `ElevatedTo` naming the target register, and routes
the ordinary parent-ward notice; the receiving register's owner opens a new
row citing the source row (`SourceRef` + `NoticeRef`). No actor ever writes
a register outside its own loop's write scope (K-WRITE-1). Escalation
transport is the existing notice flow — no second channel (§8.3).

### 6.3 Schema (Q6)

`[SYNTHESIS]` Authoritative form: **one `REGISTER.csv` per register**
(`[FINDING F-17]` — the CSV is the single authoritative file; an optional
`TM-<LOOP>-<seq>.md` narrative per item is a non-authoritative summary in
the `_DEPENDENCIES.md`-over-`Dependencies.csv` pattern, and `taskmgmt
validate` checks the summary's header block against its row). Columns:

```text
RegisterSchemaVersion   column 1, every row (v3.1 precedent, docs/SPEC.md:438)
ActionItemID            TM-<LOOP>-<seq>
Title                   one line
Concern                 what needs attention, and the HOLD it prevents/resolves
SourceRef               K-PROV-1 citation: path + section/line, or explicit `location TBD`
SourceSha               git blob SHA of the cited source at promotion (staleness basis)
CandidateRef            scan candidate ID, or DIRECT
DomainLenses            one or more of the nine (scanning aid, never a queue key)
AssociatedWith          deliverable/package/loop/system IDs or EXTERNAL/UNKNOWN
NoticeRef               notice path when the row was carried by / carries a routed notice, else NONE
ScaRef                  SCA ID when superseded by or feeding a scope change, else NONE
Assignment              R/S/C/I parties; no A field for agents, ever (§8)
Priority                stated priority
PriorityBasis           who set it, when, on what basis
Status                  OPEN | DEFERRED | ELEVATED | CLOSED
Trigger                 required when DEFERRED: the condition that reopens attention
ElevatedTo              register + row ID when ELEVATED
Disposition             required when CLOSED: §7.3 taxonomy value
EvidenceRef             required when CLOSED: cited path(s) or explicit no-artifact rationale
EvidenceSha             git blob SHA(s) of cited evidence at closure (K-AUTH-2 posture; HINGE-3)
EvidenceQuote           minimal quote surviving source edits (v3.1 precedent)
Opened / LastReviewed / Closed   dates
Notes
```

`[FINDING F-13/F-14/F-16/F-18 dispositioned]`. No IN_PROGRESS state: work
happens in the owning loop's surfaces, and the register records attention
and disposition, never execution status `[OWNER, 2026-07-31]`.

**Closure-capable-schema rule** `[MEASURED — TP-EXPORT-006]`: a Task
Management register schema must always be able to record its own closure;
`Status` and `Disposition` columns are mandatory in every schema version.

### 6.4 Staleness

`[FINDING F-15]` Only K-STALE-2 semantics transfer: deterministic checks
flag rows whose `SourceSha`/`EvidenceSha` no longer match the cited bytes,
tags whose row vanished, and CLOSED rows whose evidence path is gone —
reported for human triage, never auto-resolved. Transitive staleness
propagation (K-STALE-1) stays with the dependency surfaces it belongs to;
this product does not compute it.

### 6.5 Closure echo

`[MEASURED]` The program's records show a repeating fate: substance closes
downstream while the originating record never learns (HZN-001 ruled by
D-GOV-31, source row still `PENDING_INPUT`; "Code has de facto resolved the
conflict; the ledger row has not been updated"). The service therefore
reports, as labeled display only: rows whose cited source still shows open
after disposition, and candidates whose concern was already dispositioned in
a register. It never writes to the source surface.

## 7. Promotion and disposition (Q5)

### 7.1 The promotion test

`[OWNER, 2026-07-31]` The gate condition wrapping every trigger: the matter
**arose during loop work and cannot or should not be resolved in that
session**. Matters resolvable in-session resolve there and never enter a
register. Within that gate, the HOLD-centered trigger list `[CORPUS]`:

- a HOLD present, or at risk;
- scope clarification or missing information needed;
- a decision on alternatives needed from the owner, leadership, client, or
  third party;
- a need to change scope, schedule, budget, or key resources;
- an outstanding formal-approval concern at HOLD risk — `[OWNER,
  2026-07-31]` approval-readiness itself is loop and REVIEW business; the
  register carries only the concern that an approval is outstanding and
  blocking, never a queued approval task;
- lack of resources;
- an inter-discipline / cross-loop need that cannot be met before a HOLD
  occurs.

### 7.2 The NOTs

`[CORPUS + OWNER]` Not promoted: routine progress; ordinary work-graph and
dependency needs (they stay in loop surfaces and K-DEP registers); routine
judgment within scope; anything discoverable as ordinary work through the
loop's own instruments. A returned observation is not automatically an
Action Item — the triage owner's nine-domain scan dispositions it (ordinary
work in scope / durable Action Item / decision or approval need /
scope-change candidate / planning or checking matter / valid deferral with
trigger / evidence only / duplicate / rejected or already resolved). The
promotion contract must not turn every observation into backlog.

### 7.3 Closure disposition taxonomy

`RESOLVED_WITH_CHANGE` (cites the loop-side change) · `RESOLVED_BY_DECISION`
(cites the decision record) · `INFORMATIONAL_NO_ACTION` · `DUPLICATE` (cites
the surviving row) · `REJECTED` (with reason) · `SUPERSEDED_BY_SCOPE_CHANGE`
(via `ScaRef`) · `OBE` (with rationale). Closure never grants scope,
authority, approval, or lifecycle effect.

## 8. Assignment and authority (Q9)

### 8.1 RASCI with one hard constraint

`[GOVERNED]` K-AUTH-1. Agents may hold R, S, C, I. **A is human-only,
invariantly** — no register field, view, or report shows an agent as
accountable. Capability-invariant by design
(`docs/thesis/09_discussion.md` §9.3.5).

### 8.2 Decision-tier visibility

Every open row carries the judgment tier it waits on: ordinary execution /
Agent 1 within latitude / Agent 0 cross-manager / reserved human act — data
derived from the register level and needed disposition, not a workflow the
service enforces. Views never collapse all open matters into one owner-facing
approval queue (parent basis §6.3).

### 8.3 Escalation reuses the notice flow

"Transferred up, triaged, elevated when unresolvable" is the existing
parent-mediated rule in `AGENTS.md`. Registers add durable disposition under
that flow; `NoticeRef` ties rows to the notices that carried them
(`[FINDING F-13]` — this is also what makes measurement §18.1 computable).

### 8.4 Lateral visibility, fenced

Shared reads are allowed; the register is the sanctioned lateral-visibility
surface siblings otherwise lack — under schema-level conditions carried by
K-TM-3: rows contain claims, provenance, and disposition state, **no
directive fields**; reading never creates a duty outside a loop's own
adopted instruments; disposition authority stays with the register's loop; a
sibling who cares responds through its own parent. `[FINDING AF-7]`

### 8.5 Human-framework rules that do not transfer

`[CORPUS + SYNTHESIS]` The source's "communication occurs across all
channels" stands for humans, remains prohibited for agents (no sibling
messaging, no parent bypass); §8.4 is the substitute. The source's
inter-discipline NOT maps to the K-DEP fence (§5.5).

## 9. The service (Q8)

### 9.1 Deterministic operations (all of the service)

- **Scan**: harvest candidates from §5.1 surfaces and §5.2 markers into a
  derived, rebuildable, gitignored candidate inventory (D-GOV-01).
- **Views**: per-register and cross-register listings; open-by-tier;
  stale rows; closure-echo report; candidate-coverage report; every row
  labeled by authority class (authoritative / derived / observed / unknown /
  stale) in the practitioner-harness pattern.
- **Staleness and closure-echo checks** (§6.4, §6.5).
- **Validation**: schema conformance; referential checks (`ElevatedTo`
  resolves; `Disposition` present iff CLOSED; `EvidenceSha` matches);
  CSV↔summary-MD consistency; refuses objectively broken register writes;
  never judges content.

### 9.2 Scanner precision rules

`[FINDING F-7/F-8/F-9/RF-A]` rebuilt from measured false-positive sources:

- Scan targets are the **structured surfaces of §5.1 by filename/schema**,
  not free-text trees. This alone removes the token-flood problem
  (`[FINDING F-10]`).
- Exclusion set (declared in configuration, reported in every output):
  `domains/*/_Decomposition/**` generated corpora (`dispatch_briefs/`,
  `dispatch_outputs/`, `gate5_coverage/`, `source_review_html/`,
  `atom_review_html/`, `source_section_nodes/`), `*_pdf2md_work/` and
  `_Sources/` conversion trees, generated `.html` reports (scanned only via
  the §5.5 review-report rule), `docs/thesis/**`, `tools/**` test fixtures,
  and this PRD's own directory.
- Historical managed-run trees (`AgentRuns/SOW-*`) are **scanned only for**
  `NEEDS_HUMAN_RULING:`/`MISSING:`/`TM-CANDIDATE:` content and unreleased
  handoff blockers — never for template boilerplate (`[FINDING F-8]`
  resolves the Rev-1 contradiction: run records are inputs for escalation
  content; their scaffolded `## Open Questions` headings are not
  candidates).
- **Canonical-vs-copy dedup** `[FINDING RF-A]`: where a register or ledger
  is copied into `_Evaluation/` snapshot packages, the `_Coordination/`
  original is canonical; copies are reported once.
- `FAILED_INPUTS` and kin matched in value position only, never in enum
  prose (`[FINDING F-12]` held).
- Notice `TRACKED_OPEN` presented as open concern, never gating.
- No silent caps: whatever the scan skips, it says it skipped.

### 9.3 Judgment operations (none of the service)

Promotion, prioritization, disposition, closure, staleness resolution, and
escalation are acts of the owning loop's humans and managers, recorded in
the register by their actors. The service validates form, never makes the
call.

## 10. Candidate invariants (K-TM-*)

| ID | Candidate invariant |
|---|---|
| K-TM-1 | Task Management owns per-loop Action Item registers and nothing else. Every other domain's state is displayed by citation and remains with its owner |
| K-TM-2 | Registers are git-tracked files inside the owning loop's coordination surface. Any service store or index is a rebuildable, gitignored projection per D-GOV-01, never cited as authority. No engine-store exemption |
| K-TM-3 | Register writes are judgment acts of the owning loop. Rows carry no directives; no cross-loop register writes; reading a register creates no duty outside a loop's own adopted instruments; no agent appears as accountable (A) for any row (K-AUTH-1) |
| K-TM-4 | Graceful absence, re-scoped `[FINDING F-20]`: no act **outside a loop's own adopted instruments** may require a Task Management read or write. A loop binds itself by its own revocable ruling; deleting the service and its projections blocks nothing anywhere; registers remain plain readable, writable files. Kill test at every release (PEC-K-01 / PEC-SVC-004 pattern) |
| K-TM-5 | A register row, view, or scan output never constitutes approval, acceptance, scope, priority authority, or lifecycle effect. Closure evidence binds to bytes (`EvidenceSha`); a row whose evidence changed after closure is stale, not still-closed |
| K-TM-6 | Closure-capable schema: every register schema version carries `Status` and `Disposition`; a register that cannot record its own closure is invalid |

## 11. Interfaces (Q12, Q13)

### 11.1 File-native first

The primary interface is the filesystem: loop actors read and write their
own registers with ordinary file tools inside existing scopes. Not a
degraded mode — the contract (Q16).

### 11.2 CLI second

`taskmgmt` (scan / views / validate / staleness / echo), stdout markdown +
`--json-report`, practitioner-harness posture: reads authored files and git
history, reports facts with sources, refuses objectively broken register
writes, and none of its output is authority. No resident index until a
measured query-pain threshold is crossed (harness cache lesson,
`projects/pec/docs/PRD.md:474`).

### 11.3 Agent query

Agents read files or invoke the CLI read-only within declared tool scopes.
Pull-oriented, consumer-owned use (PEC-K-03 mirror): no push, no injection,
no polling. A daemon read route is `[OPEN]`, explicitly deferred behind
DEL-02-06 activation (`[FINDING, review §04]` — any runtime-side surface is
the longest path in the program).

### 11.4 The App Tasks module (Q12)

`[GOVERNED]` No Tasks module exists; the App's Work/Agents panel is
"projection, not authority" and may display task lists only from admitted
sources (App SPEC §17.4, PRD Principle 28, K-FS-1). `[SYNTHESIS]` The
initial Tasks module is precisely the adopted registers rendered as an
admitted-source projection — open items by tier, staleness and echo flags —
creating, approving, and assigning nothing. Routed through the App project's
own scope-change process after (and only after) the App loop adopts a
register by its own ruling (F-APP-5). This PRD grants the App nothing.

## 12. Integration without subsumption (Q11, Q17)

### 12.1 Decisions, approvals, changes, checking (Q11)

Rows link outward by citation (`RESOLVED_BY_DECISION` + decision ID;
approval concerns cite the human instrument; checking cites validator
output; `ScaRef` types the scope-change linkage). The corpus's
decision→change chain stays in the owning surfaces; the register displays it
by citation.

### 12.2 PEC

The seam, stated as decisions rather than left implicit `[FINDING, review
§04]`: Task Management registers are **git-tracked, authoritative, citable**
(N-1 substrate); PEC is a **gitignored, non-authoritative, never-citable
projection** (PEC-K-02/K-10). They are complementary trust tiers: an adopted
register becomes an admitted source PEC may index as paths/counts/states.
PEC's `CandidateBrief` ("work-selection queue") and PEC-ORI-001 parked-lanes
orientation remain PEC's — they orient toward work; the register
dispositions residue. **Adopting this PRD decides PEC PRD §16 open decision
1** (whether registers gain light structure at source) for the Action Item
register class specifically — this is presented to the owner as an explicit
effect of adoption, coordinated with the PEC loop by notice, not decided
silently. Neither product requires the other; both carry graceful absence,
each under its own invariant (PEC-K-01; K-TM-4) with the boundary that
PEC's kill test covers PEC and Task Management's covers Task Management.

### 12.3 Project controls

Schedule basis, estimation, and any future EVM remain with their owners;
the retired PEC v1 lookahead is not resurrected. `[CORPUS]` statusing
cadence enters only as §14's loop-entry binding.

### 12.4 Resource Governance (Q17)

Zero accepted paper exists; exclusion is by named clause: no locks, freezes,
budgets, capacity or utilization accounting, cost attribution, or forecast
monitoring, and no dependency on any future such service. If chartered, it
reads registers like any consumer.

### 12.5 Decision registers and Tier-0

The decision-register lane is the program's proven closure mechanism
`[MEASURED]` and is not displaced: owner rulings stay there; the D-T0
residual-work row convention remains Tier-0's ruled residue mechanism, and
**no Tier-0 register is created**. The scanner displays non-ruled rows as
their own class; a register row that needs an owner ruling routes to the
appropriate `_DECISIONS` register and closes `RESOLVED_BY_DECISION`.

### 12.6 Practitioner harness

The harness stays "not a control plane, not a task database"; `next` and
`bridge-status` remain its bench commands. Task Management owns registers
and the candidate scan; consolidation, if ever, is its own owner act.

### 12.7 Runtime

Run records are scan inputs per §9.2 and remain runtime-owned; Task
Management never writes `AgentRuns/` and never becomes a session-presence or
orchestration surface (D-GOV-20).

### 12.8 The reusable-work-surface gap (A-B-012)

`[FINDING, review §04]` Stated against the gap by name: a **disposition
ledger is not a work-discovery surface**. `[OWNER, 2026-07-31]` "Those
should be discovered via the development loop." Task Management does not
fill, claim, or imply the reusable program work surface; A-B-012 remains
deliberately open, to be filled only by its own PRD act if ever.

## 13. Availability and graceful absence (Q16)

By construction and K-TM-4: registers and tags are plain files; only derived
views degrade when the service is absent. Release gate: the kill test —
delete the service and all projections, run representative governed
workflows and register operations by hand, nothing blocks. The re-scoping of
K-TM-4 (loop-adopted duties are lawful) does not weaken the kill test: a
loop's adopted entry step reads a *file*, not the service.

## 14. The reader binding (replaces Rev 1 "gate hooks")

`[FINDING F-19/F-20/F-21]` Rev 1's checklist lines in agent files are
withdrawn — they cost ~11 agent-file edits plus notice fan-out, and they sat
in the self-cancelling pincer between K-TM-4 and the 29/30 outcome. The
counterweight that the evidence supports is **loop-entry binding**:

- A loop that adopts a register amends **its own** `LOOP_INIT.md` /
  workplan / receipt contract — one loop-owned file, one loop ruling — so
  that session entry reads open rows (the root loop's entry step already
  requires enumerating parked lanes; the register becomes the instrument
  that step reads) and session close records dispositions or receipts the
  residue.
- `[OWNER, Receipt 89, 2026-07-22]` The owner has explicitly refused a
  standing sweep obligation imposed from outside ("No, I explicitly do not
  want this…"). The binding is therefore never imposed: each loop adopts,
  amends, or declines by its own ruling, and per-run steering remains the
  lawful mechanism for the uncommon case.
- No agent instruction file changes at Stage A. Instruction-text adoption of
  the `TM-CANDIDATE:` grammar happens only under §15-lifecycle maintenance
  as files are touched (§5.2).

Residual, stated honestly `[FINDING F-6]`: binding to loop entry means rows
age while no session runs. Nothing in this product starts sessions; it makes
the aging visible and measurable (§18.3). That is the product's limit, not a
defect to design around.

## 15. Open data, export, recovery, migration (Q15)

CSV + Markdown, `RegisterSchemaVersion` per row; export is `cp`; recovery is
`git`; schema migration ships as a deterministic tool with the version bump.
`[CORPUS]` "Tools must serve the framework, not dictate it"; simpler open
tools "will enable agentic workflows with AI more easily."

## 16. Prioritization representation (Q10)

The register records stated priority and `PriorityBasis`. The service
computes no score, produces no ranking, never reorders by recency or volume.
Views may sort by stated priority and HOLD-proximity facts; the judgment
remains cited and human/manager-owned.

## 17. Users and staging (Q1) and smallest first release (Q14)

`[SYNTHESIS]`

- **Stage A (smallest useful release; one loop, zero agent-file changes):**
  the register standard (schema §6.3, naming §3.2) · the root-loop program
  register at `execution/_Coordination/_TaskManagement/`, minted by the
  adoption act · **seeded from the measured backlog** (~115 items: 29 open
  notices, the 07-28 review's §09 ranked actions and §08 held-open
  questions, horizon findings, D-45, open packet questions, TBD-register
  rows — each seeded row citing its source) · a first owner triage session
  dispositioning the seed · `taskmgmt scan/validate` v0 over §5.1 surfaces ·
  the root `LOOP_INIT` amendment binding entry to the register — all by
  owner ruling in the root loop's own instruments. Users: the owner and
  root-loop sessions.
- **Stage B:** the standard routed as coordination notices to the other
  loops; each adopts, amends, or declines by its own decision record on its
  own cadence (F-APP-5 / F-PIP-5 / D-PEC packet). Receipt-contract
  amendments where adopting loops choose them. Staleness and closure-echo
  reports.
- **Stage C:** App Tasks module projection (via App scope change, after App
  adoption) · `TM-CANDIDATE` grammar spreading under §15-lifecycle
  maintenance · any daemon route only behind DEL-02-06 activation.

Each stage separately owner-gated; nothing later is implied by adopting
earlier. `[FINDING, review §08 risk 2]` Stage A includes the first triage
session by design: a register seeded and not triaged opens at 0% closure —
indistinguishable from the notice ledger it answers.

## 18. Measurements (Q19)

1. **Disposition rate and latency** per register: Opened→Closed /
   Opened→LastReviewed ages; percent of rows with a disposition within one
   loop-entry cycle. (Not referential integrity alone `[FINDING F-21]`.)
2. **Acknowledgment closure**: notices out of `TRACKED_OPEN`, computable via
   `NoticeRef` — baseline 29/30 open (2026-07-28).
3. **Row aging while loops idle** (§14 residual, made visible): age
   distribution of OPEN rows vs. loop-session dates.
4. **Capture coverage gap**: scan candidates without register disposition —
   baseline 100% (~115 items, pre-seed).
5. **Closure echo count**: sources still showing open after disposition.
6. **Burden check (anti-metric)**: rows opened vs. closed per session;
   growth without disposition is §19.1, not success.

## 19. Falsification (Q20)

The thesis is falsified, and the register/service should be retired or
redesigned, if sustained evidence shows:

1. **Accumulation without disposition** — including the seed backlog: if
   the Stage-A register still holds its seed untriaged after the first two
   root-loop sessions, the product has reproduced the notice ledger.
2. **Bypass in practice**: concerns reach resolution through existing
   surfaces while adopted-loop registers sit unread at bound entry steps.
3. **Precision collapse**: scan output false-positive rate stays high
   enough after §9.2 that triage owners stop reading it.
4. **Coercion drift**: any act outside a loop's own adopted instruments
   comes to require a Task Management read/write (K-TM-4), or a loop's
   binding becomes irrevocable in practice.
5. **Authority drift**: a row or view cited as approval, scope, or
   lifecycle authority survives review (K-TM-5).
6. **Queue drift**: registers observed functioning as work-discovery
   backlogs for deliverable production (`[OWNER, 2026-07-31]` boundary) —
   the loop stopped discovering work through its own instruments.

## 20. Findings register

Rev-1 findings AF-1..AF-8 (parent-basis/addendum testing) stand as recorded
in Rev 1; AF-4's instrument identification is corrected by F-27's (the
gating rule is SPEC §1.2's tool-root registry, dissolved by not minting a
tool root). Architecture-review findings and dispositions:

| Finding | Disposition in Rev 2 |
|---|---|
| F-1 tiers without occupants (CRIT) | §6.1 per-loop registers; owners are loops, not roles |
| F-2 loops re-derive, distrust derivatives | §1/§6: register authoritative only for Action Item existence + disposition; all else cited |
| F-3 PEC split home (HIGH) | §6.1: register lives with the loop's standing surfaces |
| F-4 nine levels vs four tiers (HIGH) | §6.1: loops only; Tier-0 keeps its own convention |
| F-5 elevation-as-move vs K-WRITE-1 (CRIT) | §6.2 linked rows; no cross-loop writes |
| F-6 program triage = owner memory (HIGH) | §14 residual stated honestly; §18.3 measures it |
| F-7/F-8/F-9 exclusion set wrong (CRIT/HIGH) | §9.2 rebuilt from measured sources; run-record contradiction resolved |
| F-10 TBD is lawful token (CRIT) | §5.1 structured surfaces only; TBD signal only in disposition columns |
| F-11 signatures yield ~1/~1/0 (CRIT) | §5.1 sources rebuilt around actual live surfaces with measured loads |
| F-12 value-position rule holds | retained |
| F-13 no NoticeRef (HIGH) | §6.3 adds `NoticeRef`; §18.2 computable |
| F-14 no SHA binding (HIGH) | §6.3 `SourceSha`/`EvidenceSha`; K-TM-5 staleness rule |
| F-15 K-STALE-1 unavailable (MED) | §6.4 claims K-STALE-2 semantics only |
| F-16 RegisterSchemaVersion absent (MED) | §6.3 column 1 |
| F-17 dual-authoritative CSV+MD (HIGH) | §6.3 CSV authoritative; MD summary non-authoritative; validator checks consistency |
| F-18 SCA linkage untyped (LOW) | §6.3 `ScaRef` |
| F-19 checklist-line cost (CRIT) | §14 loop-entry binding; zero agent-file changes at Stage A |
| F-20 K-TM-4 pincer (HIGH) | K-TM-4 re-scoped: loop-adopted duties lawful; §13 kill test unchanged |
| F-21 register already failed as 29/30 (CRIT) | §1/§2/§14: the bound reader is the product's differentia; §19.1 fires if it isn't |
| F-22 HOLD registers, FINDINGS.csv unscanned (HIGH) | §5.1/§5.5 extended by name |
| F-23/F-24 review outputs tracked nowhere (HIGH) | §5.1 review-report source class; §17 seed backfill |
| F-25 `AI-` collision (HIGH) | §3.2 `TM-` identifiers |
| F-26 `taskmgmt`/`_TaskManagement` clean | retained |
| F-27 SPEC §1.2 / no writing agent (CRIT) | §6.1 no tool root minted; registers are `_Coordination/` subdirectories |
| F-28 no RETURN.md contract (CRIT) | §5.2 withdrawal; receipts + marker grammar instead; runtime standardization deferred to DEL-02-06 |
| F-29 scan_tbd_markers.py overclaimed (MED) | citation dropped; per-document mode only |
| F-30 "only by PRD act" over-cited (LOW) | §6.1/§23 cite OBJ-6 directly as the operative clause |
| RF-A derivative double-count | §9.2 canonical-vs-copy dedup |
| RF-B free-text flood | §5.1 per-document mode only |

## 21. Remaining open questions

| Q | Status |
|---|---|
| Field-level schema finalization | Working shape §6.3; finalize at decomposition inside this PRD's fences |
| Daemon read route | `[OPEN]` behind DEL-02-06 activation |
| PEC-loop register placement detail | `[OPEN]` with-loop-surfaces rule stated (§6.1); exact directory on PEC-loop adoption, by D-PEC packet |
| `TM-CANDIDATE` grammar finalization | `[OPEN]` fixed when first adopted into an instruction file under §15 lifecycle |
| Service placement (`tools/taskmgmt/`) | `[OPEN]` recommended at Root per harness precedent; confirm at decomposition |
| Whether receipt contracts gain a required residue field | `[OPEN]` per adopting loop's ruling |

## 22. Adjacent Root architecture question — fenced

The owner's separately expressed desire to eliminate required handoff-state
artifacts (parent basis §11) remains adjacent. This PRD gives session
residue a home and makes that future change more feasible; it does not amend
Root workflow doctrine, deprecate `HANDOFF_STATE.md`, or claim the change is
accepted. The scanner treats handoff records as inputs precisely because
they remain authoritative under current doctrine.

## 23. Adoption protocol and next sequence

1. Owner reviews Rev 2 and, if satisfied, adopts by explicit act naming:
   the PRD revision adopted; the K-TM-1..6 rows entering `docs/CONTRACT.md`;
   the root-loop register home under `execution/_Coordination/` (this is the
   OBJ-6 "new product function" act, cited as such); the root `LOOP_INIT`
   amendment; and the acknowledged side-effect that adoption decides PEC PRD
   §16 open decision 1 for the Action Item register class (§12.2).
2. Stage A executes in the root loop: seed, first triage session, tooling
   v0.
3. The standard routes as coordination notices to the other loops' surfaces
   (`AGENTS.md` notice rule); each loop adopts, amends, or declines by its
   own decision record. Per-loop registers exist only after per-loop
   rulings (F-APP-5, F-PIP-5, D-PEC packet).
4. Only after two loops run registers through real sessions: consider
   `SOFTWARE_DECOMP` for service tooling as a governed project, the App
   admitted-source projection via App scope change, and PEC reconciliation
   — each by its own gate.
5. Any instruction-file adoption of the marker grammar routes through
   HELPS_HUMANS under the component lifecycle, with the agent-index
   change-notice rule applied.

No project execution tree, package, deliverable, agent-instruction change,
loop-instrument change, tool, schema adoption, or implementation is created
by this record.

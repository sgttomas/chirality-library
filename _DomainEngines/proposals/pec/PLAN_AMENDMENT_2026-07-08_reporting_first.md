# PLAN AMENDMENT (DRAFT) — reporting-first re-orientation of the PEC standing plan

> **Epistemic status: agent-authored DRAFT amendment — NOT authority, for owner
> review.** Authored 2026-07-08. This document authorizes nothing: the adopted
> standing plan `_DomainEngines/pec/WORKPLAN_2026-07-08_pec_uiux_redesign.md`
> governs unchanged until the owner adopts this amendment (K-AUTH-1; D-GOV-04 —
> adoption is a human act). Its basis is the owner direction of record given
> in-session 2026-07-08 (quoted verbatim in §1) plus four owner clarification
> selections given the same day via structured question (§1). Per the owner's
> process selection ("Draft for review first"), the standing plan is untouched;
> §3 states the proposed edits as exact reviewable changes and §5 states how
> they land only on owner approval. Sources govern on any disagreement; every
> claim about existing capability cites its file/section.

---

## §1 The direction and the clarification rulings

**Owner direction of record (2026-07-08, in-session, Ryan Tufts, verbatim):**

> "Good.  Now My intention for this continuing development phase is to produce
> an effective reporting tool for project status, according to issues tracked
> at a package level and completeness tracked at a deliverable level.  I don't
> need this to be task management or planning or scheduling platform at this
> time.  It can possibly grow into those functions but to begin with I want to
> be able to upload documents that allow the issues and status to be updated,
> and the for the agent to produce reports (both standard reports and novel
> user-defined)."

**Owner clarification selections (2026-07-08, in-session, via structured
question — recorded as owner selections):**

1. **Plan tranches: "Defer both; keep F2 fix."** D-PEC-28 and D-PEC-28b move
   to a deferred (planning-phase) section. The fabricated-risk-score fix
   (design spec §12 F2) must ride an earlier tranche so no surface reports
   invented data. The Plan page is otherwise left as-is.
2. **Upload scope: "Agent-adaptive structured files."** Extend the existing
   proposal-gated import path (the D-PEC-08 / D-PEC-22 pattern): registers,
   MDLs, trackers in whatever structured schema they arrive; the agent maps
   them, the human accepts/applies. This selectively reactivates the postponed
   import lane for this purpose only.
3. **Reporting: "Exported files, drill-backed."** The agent composes reports
   as exportable documents (e.g. weekly project status, package issue summary,
   deliverable completeness/MDL status) from the same Explain-shaped server
   data; user-defined reports via a prompt to the agent; in-app viewing
   optional later.
4. **Process: "Draft for review first."** This document; the standing plan is
   untouched until the owner approves.

---

## §2 Alignment analysis — the adopted roadmap against reporting-first

Issues are tracked at package level and completeness at deliverable level
**already, server-side**: `packageDetailView.issues[]` (5-type union,
`server/src/services/views.ts:251-276`), `deliverableDetailView.openItems` +
`facts{}` (views.ts:419-454), MDL `deliverablesView` (views.ts:375-399). The
redesign roadmap mostly *serves* the new direction:

- **D-PEC-24 (design-system/a11y):** serves — every report-backing drill path
  must be keyboard-reachable and token-consistent (spec §2.4–2.5); foundation
  for all later surfaces. Also unblocks the `shared.tsx` sequence.
- **D-PEC-25 (drill spine):** serves directly — "drill-backed" reporting
  (clarification 3) is exactly the `<RecordRef>`/`refRoute` spine (spec §2.6);
  a report line that can be interrogated to its records depends on it.
- **D-PEC-26 (Admin operations console):** serves — the upload lane's
  accept/apply surface is Admin's proposals-first Import tab (spec §10);
  carries fix F3 (threshold garbage silently corrupts computed severity —
  spec §12), a factual-correctness obligation of the reporting value.
- **D-PEC-27 (Log → issue dashboard):** serves directly — issue awareness at
  package level; carries fix F1 (fabricated Age-0, spec §12) and the
  Explain-shaped `logSummaryView` (spec §11B P1) that the package issue
  summary report draws on.
- **D-PEC-29 (Packages/Deliverables linkage):** serves directly — the two
  levels the owner named; risks on deliverable detail (P6), package issue mix
  (P7).
- **D-PEC-30 (Registers consistency):** serves — registers are the drill
  targets reports resolve to; consistency and `?ref=` parity keep report
  drill-backs landing somewhere legible.
- **D-PEC-31 (Overview & My Week polish):** serves — Overview is the on-screen
  twin of the weekly project-status report (same `overviewView` basis,
  REPORT_BASIS.md "Overview KPIs").
- **Misaligned: D-PEC-28 (Plan control board) + D-PEC-28b (WBS view)** — both
  are planning-phase machinery the direction explicitly does not need now
  ("I don't need this to be task management or planning or scheduling
  platform at this time"). Deferred per clarification 1, not deleted.
- **Missing lanes:** document **upload** (agent-adaptive, proposal-gated —
  clarification 2) and **agent reporting** (standard + user-defined exported
  documents — clarification 3). Neither has a roadmap row today.

---

## §3 Proposed standing-plan edits (exact, reviewable)

All edits target `_DomainEngines/pec/WORKPLAN_2026-07-08_pec_uiux_redesign.md`.

### 3(a) New Owner-intent addendum — reporting-first north star

**Section:** "Owner intent", after the addendum ending *"…with
protocol/fences/gate carried unchanged, conflicts decided on the merits and
recorded, and each source tranche remaining future owner-ruled."*
**Current text:** none (addition).
**Proposed addition:**

> **Addendum (2026-07-08, owner direction of record — verbatim in the
> adopting receipt; this phase's north star):**
>
> > "Good.  Now My intention for this continuing development phase is to
> > produce an effective reporting tool for project status, according to
> > issues tracked at a package level and completeness tracked at a
> > deliverable level.  I don't need this to be task management or planning
> > or scheduling platform at this time.  It can possibly grow into those
> > functions but to begin with I want to be able to upload documents that
> > allow the issues and status to be updated, and the for the agent to
> > produce reports (both standard reports and novel user-defined)."
>
> With four same-day owner clarification selections: (1) defer D-PEC-28/28b,
> keep the F2 fix on an earlier tranche; (2) upload = agent-adaptive
> structured files via the proposal-gated D-PEC-08/22 pattern; (3) reporting
> = drill-backed exported documents from Explain-shaped server data,
> user-defined via agent prompt; (4) this landed as a reviewed amendment
> (`_DomainEngines/proposals/pec/PLAN_AMENDMENT_2026-07-08_reporting_first.md`).
> The UI/UX redesign continues **in service of** reporting-first: the drill
> spine, factual-correctness fixes, and package/deliverable surfaces are what
> make reports interrogable.

### 3(b) Receipt-51 reconciliation — recorded, not silent

**Section:** "Owner intent", the 2026-07-08 redesign addendum's closing
paragraph. **Current text (short quote):** *"D-PEC-14/15/19 stay postponed;
nothing here reopens import-refinement or the tracker edit path as
objectives."*
**Proposed addition immediately after that paragraph:**

> *Reconciliation note (2026-07-08):* the 2026-07-07 direction that
> "importing should be indefinitely postponed" (Receipt 51) is **selectively
> narrowed** by the newer 2026-07-08 reporting-first direction (a newer
> specific steer governs — LOOP_INIT §7, the D-PEC-23 precedent): the import
> lane reactivates **only** as the agent-adaptive, proposal-gated
> document-upload path (the D-PEC-08/D-PEC-22 pattern: agent maps → import
> proposal → human accept/apply; no direct writes). The D-PEC-14/15/19
> rulings otherwise stand — no live-evidence obligation reopens, the
> FILE_DROP_RUNBOOK v1.2 step-5 interim re-import rule stands, and the
> tracker stays import-owned/read-only.

### 3(c) Roadmap re-weight — D-PEC-28/28b to a Deferred section; slate item 4 answered

**Section:** "Roadmap" table. **Current text:** the two P1 rows beginning
*"| P1 | **D-PEC-28 · Plan → planning control board** |"* and
*"| P1 | **D-PEC-28b · Schedule WBS view (optional)** |"*.
**Proposed change:** delete both rows from the table and add, after the
table's sequencing-rationale paragraph, a new subsection:

> **Deferred (planning-phase) — owner clarification 1, 2026-07-08.**
> D-PEC-28 (Plan → planning control board) and D-PEC-28b (Schedule WBS view)
> are deferred, not deleted: the direction of record needs a reporting tool,
> not a planning/scheduling platform, "at this time." Their full scope stays
> specified in the T0 design spec (§8, §11B P5/P9/P10) and reactivates only
> by owner direction, as the last phase. The Plan page is otherwise left
> as-is, except fix F2, which is re-homed to **D-PEC-34** (below) so no
> surface reports invented data while D-PEC-28 sleeps. Spec projections P5
> and P9/P10 sleep with their packets; §3 M3.11 and §5 M5.8 cell-explains
> ("once D-PEC-28 lands") defer accordingly.

**Section:** "Open owner decisions" slate item 4. **Current text (short
quote):** *"4. **Plan schedule view (D-PEC-28b)** — pursue the read-first WBS
view from the imported schedule now, later, or not?"*
**Proposed replacement:**

> 4. **Plan schedule view (D-PEC-28b)** — ~~open~~ **ANSWERED 2026-07-08:
>    effectively ruled "defer"** by owner clarification 1 ("Defer both; keep
>    F2 fix") under the reporting-first direction; lives in the Deferred
>    (planning-phase) section.

### 3(d) F2 re-homing — new small packet D-PEC-34

**Section:** "Roadmap" table, new row (P0). Spec §12 assigns F2's fix-owner
to D-PEC-28; with 28 deferred, F2 needs its own minimal governable home:

> | P0 | **D-PEC-34 · Plan factual-correctness fix (F2) — minimal** | Raise-risk stops fabricating `probability: 4, impact: 3` (Plan.tsx:65): create call sends no scores unless a human enters them (nullable per core/src/types.ts:474-475); confirm drawer previews the week/discipline/load basis verbatim and says "may create"; duplicate-guard per spec §12 F2 acceptance via the existing `GET /api/projects/:pid/risks` (api.ts:275, already client-consumed at Registers.tsx:629 — read, not a fence write). No other Plan change. | `web/src/pages/Plan.tsx` | T0 | U | S |

**Rider (named, for adoption):** on adoption, the design spec
`projects/pec/execution/_Coordination/DESIGN_SPEC_2026-07-08_uiux_redesign.md`
§12 F2 **fix-owner cell** needs a dated pointer edit (D-PEC-28 → D-PEC-34,
citing this amendment) via its own branch+PR — the spec is a governed
coordination artifact and is not edited by this proposal.

### 3(e) Two new roadmap lanes — upload and reporting

**Section:** "Roadmap" table, new rows (new phase tag **PR**,
reporting-first). Honest inventory first — what already exists vs what's new:

- **Exists:** the proposal-gated import seam end-to-end — §16 contracts + the
  tracker contract (D-PEC-13), in-app `import_proposal` with dry-run +
  hash-bound owner accept/apply (D-PEC-12; register rows D-PEC-08/12/13), the
  per-drop mapping loop and standing rules (`IMPORT_TEMPLATES/
  FILE_DROP_RUNBOOK.md` steps 1–5, incl. "never silently guessed"), the
  embedded upload agent (D-PEC-08 tranche), the sidecar agent with bounded
  acts + agentic turn loop (D-PEC-21, RULED O-A 2026-07-07) + session
  profiles (D-PEC-22), read acts over RBAC'd GETs (D-PEC-20), and existing
  report surfaces: register CSV exports, sponsor brief, package pack
  (REPORT_BASIS.md).
- **New:** schema-**adaptive** mapping of arbitrary structured
  register/MDL/tracker files (beyond the already-mapped owner workbook
  shapes) as first-class agent behavior; and agent-**composed** exportable
  report documents (standard set + user-defined), which no surface produces
  today.

> | PR | **D-PEC-35 · Upload lane — agent-adaptive structured-file ingestion** | Extend D-PEC-08/22: agent accepts registers/MDLs/trackers in arbitrary structured schemas (CSV/XLSX-derived/tabular), proposes a schema mapping to the §16/tracker contracts (extending `IMPORT_MAPPING.md` per FILE_DROP_RUNBOOK step 2), files an import proposal; human accept/apply always; **no direct writes, ever**; unmappable rows are questions or rejects with reasons, never guesses. Runbook rules (RV-7 approval-follows-proposal, v1.2 step-5 re-import interim rule) carry unchanged | `projects/pec/agent-sidecar/**`, `execution/_Coordination/IMPORT_TEMPLATES/**`; `server/src/api.ts` only if a new upload endpoint is needed (else none) | D-PEC-08/22 (landed); D-PEC-26 improves the accept/apply surface but is not a hard dep | S | M |
> | PR | **D-PEC-36 · Reporting lane — standard report set** | Agent composes drill-backed **exported documents** from Explain-shaped server data (E-rows + P1/P7/P6 as landed): weekly project status (overviewView basis), package issue summary (packageDetailView.issues[] / logSummaryView), deliverable completeness/MDL status (deliverablesView + openItems/facts) — the owner's three named examples. Every figure carries its rule-id/register basis per REPORT_BASIS.md ("names its basis by pointer"); **factual-or-absent** — reports contain only what records support; export-what-is-displayed / no-invented-data guarantees apply; export format/egress stays inside the profile's ruled `data_residency` basis (F-PEC-3) | `projects/pec/agent-sidecar/**`; `server/src/services/views.ts` + `server/src/api.ts` only for named read-only report payloads | D-PEC-25 (drill-backs); D-PEC-27 enriches the issue summary (soft) | S | M |
> | PR | **D-PEC-37 · Reporting lane — user-defined reports** | Novel reports via a prompt to the agent (the D-PEC-21 agentic-turn-loop vehicle, already RULED O-A: read acts → compose → export); same factual-or-absent constraint — a figure the records don't support is absent and said to be absent, never synthesized; in-app viewing of reports is explicitly **optional later**, not in scope | `projects/pec/agent-sidecar/**` | D-PEC-36 (report composition conventions), D-PEC-21 (landed) | S+O (any new export egress route is an owner call) | M |

Each row lands, like every other roadmap row, as its own owner-ruled D-PEC
packet with an exact fence, verification plan, and rollback — the table is
candidate scope only.

### 3(f) Re-stated default sequence

**Section:** "Sequencing rationale" paragraph. **Current text (short
quote):** *"The owner's three named pains (Admin, Log, Plan) come next as
P0/P1."* **Proposed replacement paragraph (whole):**

> **Sequencing rationale (reporting-first).** Default order:
> **24 → 25 → 27 → 29 → 26 → 30/31 → upload/reporting lanes (35/36/37) as
> their packets are ruled → deferred planning phase (28/28b) last**, with
> **D-PEC-34** riding early in parallel (Plan.tsx only — no `shared.tsx`
> contention) so no surface reports invented data. 24/25 stay first as
> force-multipliers; 27 and 29 rise because issues-at-package-level and
> completeness-at-deliverable-level are the direction's two named axes; 26
> follows (Admin is the upload lane's accept/apply surface and carries F3);
> 30/31 inherit the spine cheaply and polish the report drill targets. The
> `shared.tsx` constraint is unchanged: tranches touching it (24/25/27/29/30)
> run sequentially, never in parallel. P3 (32/33) remains owner-gated where
> it sits; F1 stays on 27, F3 on 26, F2 on 34. Each tranche is independently
> shippable behind its own PR; the peer proposal's regression-evidence pass
> rides every tranche as the step-4 visual check rather than landing as a
> separate tranche.

### 3(g) "Grows into, later" note

**Section:** after "Design principles" item 6 (or as a dated note at the end
of that list). **Current text:** none (addition):

> *Scope note (2026-07-08 direction):* task management, planning, and
> scheduling functions are **explicitly out of scope for this phase**. The
> owner's direction allows that the tool "can possibly grow into those
> functions" — that growth is a possible future phase behind its own owner
> direction, and principle 6 ("Dashboards, not task managers") governs until
> then.

---

## §4 What does NOT change

- The loop protocol (steps 0–5), branch-first + PR, never self-merge, the
  receipt discipline.
- Fences **F-PEC-1..4** and the redesign-phase corollaries verbatim —
  including zero new runtime/web dependencies (ADR-002), no egress beyond the
  ruled `data_residency` basis, computed status never hand-settable.
- The **owner gate**: every new row (34/35/36/37) is a future owner-ruled
  D-PEC packet; this amendment authorizes no source work.
- Session model conventions (LOOP_INIT §7 application) and the Opus-salvage
  fallback.
- Slate items **1, 2, 3, 5, 6 remain open** exactly as written; only item 4
  is marked answered (§3(c)).
- D-PEC-14/15/19 stay indefinitely postponed (§3(b)); D-PEC-21/22/23 rulings
  stand as their registers record them.
- The T0 design spec remains the design authority for 24–33; §12 F1/F3
  fix-owners unchanged.

## §5 On-adoption mechanics (only if the owner approves)

1. **Amendment PR:** apply §3(a)–(g) to
   `_DomainEngines/pec/WORKPLAN_2026-07-08_pec_uiux_redesign.md` on a branch,
   PR citing this proposal by path; owner merges (F-PEC-4 permits the write;
   adoption is the owner's merge + direction).
2. **Receipt:** the closing receipt in `_DomainEngines/pec/LOOP_RECEIPTS.md`
   records the 2026-07-08 direction **verbatim** and the four clarification
   selections as gate outcomes.
3. **Spec rider PR:** separate small PR adding the dated §12 F2 fix-owner
   pointer (D-PEC-28 → D-PEC-34) to the design spec, citing this amendment
   (§3(d) rider).
4. **Slate item 4** marked answered in the plan (rides the amendment PR).
5. Subsequent work proceeds by the §3(f) sequence, each tranche as its own
   D-PEC packet at the owner's gate. If the owner amends any selection during
   review, this draft is revised — it is provenance, not authority.

---

## §6 Tensions noted for the owner's read (beyond Receipt-51)

- **F2 acceptance vs the minimal fence — RESOLVED 2026-07-08 (live-tree
  check).** `GET /api/projects/:pid/risks` already exists
  (`server/src/api.ts:275` → `riskRegisterView`, `views.ts:614`) and is
  already consumed client-side (`Registers.tsx:629`); fences bound writes,
  not reads, so the duplicate-guard is implementable in full within the
  `Plan.tsx`-only fence. No widening, no narrowed acceptance.
- **Report egress vs F-PEC-3/residency.** Exported report *files* carry
  instance content out of the app; the current basis is demo/scratch
  (D-T0-20 enumerated OPEN surface; D-PEC-12 CLOSED-residency report
  visibility). Any report export beyond the ruled `data_residency` basis is
  its own owner decision — D-PEC-36/37 must state their egress basis.
  *Resolution path: an owner act; the natural gate is each packet's ruling
  (the packet states its basis and the owner rules on it there) — nothing is
  gained by ruling before the packet exists, unless the owner wishes to
  pre-rule the basis now.*
- **Agent act budget.** D-PEC-21's loop is bounded (8 acts/turn); composing a
  multi-register report may strain it. If so, raising the budget is a
  D-PEC-21-shaped follow-up ruling, not a silent change.
  *Resolution path: empirical — through implementation. Measured during
  D-PEC-36's build; only if a real report strains the budget does a small
  follow-up ruling raise the knob. Deciding now would be guessing.*
- **Weekly re-import friction stands.** D-PEC-15 stays postponed, so the
  v1.2 step-5 interim rule (dispositioned rows re-land as NEW intake) applies
  to any weekly upload cadence D-PEC-35 enables — a live cost the owner
  accepted 2026-07-07 that reporting-first will now exercise more often.
  *Resolution path: remains until it rises in significance — the resolution
  is un-postponing D-PEC-15, purely an owner ruling available any time; the
  cost is visible (intake churn), reversible, and worth deciding only once
  weekly uploads are actually routine.*

*End of draft. Nothing above is in force until the owner adopts it.*

# PEC product-direction interview — findings and requirements of record

> **Epistemic status: agent-authored provenance record — not authority.**
> Authored 2026-07-09 at owner direction (Ryan Tufts, K-AUTH-1) from the
> 2026-07-08 product-direction interview conducted with the owner. Owner
> statements quoted are verbatim from that session; everything else is the
> interviewing agent's synthesis and is only as good as its citations. The
> receipt-level anchor is `_DomainEngines/pec/LOOP_RECEIPTS.md` Receipt 69
> (which applied these findings as execution riders on D-PEC-30/31/35/36/37)
> and Receipt 70 (which records this document's authoring). This document is
> the **detail home** the reporting-product workplan points to; future D-PEC
> packets cite it instead of re-deriving the requirements. It authorizes no
> work: owner rulings on numbered D-PEC packets do (D-GOV-04).

## 1. Context

PEC is demo software the owner is preparing for a client; the client contact
is a Project Director. The interview elaborated the Receipt-60 reporting-first
intent ("an effective reporting tool for project status, according to issues
tracked at a package level and completeness tracked at a deliverable level")
into a concrete operating model, a concrete recurring deliverable, and
concrete data semantics. The prior sponsor brief and package weekly-review
pack were, in the owner's words, "useful carrots to build the scaffolding" —
they are not the product's real reporting output.

## 2. Operating model — the PE/PD pair

- **Project Engineer (PE)** — the owner's seat. Responsible for data upload
  and preparing the reporting. All data is collected by humans and vetted by
  the PE before it reaches PEC. Verbatim: *"The data is collected by humans
  and vetted, then provided to PEC / the agent for processing and updating
  and maintaining the database."*
- **The in-app agent (sidecar)** — processes uploads, maintains the database,
  and resolves **application-level** issues ("the kind that affect the
  application not the kind surfaced in the project") interactively with the
  PE. It also drafts the periodic reports, which the PE vets. Verbatim on
  responsiveness: the agent *"should respond when in-app tools catch errors.
  Or at the behest of the user,"* and its responses to caught matters are
  *"either automatically or in response to the human (configurable)."*
- **The Admin panel** is the manual fallback, not the primary lane. Verbatim:
  *"Admin panel is optional manual way if the agent is not available, wanted,
  or the matter has become so routine that it isn't needed."*
- **Project Director (PD)** — consumes only. Verbatim: *"The project director
  (PD) just uses this app as the interface to receive the information and
  have the ability to drill down into matters as they see fit."*
- **Reports live outside the app.** Verbatim: *"The report lives outside this
  app in terms of the workflow. It may be saved in the app as a convenience,
  but it will be issued and edited outside of this app by the PE."*

## 3. The recurring deliverable — the discipline status report

The owner provided a real example report,
`2026-07-08-Disciplines_Status_Report.docx` (owner-held; per the D-PEC-01
convention its content belongs in gitignored `projects/pec/pilot-scratch/`,
not this repo — this section records only its structure). The owner's framing:
*"This isn't perfect, but the headings and contents are reasonably close."*

**Cadence and scope:** weekly, organized **by discipline** (not by package).
Monthly is not a distinct report type — verbatim: *"The 'monthly' report will
be any aggregate of any number of weeks more than 1. It will be PE's job to
edit it after the fact to be more precise in naming it or declaring what it
covers."*

**Structure** (Word styles observed in the example): one `Heading1` per
discipline (the example uses Process, Mechanical, Civil & Structural, Piping,
Instrumentation, Electrical, Controls), each with four `Subtitle` sections and
`ListParagraph` bullet prose:

| Section | Content pattern | PEC data mapping |
|---|---|---|
| **Activities** | In-work deliverables grouped by kind/purpose ("IFR process deliverables", "studies/calculations"), each named with its **% complete** in parentheses | Deliverables in work for the discipline, grouped by the existing deliverable-**type** column, with the PE-attested % complete (§4.2) |
| **Issuances this week** | Documents issued in the period, or "None." | Issue events recorded within the report's covered period |
| **Needs** | What the discipline is waiting on: client inputs, other disciplines, decisions required, resources | Open items where the discipline is the requester, **triaged internal vs client** (§4.4) |
| **Risks** | Open risk items in prose | Open risk-register entries for the discipline |

**Format:** a template-conformant `.docx` the PE hand-edits before issuing.
Generating the draft from PEC data is in scope; editing and issuing are not.
On prose quality the owner's bar for now: *"getting the prose right at a basic
level is easy, while the nuance you're indicating requires more effort and
scrutiny"* — and on presentation: *"Clarity is not just volumes of prose, it's
saying things the right way and formatting or portraying them in a fitting
manner."*

## 4. Data semantics of record

### 4.1 Reporting periods — declared per uploaded document

Verbatim: *"I will need to specify the dates being covered when I upload
data,"* refined to: *"it should be per document uploaded."* Every uploaded
document individually declares the date range it covers. Overlaps, gaps, and
retroactive corrections are **not** schema conditions to prevent — they are
conditions the in-app tools should catch and the agent should resolve with the
PE (§2). Period boundaries are what make "issuances this week" and
week-over-week % deltas derivable.

### 4.2 % complete — PE-attested source data, not a derived status

Verbatim: *"% complete is derived from rules of credit based on how far a
specific document has progressed through its development lifecycle for that
particular phase of the project. It is data collected by the PE."* And: *"the
MDL column will hold an integer number between 0 and 100."*

Classification (reconciliation recorded in the workplan): % complete is a
**PE-attested fact arriving as import data**, computed outside the app from
externally maintained rules of credit. It is not an in-app derivation and no
future tranche should "fix" it into one. The rules-of-credit table stays
external — verbatim: *"The rules of credit are maintained outside of this app
and don't need to be portrayed here, but I may add it later, though they would
perform no function except to help in reporting purposes."*

**Rollup rule:** no hours estimates exist yet, so package-level weighted
rollup is not possible. Within a discipline, verbatim: *"the % complete for
each document within a document kind will contribute an equal proportion
depending on the number of documents of that kind"* — where "document kind"
**is the existing deliverable-type column** (owner confirmed; "kind" and
"type" were used interchangeably).

### 4.3 Status vocabulary and the MDL↔RAIL consistency rule

"On hold" will appear as **both** an MDL status and a RAIL issue. Verbatim:
*"'on hold' will be a status in the MDL and an issue raised in the RAIL. Both
will report. Discrepancies between the two should flag a review by the agent
and a report to the human."* Ruled refinement: *"there should be tools that
intake/triage machinery catches. Then the agent can respond to that matter,
either automatically or in response to the human (configurable)."* The full
status vocabulary arrives with the revised templates (§6).

### 4.4 Needs typing

Verbatim: *"Needs will be triaged into 'internal' and 'client'."*

### 4.5 Reporting vocabulary of "issues"

The owner's working reporting vocabulary: *"We track 'issues' (action items
and risks) by package, and status (in progress, on hold, complete, etc.) with
a % complete."* This is narrower than the app's ADR-011 five-type package
union (holds, interfaces, decisions, risks, actions). Reconciliation recorded
in the workplan: this is a **display/reporting-vocabulary decision**, not a
cockpit re-litigation — holds, decisions, risks, and actions all arrive
through the RAIL and MDL the owner uploads; package interfaces arrive as a
separately maintained, periodically uploaded document.

## 5. The first-class discipline view

Owner direction: *"Yes. Create a first-class discipline view too,"* shaped as
the live, drillable mirror of the weekly report (the owner: *"Oh, that's a
great idea"*), with *"some additional dashboardy type metrics (only derived
ones, and the most grounded in that perspective of the project)."*

Per discipline: the four report sections (§3) plus a metric band the owner
endorsed as roughly complete ("Those are good, and I don't think I would give
many more than that"):

1. % complete by deliverable kind (the §4.2 equal-weight rollup), with
   week-over-week delta;
2. Issuances — this period's count plus next period's forecast from due dates;
3. Needs aging, split internal vs client, oldest first;
4. Open risks count, newly-raised-this-period flagged;
5. "Stalled" deliverables — in work with no % movement across N periods.

General sorting posture, verbatim: *"The tool should allow for proportionately
comprehensive flexibility in how to sort and organize the information."*

## 6. Owner-provided prerequisites (the blocking inputs)

| Input | Status at authoring | Blocks |
|---|---|---|
| **Revised MDL + RAIL templates** (XLSX; carry % complete 0–100, full status vocabulary, coverage-date declaration) | Owner has made them; not yet provided. Verbatim: *"I have made new versions of the RAIL and MDL that I need to provide before you can make progress fully in this area."* | Contract v2; % complete ingestion; status vocabulary; the D-PEC-35 XLSX follow-on; consistency checks |
| **Rules-of-credit table** | Later, optional; reporting explanation only (§4.2) | Nothing hard |
| **Interfaces document format** | Maintained and periodically uploaded by the owner; format not yet provided | Interfaces import contract |
| **Discipline report template** | Provided 2026-07-08 (structure in §3); the file itself is owner-held / pilot-scratch | `.docx` conformance work needs the file accessible at execution time |

The owner's source files are XLSX workbooks (`mdl.xlsx`, `rail.xlsx`,
`risk.xlsx`, `tracker.xlsx` — the pilot-scratch originals), which is why the
D-PEC-35 rider names XLSX parsing as the expected follow-on once the revised
templates arrive.

## 7. Gap analysis — interview needs vs the tree at authoring

Status-shaped by design; this section lives here and never in the workplan.
Verified against the live tree on 2026-07-09 (post-D-PEC-38, post-Receipt-69).

1. **No reporting-period concept.** Imports are stateless snapshots; nothing
   stores per-document coverage declarations or period snapshots. D-PEC-38's
   "reporting foundation" was drill/factual/a11y closeout, not periods
   (Receipt 69 gate outcome states no period/snapshot model was built).
2. **No % complete field.** The §16 MDL contract has no such column. Blocked
   on the revised templates.
3. **No discipline rollup.** All rollups are package-centric; discipline is a
   filter/column on the MDL register and a capacity dimension on Plan.
4. **No `.docx` generation.** Existing report outputs are print-HTML
   (sponsor brief, package pack — which the owner will not use) and, once
   D-PEC-36 executes, JSON/Markdown-style payloads.
5. **No internal/client typing** on work items, holds, or any "needs"-shaped
   record.
6. **No interfaces import contract.** Import contracts exist for MDL, RAIL,
   decisions, risks, schedule, tracker; interfaces have export only.
7. **No MDL↔RAIL consistency checks** in intake/triage, and no configurable
   agent auto-response policy for caught conditions.
8. **Vocabulary drift.** Register/report surfaces speak the ADR-011 union;
   the owner's client-facing vocabulary is §4.5's. Display-layer decision.

Adjacent-and-ruled (not gaps): D-PEC-35 (CSV/TSV upload lane, interim),
D-PEC-36 (standard reports with the discipline-grouping rider), D-PEC-37
(user-defined reports, gated on 36) — see Receipt 69 for the riders and
rejection rationale of each O-B.

## 8. Priority posture the owner expressed

Development is proceeding on many fronts; the owner prefers a basically-right
foundation now over nuance requiring scrutiny (§3 verbatim). Report
correctness values already standing (factual-or-absent, drill-backed basis,
REPORT_BASIS.md conventions) apply to everything above; nothing in these
findings relaxes them.

# CANDIDATE development plan — PEC UI/UX redesign (standing-plan successor)

> **Epistemic status: agent-authored CANDIDATE — not adopted, not authority.**
> Prepared 2026-07-08 by the PEC work loop at owner direction (Ryan Tufts,
> K-AUTH-1). Adoption is the owner's act (K-AUTH-1; D-GOV-04) — this plan
> authorizes nothing. It is offered to **fill the role of the standing plan**
> (LOOP_INIT §2) for the redesign phase: it carries new owner intent + a
> roadmap; it inherits the loop **protocol, fences F-PEC-1..4, and gate**
> unchanged from `WORKPLAN_2026-07-04_pec_loop.md` and `LOOP_INIT.md`. On owner
> adoption it can be promoted into `_DomainEngines/pec/` as the newest
> `WORKPLAN_*.md` (the file the loop reads as its standing plan, LOOP_INIT §2).
> Every factual claim below cites the live tree at authoring; sources govern on
> any disagreement. The per-tranche source work is NOT authorized here — each
> roadmap item lands as its own owner-ruled D-PEC source-tranche (the D-PEC-08 /
> D-PEC-17 / D-PEC-23 precedent).

## Owner intent (this run, verbatim — the new north star)

Owner launcher steer, 2026-07-08 (Ryan Tufts, verbatim):

> "The demo application is now over the minimum viable threshold. There remains
> lots of poor UI and UX design choices, particularly the Admin page. The
> Packages and Deliverables are well linked but it's not clear if the issues
> are. The Action & Hold Log has a good schema but isn't a well designed page it
> is a terrible task management interface - for now it should just be a good
> dashboard with comprehensive tools and an intuitive and contemporary
> interface. The Plan page has some good ideas but is a very poor implementation
> and needs to be redesigned to be an effective UI that utilizes the best
> practices and known patterns in this domain."
>
> "This is a planning phase not implementation. The result of your work after
> completing all your assessments and redesigning is a new development plan for
> PEC, to fill the role of the 'standing plan' in terms of this init prompt."

### Priority delta this steer creates (recorded, not silently applied)

Receipt 51 (2026-07-07) postponed **interface/UI refinement indefinitely**
("future refinement of the interface and importing should be indefinitely
postponed") and set the standing value: *"simplify workflows and reinforce only
reporting on what is factual and has a clear basis."* This run's steer is a
**newer, specific owner direction that reactivates UI/UX work as a planning
effort** — LOOP_INIT §7 makes a per-run steer govern on top of the plan, exactly
as the D-PEC-23 steer governed over the same postponement. So:

- The reactivation is lawful and directed. The postponed **D-PEC-14/15/19 stay
  postponed** — nothing here reopens import-refinement or the tracker edit path.
- This redesign is **not feature-expansion**; it is squarely in service of the
  standing value. Its through-line is *clarity and factual, drill-to-source
  reporting* — restoring the app's computed-from-records honesty where the UI
  currently hides or breaks it, fixing values that are shown wrongly, and
  refusing to invent anything not derivable from records (no critical-path, no
  fabricated risk scores). The Log becomes **a dashboard, not a heavier task
  manager** — exactly the owner's framing.

## How this plan works as the standing plan

This document supplies **owner intent + a phased roadmap**. It does **not**
restate or replace the loop mechanics. Inherited unchanged:

- **Protocol** — the 6-step loop (Discover → Select → Brief/slate → Gate →
  Execute+check → Receipt) from `WORKPLAN_2026-07-04_pec_loop.md` §"The loop
  protocol"; state is re-derived each iteration; closeouts append to
  `LOOP_RECEIPTS.md`.
- **Fences F-PEC-1..4** — unchanged. Note the operative consequence: **F-PEC-1
  forbids `web/**`, `server/**`, `core/**` writes by default.** Every redesign
  tranche below therefore requires its **own owner-ruled D-PEC source-tranche
  authorization** that names an exact file fence before any code is written —
  the same mechanism that authorized D-PEC-08 (upload agent), D-PEC-17 (agent
  UI), and D-PEC-23 (schema-fit). This plan proposes those tranches; it does not
  pre-authorize them.
- **Gate (§6)** — adoption/ruling/direction are the owner's acts. This plan is a
  CANDIDATE; the owner adopts/declines/amends (see the decision slate at the
  end).
- **Standing constraints** — **zero new runtime/web dependencies** (ADR-002,
  F-PEC-3): everything below is buildable with React 18 + Vite + react-router +
  the single hand-written `styles.css` + inline SVG. **No charting library, no
  component library, no CSS framework.** Any proposed dependency is an explicit,
  costly owner decision — this plan takes none. Status stays computed from
  records, never hand-set (F-PEC-2, I-4).

Provenance of the assessment: a source-grounded multi-agent pass (8 surfaces
assessed, adversarially verified against `file:line`, plus contemporary-pattern
research), reconciled against the loop operator's own direct reads of
`main.tsx`, `shared.tsx`, `styles.css`, `Admin.tsx`, `LogHome.tsx`, `Plan.tsx`,
`Packages.tsx`, and `server/src/services/views.ts`. The 69 verified defects are
tabulated in Appendix A.

---

## 1. Diagnosis — one root cause under most of the pain

PEC's signature strength is **"one record system, many lenses" with computed
status that always drills to its contributing records** (principle I-4): every
health badge, KPI, and signal opens an *explain drawer* that lists the records
behind the number and lets you click through to their source. The drill
primitive already exists and works — `refRoute()` in `shared.tsx:47-60` maps any
record ref to its home with a `?ref=` deep-link, `useHighlightRef()` reads it
back, and `.row-flash` lands it.

**The dominant finding across every surface: that spine is unwired or broken
wherever it matters most, and where it is wired it is keyboard-inaccessible.**

- The Package **issues cockpit** — the exact "are issues linked?" surface the
  owner flagged — uses a hand-rolled `issueHref` (`Packages.tsx:79-83`) that
  routes **decisions and risks to `/log`** (a page that structurally cannot list
  them — a dead-end) and **interfaces to the wrong register tab**, never
  appending `?ref=`. `refRoute` is ignored. *(verified CONFIRMED/critical)*
- The **Action & Hold Log** open-items table passes no `onRowClick`
  (`LogHome.tsx:158`) — every row is a dead-end. My Week's "Waiting on others"
  and Notifications, the Deliverable detail's holds/decisions/approvals, "Needs
  the lead this week", the Plan's deliverable doc-nos, and the Registers'
  reference cells are all **inert text** despite `refRoute` resolving their
  types.
- The clickable elements that *do* exist are **mouse-only**: `KpiCard` is a
  `<div onClick>`, register rows are `<tr onClick>`, the explain drawer's refs
  are hrefless `<a className="reflink">` — none focusable or keyboard-operable
  (`shared.tsx:129-131,166,313-314`). The mandated drill mechanism is
  unreachable by keyboard/AT on every page. *(verified CONFIRMED/critical, a11y)*

Three **factual-correctness** defects compound it — these directly violate the
owner's standing "report only what is factual" value and are the cheapest wins:

1. **Every open interface shows Age 0** and, because the Log sorts by age-desc,
   genuinely old interfaces are mislabeled brand-new and sink to the bottom
   (`views.ts:531,556`).
2. **Plan "raise risk" fabricates** probability 4 × impact 3 and canned text on
   one un-confirmed click, and repeat clicks create duplicate Risks (no dedup)
   (`Plan.tsx:58-71`; `registers.ts:36-58`).
3. **The thresholds editor accepts warn > escalate and negatives** with no
   validation in the client *or* the server PUT, silently corrupting every
   computed severity downstream (`Admin.tsx:439-445`; `api.ts:400-429`).

The good news is a **feasibility gift**: because the server already composes the
data (the package `issues[]` cockpit at `views.ts:251-330`, deliverable
`openItems` at `views.ts:419-439`, `capacityView.planItemIds`, the schedule WBS
rows), **most of the highest-value redesign is UI re-wiring and re-composition
of existing components — zero new dependencies, little or no new server work.**
A minority needs read-side server changes; a smaller minority needs schema
migration; a few items are genuine owner decisions (see the data-readiness tiers
in §4 and the slate in §7).

## 2. Vision

> PEC should read as **one honest instrument**: every surface answers its own
> headline question at a glance, every number is interrogable to the records
> that produced it, and every reference is one accessible click from its source.
> The redesign adds no invented data and no task-manager machinery — it makes
> what is already computed *legible, navigable, and trustworthy*, in light and
> dark, by mouse and keyboard.

## 3. Design principles (govern every tranche)

1. **Drill or it doesn't ship.** Every badge, KPI, aging bar, and record ref is
   click-to-explain and/or routes through `refRoute` to its source. A `title`
   tooltip is never a substitute for the explain drawer (I-4).
2. **Compute on the server, render on the web.** No new rollups, thresholds, or
   status in React (SPEC §1). New aggregates are server views emitting the
   existing `Explain` shape `{value, ruleId, detail, contributing[]}`.
3. **Factual or absent.** Show only what records support. No fabricated scores,
   no critical path (PEC imports WBS parentage but no logic links), no
   hand-settable computed values (F-PEC-2, I-4). Fix values shown wrongly first.
4. **Re-compose, don't re-import.** Build from the existing vocabulary — cards,
   `KpiCard`, `HealthBadge`, `Drawer`, `RegisterTable`, badges/state/itype tags,
   `WorkflowStages` — plus tiny hand-rolled inline-SVG marks. Zero new deps.
5. **Accessible by construction.** Real `<button>`/`<a href>` for actions,
   `:focus-visible` rings, `role`/`aria` on dialogs and tablists, keyboard
   operability, AA contrast. The drill spine must be reachable without a mouse.
6. **Dashboards, not task managers.** Monitoring surfaces (Log, Overview,
   package cockpit, Plan) summarize "what is off-plan / falling through" first;
   they never grow drag-to-mutate boards, editable status, or bulk state edits.
7. **Theming through tokens only.** All color flows through a two-tier token
   layer (primitive palette + semantic roles); dark mode swaps semantic tokens,
   never per-component hex.
8. **Preserve the guarantees.** Export-what-is-displayed, verbatim intake
   statements (OM-3), unanchored-stays-visible (I-2), append-only history — a
   redesign never regresses these.

## 4. Data-readiness tiers (honest cost basis for sequencing)

- **Tier U — UI only (zero new deps, no server change).** Drill-to-source
  re-wiring; accessible interaction + focus rings; token layer + dark mode;
  Admin sub-nav + importer consolidation + threshold grouping (display) + rename
  People; Plan pickers, rollups, legend, sticky column, wiring the *existing*
  PUT for plan-item edit, confirm-before-raise-risk; Log client-side group-by +
  quick-view URL presets + color-typed rows.
- **Tier S — read-side server (still zero-dep node:sqlite).** `logSummaryView`
  Explain-shaped aggregates for the Log KPI band; widen `logRegisterView` to
  decisions + risks; populate hold `packageId` via `isInPackage`; fix interface
  `ageWd`; default sort overdue-first; join the schedule WBS rows into `/plan`;
  expose link-edges + unmerged threshold overrides in detail payloads; server
  threshold validation.
- **Tier M — schema / model migration (owner-gated).** `Risk.log` field +
  migration + register/visibility parity; `interface`/`decision` deliverable
  FK (so a deliverable can show them); widen `isInPackage` to more hold target
  types; deep-linkable drawer records (check/work_item/comment/revision).
- **Tier O — owner decisions (no default).** A `project_role` **assignment
  route** (none exists — role management is impossible in Admin without new
  server work); how far the model should extend (Tier M); dark-mode priority;
  how comprehensive the Log dashboard should be; confirmation of the zero-new-
  dependency posture.

---

## 5. Per-surface redesign specs

Each cites the verified current problems (full list in Appendix A) → target
design (pattern-grounded, existing components) → data tier → effort/priority.

### 5.1 Admin — *the owner's "worst offender"* (P0)
**Problems (verified):** five heavyweight unrelated concerns on one scroll with
no sub-nav; two overlapping importers (safe proposal flow + co-equal one-click
force-import); 20 flat cryptic threshold inputs with no grouping/validation and
no override-vs-default visibility (corruptible); "People & roles" shows neither
roles nor any management; `window.prompt` for reject reasons; internal codes as
headings; write forms shown to users who lack `config.manage` (403-on-submit).

**Target:** route-tabbed Admin (`/p/:pid/admin/:section`, reusing the Registers
`registers/:tab` pattern) — **Users & Roles · Import · Exports · Thresholds ·
Activity**. Collapse to **one canonical import path** (dry-run → accept(SHA) →
apply); demote force-overwrite to a labeled, confirm-gated danger action;
promote proposals into a persistent **import-history feed** (`RegisterTable`,
state badges, expandable `ImportReportView`). Group the 20 thresholds by signal
family with warn/escalate adjacency, a one-line "drives: <signal>" link to the
Overview `HealthBadge` each feeds, and validation (`warn ≤ escalate`, `≥ 0`) in
**both** client and server. Rebuild People into **Users & Roles**: members with
their real project-role pills + a role→capability matrix rendered from server
data; if assignment stays instance-admin-only, say so inline and **rename to
"People directory"** rather than over-promise. Add an **Activity/Audit** panel
(`HistoryTrail` + filters + export) over the already-written audit events. Gate
write forms on the server `can/:action` probe (as `AgentDock` does) — never
client-invented RBAC.

**Data:** Tier U + Tier S (server threshold validation; expose unmerged
overrides). **Role management = Tier O** (new `project_role` write route).
**Effort L · Priority P0.**

### 5.2 Action & Hold Log → *a good dashboard, not a task manager* (P0)
**Problems (verified):** no summary layer (raw filters + one flat table); rows
don't drill; interface Age 0 factual bug + age-sort; opens fully unfiltered with
a single overdue toggle and a fixed server sort; free-text `area` filter that
silently returns empty on any mismatch; the "Anchor" column is redundant while
the useful `state` is fetched-but-unrendered; the Log omits **decisions and
risks** that the package cockpit counts as issues; hold rows carry
`packageId:null` so the package filter drops all holds.

**Target:** a **dashboard header band** of `KpiCard`s — Open (by type) ·
Overdue · Aging > 5 wd · Untriaged intake (+ oldest) · Active holds — each
**click-to-explain** (this requires a server `logSummaryView` emitting the
`Explain` shape, so the tiles preserve I-4 drill-down; a bare number would break
it). A pure-CSS **aging strip** (three-segment green/amber/red stacked bar,
click-to-filter). **Color-typed** Type column using the existing unused
`.itype-*` classes. A **Group by: none | owner | package | cause** control that
regroups the already-loaded rows (reuse My Week's group-by code). **Quick-view
URL presets** (Overdue · Aging>5 · Holds by cause · Untriaged · Mine) — the
zero-infra substitute for saved views; remember only the last in localStorage.
**Drill-through** on every row (via §5.8). Default order overdue-first. Widen the
server view to decisions + risks; fix hold `packageId` and interface `ageWd`.
**Demote Triage** from a co-equal tab to a called-out queue KPI that deep-links
into the (retained, unchanged) disposition workflow. **No board, no inline
status edits, no bulk mutation** — export-displayed-rows stays the only bulk
tool.

**Data:** Tier U + Tier S. **Effort L · Priority P0.**

### 5.3 Plan — *good ideas, poor implementation → real project-controls UI* (P1)
**Problems (verified):** the two headline computed values (capacity %, lookahead
cell) **bypass the explain drawer** though the server already ships the
contributing ids; no way to edit hours/discipline or remove a plan item (the PUT
endpoint exists but has no caller); "raise risk" fabricates 4×3 and dup-creates;
ISO week is raw free-text (no picker) while the app uses native date pickers in
15 other places; the shift-review workflow is buried in a flat 50-row log with
no "needs my review" and no reject reason; capacity is one cell per modal with
free-text discipline; Now/Next/Later show no rollups and are disconnected from
capacity; the lookahead overloads the health palette with no legend and renders
check/work identically; the first column isn't sticky.

**Target:** restore **click-to-explain** on every capacity cell and lookahead
cell (small server Explain payload over the already-present `planItemIds` /
`detail`). Pivot capacity into a **discipline × week heatmap** with an in-cell
work/check/approve mini stacked bar and per-cell drill + raise-risk. Native
`<input type="week">`/week-`<select>` and a discipline `<select>` from the
people directory. **Horizon rollups** (WIP + hours per column) and a "fits
capacity?" chip. Wire the existing **PUT** for edit + add remove. **Confirm +
preview** before raise-risk (and surface it as *may create* honestly). A **"needs
my review"** shift surface with reject-with-reason (the server already accepts a
note). Lookahead **legend**, distinct check/work, **sticky first column**,
current-week highlight. *Optional, higher-cost:* a **read-first CSS WBS
tree-table / week-grid Gantt** from the imported schedule rows (baseline vs
actual, % complete, variance-days) — this needs the Tier-S schedule join and is
the single biggest reuse of already-imported, unrendered data. **No Gantt
library, no critical path, no drag-to-mutate** (a drag may only open the
governed shift drawer).

**Data:** Tier U + Tier S (explain payloads; schedule WBS join). **Effort L
(core) / XL (with Gantt) · Priority P1.**

### 5.4 Packages & Deliverables — *make the issue linkage real* (P1)
**Problems (verified):** the package issues cockpit's `issueHref` misroutes
decisions/risks/interfaces (§1); the Deliverable detail has no path back to its
Package and lists holds/decisions/approvals as inert text; "Needs the lead this
week" is non-navigable; deliverable-scoped **risks are never shown on the
deliverable** though the server links them by `deliverableId`; refs render as
plain text instead of the learned `.reflink` affordance.

**Target:** the drill spine from §5.8 fixes the cockpit, "Needs the lead", and
the detail cross-record tables (route through `refRoute`, append `?ref=`). Add a
**breadcrumb** (back to register/parent package) on both detail pages. **Surface
risks** on the deliverable detail (server: add risks to
`deliverableDetailView.openItems` — data already exists). Make the MDL "Package"
cell a link/filter to its package. Optionally add a **Related-records** panel
from server-exposed link edges.

**Data:** Tier U (drill) + Tier S (risks on deliverable; link edges).
**Effort M · Priority P1.**

### 5.5 Registers — *consistency & scannability* (P2)
**Problems (verified):** reference cells are inert (no drill); two incompatible
mutation models (click-row-to-edit vs trailing action button) with no signal of
which rows are actionable; the tab bar reuses filter chrome with no `tablist`
semantics and read-only Schedule/Tracker sit ungrouped/unmarked among editable
tabs; wide registers (16–17 cols) overflow the whole page with no frozen Ref
column; hold-withdraw uses `window.prompt`; the Schedule tab lacks the agent-
context/deep-link wiring its Tracker sibling has; stale docstring.

**Target:** unify the row-actionability signal; add `role="tablist"`/
`aria-selected`, group and mark the read-only tabs; wrap wide tables in an
`overflow-x` container with a **sticky Ref column**; replace the withdraw prompt
with a Drawer form; optional per-tab summary strip (`KpiCard`); bring Schedule to
parity; refresh the docstring. **Data:** Tier U. **Effort M · Priority P2.**

### 5.6 Overview & My Week — *consistency pass* (P2)
**Problems (verified):** My Week's "Waiting on others" and Notifications
dead-end; empty tables render a wall of "no records"; CSV export applied
inconsistently; the sponsor-brief action masquerades as a computed KPI (and is a
non-focusable div); mixed severity vocabulary (warn/ok/red vs green/amber/red);
a dead `StateTag` import; decisions/approvals a user owes appear only on Overview
("Waiting on you"), not on the IC home.

**Target:** drill-fixes (§5.8); conditional tables + an affirmative all-clear
empty state; consistent `exportName`; make sponsor-brief a real labeled action,
not a fake KPI tile; unify the tone vocabulary to green/amber/red; remove dead
import. **Owner decision:** surface decisions/approvals-owed on My Week (cheap
cross-link vs fuller section). **Data:** Tier U. **Effort S–M · Priority P2.**

### 5.7 Cross-cutting: design system, tokens, theming, a11y (P0 foundation)
**Problems (verified):** ~30 hardcoded hex values sit outside `:root`, blocking
any systematic restyle or dark mode; **no** `:focus-visible`/focus styling
anywhere; the amber health badge fails AA contrast (3.1:1) and green is
marginal (4.4:1); the Drawer has no `role="dialog"`/`aria-modal`/focus
trap/restore; 8 flat ungrouped nav items despite the "six lenses" framing; no
breadcrumb/orientation layer; the project switcher discards the current lens and
Sign-out is a styled `<a href="#">`.

**Target:** **two-tier token layer** (primitive palette + semantic roles:
`--surface`, `--text`, `--text-muted`, `--border`, `--accent`, `--row-hover`,
`--shadow`), migrate all hardcoded hex onto it; **dark mode** via
`@media (prefers-color-scheme)` + `:root[data-theme]` override + a sidebar toggle
persisted to localStorage (swap semantic tokens only); a global `:focus-visible`
ring; fix badge contrast to AA; make `Drawer` a proper dialog; make `KpiCard`
and clickable rows real/keyboard-operable; group the sidebar (six lenses vs
Registers/Admin) with a divider; add a `<Breadcrumb>`; fix the switcher to keep
the current lens. **Data:** Tier U. **Effort M · Priority P0 — this is the
foundation the page redesigns build on.**

### 5.8 Cross-cutting: the drill-to-source spine (P0 foundation)
A shared `<RecordRef ref recordType id>` that renders the `.reflink` affordance
and routes through `refRoute` (with `?ref=` highlight), plus `onRowClick`/
keyboard handlers, adopted on: Log open-items, package cockpit + "Needs the
lead", deliverable detail cross-record tables, My Week waiting/notifications,
Plan deliverable doc-nos, Registers reference cells. **Coverage caveat (verified,
carry into scope):** `refRoute` resolves holds/decisions/risks/interfaces/
approvals/deliverables today, but returns `null` for `work_item` and drawer-only
records (check/comment/revision); those need a `/log?ref=` case and, later, a
deep-linkable drawer param (Tier M) to complete traceability. **Effort M ·
Priority P0.**

---

## 6. Roadmap — phased candidate tranches

Each is one owner-gated unit: a proposed decision packet (continuing the series
from D-PEC-23), an exact write fence, dependencies, verification, effort, and the
owner gate. **Foundation first**, then the owner's top pain, then linkage/polish,
then optional model completeness. Standard per-tranche verification =
`npm run typecheck && npm test && npm run build && npm run drill` green + full
`tools/` pytest with the self-check baseline held + `git diff --check` + scope ⊆
fence + a visual/keyboard pass on the changed surface; CI green; owner merges
(never self-merge).

| # | Proposed packet | Scope (summary) | Write fence | Deps | Tier | Effort |
|---|---|---|---|---|---|---|
| P0 | **D-PEC-24 · Design-system & a11y foundation** | Token tiers, dark mode, `:focus-visible`, AA badge fix, dialog/`KpiCard`/row accessibility, sidebar grouping, breadcrumb, switcher fix | `web/src/styles.css`, `web/src/shared.tsx`, `web/src/main.tsx` | — | U | M |
| P0 | **D-PEC-25 · Drill-to-source spine** | `<RecordRef>`/`refRoute` everywhere; fix `issueHref`; wire Log/cockpit/detail/My Week/Plan/Registers refs; breadcrumbs | `web/src/shared.tsx`, `web/src/pages/*` | D-PEC-24 | U | M |
| P0 | **D-PEC-26 · Admin restructure** | Route-tabbed Admin; one canonical importer + import-history feed; grouped+validated thresholds; Users&Roles (or rename); Activity panel; can-probe gating | `web/src/pages/Admin.tsx`, `web/src/main.tsx`; `server/src/api.ts` (threshold validation, unmerged overrides) | D-PEC-24/25 | U+S (role route = O) | L |
| P0 | **D-PEC-27 · Log → dashboard** | `logSummaryView` Explain aggregates; widen view to decisions+risks; fix hold `packageId` + interface `ageWd` + sort; KPI band, aging strip, group-by, quick-views, typed rows; demote Triage | `server/src/services/views.ts`, `server/src/api.ts`, `web/src/pages/LogHome.tsx`, `web/src/shared.tsx` | D-PEC-24/25 | U+S | L |
| P1 | **D-PEC-28 · Plan redesign** | Explain on capacity/lookahead; capacity heatmap; week/discipline pickers; horizon rollups; wire PUT edit/remove; confirm raise-risk; needs-my-review; legend/sticky | `web/src/pages/Plan.tsx`, `web/src/shared.tsx`; `server/src/services/plan.ts`, `server/src/api.ts` | D-PEC-24/25 | U+S | L |
| P1 | **D-PEC-28b · Schedule WBS/Gantt (optional)** | Join schedule WBS rows into `/plan`; read-first CSS WBS tree-table + week-grid Gantt (baseline/actual/%/variance) | `server/src/services/plan.ts`, `web/src/pages/Plan.tsx`, `web/src/shared.tsx` | D-PEC-28 | S | XL |
| P1 | **D-PEC-29 · Packages/Deliverables linkage** | Risks on deliverable detail; MDL Package link/filter; optional Related-records panel from server link edges | `server/src/services/views.ts`, `web/src/pages/{Packages,Deliverables}.tsx`, `web/src/shared.tsx` | D-PEC-25 | U+S | M |
| P2 | **D-PEC-30 · Registers consistency** | Unify row-action signal; tablist ARIA + read-only grouping; overflow + sticky Ref; withdraw Drawer; Schedule parity; docstring | `web/src/pages/Registers.tsx`, `web/src/shared.tsx` | D-PEC-24/25 | U | M |
| P2 | **D-PEC-31 · Overview & My Week polish** | Drill-fixes; empty states; export consistency; sponsor-brief as action; tone vocabulary; (owner) decisions/approvals-owed on My Week | `web/src/pages/{Overview,MyWeek}.tsx` | D-PEC-25 | U | S–M |
| P3 | **D-PEC-32 · Issue-model completeness (owner-gated)** | `Risk.log` field + migration + parity; interface/decision deliverable FK; widen `isInPackage` | `core/src/types.ts`, `server/src/{db,services,...}`, `web/src/*` | D-PEC-27/29 | M | L |
| P3 | **D-PEC-33 · Deep-linkable drawer records (follow-up)** | Stable URLs (`?open=check:123`) for check/work_item/comment/revision; completes traceability | `web/src/shared.tsx`, `web/src/pages/*` | D-PEC-25 | M | M |

### Sequencing rationale
D-PEC-24 (accessible token/interaction layer) and D-PEC-25 (drill spine) are
force-multipliers — nearly every page defect is an instance of "value doesn't
drill" or "control isn't accessible," so building these first means each later
page tranche is mostly *adoption*, not net-new plumbing. They also both touch
`shared.tsx`, so they run **sequentially, not in parallel** (disjoint-scope rule).
The owner's three named pains (Admin, Log, Plan) come next as P0/P1. Linkage/
register/overview polish (P2) inherit the spine cheaply. Model completeness (P3)
is deliberately last and owner-gated because it is the only schema-migration
work and the only place the "factual basis" value needs an explicit owner call.
Each tranche is independently shippable behind its own PR.

## 7. Decision slate (what only the owner can decide)

1. **Adopt this plan** as the standing development plan — whole, or a subset of
   phases? (On adoption it promotes to `WORKPLAN_2026-07-08_*`; each tranche
   still lands as its own ruled source-tranche.)
2. **Zero-new-dependency posture** — confirm the plan's commitment to hand-rolled
   CSS + inline SVG (no charting/component/CSS-framework library). *Recommend:
   yes* (preserves ADR-002/F-PEC-3; every redesign above is buildable without
   one).
3. **Admin role management** — build a `project_role` **assignment route** (new
   zero-dep server work, Tier O) so Admin can manage roles, or keep assignment
   instance-admin-only and simply **rename "People & roles" → "People
   directory"**? *Recommend: rename now (D-PEC-26), decide the route separately.*
4. **Log dashboard scope** — full band (KPI + aging + group-by + quick-views) as
   D-PEC-27, or a leaner first cut? *Recommend: full band — it is the owner's
   headline ask and all data is server-computable.*
5. **Plan Gantt (D-PEC-28b)** — pursue the read-first WBS/Gantt from the imported
   schedule now, later, or not? (Highest-value reuse of unrendered data, but XL.)
6. **Issue-model completeness (D-PEC-32)** — pursue `Risk.log` + deliverable FKs
   + `isInPackage` widening (schema migration), or leave the model as-is and
   accept the bounded under-counts documented in Appendix A? *This is the one
   item touching data shape — squarely an owner call.*
7. **Dark mode** — P0 foundation as written, or defer the toggle?

## 8. Risks & watch-items

- **`shared.tsx` contention** — D-PEC-24/25/27/28/29/30 all touch it; sequence
  them, never parallelize, to keep write scopes disjoint (loop rule).
- **Explain-shape discipline** — the Log/Plan KPI tiles must emit real
  `contributing[]` refs or they silently break I-4; verify each tile drills.
- **Scope creep toward a task manager** — the Log and Plan redesigns must stay
  read/flag dashboards; reject any board/bulk-mutate/editable-status request
  against principle 6 and the owner value.
- **Partial `refRoute` coverage** — `work_item` and drawer-only records don't
  resolve yet; D-PEC-25 must handle them gracefully (no dead links) and
  D-PEC-33 completes them.
- **Fable availability** — the planning/verification convention prefers
  `fable@high`, but fable hit session-wide rate limits during this assessment;
  the verification was completed on Opus (the Receipt-54 precedent). Tranche
  execution should not block on fable.

## Appendix A — verified defect register (69, source-grounded)

Severity/verdict from the assessment's adversarial verification pass; every item
carries a `file:line` in the full digest. Counts by surface: Admin 8 · Log 8 ·
Plan 11 · Packages&Deliverables 5 · Registers 9 · Overview&MyWeek 9 ·
Design-system 10 · Data-linkage 9. Highest-severity items (critical/major)
drive the P0/P1 tranches above; the minors are folded into their surface's
tranche. **The full per-defect table** — verdict/severity, category, claim, and
`file:line` for all 69 — is committed alongside this plan as
[`PLAN_2026-07-08_pec_uiux_redesign.appendix.md`](PLAN_2026-07-08_pec_uiux_redesign.appendix.md).

## Human ruling / adoption (owner)

- **Adopt as standing plan:** ☐ whole ☐ phases: ______ ☐ decline
- **Slate answers (§7):** 1 ___ 2 ___ 3 ___ 4 ___ 5 ___ 6 ___ 7 ___
- **Direction / amendments (verbatim):**

_(Adoption is the owner's act — K-AUTH-1; D-GOV-04. On adoption, the loop opens
the ruled D-PEC tranches, executes each branch-first + PR under its fence, and
receipts each closeout.)_

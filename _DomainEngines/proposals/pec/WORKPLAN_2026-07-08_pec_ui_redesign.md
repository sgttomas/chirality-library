# PEC Work Loop — standing development plan (UI/UX redesign)

> **Epistemic status: agent-authored development plan — not authority.** Written
> at owner direction on 2026-07-08. This is the newest `WORKPLAN_*.md` in this
> loop directory and therefore fills the standing-plan role named by
> `LOOP_INIT.md`. It authorizes no source implementation by itself: source
> tranches still require owner adoption/ruling/direction under K-AUTH-1 and the
> PEC fences. Live source, registers, profile, and receipts govern on any
> disagreement.

## Owner intent now

The demo application has crossed the minimum viable threshold. The next
development objective is to redesign the PEC user experience around effective
project-control workflows, with immediate attention to:

- the Admin page, which currently mixes unrelated high-risk and routine tasks;
- the Action & Hold Log, whose schema is useful but whose page is a poor
  task-management interface and should first become a strong dashboard with
  comprehensive tools;
- the Plan page, which has valid primitives but needs to become an effective
  planning-control interface using established project-controls patterns;
- the Packages / Deliverables / Issues relationship, where package and
  deliverable linking is good but issue visibility and drill paths are not yet
  clear enough.

This direction supersedes the 2026-07-07 postponement only to the extent needed
for UI/UX planning and later owner-authorized source tranches. It does not
reopen import-behavior refinement as an objective in itself; data-import work
remains subordinate to workflow simplification and factual, basis-clear
reporting.

## Live discovery return for this plan

- `REPO_ROOT`: resolved by `git rev-parse --show-toplevel` for this run; use
  `$REPO_ROOT` in governed artifacts rather than a machine-absolute path.
- Current branch at planning: `codex/pec-ui-redesign-plan`.
- Latest receipt checked: `LOOP_RECEIPTS.md` Receipt 54, which records D-PEC-23
  as discharged end-to-end and parks only P4 weekly rehearsal before this new
  steer.
- Pre-existing dirty state observed and not touched: piping equation audit JSONs
  and `projects/pec/pec-demo.db{,-shm,-wal}`.
- Live authority checked: `_DomainEngines/profiles/pec.yaml` is ADOPTED,
  `integration_level: OPERATION_PROPOSAL`, `data_residency: OPEN_ENUMERATED`;
  tier-0 register rows through D-T0-22 are ruled; PEC-local register rows through
  D-PEC-23 are ruled.
- Widest lawful tranche opened by this run: planning and assessment artifacts
  under `_DomainEngines/pec/**`.
- Still parked: source implementation, import-behavior changes, real/non-scratch
  mutation beyond existing demo-basis permissions, reserved human acts, and P4
  weekly rehearsal unless the owner is at the screen.

## Assessment evidence

Screenshots were captured from the live local demo app as admin on project `EXP`
and saved under:

`_DomainEngines/proposals/pec/PEC_2026-07-08_ui-redesign-planning/screenshots/`

Reference screenshots for this plan:

> The screenshots were removed from the public library because they showed
> client project data. They remain in the archived source repository.

| Screenshot | Page | Why it matters |
|---|---|---|
| `_DomainEngines/proposals/pec/PEC_2026-07-08_ui-redesign-planning/screenshots/01-admin.png` | Admin | Shows proposed imports, direct imports, exports, thresholds, and people sharing one long operations page. |
| `_DomainEngines/proposals/pec/PEC_2026-07-08_ui-redesign-planning/screenshots/02-packages.png` | Packages register | Shows package/deliverable linking works at register scale, but issue posture is secondary to the table. |
| `_DomainEngines/proposals/pec/PEC_2026-07-08_ui-redesign-planning/screenshots/03-deliverables.png` | Deliverables register | Shows document workflow status is legible, while issue relationships are not a first-order row affordance. |
| `_DomainEngines/proposals/pec/PEC_2026-07-08_ui-redesign-planning/screenshots/04-log-open.png` | Action & Hold Log, open items | Shows the flat 254-row register that proves schema coverage but not dashboard usability. |
| `_DomainEngines/proposals/pec/PEC_2026-07-08_ui-redesign-planning/screenshots/05-log-triage.png` | Action & Hold Log, triage queue | Shows intake triage exists as a mode but lacks dashboard metrics, grouping, and queue workbench patterns. |
| `_DomainEngines/proposals/pec/PEC_2026-07-08_ui-redesign-planning/screenshots/06-plan.png` | Plan | Shows useful planning primitives surrounded by weak empty-state, readiness, intake, and commit UX. |
| `_DomainEngines/proposals/pec/PEC_2026-07-08_ui-redesign-planning/screenshots/07-package-detail-issues.png` | Package detail | Shows the package-level issue cockpit and issue-count language; this is the strongest current issue-link affordance. |
| `_DomainEngines/proposals/pec/PEC_2026-07-08_ui-redesign-planning/screenshots/08-deliverable-detail-issues.png` | Deliverable detail | Shows deliverable workflow detail is rich, but related issues are absent from the visible first-screen context. |
| `_DomainEngines/proposals/pec/PEC_2026-07-08_ui-redesign-planning/screenshots/09-overview-issue-rollup.png` | Overview | Shows governance signals for untriaged intake and unanchored items, but not a coordinator-grade issue dashboard. |

Key observations from browser and Computer Use inspection:

- `Admin` exposes proposed imports, direct imports, exports, governance
  thresholds, and people in one long page. The safer proposal path and direct
  import path are sibling forms, not clearly separated by risk or task.
- `Action & Hold Log` renders 254 open rows in a flat register with filters.
  It proves the schema but does not provide a coordinator dashboard: no summary
  strip, grouping, aging buckets, saved views, queue focus, or row workbench.
- `Plan` exposes commit, add, capacity, lookahead, and shift primitives, but the
  primary action is "commit week" even when no plan exists; there is no visible
  planning intake/backlog, capacity heatmap, readiness checklist, or link from
  127 imported schedule activities to practical planning choices.
- `Packages` and `Deliverables` both render large registers successfully, but
  issue posture is not prominent in the register workflow. Package details have
  an issues cockpit in code; the register-level and deliverable-level issue
  affordances need to make that relationship explicit.
- `Overview` already reports governance signals such as untriaged intake age
  and unanchored items, but those signals are not yet converted into a focused
  issue-routing dashboard with saved views and drill context.

## Product design principles

1. **Factual dashboard before task-manager ambition.** The next UI should
   summarize and route factual record state before adding new task-management
   behavior.
2. **One primary job per page.** Admin is operational control, Log is issue
   awareness and triage, Plan is weekly planning control, Packages are scope
   ownership, Deliverables are document workflow.
3. **Issue clarity by drill path, not duplicate truth.** Issues remain typed
   source records. The UI may aggregate and group them, but every count must
   drill to its contributing records and export what is displayed.
4. **High-risk actions are fenced visually.** Import apply, direct import,
   threshold changes, and destructive/demo-state actions must be visually and
   structurally separated from read/export tasks.
5. **Dense, contemporary, non-marketing UI.** Use restrained dashboards,
   filters, tabs, split panes, sticky summary bars, status chips, data grids,
   and drawers. Do not introduce hero sections, decorative cards, or narrative
   onboarding copy.
6. **Basis-clear reporting.** Every KPI, badge, and dashboard count must carry
   a rule/source basis or drill path; avoid reporting "health" or "readiness"
   without its contributing records.

## Target information architecture

### Admin: Operations Console

Replace the single long Admin page with task-scoped sections:

- **Import proposals:** current safe proposal workflow, proposal list, stale /
  accepted / applied states, dry-run summary, detail drawer, and hash-bound
  accept/apply posture.
- **Data exchange:** exports, report render links, templates, and import mapping
  references. Direct import moves here as an "advanced/direct import" surface
  with a warning boundary and no visual parity with proposal apply.
- **Configuration:** governance thresholds in grouped sections with current
  values, last changed by/at if available, and save review.
- **People & access:** searchable directory, project roles, agent person, and
  read-only/access-management posture.
- **System evidence:** app/version, current project, DB/demo-basis notice,
  recent import-proposal states, and relevant runbook links.

### Action & Hold Log: Issue Dashboard

Promote the page from raw register to coordinator dashboard:

- top summary strip: open total, overdue, unanchored, aging buckets, owner gaps,
  active holds, decisions pending, interfaces due, intake needing triage;
- issue groups: `Overdue`, `Unanchored`, `Needs owner`, `Due this week`,
  `Recently raised`, `By package`, `By owner`, `By type`;
- saved views: "Coordinator today", "Unanchored intake", "Package log",
  "Client/internal log", "Hold causes", "Due soon";
- split-pane row workbench: selected row details, source links, package /
  deliverable context, contributing history, and allowed existing actions;
- triage queue remains a distinct mode, but with queue metrics, batch filters,
  and clear distinction between "open triage" and final disposition.

### Plan: Planning Control Board

Redesign Plan as a planner cockpit:

- planning readiness header: current week, commit status, planned hours,
  capacity coverage, unplanned eligible records, schedule coverage, blockers;
- intake/backlog rail: eligible work/check/approval records not yet planned,
  grouped by source, owner, package, and due date;
- Now / Next / Later board: compact lanes with owner, week, hours, discipline,
  package, and issue/blocker chips; empty lanes should route to planning intake;
- six-week lookahead: matrix grouped by package/discipline with schedule
  activities, planned work, issue/hold/approval/check markers, and empty-state
  explanation when schedule data exists but no plan linkage exists;
- capacity: discipline-week heatmap with drilldown to planned records and
  raise-risk affordance only where overload basis is clear;
- commit workflow: readiness checklist before "Commit week", showing what will
  stamp into My Week and what is excluded.

### Packages / Deliverables / Issues

Make issue posture obvious without duplicating truth:

- Packages register: add issue mix and "worst issue" / "oldest overdue" context
  next to open issue count; make row click land in a detail page with issue
  cockpit first.
- Package detail: preserve the current issue cockpit but add group toggles,
  count chips, and direct filters for holds/interfaces/decisions/risks/actions.
- Deliverables register: keep workflow status as the primary status, but add
  issue indicators when package/deliverable/revision-linked issues affect the
  row.
- Deliverable detail: add a compact "related issues" panel that links to the
  exact source records and package issue cockpit.
- Global navigation: make "Issues" a conceptual label in page copy and tabs
  where useful, while keeping the existing route as Action & Hold Log unless
  the owner later authorizes a route rename.

## Development tranches

All tranches below are candidate source work. Each requires owner adoption or a
specific source-tranche ruling before implementation.

### Tranche 0 — Design specification and data contract inventory

Produce a design spec under `projects/pec/execution/_Coordination/**` that
freezes page jobs, required metrics, drill paths, and existing/new API needs.
No source code. Exit when every proposed dashboard count maps to an existing
server field or a named new read-only projection.

### Tranche 1 — Shared UI foundations

Implement reusable page primitives before page rewrites: summary metric strip,
toolbar/saved-view pattern, split-pane detail workbench, compact issue chips,
responsive data grid wrapper, empty-state component with basis text, and
export/drill conventions. Keep the current color system but improve hierarchy,
spacing, sticky toolbars, and table legibility.

### Tranche 2 — Issue dashboard and issue drill clarity

Build the Action & Hold Log dashboard and improve package/deliverable issue
indicators. Prefer read-only projections first; post actions remain existing
RBAC-guarded actions only. This tranche discharges the owner's concern that
issues are not clearly linked.

### Tranche 3 — Planning control board

Redesign the Plan page around readiness, planning intake, lanes, capacity, and
lookahead. Add read-only summary projections if needed. Preserve current
plan-item, shift, capacity, and commit semantics; do not change planning rules
without a separate ruling.

### Tranche 4 — Admin operations console

Split Admin into task-scoped tabs/sections and demote direct import behind an
advanced boundary. Preserve import-proposal semantics and export contracts.
Threshold editing and people/access surfaces become separate workspaces with
clear save/review affordances.

### Tranche 5 — Visual polish, accessibility, and regression evidence

Run viewport checks at desktop and mobile widths; verify no blank pages, table
overflow failures, unusable forms, or text overlap. Capture screenshots for
Admin, Log, Plan, Packages, Deliverables, and at least one detail page. Add or
update focused tests for any new projections and page states.

## Verification for source tranches

For any implementation tranche, run at final SHA:

- `PYTHONDONTWRITEBYTECODE=1 python3 tools/practitioner_harness/harness.py self-check`
- full `tools/` pytest if `tools/**` changed, otherwise as required by the
  active loop receipt/check convention;
- `cd projects/pec && npm run typecheck && npm test && npm run build && npm run drill`
- `git diff --check`
- browser screenshot verification for changed pages, including at least one
  1280px desktop viewport and one mobile/narrow viewport;
- citation/adversarial review for any governed coordination artifact.

## Owner gates

This plan opens no implementation by itself. The next owner-shaped decisions are:

- adopt, amend, or reject this standing development plan;
- if adopted, authorize Tranche 0 as the next non-source design-spec tranche;
- after Tranche 0, rule each source tranche separately or provide a combined
  source-tranche authorization with explicit file fences.

Until then, stop at planning artifacts and screenshots.

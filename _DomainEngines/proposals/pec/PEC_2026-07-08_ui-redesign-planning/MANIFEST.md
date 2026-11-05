# PEC UI Redesign Planning Evidence — 2026-07-08

> Derivative planning evidence. Screenshots and observations are not
> authoritative product truth; live source, registers, profile, and owner
> rulings govern.

## Basis

- Repo root: resolved by `git rev-parse --show-toplevel`; governed references
  below are repo-relative.
- App inspected: local PEC demo at `http://localhost:4811/`
- Persona: `admin@aurora.dev` against project `EXP — Example Project`
- Method: browser screenshots, Computer Use inspection of Chrome's visible
  accessibility tree, and headless Chrome DevTools captures for detail-page
  evidence.

## Screenshots

> The screenshots were removed from the public library because they showed
> client project data. They remain in the archived source repository.

| File | Page | Notes |
|---|---|---|
| `screenshots/01-admin.png` | Admin | Proposed imports and direct import appear as peer forms; export/config/people continue below. |
| `screenshots/02-packages.png` | Packages | Large package register; open issue count exists but issue posture is not prominent. |
| `screenshots/03-deliverables.png` | Deliverables | Large MDL register; workflow status is clear, issue relationship is indirect. |
| `screenshots/04-log-open.png` | Action & Hold Log / open items | 254-row flat issue register; schema is good, dashboard layer absent. |
| `screenshots/05-log-triage.png` | Action & Hold Log / triage | Intake queue state captured. |
| `screenshots/06-plan.png` | Plan | Good primitives, but empty board/readiness/commit state is not an effective planning cockpit. |
| `screenshots/07-package-detail-issues.png` | Package detail | Package-level issue cockpit and issue-count language are visible; this is the strongest current issue-link affordance. |
| `screenshots/08-deliverable-detail-issues.png` | Deliverable detail | Workflow detail is rich, but related issues are absent from visible first-screen context. |
| `screenshots/09-overview-issue-rollup.png` | Overview | Governance signals expose untriaged intake and unanchored items, but the page is not a dedicated issue dashboard. |

## Immediate planning conclusions

- Admin should become an operations console with task-scoped workspaces.
- Action & Hold Log should first become a dashboard and queue workbench, not a
  generic task manager.
- Plan should become a planning-control board with readiness, intake, lanes,
  lookahead, and capacity.
- Package/deliverable issue clarity should be solved by drill paths and issue
  indicators, not duplicated issue truth.

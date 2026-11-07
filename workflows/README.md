# Workflows

A workflow describes how to carry an undertaking through: its methods, decisions,
relationships, artifacts, and recovery. It can branch, iterate, and coordinate
several contributions. Agents bring the role; workflows bring the method; a brief
binds both to the present work.

## Select and load

Select explicitly with `Workflow: <name>`. The inventory is the immediate
subdirectories containing `WORKFLOW.md`. Discover names when needed; routine role
context loads no workflow catalog or bodies.

Resolve a selected workflow from any working directory:

```bash
python3 "$INSTRUCTION_ROOT/tools/workflow_runtime/resolve_workflow.py"   --root "$INSTRUCTION_ROOT" --role TASK --workflow dependency-extract
```

Supply `--resource CONTRACT.md` or another package-relative resource only when the
current stage needs it. The resolver returns selected context and fingerprints.
A workflow can be omitted for an assignment expressed entirely through its brief.

WORKING_ITEMS owns orchestration. TASK performs a bounded contribution, including
a separately specified stage of a larger workflow. HELPS_HUMANS can use a
compatible workflow while developing the design. An opt-in INTERLOCUTOR
advises Agent 0 from its brief and needs no method. Loading a method grants no
additional capabilities or decision rights.

## Package form and catalog

Each bundled package has canonical YAML metadata in the frontmatter of
`workflows/<name>/WORKFLOW.md`. Its `name` and `description` combine with the
compatible roles and restrictions in `execution.json`; the index generator
enumerates the package's contained resources. Optional resources hold detailed
contracts, templates, examples, or helpers. Package resources must remain
inside the package after real-path resolution.

`workflows/catalog.yaml` contains the bundled library identity and the ordered
set of central workflows shown by selectors. `workflows/index.json` is
generated from package metadata with
`python3 tools/validation/build_workflow_index.py`. Consumers use the index or
parse the canonical frontmatter and execution metadata themselves; the Library's Python command is an
authoring and validation tool, not a production parser.

Optional `execution.json` provides compatible roles and capability/command
restrictions. Without it, the package is compatible with HELP_HUMAN,
HELPS_HUMANS, WORKING_ITEMS and TASK; INTERLOCUTOR is eligible only where
`compatible_roles` names it. Stage-specific resources are selected explicitly without changing
role compatibility. See
[the workflow runtime utilities](../tools/workflow_runtime/README.md). A command is invoked
through the available session tools, against the declared tool root. A documented
operation does not imply that the host exposes or enforces it.

## Compatibility and maintenance

Select a method with `Workflow: <name>`, a source-qualified identity or an
ordered method list. The legacy alias ledgers (converted `TaskSkill` names and
retired agent names) have been removed: `TaskSkill` is no longer accepted, and a
retired or removed name fails as unknown rather than being redirected. Historical
methods are never inferred from files or prose.

Method libraries may exist at project, user, and bundled scope. Resolution uses
that precedence order. Identity is the complete tuple `source`, `sourceRootId`,
`kind`, and `name`; `sourceRootId` identifies the actual library root. Catalogs
expose every qualified collision and the selected candidate. A malformed
higher-precedence package blocks that unqualified identity instead of falling
through. Project files such as a flat `WORKFLOW.md` outside a package with
canonical metadata are documents only and never become discoverable methods.

Existing package names and legacy status survive this migration;
`scope-of-work` carries the current SOW_V1 method. The legacy
`dbm-concordance-seed` package was restored for explicitly selected historical
or resumed work; its own instructions identify it as legacy. The
`four-documents` package was removed on 2026-11-04 and is recoverable from the
private `sgttomas/chirality` Git history at or before `05d96f3e11`. Historical
briefs, snapshots, and pinned evidence retain their original identifiers.

### Retired packages

The `change` workflow and Root-only `chirality-change` skill are retired from
active discovery. They have no replacement Git method. Use an ordinary authorized
brief and the repository's own conventions; the Library's surviving conventions are in
[AGENTS.md](../AGENTS.md#standing-git-grant), with holding recovery/custody in its
[working instructions](../AGENTS.md#holding-changes-and-recovery). The Library's grant
never transfers to a consumer. The legacy `CHANGE` name and explicit
removed-package selections fail. No automatic skill substitution or consumer
repin occurs.

The last integrated pre-retirement source is
`8d0c5d1a19eec865a8a92750cb3de590d04f9c02` in the private `sgttomas/chirality`
repository. Use `git show <selected-revision>:workflows/change/WORKFLOW.md` (or
the skill path) there to read that historical basis. Existing consumer declarations and copies retain
their own source identities; a consumer owns any current pointer/wording repair.

These workflow packages were retired on 2026-09-26 because a canonical skill of
the same name replaced them under D-GOV-42. Select the skill by its own name;
the legacy alias ledger that redirected the old workflow names was removed. The
last revisions below are in the private `sgttomas/chirality` Git history and hold
each package's final bytes for historical replay.

| Retired workflow | Canonical successor | Last revision |
|---|---|---|
| `deliverable-consistency` | skill `deliverable-consistency` | `d1166698d433da2fefbb6e3caee68b7d7910f27d` |
| `preparation` | skill `preparation` | `29decb9fee2901f044457296f214163838bebb0f` |
| `proposal-format` | skill `proposal-format` | `d1166698d433da2fefbb6e3caee68b7d7910f27d` |
| `researcher` | skill `researcher` | `00e79872ae507b5041ab8c1482b4879629f6a495` |
| `software-code-review` | skill `software-code-review` | `d1166698d433da2fefbb6e3caee68b7d7910f27d` |
| `software-defect-diagnosis` | skill `software-defect-diagnosis` | `d1166698d433da2fefbb6e3caee68b7d7910f27d` |

`software-bounded-implementation` was retired on 2026-09-26 without a successor
package. Implementation is commissioned as a bounded TASK assignment whose brief
carries the objective, accepted basis, write fence, exclusions, acceptance
criteria and authorized checks; `construct-local-work-graph` states the node
requirements. It is no longer bundled or aliased, so a bundled selection of the
name fails. Its last revision is `d1166698d433da2fefbb6e3caee68b7d7910f27d` in
the private `sgttomas/chirality` repository.

HELPS_HUMANS helps develop or revise workflows; WORKING_ITEMS coordinates their
implementation. Validate a package with the Library workflow validator and review
whether its particular method, outputs, and recovery fit its intended use.

Consumers select their own source basis and adoption. Copy a workflow's complete
package, including the resources its method needs, and retain the applicable
license notices and original source identity. A copied package is not automatically
a registered workflow or a replacement for a product's pinned bundle. Check the
actual receiving contract before claiming compatibility; preserve a supported
path or coordinated adapter before an incompatible change. Export staging is not
a release. Runtime is frozen. A consumer's own adoption determines which scoped
contracts apply.

Some workflow resources cite historical contracts as
`sgttomas/chirality:<path>`, for example
`sgttomas/chirality:docs/COMPATIBILITY_FORMATS.md#historical-decomposition-contract`.
Those documents were removed from this repository on 2026-11-04. They, and
anything a citation labels "private archive" or "preserved in the private
`sgttomas/chirality` repository", are not on that repository's `main`; read
them from its Git history at or before `05d96f3e11`, for example
`git show 05d96f3e11:docs/COMPATIBILITY_FORMATS.md`.

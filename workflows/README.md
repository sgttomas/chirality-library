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
python3 "$INSTRUCTION_ROOT/tools/workflow_runtime/resolve_workflow.py"   --root "$INSTRUCTION_ROOT" --role TASK --workflow audit-decomp
```

Supply `--resource CONTRACT.md` or another package-relative resource only when the
current stage needs it. The resolver returns selected context and fingerprints.
A workflow can be omitted for an assignment expressed entirely through its brief.

WORKING_ITEMS owns orchestration. TASK performs a bounded contribution, including
a separately specified stage of a larger workflow. HELPS_HUMANS can use a
compatible workflow while developing the design. Loading a method grants no
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
parse the canonical frontmatter and execution metadata themselves; Root's Python command is an
authoring and validation tool, not a production parser.

Optional `execution.json` provides compatible roles and capability/command
restrictions. Stage-specific resources are selected explicitly without changing
role compatibility. See
[the runtime contract](../docs/AGENT_WORKFLOW_RUNTIME.md). A command is invoked
through the available session tools, against the declared tool root. A documented
operation does not imply that the host exposes or enforces it.

## Compatibility and maintenance

`TaskSkill: <name>` remains a legacy input spelling only for names explicitly
mapped in [the converted-method ledger](legacy-methods.json). Supplying both
fields with different selections fails. [The legacy agent map](legacy-agents.json)
records retired names and their historical role/workflow or deterministic
audit tool. A removed workflow resolves only when it has an explicit maintained
successor; otherwise invocation fails. Those names are not additional roles. Unconverted legacy methods
remain historical and are never inferred from files or prose.

Method libraries may exist at project, user, and bundled scope. Resolution uses
that precedence order. Identity is the complete tuple `source`, `sourceRootId`,
`kind`, and `name`; `sourceRootId` identifies the actual library root. Catalogs
expose every qualified collision and the selected candidate. A malformed
higher-precedence package blocks that unqualified identity instead of falling
through. Project files such as a flat `WORKFLOW.md` outside a package with
canonical metadata are documents only and never become discoverable methods.

Existing package names and legacy status survive this migration. In particular,
`dbm-concordance-seed` remains legacy; `four-documents` serves legacy production
compatibility while `scope-of-work` carries the current SOW_V1 method. Historical
briefs, snapshots, and pinned evidence retain their original identifiers.

### Retired packages

The `change` workflow and Root-only `chirality-change` skill are retired from
active discovery. They have no replacement Git method. Use an ordinary authorized
brief and the repository's own conventions; Root's surviving conventions are in
[AGENTS.md](../AGENTS.md#standing-git-grant), with holding recovery/custody in its
[working instructions](../AGENTS.md#holding-changes-and-recovery). Root's grant
never transfers to a consumer. Legacy `CHANGE` remains an identified historical
route but fails current invocation without a successor; explicit removed-package
selections also fail. No automatic skill substitution or consumer repin occurs.

The last integrated pre-retirement source is
`8d0c5d1a19eec865a8a92750cb3de590d04f9c02`. Use
`git show <selected-revision>:workflows/change/WORKFLOW.md` (or the skill path)
to read that historical basis. Existing consumer declarations and copies retain
their own source identities; a consumer owns any current pointer/wording repair.

These workflow packages were retired on 2026-09-26 because a canonical skill of
the same name replaced them under D-GOV-42. The legacy-method ledger resolves an
unqualified legacy selection of each name to its skill. The last revision
holds the package's final bytes for historical replay.

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
requirements. The legacy-method ledger lists it as historical only; it is no longer
bundled or aliased, so a bundled selection of the name fails. Its last revision is
`d1166698d433da2fefbb6e3caee68b7d7910f27d`.

HELPS_HUMANS helps develop or revise workflows; WORKING_ITEMS coordinates their
implementation. Validate a package with the Root workflow validator and review
whether its particular method, outputs, and recovery fit its intended use.

Consumers select their own source basis and adoption. Copy a workflow's complete
package, including the resources its method needs, and retain the applicable
license notices and original source identity. A copied package is not automatically
a registered workflow or a replacement for a product's pinned bundle. Check the
actual receiving contract before claiming compatibility; preserve a supported
path or coordinated adapter before an incompatible change. Export staging is not
a release. Runtime is frozen. The [interface reference](../docs/AGENT_WORKFLOW_RUNTIME.md)
describes scoped contracts; a consumer's own adoption determines which apply.

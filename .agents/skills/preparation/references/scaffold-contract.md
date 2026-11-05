# Current scaffold contract

The current PROJECT/SOFTWARE layout is `execution/PKG-nn/DEL-nn-nn/`.
The accepted decomposition supplies the exact identity widths and names.
Descriptions can remain in canonical accepted IDs and source records; directory
names use their numeric PKG/DEL identity. No automatic migration of an existing
layout is part of preparation.

## Operations

Resolve commands against the selected library root. Python 3 and PyYAML are
required by the current route; `PYTHON` may select the interpreter.

| Operation | Command | Result |
|---|---|---|
| Package | `zsh tools/scaffolding/scaffold_package.sh --current <execution-root> <PKG-ID> <accepted-name>` | Numeric package directory; no lifecycle subfolders |
| Deliverable | `zsh tools/scaffolding/scaffold_deliverable.sh --current <package-path> <accepted-DEL-ID> <accepted-name>` | Numeric DEL directory, `Work/`, and `deliverable.yaml` with accepted numeric identity/name and `needs: []` |
| Prepared structure | `zsh tools/validation/check_min_viable_fileset.sh --current --prepared <DEL-path> <accepted-DEL-ID>` | Checks current folder/identity, Work and valid native YAML; ScopeOfWork is not yet required, but an existing one must have consistent identity |
| Authored structure | Same check without `--prepared` | Additionally requires ScopeOfWork with matching schema/package/DEL frontmatter; content/acceptance verification is separate |

Creation reports each new path as `CREATED_PATH`. Existing files are preserved,
including their needs, scope and work content. Conflicting identities, malformed
declarations and file/directory mismatches are errors, not an instruction to repair
or replace the target. Current generated components must be real directories and
regular files; symlink targets are refused. An existing chosen source/root can be
resolved explicitly, but child creation does not traverse substituted links.

Creation exits 0 on success and 2 on invalid input/operation failure. Checking
exits 0 on the selected structural stage and 1 on a finding/operational failure;
argument usage errors exit 2. A failure can leave reported newly created paths;
inspect them before resuming. Existing work is never deleted as rollback.

## Scope and needs

The helpers do not create a blank ScopeOfWork or production claims. The authoring
stage supplies the actual contract from accepted decomposition and objectives,
then runs `validate_scope_of_work.py` and its applicable checks. Structural success
does not validate production meaning or acceptance.

Actual needs are authored after scope exists using the project's relevant work
and source conditions. Preserve cases, unknowns and technical holds; derive reverse
links when needed. No dependency register or completeness claim is created by
initial `needs: []`. The accepted deliverable ID's numeric prefix binds YAML and
ScopeOfWork; preparation does not change the canonical decomposition identity.

## Retained routes

The unflagged shell interfaces retain their historical labelled/phase layout and
control files, including optional `--memory` where explicitly selected. They are
documented in [the legacy contract](legacy-scaffold-contract.md), for projects
that still adopt it. Do not use those calls for current flat setup or create their
control files just to satisfy a legacy validator. KTY/domain schema behavior is
unchanged and is not selected by `--current`.

Tool-root and aggregation operations from the retained contract are available
only when the undertaking actually requires them. Preserve existing sources;
there is no automatic lifecycle update or movement between layouts.

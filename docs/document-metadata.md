---
name: document-metadata
description: Document metadata.
metadata:
  kind: instruction
  surface: reference
---
# Document metadata

When typing a maintained Markdown document, begin with YAML frontmatter:

```yaml
---
name: project-entry
description: Establish a project's bootstrap, standing instructions and operating entry.
metadata:
  kind: instruction
  surface: reference
---
```

Use a stable lowercase identifier with hyphen-separated words, at most 64
characters, and a one-line description of purpose. For workflow and skill
entrypoints, retain the package name and existing description. Preserve existing
package-specific keys, including `metadata.applicability` where used. Validate
frontmatter against [the schema](document-metadata.schema.json).

Choose `metadata.kind` for the document's principal use:

| Kind | Use |
| --- | --- |
| `instruction` | Direct action under the applicable authority |
| `explanation` | Develop an account, definition or interpretation |
| `example` | Illustrate a case or arrangement |
| `proposal` | Present a change for decision |
| `historical-source` | Preserve an earlier source for identified uses |

Choose `metadata.surface` for its place in the project:

| Surface | Document home or contribution |
| --- | --- |
| `bootstrap` | `init/init-prompt.md` |
| `standing` | `AGENTS.md` |
| `operating-entry` | `loop/LOOP_INIT.md` |
| `role` | `agents/AGENT_*.md` |
| `workflow` | `WORKFLOW.md` |
| `skill` | `SKILL.md` |
| `tool` | Tool-use README |
| `reference` | Publications, explanations and supporting references |
| `requirements` | Product requirements |

Classify the document as a whole; retain distinctions within its body where it
contains examples, quoted sources or proposed changes. Keep status, date and
revision out of frontmatter; use Git for change history and resolved revisions
with dependent results. Preserve dated evidence and source citations in the
body when their meaning requires them.

Put the header above the `<init-prompt>` block. Paste only the block to start a
session. Keep `CLAUDE.md` exactly `@AGENTS.md`. Maintain execution declarations
with `deliverable.yaml` and the ScopeOfWork schema. Preserve frozen snapshots
and retained historical edition bytes at their selected source identities.

When adding metadata to a published source, keep its body and anchors stable.
Exclude the YAML header from rendered prose and regenerate affected derivatives
with the complete source fingerprint. Regenerate consumed workflow indexes when
package metadata changes. Consumers select revisions and adopt changes through
[their own route](../README.md#obtain-and-use-the-library).

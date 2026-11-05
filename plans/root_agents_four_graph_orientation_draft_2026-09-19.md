# Draft: orienting agents to four views of project information

Status: deferred agent-authored proposal, saved at the owner's direction on
2026-09-19. Not an instruction or adopted governance. Root `AGENTS.md` remains
unchanged. The owner will revisit whether and where this material belongs in
the governance documents; saving or merging this file does not settle that.

## Purpose and basis

The proposed addition would help agents discover relationships in the files,
folder structure and Git state according to the task. The intention is a short
orientation, without importing more of the project-management thesis into the
root entry instructions or requiring a new recurring procedure.

Context:

- [Illustrated four-graph explanation](four_graphs_of_knowledge_work_2026-09-19.html)
- [Earlier agent-facing orientation](four_graphs_agent_orientation_2026-09-19.md)
- [Theory draft](../docs/ai_software_project_management/01_theory.md), §4

The proposed placement in root `AGENTS.md` is unresolved. This file preserves
the assistant's draft from the conversation for later consideration. The four
views can concern the same work item; a folder location does not describe all
its relationships. Git commit ancestry is distinct from production dependencies.
Attention describes relating and synthesizing material, with traces in working
artifacts; it need not exist as a separately stored graph.

## Proposed text

```markdown
## Reading project information

Project information is carried by files, their folder structure, and Git
history and working state. Read this material through the views useful to
the task:

- Tree: composition, scope, identity and the local context of a work unit.
- Production graph: dependencies, prerequisites, interfaces and the order
  in which work can proceed.
- Network: sources, decisions, constraints, provenance and supersession
  that connect material across folder and package boundaries.
- Attention: selecting, comparing and synthesizing relevant material into
  an understanding, decomposition, plan or other contribution.

These are complementary views of the same work. Discover and traverse the
relationships needed for the question at hand, using existing records and
available tools. Expand the context when a relevant relationship leads
beyond the initial scope of inspection.

Git identifies versions and integration state; commit ancestry alone does
not establish production dependencies. Read the records that express those
dependencies and their basis. Likewise, a search result or derived graph
helps locate information but does not replace its source or establish
authority.

Use these views proportionately. There is no requirement to construct all
four graphs, scan the whole repository or rebuild an accepted project DAG
for every task.
```

## Deferred question

When the owner returns to this proposal, consider whether this brief orientation
belongs in `AGENTS.md`, which explanatory detail belongs in other governance
documents, and how those references should be distributed. No implementation,
instruction amendment or distribution work is initiated by this record.

# Four graphs of one node — orientation for agents

Status: draft for review, 2026-09-19. Not governance and not an instruction: it grants no authority and changes no procedure. `AGENTS.md`, the active role file, the project's instructions and the owner's directions govern. The claim that these four structures underlie knowledge work as such is the owner's; this note only says how they show up in this repository and how to use them. Illustrated companion: `plans/four_graphs_of_knowledge_work_2026-09-19.html`.

## The idea

Any piece of work here can be seen four ways. Each view answers a different question, lives in a different place, and fails in its own recognizable way. None of them substitutes for another. Before you act, know which view your question belongs to.

| View | Shape | Question it answers | Where it lives |
|---|---|---|---|
| Structure and working memory | tree | What is this made of? | git: the project's decomposition and its deliverable folders |
| Production and dependencies | directed acyclic graph | What must come before what? | the run's work graph; the project DAG; one git worktree per concurrent line of work |
| Topic query and long-term memory | network | What bears on what, and who decided it? | versioned files: decision registers, rulings, gap lists, owner-direction records; reached today by file search; intended: a rebuildable graph projection and a BM25-plus-vector index over the same files, called through a workflow or skill, never a separate source of truth |
| Attention and decomposition | attention: many inputs to one | How does all of this become one thing? | the model, with files, tools and instructions; the decomposition workflows |

## How to use each

**Tree.** A final node (a deliverable folder) carries a fixed kit: status, context, references, a typed scope of work, semantic lensing and review, dependencies, memory. The kit exists to make an agent that arrives at the node focused on that node. Read a node's scope and dependencies before you write anything into it. Do not use a node as a log, and do not file evidence under a node you chose by its name or by precedent; keep evidence in the owning run and record a provisional link.

**Directed acyclic graph.** It has two readings, for two jobs. The *blocker subset* is sequencing truth: to choose the next action you need only what blocks. *Full closure* is audit truth: to say the work holds, every node, edge, commit and hash must close. Keep both in the run's work graph, not in prose. If a handoff knows something the work graph does not, the work graph is stale; fix it first and derive the handoff from it.

**Network.** Decisions, rulings, constraints, gaps and the owner's directions cut across the tree: one of them can bear on many nodes. Before you decide or decompose, look up what already bears on the question. The edges that matter most are provenance: who decided this, in what words, when, and what it supersedes. Record the owner's words verbatim; label your reading and your decisions as yours; a later owner statement governs an earlier one. Never write your inference in the owner's voice. Facts in a record are easy to verify and provenance is not, so an error here survives audits and the next agent obeys it.

**Attention.** Decomposition and synthesis read everything against everything until a root and its levels emerge. It is the step a model does natively, and it is only as good as what it was given. Query the network first, so that a new decomposition does not repeat or contradict a decision already made. State what you rejected and why, not only what you chose.

Footnote: attention is all the *model* needs. The work also needs a tree, a graph and a memory, and a person at two edges of the loop. Being good at this step says nothing about whether the other three were respected.

## How they connect

Decomposition produces the tree. The tree's dependencies seed the production graph. Production generates evidence and decisions, which belong in long-term memory. Memory is what the next decomposition queries first. It is a loop across passes and acyclic within one.

The owner owns two edges of that loop: what production is allowed to put into memory as something to rely on (acceptance), and what memory sends into the next decomposition (steering). Agents own the rest. When the owner cuts or defers an edge on purpose (for example, letting production run ahead of the deliverable tree and reconciling later), record the links you would have made as provisional. Do not repair the edge yourself.

## What a violation looks like

- Tree: notes and evidence accumulate in deliverable folders nobody read. Someone will have to find and re-file them.
- Graph: state lives in handoff prose and the work graph is out of date. The next session plans from the wrong picture.
- Network: an agent's conclusion appears in a later document as the owner's direction, every hash around it verifies, and the next agent follows it.
- Attention: a fluent plan that contradicts a recorded decision, because nothing was looked up first.

## The measure

Adopted by the owner in session on 2026-09-19 (verbatim in `plans/evidence/2026-09-19_owner_words_four_graph_structures.md`): the quality of the system is how much warranted confidence it produces per unit of the owner's attention, and a validation level sets how much of that confidence a given piece of work needs.

What follows for an agent:

- Spend the owner's attention only where judgment is needed. Whatever a machine can verify (closure, hashes, protected tests, byte-identity), verify it and report the result as a fact.
- When you bring the owner a decision, help them understand it, not only approve it: the conflict with its numbers, the alternatives you rejected, what a change does before and after, and how to reverse it.
- The validation level of a piece of work follows its consequence and its reversibility. You do not lower it to finish sooner; that is the owner's decision or a rule the owner wrote. Say at what level the work was validated when you hand it over.
- Some things do not toggle at any level: protected criteria, provenance and honest claims.

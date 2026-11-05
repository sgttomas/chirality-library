# Agent and Workflow Runtime Contract

> Historical App v3 and Runtime implementation paths in this reference resolve through [Frozen products](../projects/FROZEN.md), not the current working tree. Their contracts apply only upon explicit reactivation.

Technical reference for existing host integrations. Development instructions live in [AGENTS.md](../AGENTS.md).

Interface adoption remains project-specific; this reset does not establish final acceptance, downstream qualification or release of prospective interfaces. This document describes configuration and loading, not host enforcement.

Under the retained App v3/Runtime contract, the Runtime project owns production
discovery, context supply, session history, replay, permissions, and execution.
This allocation does not appoint a production provider for the current Root
library or an independent consumer. Each consumer's adopted basis determines
which interfaces apply; consultation alone does not adopt this contract.
Root Python utilities are authoring,
compatibility, and validation references for this contract; their presence or
successful execution does not establish the production provider implementation.

## Role configuration

`agents/registry.json` is the machine-readable role inventory. It has
`schema_version: 1` and a `roles` object keyed by the four role names. Each role
contains:

| Field | Meaning |
|---|---|
| `instruction` | Repository-relative path to its four-section instruction file |
| `type` | Integer 0, 1, or 2 |
| `direct_entry` | Whether the human may select this named role directly |
| `delegates_to` | Named roles eligible for managed delegation |
| `allow_generalist_agent2` | Whether bounded ephemeral Type 2 execution is eligible |
| `tools` | Role capability ceiling, using runtime capability names |
| `write_scope` | Scope ceiling description; actual writable targets come from the brief |

HELP_HUMAN is Type 0, directly selectable, with HELPS_HUMANS, WORKING_ITEMS, and
TASK as eligible named children. HELPS_HUMANS and WORKING_ITEMS are directly
selectable Type 1 roles and may dispatch TASK. These three roles may also use
bounded ephemeral Type 2 instances. TASK is Type 2, has no direct-entry or
delegation eligibility, and cannot launch another executor.

Native descendant creation and role assignment are distinct. The registry states role conduct
and managed eligibility. A host must report the actual enforcement boundary.
The registry never grants a filesystem path or bypasses host permission checks.

## Method libraries and catalogs

Skills and workflows are independently modeled methods, with different ordinary
App discovery policies:

| Library | Project | User | Bundled | Ordinary App policy |
|---|---|---|---|---|
| Skills | `.agents/skills/<name>/SKILL.md` | `~/.agents/skills/<name>/SKILL.md` | App-supplied reviewed skill library | Follow Codex's native discovery of all three sources; display each skill's origin |
| Workflows | `.chirality/workflows/<name>/WORKFLOW.md` | `~/.chirality/workflows/<name>/WORKFLOW.md` | App-supplied reviewed workflow library; Root source packages currently live under `workflows/` | Discover all three sources |

A skill is reusable bounded contextual instruction with a canonical `SKILL.md`.
A workflow is reusable coordination or method guidance with a canonical
`WORKFLOW.md`. Either may be simple or complex. A selected workflow is optional
unless the brief or an accepted instrument requires one. Skills, workflows,
tools, roles, briefs, and plans remain distinct.

Catalog operations are `list`, `inspect`, and `selected-context`. `list` returns
names, descriptions, source class, source root, source-qualified identity, and
collision status without loading bodies. `inspect` returns one explicitly named
definition and its metadata. `selected-context` returns only explicitly selected
method bodies and requested resources, with fingerprints and selection order.

For workflows, unqualified lookup precedence is project, then user, then
bundled. Selection retains source-qualified identity; a result is never reduced
to its basename in run history. Every workflow collision exposes all origins.
Discovery after selection may report a higher-precedence collision, but it must
not silently replace the selected workflow. Explicit source qualification
resolves a collision. In a deployment adopting the Root-governed shared suite,
project instructions and workflows may specialize it but cannot weaken that
adopted Root governance. Wherever this contract is adopted, project instructions
and workflows cannot escape the active working root; that containment restriction
does not depend on adopting Root governance. Root's repository
grants do not transfer to independent consumers. Their governing instructions,
adopted contracts and authorized undertaking supply authority; actual host
permissions constrain execution. Source-qualified selection and collision
handling do not themselves grant permission.

Ordinary App skill availability follows Codex's native discovery
(`skills/list` over project, user, and bundled skills) under D-GOV-43 item 10.
The App offers read-only, less prominent skill inspection that shows each
skill's origin; the former bundled-only trust restriction on ordinary App
skill resolution is superseded. Project and user `SKILL.md` inspection remains
available to Root reference and standalone compatibility interfaces, and
original identities remain valid historical evidence. Read-only replay may
render the exact preserved bytes and origin of an earlier selection, or report
historical bytes unavailable, without activating that skill for a new model
turn. A historical selection is never silently rebound to a same-named
definition from another origin.

Context-supplied skills that do not originate at a readable filesystem library
are labeled `context-supplied` with the provider origin and available
fingerprint. Do not invent a filesystem path, claim local installation, or
present unavailable bytes as replayable.

## Workflow packages

Within each workflow library, the discoverable inventory consists of immediate
subdirectories containing `WORKFLOW.md`. Its YAML `name` matches the folder;
`description` explains the undertaking briefly. The body supplies guidance, including
branching, iteration, coordination, artifact contracts, and recovery when
applicable. Resources are optional and loaded as needed. Existing legacy
package status survives migration and is explicit in the workflow inventory.

Optional `execution.json` companions use `schema_version: 1`. They declare
`compatible_roles` and optional `tools` restrictions. `tools.capabilities` is a
list of runtime capability names. `tools.commands` is a list of legacy
`<interpreter> tools/path:<scope_glob>` expressions, preserved losslessly with
placeholders bound by the brief. Capability and command restrictions intersect
independently with their corresponding outer policies; never compare command
expressions with capability names. Missing restrictions inherit the applicable
outer policy; an explicit empty command list denies shell commands. A host that
cannot enforce an expression records the boundary as instruction-asserted. Absence of a companion means no additional workflow restriction;
it does not expand the role or brief. A workflow requiring delegation belongs
with a compatible manager. A TASK assignment selects a separately bounded child workflow or a bounded
brief. It cannot load an incompatible manager workflow by labelling the whole
workflow a bounded stage.

`Workflow: <name>` normally selects a workflow. The legacy-input adapter first
applies the explicit converted-alias exception described below; a
source-qualified identity bypasses that exception. A run may select multiple
methods as an explicit ordered list. The
order records intended composition and does not imply that later methods
override earlier ones. Conflicting requirements are surfaced before execution.

`TaskSkill: <name>` is accepted by the legacy-input adapter. An unqualified
legacy `Workflow` name present in `workflows/legacy-methods.json` uses the same
explicit conversion and may resolve to a canonical skill. If `Workflow` and
`TaskSkill` select the same resolved source-qualified identity, resolve once.
Different selections fail as conflicting input unless an explicit
ordered-method adapter maps both while preserving their original fields and
order. A source-qualified `Workflow` identity explicitly preserves its
historical workflow and bypasses alias conversion. New selections use the
complete `kind`, `source`, `sourceRootId`, and `name` identity. Original
compatibility fields, mapping decisions, and resolved identity remain distinct
evidence. Retired agent identifiers are resolved through the migration ledger
to a role and workflow,
never re-registered as roles. Historical evidence retains the session type,
role identifier, `TaskSkill`/`Workflow` inputs, resolved origins, and adapter
decisions actually used. Historical flat `.chirality/workflows/*.md` files
remain ordinary documents and are not reinterpreted as canonical workflow
packages. Project workflow discovery recognizes only
`.chirality/workflows/<name>/WORKFLOW.md` packages.

Workflow authoring is chat-driven and follows the core `create-workflow`
workflow. On a user's request, an authorized agent prepares a project or user
workflow package with the available file tools, subject to the active
permission policy, real-path containment, and the package metadata rules above.
In the App it writes a draft at `.chirality/workflow-drafts/<name>/WORKFLOW.md`
under the project or user root, with its resources inside the draft and no
symbolic or hard links, and validates the entrypoint and resources. The human
inspects the draft, gives feedback in chat, and registers the reviewed bytes
through the Workflows panel; registration does not overwrite an existing name
or run the workflow. Another host presents the complete package for the
human's explicit acceptance before it is registered through available file
tools. The agent does not write straight into `.chirality/workflows` as a
substitute for review, and reports discovery only after observing the
refreshed catalog. Revising a registered workflow follows the revision route in
`create-workflow`. The MVP has no separate workflow-editor surface or alternate
workflow document format.

## Context selection and execution

Ordinary selective App context contains the product `AGENTS.md`, applicable
native user/project instructions, the active role instruction, and the names and descriptions of
the skills Codex reports as available. It excludes other full role
instructions, broad governance documents, and unselected method bodies. Selected skill/workflow bodies and
only the resources needed for the current stage load on demand. A selected
resource must exist and remain within its source package after real-path
resolution. Deliberate wider-index consultation is a recorded catalog
operation, not routine context expansion.

For the desktop App, the product default is maintained at
`projects/chirality-app-dev/instructions/AGENTS.md`. The App seeds an editable
`instructions/AGENTS.md` under its own user data, preserves it across updates,
and exposes opening and restoration through Settings. Codex owns global and
project `AGENTS.md` discovery, including native override precedence; Runtime
does not inject a second project copy on this path. The product file and only
the active full role are additive to Codex's base instructions. The Root
repository entry and other open-source references remain available for their
applicable work.

Native named-role configuration carries common product guidance plus one full
role. Its immutable paths are bound to the primary's adopted instruction basis
so an edit does not change running descendants. Fresh role dispatch uses a
bounded brief and fresh child context; arbitrary full-history forks do not
establish role replacement. User native feature, model and depth settings are
preserved. At Codex 0.154.0, a loaded thread can ignore instruction overrides;
changed persistent guidance therefore requires confirmed idle unload followed
by cold resume and acknowledged developer-level history injection before
another turn. Configuration alone does not establish that restored history
received new guidance. Record the actual supplied update text and hash; an
uncertain acknowledgment leaves the user turn unstarted. Failed or deferred adoption remains
explicit and must not be represented as successful application through a
user-message append. Historical instruction basis and the visible conversation
remain intact.

The provider returns exact supplied origins, content hashes when bytes are
available, ordered selection, resource history, and context events. Governed
session history and replay preserve what was actually supplied, including
source-qualified identities and amendments. A current file with the same name
is not substituted during replay. When exact historical bytes are unavailable,
replay reports that limit rather than claiming exact reconstruction.

Conversational or structured run-specific instructions form the brief. A
structured brief identifies purpose, governing basis, scope, required context,
tools, writable targets, expected outputs, acceptance checks, and return path
when those controls are needed.
A workflow may be omitted. Loading one does not grant permissions or alter role
type. Effective authorization is bounded by the host, role, workflow, and brief.
An empty explicit tool allowance permits no tools; a missing optional workflow
restriction adds no restriction. Write targets must be explicit and contained in
the authorized working root; `ScopePath` alone does not grant writes.

Selection, compatibility, coordination, and execution are separate acts.
Selecting a method loads guidance; compatibility determines whether the active
role may use it; coordination may propose a route; execution requires an
authorized actor and actual host operation. A method selection never silently
switches roles or launches a task. HELP_HUMAN may coordinate a request that
needs `project-setup`, but execution routes to an eligible WORKING_ITEMS
instance under the normal authority and brief rules.

The tool root is declared independently from the working directory. Commands
resolve against that root or their workflow package. Agents invoke them through
available session capabilities and interpret their results according to the
workflow. A documented command is not evidence that a host exposes it.

Freeze role instructions, selected methods/resources, and brief revisions for
a run. Record actual supplied context and hashes where the mechanism exposes
it. Describe instruction-mediated loading as instruction-asserted, separately
from mechanically recorded loading. Amendments name changed basis and scope;
new role instructions take effect between runs.

## Interaction, permissions, plans, and replacement

The App MVP uses Codex as its sole engine qualification and release target.
Model selection within Codex is recorded as model configuration and does not
constitute engine replacement. The App-facing Runtime engine registry contains
Codex only for the MVP. Generic provider-succession fields below and
retained compatibility surfaces preserve historical and standalone behavior;
they do not establish qualified MVP support for another engine, permit one to
substitute for required Codex capability, or authorize its release.

`interactionMode` distinguishes ordinary conversation from qualified native
Plan Mode. Native Plan Mode is selectable only when the active adapter
advertises qualified support; an unsupported request is exposed as unavailable
or as the adapter's typed capability result rather than being silently
simulated. Plan revisions and history remain in the same conversation. The
default plan is stored with that conversation; export to a project file occurs
only when the user explicitly selects it. Ordinary native Plan Mode creates no
decomposition checkpoint by itself.

`permissionMode` maps onto the user's chosen Codex approval policy and
sandbox mode, selected per project with per-turn override from Codex's own
options (D-GOV-43 item 4), and is orthogonal to `interactionMode`: changing
modes grants no permission beyond what the host enforces, and changing a
permission mode does not add a semantic human checkpoint. A native
host plan is an ad hoc plan representation unless a source-qualified workflow
explicitly adopts it; adapters preserve this qualification and do not relabel
it as an accepted repository workflow. Plans remain optional and may compose
ordered workflows, skills, tools, and authorized delegation.

One conversation may safely replace a method or provider when the transition
has an explicit boundary event. Finish or suspend the prior method, record its
state and supplied context, select the successor by source-qualified identity,
recompute effective permissions, and preserve the conversation history. A
replacement does not inherit unrecorded state, permissions, or acceptance from
its predecessor. Provider succession records both providers and the exact
handoff boundary.

## Structured brief compatibility

The Root reference utility `tools/workflow_runtime/resolve_workflow.py` accepts
`--root <instruction-root> --role <role>` and optional `--workflow`,
`--task-skill`, or `--legacy-agent`. Repeat `--resource <package-relative-path>`
to request stage resources. No resource selection overrides whole-workflow
role compatibility.

`--brief <json-file> --repo-root <active-checkout>` accepts structured inline
fields and an optional structured file brief. `InitTaskPath`/`INIT_TASK_PATH`
selects that file; otherwise the adapter checks `ScopePath/INIT-TASK.md` and then
`DeliverablePath/INIT-TASK.md`. File values fill omitted inline fields; inline
values take precedence, while inconsistent path fields or aliases fail.
The file is a YAML mapping or has YAML frontmatter. The caller interprets prose
briefs into explicit fields before using this adapter.

`DeliverablePath` supplies a context anchor when `ScopePath` is absent.
`TaskProfile: DELIVERABLE_TASK` remains a compatibility label and selects no
method. Unsupported profiles fail. Roots bind independently from CWD; explicit
working roots and resolved scopes remain contained in the active checkout.
The inferred project/domain root or checkout fallback establishes a path anchor,
not authority to maintain Root instructions or execute product work.

The structured adapter defaults `ApplyEdits` to false and then returns no
writable targets. With edits enabled, `AllowedWriteTargets` supplies explicit
contained targets; the host still enforces their effects. The read-only role
ceiling clears targets for HELP_HUMAN. `AllowedTools` supplies command
expressions, independently from capability names in `--policy`. The policy
object carries optional host/brief restrictions and placeholder bindings.

Command restrictions return as conjunctive `effective_tools.commands.all_of`
layers, each containing alternatives. This preserves intersecting scope rules
without approximating them as a single glob. The utility evaluates declared
command/target claims; a host must establish and enforce actual process effects.
The utility README specifies these interfaces and return fields. Resolver
success establishes reference input processing, not production catalog parity,
downstream adoption, context delivery, compatibility, coordination, execution,
model delivery, or replay fidelity.

## Role authoring shape

A role instruction has a title and four ordered sections: PROTOCOL (conduct),
SPEC (standards), STRUCTURE (relationships), RATIONALE (purpose). Machine metadata
belongs in agents/registry.json. Workflow authoring follows create-workflow;
format schemas remain in workflows/catalog.schema.json and the catalog index.
Historical R-identifiers are in [the compatibility reference](COMPATIBILITY_FORMATS.md).

## Retained Runtime process interface

The following service and process requirements retain their App v3/Runtime
subject. They apply only upon explicit reactivation, as qualified above, and do
not establish a current provider implementation or App v4 architecture.

The `projects/chirality-runtime/` project owns versioned contracts, provider-neutral
orchestration, the Runtime service, a Unix-socket client, a CLI, and safe
engine/provider adapters. It is an independent Node workspace with its own
lockfile. Project applications consume its public packages; private project
adapters do not become generic runtime dependencies. The service composition
stays independent of Electron and Next so a later Chirality application can
run it as its own sidecar (D-GOV-43 A2 supplement).

### 14.1 Application-owned Runtime service and Codex child

The Chirality App starts one Runtime service as a child process at launch,
owns it for the life of the App instance, and stops it deliberately on quit.
There is no per-user LaunchAgent, installer, or headless daemon mode. The
service reports readiness with one ready line on its standard output; the App
waits for that line before routing any request. If the service exits
unexpectedly the App restarts it with bounded backoff and shows the outage;
it never presents unexpected termination as completion.

The service's only control listener is one Unix-domain socket beneath the
application user-data directory, with a `0700` parent directory and a `0600`
socket. Stale-socket recovery verifies current-user ownership and absence of a
live recorded process before removal. The App issues a per-launch client
token, stored under user data and private to the application, and presents it
on every request; the token is not exposed to the renderer. No second socket
and no TCP listener exist under any configuration. The service's HTTP/1.1
JSON and SSE routes cover health, project registration and status, thread
create, list, resume, turn, interrupt, and server-request answers, and
Codex-managed login and logout.

The service owns the stock, version-pinned `codex app-server` child from the
official `@openai/codex` distribution, launched over stdio against Chirality's
effective Codex home, which shares the user's configuration, skills, plugins,
MCP definitions, instruction caches, and sessions store by reference and
keeps `auth.json` and the models cache private. The service forwards the
complete notification and server-request stream; every server request
receives an answer, and an unfamiliar request receives an explicit error
response rather than silence.

Execution, observation, interruption, and shutdown are distinct. The Runtime
owns the active turn. The renderer observes it through loopback HTTP and SSE
served by the in-process Next server; a renderer subscription that drops does
not stop the turn, and reopening recovers current state, missed activity, and
outstanding decisions without re-sending the prompt or executing twice.
Explicit Stop is the interrupt. Quit stops the owned Runtime and Codex
processes deliberately and leaves an accurate continuation record; no
unattended execution after quit is promised.

The App keeps a thread index keyed by Codex thread id in its operational
user-data state (title, project, role, plan revisions, workflow selections,
evidence pointers). On relaunch the App resumes an indexed thread through
`thread/resume`; the sidebar shows the App's index, not every thread in the
shared store.

### 14.2 Project manifests and sessions

Each registered checkout supplies `chirality.project.json`. Schema
`chirality.project/v1` remains supported for in-tree manifests with relative
working and instruction references. Schema `chirality.project/v2` declares
`instructionRoot: {"mode":"runtime"}` so an external writable checkout can
consume the read-only `CHIRALITY_INSTRUCTION_ROOT`. V2 registration requires
that root to be readable and disjoint from the working root. Both schemas carry
a stable project ID and display name, execution and profile references, enabled
adapter IDs, and an embedded-UI declaration. Registration containment-checks
the resolved paths and records the manifest hash and approval outside the
checkout. Privileged execution stops on manifest drift until re-registration.

Threads are ordinary Codex threads in the shared Codex sessions store of
Chirality's effective home; the App keeps its own index and metadata keyed by
Codex thread id under user data (§14.1). Both are operational,
non-authoritative state. Daemon-era session records beneath
`{userData}/runtime/projects/<projectId>/sessions` are preserved unchanged in
place as a readable archive; no import is a release prerequisite, and their
continuation as Codex threads is not promised. Chirality evidence required by
a governing workflow is written to checkout-contained project evidence in
JSON/JSONL.

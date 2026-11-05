# Package activation and production

WORKING_ITEMS applies this method to a package-based undertaking; its general role also accepts other bounded undertakings.

1. Resolve PackageID, package path, selected deliverables, accepted source/decomposition basis, objective, completion criteria, authorization, dependencies, and write ownership. A single-deliverable undertaking selects that deliverable within its parent package.
2. Inspect the selected ScopeOfWork, current Work, needs, relevant source evidence and Git state. Read historical control or recovery records only where the project actually adopts or needs them. Resolve each PROJECT/SOFTWARE representation as LEGACY_FOUR_DOC, SOW_V1, MIGRATION_DUAL, AMBIGUOUS, or INVALID. MIGRATION_DUAL requires the exact isolated conversion grant; ambiguous/invalid state remains blocked for dependent production. Do not require a lifecycle file for current SOW_V1 work.
3. Use `construct-local-work-graph` to derive the selected undertaking's work graph from consumer-local `deliverable.yaml` needs, scope and relevant work material in the project's adopted locality (`Work/` by the shared default). Include objectives, actual input/use conditions, read context, write ownership, integration owner, expected returns and concurrency. Assess each needed condition from evidence; retain source unknowns and reciprocal/technical holds. Record the descriptive posture and revise the plan as actual conditions change; a saved view does not become dependency authority.
4. Assign disjoint work whose actual input conditions permit the selected activity to TASK or an authorized ephemeral Type 2 instance. Each brief names its context, tools, writes, outputs, acceptance, dependencies, and return path. Serialize overlapping writes.
5. Record, relay, amend, hold, replan, escalate, or route updates through the parent. Version amendments and preserve claim status and evidence. A direct-human manager presents cross-package decisions to the human.
6. Before integration, reconcile the concrete result and verification with affected ScopeOfWork, Work and dependency conditions/pointers in the same change. The implementation owner carries this into every brief; TASKs report their slice's effects, and the integration owner checks the combined result. Revise what changed, add and connect new material where needed, and preserve unchanged declarations and historical evidence. Use `bounded-reconciliation`; a no-edit finding needs only a brief return/PR statement. Missing required behavior remains unfinished work.
7. Verify the changed result, relevant consuming paths and permitted write scope.
Return usable outputs, checks and remaining conditions or reserved choices in the
actual review/change record. Keep a recovery note only for a concrete need. Follow
the owning project's Git conventions; integration is not owner acceptance or
release. Formal scope changes and explicitly adopted lifecycle decisions retain
their real authority. This method does not require routine receipts or a handoff
chain, and it does not itself require Git.

When runtime telemetry is required, use tools/workflow_runtime/runtime_telemetry.py with stable session/event IDs. Record attempts, checks, retries, remediations, detection layers, failure classes, reason codes, member IDs, and dispositions. Exposed token/context occupancy may be recorded; missing measurements remain explicit. Bind RUNTIME_SUMMARY.json in the package manifest and disclose interrupted sessions and required reruns.

For representation conversion, load workflows/scope-of-work/resources/representation-migration.md. Each child brief names affected OUT-*, REQ-*, AC-*, VER-* IDs or the frozen mapping basis and exact migration authority.

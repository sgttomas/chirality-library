# Deterministic evaluation tools

Run commands using the declared tool root. Input workspaces are read-only; only
explicit report destinations are written. Commands work independently of the
current working directory. Report paths must be outside production-unit source
paths, including flat DEL localities. These commands perform mechanical checks;
the invoking workflow interprets their findings and owns acceptance.

## Native DEL dependencies

```sh
python3 "$INSTRUCTION_ROOT/tools/evaluation/audit_dependencies.py" --project "$PROJECT_ROOT" --output "$REPORT_DIR/dependencies.json"
```

`--project` is the project root containing the execution localities, rather
than necessarily the execution directory itself. Native document, evidence,
code and check paths resolve relative to that project root. The audit invokes
`tools/deliverables/cli.py --project <project> check` with the project as its
working directory. Python 3, PyYAML, Git, an existing repository and a resolvable
HEAD are required; the project must be inside that repository. Missing inputs
produce `FAILED_INPUTS`; the audit never silently switches parsers or reads
other dependency representations. When the native query is unavailable, the
invoking workflow may inspect selected `deliverable.yaml` files directly and
state that limitation.

The nested `query` is the native check result, including its Git/working-tree
basis, structural errors, each declared need with its source location,
reference-presence observations, unknown references and native cycle
components. Distinct conditions and triggers between the same endpoints remain
separate. Outward obligations retain their direction. No CSV or Markdown
dependency companion, central graph or acceptance record supplies query input.
See [native query semantics](../deliverables/README.md) for the parser contract.

JSON schema v2 has `root`, `run_status`, `subject_status`, `issues`, `assessment`,
`query`, and, when the query establishes a basis, `summary`. Summary counts are
valid deliverables, needs, unknown references and native cycle components.
`PASS` means only that the query found no structural errors in the metadata it
read. Invalid metadata produces `FAIL` and preserves usable partial results;
no metadata produces `NOT_ASSESSED`. This does not establish that every intended
locality exists or that all useful needs were declared. Use a selected structure
inventory or decomposition comparison for that separate question.

Unknown references and cycles do not fail this structural subject assessment.
The cycle graph includes upstream relations between native DEL declarations,
including non-gating relations; it excludes outward obligations and non-native
or absent endpoints. Cycle components are not every simple cycle and do not
establish a complete accepted project graph. Supplier or path presence does
not establish suitability, availability, satisfaction, completion or readiness.
Every need's suitability remains unknown. Checks are referenced, never executed.

## Workspace structure

```sh
python3 "$INSTRUCTION_ROOT/tools/evaluation/audit_structure.py" --root "$EXECUTION_ROOT" --variant SOFTWARE --output "$REPORT_DIR/structure.json"
```

`--variant` is required: PROJECT and SOFTWARE discover immediate live
`PKG-*/{1_Working,2_Checking,3_Issued}/DEL-*` units; DOMAIN discovers
`CAT-*/{1_Working,2_Checking,3_Issued}/KTY-*`. To audit an
accepted list, including missing units or flat localities, supply
`--inventory inventory.json`:

```json
{"schema_version":1,"units":[{"path":"PKG-01_Example/1_Working/DEL-01-01_Result","required_files":["Result.md"]}]}
```

Paths resolve within the execution root. Each unit is unique. DEL localities
require `deliverable.yaml` alongside `_STATUS.md`, `_CONTEXT.md` and
`_REFERENCES.md`. The structure audit checks presence; the native dependency
query checks YAML structure. `required_files` extends those requirements.
DOMAIN checks declared content through `required_files`; KTY dependencies are
outside this audit's assessment. The tool neither requires nor observes their
dependency companion files. The selected inventory and actual materialized
directories are different facts; use a decomposition audit for full forward/reverse declaration
reconciliation.

JSON v1 includes `variant`, `contract`, `inventory_source`, `units`, `partitions`,
`tool_roots`, `summary`, and `issues`, alongside common status fields. Unit rows
include presence by filename, current lifecycle state, format resolution, and
specific violations. Current State is parsed as an explicit Markdown/plain-text
field; explicit historical `State:` syntax is a compatibility input. Ambiguous
multiple current fields fail. Historical narrative state words are ignored.
RETIRED is recognized; retired units remain in the census without requiring
active production content. OPEN units may lack production content; initialized
and later active states require a valid production format. Any present partial
or invalid format is reported even for OPEN/RETIRED units.

PROJECT/SOFTWARE format uses the canonical SOW resolver and reports `SOW_V1`,
`LEGACY_FOUR_DOC`, `MIGRATION_DUAL`, `AMBIGUOUS`, or `INVALID` with its detailed
findings. `--isolated-migration --migration-authority <exact-authority>` passes
through to that resolver; authorized dual content has `accepted_baseline=false`.
DOMAIN format is `NOT_APPLICABLE`, with its declared content checked separately.
The report names `structure-audit/v1` and its SPEC basis for required partition
and tool directories; an audit result is limited to those checks.

## Command status

Both audit CLIs accept `--output -` for JSON on stdout. A completed observation
has `run_status=COMPLETE` and exits 0 even when `subject_status=FAIL`. Bad invocation
or unavailable audit input/output exits 2. A valid empty scope is
`NOT_ASSESSED`, not evidence of subject conformity. Callers must inspect both
statuses and findings. Malformed native metadata is an observed structural
defect; unavailable Git/HEAD/project inputs prevent the dependency observation.

`count_deliverable_files.sh` and `extract_lifecycle_states.sh` return the SOFTWARE
structure JSON report; the former retains its production-format migration flags.
Consumers requiring another variant use the explicit Python CLI.

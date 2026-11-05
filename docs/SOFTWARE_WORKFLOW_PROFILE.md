# Software check profile

Technical reference for existing `software-workflow.json` consumers.
Use checks proportionate to the change; this profile does not require a workflow,
activation packet or duplicate local execution of checks already run by CI.

## Profile schema

Profiles use `chirality-software-workflow/v1` JSON:

```json
{
  "schema": "chirality-software-workflow/v1",
  "project_root": ".",
  "workspace_root": ".",
  "checks": {
    "unit": {"cwd": ".", "command": ["python3", "-m", "pytest", "-q"]}
  },
  "always_checks": [],
  "path_rules": [
    {"paths": ["src/**"], "checks": ["unit"]}
  ]
}
```

`project_root` defines project-relative path rules. `workspace_root` is the
outer containment boundary for registered check working directories and may
include repository-level governance checks. Commands are argument arrays
executed without a shell. A profile is a
registered tool surface, not permission to run unlisted commands. Agent briefs
still declare the checks and write targets allowed for the run.

### Optional managed service

A check that requires a local execution substrate may declare one `service`
object. `run_registered_checks.py` allocates an isolated loopback port when
`port` is `auto`, starts the registered service without a shell, waits for the
registered readiness URL, injects only the declared `check_env`, executes the
check, and terminates the service in all outcomes. Service and check working
directories remain inside `workspace_root`.

```json
{
  "checks": {
    "premerge": {
      "cwd": "frontend",
      "command": ["npm", "run", "validate:premerge"],
      "service": {
        "cwd": "frontend",
        "command": ["node", "server.js", "--port", "{port}"],
        "port": "auto",
        "ready_url": "http://127.0.0.1:{port}",
        "env": {"PROVIDER": "stub"},
        "check_env": {"BASE_URL": "http://127.0.0.1:{port}"},
        "startup_timeout_seconds": 60,
        "shutdown_timeout_seconds": 10
      }
    }
  }
}
```

`{port}` substitution is supported only in registered service command values,
service environment values, check environment values, and `ready_url`.
Service setup failure is reported separately with exit code `125`; check
timeout remains exit code `124`. Normalized evidence records readiness,
startup duration, bounded log tails, exit state, and confirmed shutdown.

## Canonical tool responsibilities

- `discover_repository.py`: manifests and test surfaces.
- `select_affected_checks.py`: deterministic path-rule selection.
- `run_registered_checks.py`: registered checks and normalized JSON evidence.
- `validate_change_scope.py`: changed-path containment.
- `compare_structured.py`: JSON API/schema/migration comparison.
- `verify_generated_manifest.py`: generated-file digest drift.

Tool output is generated evidence. It becomes accepted workflow state only
through the owning manager's validation and applicable human gates.

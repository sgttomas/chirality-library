#!/bin/zsh
# Current preparation uses --current --prepared; after ScopeOfWork authoring,
# omit --prepared. Unflagged calls retain the legacy control-files contract.
if [[ "${1:-}" == "--current" ]]; then
  shift
  exec "${PYTHON:-python3}" "${0:A:h:h}/scaffolding/current_locality.py" check "$@"
fi
# check_min_viable_fileset.sh
# Verifies metadata and the native DEL identity/needs declaration.
#
# Usage: ./check_min_viable_fileset.sh <DELIVERABLE_PATH> [ACCEPTED_DEL_ID]
#
# Inputs:
#   DELIVERABLE_PATH — Path to a single deliverable folder
#
# Outputs:
#   PASS (exit 0) if required files and native DEL declaration are valid.
#   FAIL (exit 1) if required files are absent or DEL schema/identity disagrees.
#
# Example:
#   ./check_min_viable_fileset.sh ./execution/PKG-001_.../1_Working/DEL-001-01_...

DEL_PATH="${1:?Usage: $0 <DELIVERABLE_PATH>}"

REQUIRED_FILES=(
  "_STATUS.md"
  "_CONTEXT.md"
  "_REFERENCES.md"
  "_SEMANTIC.md"
)
if [[ "${DEL_PATH:t}" == DEL-* ]]; then
  REQUIRED_FILES+=("deliverable.yaml")
fi

missing=()
for f in "${REQUIRED_FILES[@]}"; do
  if [ ! -f "$DEL_PATH/$f" ]; then
    missing+=("$f")
  fi
done

del_name=$(basename "$DEL_PATH")
del_id="${del_name%%_*}"

if [ ${#missing[@]} -eq 0 ]; then
  if [[ "${DEL_PATH:t}" == DEL-* ]]; then
    TOOL_ROOT="${0:A:h:h:h}"
    "${PYTHON:-python3}" - "$TOOL_ROOT" "$DEL_PATH" "${2:-}" <<'PY'
import re
import sys
from pathlib import Path

sys.path.insert(0, sys.argv[1])
import yaml
from tools.deliverables.cli import Invalid, UniqueLoader, parse

folder = Path(sys.argv[2])
source = folder / 'deliverable.yaml'

def read_identity_source(path):
    if path.is_symlink() or not path.is_file() or not path.resolve().is_relative_to(folder.resolve()):
        raise Invalid(f'identity source must be a contained regular file: {path}')
    return path.read_text(encoding='utf-8')

try:
    obj = parse(read_identity_source(source), str(source))
    local = re.match(r'^(DEL-\d+-\d+)(?:[_-].*)?$', folder.name)
    accepted = re.fullmatch(r'(DEL-\d+-\d+)(?:_.*)?', sys.argv[3]) if sys.argv[3] else None
    if not local or obj['id'] != local.group(1):
        raise Invalid('YAML id disagrees with owning deliverable folder')
    if sys.argv[3] and (not accepted or obj['id'] != accepted.group(1)):
        raise Invalid('YAML id disagrees with accepted deliverable identity')
    scope = folder / 'ScopeOfWork.md'
    if scope.exists() or scope.is_symlink():
        front = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)', read_identity_source(scope), re.S)
        fields = yaml.load(front.group(1), Loader=UniqueLoader) if front else None
        if not isinstance(fields, dict) or fields.get('deliverable_id') != obj['id']:
            raise Invalid('YAML id disagrees with ScopeOfWork.md deliverable_id (or its binding is absent)')
except (Invalid, OSError, UnicodeError, RecursionError, yaml.YAMLError) as exc:
    print(f'FAIL: {source} — {exc}')
    sys.exit(1)
PY
    if [[ $? -ne 0 ]]; then
      exit 1
    fi
  fi
  echo "PASS: $del_id — minimum fileset valid (structure only)"
  exit 0
else
  echo "FAIL: $del_id — missing ${#missing[@]} file(s): ${missing[*]}"
  exit 1
fi

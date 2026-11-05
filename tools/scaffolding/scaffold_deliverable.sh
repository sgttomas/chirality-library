#!/bin/zsh
# --current selects PKG-nn/DEL-nn-nn/{Work/,deliverable.yaml}; ScopeOfWork is
# authored separately. Unflagged calls retain the legacy interface below.
if [[ "${1:-}" == "--current" ]]; then
  shift
  exec "${PYTHON:-python3}" "${0:A:h}/current_locality.py" deliverable "$@"
fi
# scaffold_deliverable.sh
# Creates metadata stubs and a native needs declaration for DEL localities.
#
# Usage: ./scaffold_deliverable.sh <WORKING_DIR> <DEL_ID> <DelLabel>
#
# Inputs:
#   WORKING_DIR — Path to package's 1_Working/ directory
#   DEL_ID      — Deliverable identifier (e.g., DEL-001-01)
#   DelLabel    — Human-readable label (e.g., "Preliminary-Design")
#
# Outputs:
#   Deliverable folder with four metadata stubs and deliverable.yaml for DEL.
#
# Example:
#   ./scaffold_deliverable.sh ./execution/PKG-001_Architectural\ Design/1_Working DEL-001-01 "Preliminary-Design"

WORKING_DIR="${1:?Usage: $0 <WORKING_DIR> <DEL_ID> <DelLabel>}"
DEL_ID="${2:?Usage: $0 <WORKING_DIR> <DEL_ID> <DelLabel>}"
DEL_LABEL="${3:?Usage: $0 <WORKING_DIR> <DEL_ID> <DelLabel>}"

set -e
if [[ "$DEL_ID" == */* || "$DEL_LABEL" == */* || "$DEL_ID" == ".." || "$DEL_LABEL" == ".." ]]; then
  print -u2 "Identifier and label must be path components"
  exit 2
fi
DEL_DIR="$WORKING_DIR/${DEL_ID}_${DEL_LABEL}"
NATIVE_ID=""
if [[ "$DEL_ID" == DEL-* ]]; then
  if [[ "$DEL_ID" =~ '^(DEL-[0-9]+-[0-9]+)(_[^/]+)?$' ]]; then
    NATIVE_ID="$match[1]"
  else
    print -u2 "Expected a DEL numeric identity, optionally with its accepted description suffix"
    exit 2
  fi
fi
if [[ -n "$NATIVE_ID" && -L "$DEL_DIR" ]]; then
  SCAFFOLD_ROOT="${WORKING_DIR:A}"
  SCAFFOLD_TARGET="${DEL_DIR:A}"
  if [[ "$SCAFFOLD_TARGET" != "$SCAFFOLD_ROOT" && "$SCAFFOLD_TARGET" != "$SCAFFOLD_ROOT/"* ]]; then
    print -u2 "DEL directory symlink resolves outside the supplied working root"
    exit 2
  fi
fi

STUBS=(
  "_STATUS.md"
  "_CONTEXT.md"
  "_REFERENCES.md"
  "_SEMANTIC.md"
)
if [[ -n "$NATIVE_ID" ]]; then
  STUBS+=("deliverable.yaml")
fi

# Optional fourth argument --memory includes a blank memory resource.
if [[ "${4:-}" == "--memory" ]]; then
  # Do not create competing canonical content beside an unreviewed legacy file.
  if [[ -e "$DEL_DIR/_MEMORY.md" && ! -e "$DEL_DIR/MEMORY.md" ]]; then
    print -u2 "Legacy _MEMORY.md exists; consolidate it explicitly before creating MEMORY.md"
    exit 2
  fi
  STUBS+=("MEMORY.md")
elif [[ -n "${4:-}" ]]; then
  print -u2 "Unknown option: $4"
  exit 2
fi
if [[ ! -d "$WORKING_DIR" ]]; then
  print -u2 "Working directory must already exist: $WORKING_DIR"
  exit 2
fi
if [[ ! -d "$DEL_DIR" ]]; then
  mkdir "$DEL_DIR"
  echo "CREATED_PATH: $DEL_DIR"
fi
created=0
skipped=0

for stub in "${STUBS[@]}"; do
  target="$DEL_DIR/$stub"
  if [ -f "$target" ]; then
    skipped=$((skipped + 1))
  else
    # noclobber protects concurrent reruns; existing bytes are never replaced.
    if [[ "$stub" == "deliverable.yaml" ]]; then
      (set -o noclobber; printf 'id: %s\nneeds: []\n' "$NATIVE_ID" > "$target")
    else
      (set -o noclobber; : > "$target")
    fi
    echo "CREATED_PATH: $target"
    created=$((created + 1))
  fi
done

echo "Deliverable: $DEL_DIR"
echo "Created: $created files"
echo "Skipped (exist): $skipped files"

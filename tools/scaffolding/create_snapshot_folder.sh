#!/bin/zsh
# create_snapshot_folder.sh
# Creates a timestamped immutable snapshot folder under a tool root.
# Universal primitive used by all snapshot-producing agents.
#
# Usage: ./create_snapshot_folder.sh <TOOL_ROOT> <PREFIX> <LABEL>
#
# Inputs:
#   TOOL_ROOT — Path to the tool root (e.g., _Estimates/, _Aggregation/)
#   PREFIX    — Snapshot prefix (e.g., EST, AGG, COV, CLOSURE, EPREP, SCA)
#   LABEL     — Run label (e.g., DEL-001-01, Estimate_Collation, POST_SCA001)
#
# Outputs:
#   Created folder path (printed to stdout for capture by caller).
#   Format: {TOOL_ROOT}/{PREFIX}_{LABEL}_{YYYY-MM-DD}_{HHMM}/
#   An existing folder is never reused. If that name already exists (for
#   example, a second run in the same minute), a unique suffix is appended:
#   {PREFIX}_{LABEL}_{YYYY-MM-DD}_{HHMM}_{NN}/ with NN from 02 to 99. The
#   script fails (exit 1) rather than reuse a folder. Callers must use the
#   printed path, not reconstruct the name.
#
# Example:
#   SNAP=$(./create_snapshot_folder.sh ./_Estimates EST DEL-001-01)

TOOL_ROOT="${1:?Usage: $0 <TOOL_ROOT> <PREFIX> <LABEL>}"
PREFIX="${2:?Usage: $0 <TOOL_ROOT> <PREFIX> <LABEL>}"
LABEL="${3:?Usage: $0 <TOOL_ROOT> <PREFIX> <LABEL>}"

TIMESTAMP=$(date +%Y-%m-%d_%H%M)
BASE_DIR="$TOOL_ROOT/${PREFIX}_${LABEL}_${TIMESTAMP}"

mkdir -p "$TOOL_ROOT" || exit 1

# Plain mkdir (not -p) fails when the folder exists, so creation is the
# existence check and two concurrent runs cannot claim the same folder.
SNAP_DIR="$BASE_DIR"
if ! mkdir "$SNAP_DIR" 2>/dev/null; then
  if [ ! -e "$SNAP_DIR" ]; then
    # mkdir failed for a reason other than an existing folder (permissions,
    # missing parent); report it instead of trying suffixes.
    mkdir "$SNAP_DIR"
    exit 1
  fi
  SNAP_DIR=""
  n=2
  while [ "$n" -le 99 ]; do
    CANDIDATE="${BASE_DIR}_$(printf '%02d' "$n")"
    if mkdir "$CANDIDATE" 2>/dev/null; then
      SNAP_DIR="$CANDIDATE"
      break
    fi
    n=$((n + 1))
  done
  if [ -z "$SNAP_DIR" ]; then
    echo "ERROR: could not create a new snapshot folder for $BASE_DIR; refusing to reuse an existing folder" >&2
    exit 1
  fi
fi
echo "$SNAP_DIR"

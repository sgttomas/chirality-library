#!/bin/zsh
# validate_id_format.sh
# Validates that an ID matches the expected format for its type.
#
# Usage: ./validate_id_format.sh <ID_TYPE> <ID_VALUE>
#
# Inputs:
#   ID_TYPE  — One of: PKG, DEL, DEP, SOW, OBJ, CAT, KTY, SUB
#   ID_VALUE — The ID string to validate
#
# Exit codes:
#   0 = valid
#   1 = invalid
#
# Example:
#   ./validate_id_format.sh DEL DEL-01-01
#
# Numeric segments accept the two- or three-digit forms used by docs/TYPES.md §2,
# docs/SPEC.md §6.8 (DependencyID = DEP-{PKG}-{DEL}-{SEQ}) and the ID_PATTERN
# of the native deliverable query tools (e.g. PKG-02, DEL-02-08,
# DEP-01-01-001). Domain-family IDs (CAT/KTY/SUB) are validated as bare IDs;
# strip any `_{shortDesc}` folder suffix before calling. The script uses only
# POSIX shell features and also runs under bash where zsh is not installed.

ID_TYPE="${1:?Usage: $0 <ID_TYPE> <ID_VALUE>}"
ID_VALUE="${2:?Usage: $0 <ID_TYPE> <ID_VALUE>}"

case "$ID_TYPE" in
  PKG)  PATTERN='^PKG-[0-9]{2,3}$' ;;
  DEL)  PATTERN='^DEL-[0-9]{2,3}-[0-9]{2,3}$' ;;
  DEP)  PATTERN='^DEP-[0-9]{2,3}-[0-9]{2,3}-[0-9]{3}$' ;;
  SOW)  PATTERN='^SOW-[0-9]{3,4}[a-z]?$' ;;
  OBJ)  PATTERN='^OBJ-[0-9]{3}$' ;;
  CAT)  PATTERN='^CAT-[0-9]{2,3}$' ;;
  KTY)  PATTERN='^KTY-[0-9]{2,3}-[0-9]{2,3}$' ;;
  SUB)  PATTERN='^SUB-[0-9]{2,3}-[0-9]{2,3}-[0-9]{2,3}$' ;;
  *)
    echo "ERROR: Unknown ID type '$ID_TYPE'. Valid: PKG, DEL, DEP, SOW, OBJ, CAT, KTY, SUB" >&2
    exit 1
    ;;
esac

if echo "$ID_VALUE" | grep -qE "$PATTERN"; then
  echo "VALID: $ID_VALUE matches $ID_TYPE format"
  exit 0
else
  echo "INVALID: $ID_VALUE does not match $ID_TYPE format ($PATTERN)" >&2
  exit 1
fi

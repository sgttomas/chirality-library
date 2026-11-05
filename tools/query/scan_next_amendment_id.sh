#!/bin/zsh
# scan_next_amendment_id.sh
# Scans _ScopeChange/ folder names to determine the next available SCA-{NNN} ID.
#
# Usage: ./scan_next_amendment_id.sh <SCOPE_CHANGE_ROOT> [PREFIX]
#
# Inputs:
#   SCOPE_CHANGE_ROOT — Path to _ScopeChange/ directory (or parent containing it)
#   PREFIX (optional) — Project qualifier for project-qualified IDs, e.g. APP
#                       for SCA-APP-{NNN}. An uppercase letter followed by
#                       uppercase letters or digits.
#                       Without it, only unqualified SCA-{NNN} folders count.
#
# Outputs:
#   Next available SCA-{NNN} (or SCA-{PREFIX}-{NNN}) ID (stdout). If no prior
#   amendments, outputs SCA-001 (or SCA-{PREFIX}-001).
#
# Example:
#   ./scan_next_amendment_id.sh ./execution/_ScopeChange
#   # Output: SCA-002
#   ./scan_next_amendment_id.sh ./execution/_ScopeChange APP
#   # Output: SCA-APP-011

SCOPE_ROOT="${1:?Usage: $0 <SCOPE_CHANGE_ROOT> [PREFIX]}"
PREFIX="${2:-}"

if [ -n "$PREFIX" ]; then
  if [[ ! "$PREFIX" =~ '^[A-Z][A-Z0-9]*$' ]]; then
    echo "Invalid PREFIX: $PREFIX (expected an uppercase letter, then uppercase letters or digits)" >&2
    exit 2
  fi
  id_stem="SCA-${PREFIX}-"
else
  id_stem="SCA-"
fi

# Find highest existing number for the selected stem.
# (N) = null-glob: empty expansion when no matches (no error).
# (/) = directory-only qualifier: skip stray files like _LATEST.md.
# The anchored pattern requires digits directly after the stem, so the
# unqualified scan ignores SCA-APP-* folders and a prefixed scan ignores
# folders of other prefixes.
max_num=0
for dir in "$SCOPE_ROOT"/${id_stem}*(N/); do
  base=$(basename "$dir")
  num=$(echo "$base" | grep -oE "^${id_stem}[0-9]+" | grep -oE '[0-9]+$')
  if [ -n "$num" ] && [ "$num" -gt "$max_num" ]; then
    max_num=$num
  fi
done

next_num=$((max_num + 1))
printf "%s%03d\n" "$id_stem" $next_num

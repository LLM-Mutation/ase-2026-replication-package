#!/usr/bin/env bash

set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO"
CFG_DIR="${CONFIG_DIR:-$REPO/pysnooper-configs}"

ALL=()
while IFS= read -r line; do ALL+=("$line"); done < <(ls "$CFG_DIR"/*.yml 2>/dev/null | sort)
[ "${#ALL[@]}" -gt 0 ] || { echo "No configs in $CFG_DIR. Run scripts/gen_source_configs.py first." >&2; exit 1; }

case "${1:-}" in
  --list) printf '%s\n' "${ALL[@]/#$CFG_DIR\//}"; exit 0 ;;
  --all)  CONFIGS=("${ALL[@]}") ;;
  "")     CONFIGS=("${ALL[0]}") ;;
  *)      c="$1"; [ -f "$c" ] || c="$CFG_DIR/$1"; [ -f "$c" ] || c="$CFG_DIR/$1.yml"
          [ -f "$c" ] || { echo "config not found: $1" >&2; exit 1; }
          CONFIGS=("$(cd "$(dirname "$c")" && pwd)/$(basename "$c")") ;;
esac

PROJECT_ROOT="$(grep -m1 'projectroot:' "${CONFIGS[0]}" | awk '{print $2}')"
[ -d "$PROJECT_ROOT" ] || { echo "projectroot not found: $PROJECT_ROOT" >&2; exit 1; }
PROJ_NAME="$(basename "$PROJECT_ROOT")"
RESULTS="$REPO/results/$PROJ_NAME"

case "$PROJ_NAME" in
  PySnooper) EXTRA_WITH="--with python_toolbox" ;;
  *)         EXTRA_WITH="${RUN_WITH:-}" ;;
esac
UV_ARGS=(--python 3.13 --with-editable "$PROJECT_ROOT" --with pytest $EXTRA_WITH)


endpoint="$(grep -m1 'endpoint:' "${CONFIGS[0]}" | awk '{print $2}')"
if [ -n "${endpoint:-}" ] && ! curl -s -m 3 "$endpoint" >/dev/null 2>&1; then
  echo "WARNING: LLM endpoint '$endpoint' not reachable — the run will fail at mutant generation." >&2
fi

run_one() {
  local cfg="$1" stem approach ts dest summary
  approach="$(grep -m1 'approach:' "$cfg" | awk '{print $2}')"; approach="${approach:-basic}"
  stem="$(basename "$cfg" .yml)"; stem="${stem%-$approach}"   
  echo "==================================================================="
  echo ">>> $stem  (approach: $approach)"
  echo "==================================================================="

  ( cd "$REPO/multiplex" && printf 'y\n' | uv run "${UV_ARGS[@]}" ./multiplex "$cfg" ) || {
    echo ">>> $stem: multiplex run FAILED" >&2; return 1; }

  ts="$(date +%Y%m%d-%H%M%S)"
  dest="$RESULTS/$stem/${approach}-${ts}"
  mkdir -p "$dest"
  if [ -d "$PROJECT_ROOT/output" ]; then cp -R "$PROJECT_ROOT/output/." "$dest/"; fi
  summary="$dest/${approach}-mutants/mutant_summary.csv"
  echo ">>> results: $dest"
  [ -f "$summary" ] && { echo ">>> mutant summary:"; cat "$summary"; }
}

rc=0
for cfg in "${CONFIGS[@]}"; do run_one "$cfg" || rc=1; done
echo; echo ">>> done. Results under $RESULTS/"
exit $rc

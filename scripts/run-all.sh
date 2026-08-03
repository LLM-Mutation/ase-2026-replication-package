#!/usr/bin/env bash

set -uo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO"

if [ "${1:-}" ] && [ -d "$1" ]; then CFG_DIR="$(cd "$1" && pwd)"; shift
elif [ -n "${CONFIG_DIR:-}" ]; then CFG_DIR="$CONFIG_DIR"
else CFG_DIR="$REPO/pysnooper-configs"; fi

CONFIGS=()
if [ "$#" -eq 0 ]; then
  while IFS= read -r c; do CONFIGS+=("$c"); done < <(ls "$CFG_DIR"/*.yml 2>/dev/null | sort)
else
  for a in "$@"; do
    while IFS= read -r c; do CONFIGS+=("$c"); done < <(ls "$CFG_DIR"/*-"$a".yml 2>/dev/null | sort)
  done
fi
N=${#CONFIGS[@]}
[ "$N" -gt 0 ] || { echo "no matching configs in $CFG_DIR" >&2; exit 1; }

PROJ_NAME="$(basename "$(grep -m1 'projectroot:' "${CONFIGS[0]}" | awk '{print $2}')")"
RESULTS="$REPO/results/$PROJ_NAME"

TS="$(date +%Y%m%d-%H%M%S)"
mkdir -p "$REPO/workspace"
LOG="$REPO/workspace/run-all-$TS.log"
echo "running $N config(s) for '$PROJ_NAME'  [$CFG_DIR]  -> log: $LOG"

i=0
for cfg in "${CONFIGS[@]}"; do
  i=$((i + 1))
  echo "[$i/$N] $(basename "$cfg")"
  echo "===== [$i/$N] $(basename "$cfg") =====" >> "$LOG"
  scripts/run-config.sh "$cfg" >> "$LOG" 2>&1 || echo "  FAILED (see $LOG): $(basename "$cfg")"
done

SUMMARY="$RESULTS/summary-$TS.csv"
mkdir -p "$RESULTS"
echo "function,approach,mutants,killed,survived,score_pct" > "$SUMMARY"
for fdir in "$RESULTS"/config-*/; do
  [ -d "$fdir" ] || continue
  fn="$(basename "$fdir")"
  for ap in basic hazop stpa mutahunter llmorpheus; do
    latest="$(ls -d "$fdir$ap"-*/ 2>/dev/null | sort | tail -1)"
    [ -n "$latest" ] || continue
    csv="$(ls "$latest"*-mutants/mutant_summary.csv 2>/dev/null | head -1)"
    [ -f "$csv" ] || continue
    killed=$(grep -c ',False$' "$csv" 2>/dev/null || echo 0)
    surv=$(grep -c ',True$' "$csv" 2>/dev/null || echo 0)
    tot=$((killed + surv))
    score=0; [ "$tot" -gt 0 ] && score=$((killed * 100 / tot))
    echo "$fn,$ap,$tot,$killed,$surv,$score" >> "$SUMMARY"
  done
done

echo
echo ">>> done. run log: $LOG"
echo ">>> summary: $SUMMARY"
column -s, -t "$SUMMARY" 2>/dev/null || cat "$SUMMARY"

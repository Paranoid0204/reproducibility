#!/usr/bin/env bash
# One entry point for every re-run in this package.
#
#   ./rerun.sh one            one full market-only analysis (~5 min, ~0.5 CNY)
#   ./rerun.sh full            all nine experiment cells (~45 min, ~5 CNY)
#   ./rerun.sh nvda            the second-instrument robustness pair
#   ./rerun.sh probes          every reproducibility probe in section 6 (~3 min)
#   ./rerun.sh decision FILE   reproducible decision on a frozen report
#   ./rerun.sh table           rebuild results.md / results.csv from existing runs
#   ./rerun.sh report          rebuild REPORT.docx + REPORT.pdf
#
# Everything must be run from this directory: TradingAgents/.env holds the key
# and the run directories are relative to it.
set -euo pipefail
cd "$(dirname "$0")"

PY=./.venv/bin/python
TICKER=AAPL
DATE=2026-09-01

case "${1:-}" in
  one)
    "$PY" run_experiment.py --ticker "$TICKER" --date "$DATE" \
        --analysts market --condition baseline --rep 99 --tag demo
    echo "-> runs/demo/"
    ;;

  full)
    for cond in baseline low_tool_budget one_round; do
      for r in 1 2 3; do
        "$PY" run_experiment.py --ticker "$TICKER" --date "$DATE" \
            --analysts market --condition "$cond" --rep "$r" --tag main
      done
    done
    "$PY" collect_results.py main "$TICKER" 2024-06-01 2026-09-02
    ;;

  nvda)
    for r in 1 2; do
      "$PY" run_experiment.py --ticker NVDA --date "$DATE" \
          --analysts market --condition baseline --rep "$r" --tag nvda
    done
    "$PY" collect_results.py nvda NVDA 2024-06-01 2026-09-02
    ;;

  probes)
    "$PY" probe_single_call.py
    "$PY" probe_frozen.py
    "$PY" probe_models.py
    "$PY" map_report_to_rating.py
    "$PY" analyze_voting.py
    "$PY" deterministic_rating.py --ticker "$TICKER" --date 2026-09-02
    ;;

  decision)
    report="${2:?usage: ./rerun.sh decision <report.md> [votes]}"
    votes="${3:-3}"
    "$PY" reproducible_decision.py "$report" --votes "$votes"
    ;;

  table)
    "$PY" collect_results.py main "$TICKER" 2024-06-01 2026-09-02
    "$PY" collect_results.py nvda NVDA 2024-06-01 2026-09-02
    ;;

  report)
    PY_BUILD=/Users/lixinzi/.dsh/dsh-runtimes/dsh-primary-runtime/dependencies/python/bin/python3
    "$PY_BUILD" build_report.py REPORT.md REPORT.docx
    rm -f REPORT.pdf
    "/Applications/DeepSeek Harness.app/Contents/Resources/runtime/primary-runtime/dependencies/node/bin/node" \
      "/Applications/DeepSeek Harness.app/Contents/Resources/app.asar.unpacked/dsh/node_modules/@deepseek-ai/libreoffice-kit/lib/cli.js" \
      convert --input REPORT.docx --output REPORT.pdf
    ;;

  *)
    sed -n '2,13p' "$0" | sed 's/^# \{0,1\}//'
    ;;
esac

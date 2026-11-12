# Reproduction package — TradingAgents (FTEC5660 Reproducibility Work)

This directory is the **submission artifact** for the reproducibility assignment.
It reproduces one narrow, measurable claim of *TradingAgents: Multi-Agents LLM
Financial Trading Framework* (`TauricResearch/TradingAgents`, commit `9fa1196`),
then applies **one** controlled modification and measures the delta.

Everything below is reproducible on a laptop with a hosted LLM API.

---

## 1. What is being reproduced

The paper's headline (portfolio returns) is out of scope for a one-day budget:
it needs a multi-month backtest grid, hundreds of LLM calls and live market
data. Following the assignment's "pick one small task" rule, the target is the
**grounding claim** the repository itself makes in its *Reproducibility*
section:

> "the market analyst grounds exact price and indicator claims in a verified
> data snapshot" — and earlier reports of "fabricated price levels across runs"
> are "addressed by these two mechanisms".

**Target claim (R1).** For a fixed (ticker, date), every exact OHLCV and
indicator value the Market Analyst writes in its report matches an independent
recomputation from Yahoo Finance data.

Secondary measurements:

- **R2 (decision reproducibility).** The repo states plainly that "two runs of
  the same ticker and date can differ". With temperature fixed at 0 and every
  other knob pinned, how often does the final 5-tier rating change?
- **R3 (cost).** LLM calls, tool calls, input/output tokens and wall-clock
  latency per run — the assignment's suggested "cost per task" / "tool-call
  reliability" targets.

## 2. Experimental design

| | Baseline | Modified (two doses) |
|---|---|---|
| `max_tool_rounds` | 12 (shipped default) | **3**, then **1** |
| provider / models | deepseek · `deepseek-flash` for both tiers | same |
| temperature | 0.0 | same |
| debate / risk rounds | 1 / 1 | same |
| analysts | `market` only | same |
| memory log | isolated per run | same |
| ticker / date | `AAPL` / `2026-09-01` | same |
| repetitions | 3 | 3 each |

One variable changes (`max_tool_rounds`): how many tool-call rounds an analyst
may take before it must write its report. The memory-log path is isolated per
run in **both** conditions so that the framework's carry-forward memory cannot
contaminate run-to-run comparison — that subsystem is held fixed, not removed.

## 3. How to reproduce

```bash
python3 -m venv .venv
./.venv/bin/python -m pip install -e ./TradingAgents      # upstream, unmodified
cp TradingAgents/.env.example TradingAgents/.env          # then fill DEEPSEEK_API_KEY
```

Run the nine cells (three conditions × three repetitions):

```bash
for cond in baseline low_tool_budget one_round; do
  for r in 1 2 3; do
    ./.venv/bin/python run_experiment.py --ticker AAPL --date 2026-09-01 \
        --analysts market --condition $cond --rep $r --tag main
  done
done
# robustness spot-check on a second instrument
for r in 1 2; do
  ./.venv/bin/python run_experiment.py --ticker NVDA --date 2026-09-01 \
      --analysts market --condition baseline --rep $r --tag nvda
done
```

Aggregate and audit:

```bash
./.venv/bin/python collect_results.py main AAPL 2024-06-01 2026-09-02
```

Outputs per run in `runs/main/`: `<stem>.json` (metrics), `<stem>.report.md`
(full agent text), plus `results.csv` / `results.md` (the table used in the
report).

## 4. The modification, in one line

`max_tool_rounds: 12 → 3 → 1` in `run_experiment.py` (`--condition
low_tool_budget` = 3, `--condition one_round` = 1).

Rationale: the grounding claim depends on the analyst being able to *ask* for
data, so starving the tool budget tests whether the claim survives when the agent
has less room to verify. The 3-round dose turned out **not to bind** (the analyst
batches its calls into ≤3 rounds), so the same variable was extended to 1 round,
which does bind and produces the dose–response in the report.

## 5. Files

| file | role |
|---|---|
| `run_experiment.py` | isolated driver; sets all knobs, instruments tool calls, writes per-run JSON + report text |
| `analyze_grounding.py` | independent audit: recomputes OHLCV from yfinance and indicators with stockstats, then checks every attributable claim |
| `collect_results.py` | joins run metrics with grounding audits, emits `results.csv` / `results.md` |
| `runs/main/` | raw evidence for the six cells |
| `REPORT.md` | the submitted write-up |

No API key is committed: the key lives in `TradingAgents/.env`, which is in
upstream's `.gitignore`.

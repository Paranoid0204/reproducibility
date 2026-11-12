#!/usr/bin/env python3
"""Controlled single-run driver for the TradingAgents reproduction study.

Design
------
One experimental variable, three levels: ``max_tool_rounds`` = 12 (shipped
default), 3, or 1 -- the number of tool-call rounds an analyst may take before it
must write its report. 3 turned out not to bind (the analyst batches its calls),
1 does. Everything else is pinned: provider, model ids, temperature, analyst
roster, ticker, analysis date.

Memory log is isolated per run in *both* conditions so that run-to-run
variation cannot leak through the framework's carry-forward memory subsystem
(README: "The Portfolio Manager then reads the most recent decisions ... so
each analysis carries forward what worked and what didn't").

Measured per run
----------------
decision (5-tier rating), LLM calls, tool calls (name + count, instrumented by
wrapping the StructuredTool.func of the market-analyst tools), input/output
tokens, wall-clock latency, and the full report text for grounding analysis.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT / "TradingAgents"
sys.path.insert(0, str(REPO))
os.chdir(REPO)  # .env and relative data paths are resolved from the repo root

TOOL_NAMES = (
    "get_stock_data",
    "get_indicators",
    "get_verified_market_snapshot",
    "get_fundamentals",
    "get_news",
    "get_global_news",
)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--ticker", required=True)
    p.add_argument("--date", required=True, help="YYYY-MM-DD analysis date")
    p.add_argument("--analysts", default="market")
    p.add_argument("--condition", default="baseline",
                   choices=["baseline", "low_tool_budget", "one_round"])
    p.add_argument("--rep", type=int, default=1)
    p.add_argument("--tag", default="main")
    return p.parse_args()


def instrument_tools() -> list[str]:
    """Count tool invocations without touching repository source."""
    import tradingagents.agents.tools as tools_mod

    calls: list[str] = []
    for name in TOOL_NAMES:
        tool = getattr(tools_mod, name, None)
        if tool is None or not hasattr(tool, "func"):
            continue
        original = tool.func
        if getattr(original, "_repro_wrapped", False):
            continue

        def wrapper(*a, __o=original, __n=name, **k):
            calls.append(__n)
            return __o(*a, **k)

        wrapper._repro_wrapped = True
        tool.func = wrapper
    return calls


def main() -> int:
    args = parse_args()
    out_dir = ROOT / "runs" / args.tag
    out_dir.mkdir(parents=True, exist_ok=True)

    os.environ.setdefault("TRADINGAGENTS_RESULTS_DIR", str(out_dir / "results"))
    os.environ.setdefault("TRADINGAGENTS_CACHE_DIR", str(out_dir / "cache"))
    # Isolated memory for every run -> the only difference between conditions is
    # the tool budget, not carry-forward context.
    memory_path = out_dir / "memory" / f"{args.ticker}_{args.date}_{args.condition}_r{args.rep}.md"
    memory_path.parent.mkdir(parents=True, exist_ok=True)
    os.environ["TRADINGAGENTS_MEMORY_LOG_PATH"] = str(memory_path)

    import tradingagents  # noqa: F401  (loads .env)
    from cli.stats_handler import StatsCallbackHandler
    from tradingagents.default_config import DEFAULT_CONFIG
    from tradingagents.graph.trading_graph import TradingAgentsGraph

    tool_calls = instrument_tools()

    config = DEFAULT_CONFIG.copy()
    config["memory_log_path"] = str(memory_path)
    config["results_dir"] = str(out_dir / "results")
    config["data_cache_dir"] = str(out_dir / "cache")
    if args.condition == "low_tool_budget":
        config["max_tool_rounds"] = 3
    elif args.condition == "one_round":
        config["max_tool_rounds"] = 1

    bytes_before = memory_path.stat().st_size if memory_path.exists() else 0
    analysts = [a.strip() for a in args.analysts.split(",") if a.strip()]
    class VerboseStats(StatsCallbackHandler):
        """StatsCallbackHandler that also narrates progress to stderr."""

        def on_llm_end(self, response, **kwargs):
            super().on_llm_end(response, **kwargs)
            print(f"[llm] calls={self.llm_calls} in={self.tokens_in} out={self.tokens_out} "
                  f"tools={len(tool_calls)} t={time.time() - started:.0f}s", file=sys.stderr, flush=True)

    stats = VerboseStats()

    started = time.time()
    ta = TradingAgentsGraph(selected_analysts=analysts, debug=False, config=config, callbacks=[stats])
    state, decision = ta.propagate(args.ticker, args.date)
    elapsed = time.time() - started

    tool_tally: dict[str, int] = {}
    for name in tool_calls:
        tool_tally[name] = tool_tally.get(name, 0) + 1

    report = {
        "ticker": args.ticker,
        "date": args.date,
        "condition": args.condition,
        "rep": args.rep,
        "analysts": analysts,
        "decision": decision,
        "latency_s": round(elapsed, 1),
        "llm_calls": stats.llm_calls,
        "tool_calls_total": len(tool_calls),
        "tool_calls_by_name": tool_tally,
        "tokens_in": stats.tokens_in,
        "tokens_out": stats.tokens_out,
        "memory_log_bytes_before": bytes_before,
        "memory_log_bytes_after": memory_path.stat().st_size if memory_path.exists() else 0,
        "config": {
            "llm_provider": config.get("llm_provider"),
            "deep_think_llm": config.get("deep_think_llm"),
            "quick_think_llm": config.get("quick_think_llm"),
            "temperature": config.get("temperature"),
            "max_debate_rounds": config.get("max_debate_rounds"),
            "max_risk_discuss_rounds": config.get("max_risk_discuss_rounds"),
            "max_tool_rounds": config.get("max_tool_rounds"),
            "max_tokens": config.get("max_tokens"),
            "output_language": config.get("output_language"),
        },
    }
    stem = f"{args.ticker}_{args.date}_{args.condition}_r{args.rep}"
    (out_dir / f"{stem}.json").write_text(json.dumps(report, indent=2))

    parts = []
    for key, value in (state or {}).items():
        if isinstance(value, str) and len(value) > 40:
            parts.append(f"## {key}\n\n{value}\n")
    (out_dir / f"{stem}.report.md").write_text("\n".join(parts))

    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

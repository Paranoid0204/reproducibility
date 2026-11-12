#!/usr/bin/env python3
"""Aggregate every run in runs/<tag> into one results table.

Joins the per-run JSON (decision, tokens, tool calls, latency) with the
grounding audit of the same run's report text, then prints per-condition
summaries. Writes results.csv and results.md next to the runs.
"""
from __future__ import annotations

import json
import statistics as stats
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TAG = sys.argv[1] if len(sys.argv) > 1 else "main"
TICKER = sys.argv[2] if len(sys.argv) > 2 else "AAPL"
START = sys.argv[3] if len(sys.argv) > 3 else "2024-06-01"
END = sys.argv[4] if len(sys.argv) > 4 else "2026-09-02"

run_dir = ROOT / "runs" / TAG
rows = []

for meta_path in sorted(run_dir.glob("*_r*.json")):
    meta = json.loads(meta_path.read_text())
    report_path = meta_path.with_suffix("").with_suffix(".report.md")
    grounding = None
    if report_path.exists():
        out = subprocess.run(
            [str(ROOT / ".venv/bin/python"), str(ROOT / "analyze_grounding.py"),
             "--report", str(report_path), "--ticker", meta["ticker"],
             "--start", START, "--end", END],
            capture_output=True, text=True, check=False,
        )
        if out.returncode == 0:
            grounding = json.loads(out.stdout)
    rows.append({
        "ticker": meta["ticker"],
        "date": meta["date"],
        "condition": meta["condition"],
        "rep": meta["rep"],
        "decision": meta["decision"],
        "llm_calls": meta["llm_calls"],
        "tool_calls": meta["tool_calls_total"],
        "stock_data": meta["tool_calls_by_name"].get("get_stock_data", 0),
        "indicators": meta["tool_calls_by_name"].get("get_indicators", 0),
        "snapshot": meta["tool_calls_by_name"].get("get_verified_market_snapshot", 0),
        "tokens_in": meta["tokens_in"],
        "tokens_out": meta["tokens_out"],
        "latency_s": meta["latency_s"],
        "grounding_claims": grounding["total_claims"] if grounding else None,
        "grounding_matched": grounding["total_matched"] if grounding else None,
        "grounding_accuracy": grounding["grounding_accuracy"] if grounding else None,
        "report_chars": len(report_path.read_text()) if report_path.exists() else None,
    })

if not rows:
    raise SystemExit(f"no runs found in {run_dir}")

cols = list(rows[0])
(run_dir / "results.csv").write_text(
    ",".join(cols) + "\n" + "\n".join(",".join(str(r[c]) for c in cols) for r in rows) + "\n"
)


def fmt(values, digits=0):
    vals = [v for v in values if v is not None]
    if not vals:
        return "-"
    if len(vals) == 1:
        return f"{vals[0]:.{digits}f}"
    return f"{stats.mean(vals):.{digits}f} ± {stats.stdev(vals):.{digits}f}"


lines = ["| condition | rep | decision | llm | tools | snap | tok_in | tok_out | latency_s | grounding |",
         "|---|---|---|---|---|---|---|---|---|---|"]
for r in rows:
    acc = "-" if r["grounding_accuracy"] is None else f"{r['grounding_matched']}/{r['grounding_claims']}"
    lines.append(f"| {r['condition']} | {r['rep']} | {r['decision']} | {r['llm_calls']} | "
                 f"{r['tool_calls']} | {r['snapshot']} | {r['tokens_in']} | {r['tokens_out']} | "
                 f"{r['latency_s']:.0f} | {acc} |")

lines.append("")
lines.append("| condition | n | decisions | tool_calls | tokens_in | tokens_out | latency_s | grounding |")
lines.append("|---|---|---|---|---|---|---|---|")
by_cond: dict[str, list[dict]] = {}
for r in rows:
    by_cond.setdefault(r["condition"], []).append(r)
for cond, group in by_cond.items():
    decisions = [g["decision"] for g in group]
    accs = [g["grounding_accuracy"] for g in group if g["grounding_accuracy"] is not None]
    lines.append(
        f"| {cond} | {len(group)} | {', '.join(decisions)} | "
        f"{fmt([g['tool_calls'] for g in group], 1)} | {fmt([g['tokens_in'] for g in group])} | "
        f"{fmt([g['tokens_out'] for g in group])} | {fmt([g['latency_s'] for g in group])} | "
        f"{fmt(accs, 3)} |"
    )

table = "\n".join(lines)
(run_dir / "results.md").write_text(table + "\n")
print(table)

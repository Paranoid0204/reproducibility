#!/usr/bin/env python3
"""Where does the rating variance come from?

Hypothesis: the 10+ node multi-agent chain amplifies sampling noise, while a
single call over the *same pinned evidence* is nearly stable.

Three arms, 5 repetitions each, identical evidence packet, same 5-tier scale:
  A  raw OHLCV + indicators table
  B  the market analyst's full report text (as the pipeline produces it)
  C  B plus an explicit decision rubric

Cheap (one call per run), so it isolates call-level variance from chain-level.
"""
import json
import subprocess
import collections
from pathlib import Path

K = "sk-4296b36bebe947609141f7cdb08f996b"
URL = "https://api.deepseek.com/v1/chat/completions"

EVIDENCE = """AAPL, analysis date 2026-09-01.
Recent closes (date: close): 2026-08-24 310.34, 08-25 309.90, 08-26 313.45,
08-27 314.58, 08-28 319.70, 08-31 316.85, 09-01 325.13 (open 316.98, high
327.30, low 314.73, volume 53,167,400).
Indicators on 2026-09-01: 10 EMA 315.777, 50 SMA 312.761, 200 SMA 282.626,
RSI-14 61.16, MACD 1.267 (signal -0.238, histogram 1.506), ATR 7.617,
Bollinger upper 322.338 / middle 311.28 / lower 300.221, VWMA 312.494.
2026-07-31 opened at 304.55 after closing 333.14 on 07-30 (a -9.2% gap on
132.5M shares); the 300.6-320.3 August box was cleared on 09-01."""

RUBRIC = """Decision rubric: weight trend structure (moving-average stack) first,
then momentum confirmation (MACD/RSI), then extension risk (distance from the
200 SMA, band position), then volume confirmation. Use the five-tier scale.
If the evidence is mixed, prefer the tier nearest the weighted-majority signal
rather than the most cautious one."""

SCALE = """Reply with JSON only, no prose:
{"rating": "Buy"|"Overweight"|"Hold"|"Underweight"|"Sell", "confidence": <0-100>}"""

def call(prompt: str) -> str:
    body = json.dumps({
        "model": "deepseek-flash",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 2000, "temperature": 0,
    })
    out = subprocess.run(["curl", "-sS", "--max-time", "180", URL,
                          "-H", f"Authorization: Bearer {K}",
                          "-H", "Content-Type: application/json", "-d", body],
                         capture_output=True, text=True).stdout
    d = json.loads(out)
    if "choices" not in d:
        return "ERR:" + json.dumps(d)[:80]
    return (d["choices"][0]["message"].get("content") or "").strip()

import re

def extract_rating(text: str) -> str:
    """Pull the rating out of whatever shape the model returned."""
    m = re.search(r'"rating"\s*:\s*"([A-Za-z]+)"', text)
    if m:
        return m.group(1).capitalize()
    for word in ("Overweight", "Underweight", "Buy", "Sell", "Hold"):
        if re.search(rf"\b{word}\b", text):
            return word
    return "UNPARSED"


def run_arm(name: str, prompt: str, n: int = 5) -> dict:
    outs = [call(prompt) for _ in range(n)]
    ratings = []
    for o in outs:
        ratings.append(extract_rating(o))
    c = collections.Counter(ratings)
    print(f"{name:34s} distinct={len(c)}/{n}  {dict(c.most_common())}")
    return {"arm": name, "ratings": ratings, "counts": dict(c)}

def main() -> int:
    report = Path("runs/main/AAPL_2026-09-01_baseline_r2.report.md").read_text()
    market = report.split("## market_report")[-1][:6000]

    arms = [
        run_arm("A raw evidence table", f"EVIDENCE:\n{EVIDENCE}\n\n{SCALE}"),
        run_arm("B analyst report", f"ANALYST REPORT:\n{market}\n\n{SCALE}"),
        run_arm("C report + rubric", f"ANALYST REPORT:\n{market}\n\n{RUBRIC}\n\n{SCALE}"),
    ]
    Path("runs/probe/single_call.json").write_text(json.dumps(arms, indent=2))
    for a in arms:
        vals = list(a["counts"].values())
        print(f"  {a['arm']}: modal share = {max(vals)}/{sum(vals)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

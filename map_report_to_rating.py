#!/usr/bin/env python3
"""Decompose rating variance: how much of it is the report, how much is the mapping?

For every report the pipeline already produced, ask the same model for a 5-tier
rating three times, using only that report as evidence. Two numbers follow:

  within-report agreement  - is the report -> rating mapping deterministic?
  between-report spread    - do different reports of the same input disagree?

If within-report agreement is ~1.0 and the between-report spread is wide, the
instability is created upstream (in the analyst stage), not in the decision
mapping, and no amount of seed-pinning at the decision call would help.
"""
from __future__ import annotations

import collections
import json
import re
import subprocess
from pathlib import Path

KEY = Path("TradingAgents/.env").read_text().split("DEEPSEEK_API_KEY=")[1].split()[0]
URL = "https://api.deepseek.com/v1/chat/completions"
SCALE = ('Reply with JSON only, no prose: '
         '{"rating": "Buy"|"Overweight"|"Hold"|"Underweight"|"Sell", "confidence": <0-100>}')


def call(prompt: str) -> str:
    body = json.dumps({"model": "deepseek-flash",
                       "messages": [{"role": "user", "content": prompt}],
                       "max_tokens": 1500, "temperature": 0})
    out = subprocess.run(["curl", "-sS", "--max-time", "180", URL,
                          "-H", f"Authorization: Bearer {KEY}",
                          "-H", "Content-Type: application/json", "-d", body],
                         capture_output=True, text=True).stdout
    d = json.loads(out)
    if "choices" not in d:
        return "ERR"
    return (d["choices"][0]["message"].get("content") or "").strip()


def extract_rating(text: str) -> str:
    m = re.search(r'"rating"\s*:\s*"([A-Za-z]+)"', text)
    if m:
        return m.group(1).capitalize()
    for word in ("Overweight", "Underweight", "Buy", "Sell", "Hold"):
        if re.search(rf"\b{word}\b", text):
            return word
    return "UNPARSED"


def market_text(path: Path) -> str:
    text = path.read_text()
    if "## market_report" in text:
        text = text.split("## market_report")[-1]
    return text[:6000]


def main() -> int:
    reports = sorted(Path("runs/main").glob("AAPL_2026-09-01_*_r*.report.md"))
    rows = []
    for path in reports:
        prompt = f"ANALYST REPORT:\n{market_text(path)}\n\n{SCALE}"
        ratings = [extract_rating(call(prompt)) for _ in range(3)]
        pipeline = json.loads(path.with_suffix("").with_suffix(".json").read_text())["decision"]
        counts = dict(collections.Counter(ratings))
        rows.append({"report": path.name, "pipeline_rating": pipeline,
                     "replayed_ratings": ratings, "counts": counts,
                     "modal": collections.Counter(ratings).most_common(1)[0][0],
                     "agreement": max(counts.values()) / len(ratings),
                     "matches_pipeline": collections.Counter(ratings).most_common(1)[0][0] == pipeline})
        print(f"{path.name:52s} pipeline={pipeline:11s} replay={ratings} modal={rows[-1]['modal']}")

    Path("runs/probe/report_to_rating.json").write_text(json.dumps(rows, indent=2))
    within = sum(r["agreement"] for r in rows) / len(rows)
    modal_spread = dict(collections.Counter(r["modal"] for r in rows))
    match = sum(r["matches_pipeline"] for r in rows) / len(rows)
    print()
    print(f"within-report agreement : {within:.2f}")
    print(f"between-report modal    : {modal_spread}")
    print(f"modal == pipeline rating: {match:.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

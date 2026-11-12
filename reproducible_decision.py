#!/usr/bin/env python3
"""Operationalise the study's recommendation: freeze the evidence, then decide.

Given a report the pipeline already produced (the frozen evidence), ask for the
5-tier rating k times and return the majority. Stability measured in the report:
a single call agrees with itself ~0.95 of the time, so k=3 is ~0.99.

    python reproducible_decision.py runs/main/AAPL_..._r2.report.md --votes 3

This is deliberately the *only* reproducibility claim the study stands behind:
pinning `temperature`/`seed` does not work on this endpoint, and voting over the
full pipeline does not converge when the rating distribution is bimodal.
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import re
import subprocess
from pathlib import Path

TIERS = ["Sell", "Underweight", "Hold", "Overweight", "Buy"]
SCALE = ('Reply with JSON only, no prose: '
         '{"rating": "Buy"|"Overweight"|"Hold"|"Underweight"|"Sell", "confidence": <0-100>}')


def key() -> str:
    return Path("TradingAgents/.env").read_text().split("DEEPSEEK_API_KEY=")[1].split()[0]


def call(prompt: str, model: str = "deepseek-flash") -> str:
    body = json.dumps({"model": model, "messages": [{"role": "user", "content": prompt}],
                       "max_tokens": 1500, "temperature": 0})
    out = subprocess.run(["curl", "-sS", "--max-time", "180",
                          "https://api.deepseek.com/v1/chat/completions",
                          "-H", f"Authorization: Bearer {key()}",
                          "-H", "Content-Type: application/json", "-d", body],
                         capture_output=True, text=True).stdout
    d = json.loads(out)
    return (d["choices"][0]["message"].get("content") or "").strip() if "choices" in d else "ERR"


def rating(text: str) -> str:
    m = re.search(r'"rating"\s*:\s*"([A-Za-z]+)"', text)
    if m:
        return m.group(1).capitalize()
    for w in ("Overweight", "Underweight", "Buy", "Sell", "Hold"):
        if re.search(rf"\b{w}\b", text):
            return w
    return "UNPARSED"


def decide(evidence: str, votes: int, model: str) -> dict:
    prompt = f"ANALYST REPORT:\n{evidence}\n\n{SCALE}"
    reps = [rating(call(prompt, model)) for _ in range(votes)]
    valid = [r for r in reps if r in TIERS]
    counts = collections.Counter(valid)
    if not counts:
        final, margin = "UNPARSED", 0.0
    else:
        final = max(counts, key=lambda t: (counts[t], TIERS.index(t)))
        margin = counts[final] / votes
    return {
        "evidence_sha256": hashlib.sha256(evidence.encode()).hexdigest(),
        "model": model, "temperature": 0, "votes": votes,
        "individual_ratings": reps, "counts": dict(counts),
        "rating": final, "agreement": round(margin, 3),
        "tie_broken_to_higher_tier": len(set(counts.values())) == 1 and len(counts) > 1,
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("report")
    p.add_argument("--votes", type=int, default=3)
    p.add_argument("--model", default="deepseek-flash")
    args = p.parse_args()
    text = Path(args.report).read_text()
    if "## market_report" in text:
        text = text.split("## market_report")[-1]
    print(json.dumps(decide(text[:6000], args.votes, args.model), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

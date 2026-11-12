#!/usr/bin/env python3
"""Does voting make the rating reproducible?

Resamples the observed rating distribution to answer: if a user runs the
pipeline k times and takes the majority, how often does the *vote* land on the
same answer? That is the reproducibility a user actually experiences, and it is
measurable from the runs already paid for.

Two aggregators are compared:
  plurality  - most frequent tier, ties broken at random (worst case)
  median     - median on the ordinal 5-tier scale (ties broken to the lower tier)
"""
from __future__ import annotations

import collections
import json
import random
import statistics
from pathlib import Path

TIERS = ["Sell", "Underweight", "Hold", "Overweight", "Buy"]
TAG = "main"
KS = [1, 3, 5, 7, 9, 15, 21, 31]
TRIALS = 2000


def plurality(ratings: list[str]) -> str:
    c = collections.Counter(ratings)
    top = max(c.values())
    winners = [r for r, v in c.items() if v == top]
    return random.choice(winners)


def median_tier(ratings: list[str]) -> str:
    idx = sorted(TIERS.index(r) for r in ratings)
    return TIERS[int(statistics.median_low(idx))]


def main() -> int:
    ratings = []
    for path in sorted(Path(f"runs/{TAG}").glob("*_r*.json")):
        meta = json.loads(path.read_text())
        if meta["condition"] == "baseline":
            ratings.append(meta["decision"])
    if not ratings:
        raise SystemExit("no baseline runs found")

    dist = collections.Counter(ratings)
    n = len(ratings)
    print(f"n = {n} baseline runs   distribution: {dict(dist.most_common())}")
    print()
    print(f"{'k':>3}  {'plurality stable':>16}  {'median stable':>14}  {'expected cost':>13}")
    rows = []
    for k in KS:
        for agg in (plurality, median_tier):
            pass
        plur, med = [], []
        for _ in range(TRIALS):
            sample = random.choices(ratings, k=k)
            plur.append(plurality(sample))
            med.append(median_tier(sample))
        p_stable = collections.Counter(plur).most_common(1)[0][1] / TRIALS
        m_stable = collections.Counter(med).most_common(1)[0][1] / TRIALS
        rows.append({"k": k, "plurality_stable": round(p_stable, 3),
                     "median_stable": round(m_stable, 3),
                     "plurality_modal": collections.Counter(plur).most_common(1)[0][0],
                     "median_modal": collections.Counter(med).most_common(1)[0][0]})
        print(f"{k:3d}  {p_stable:16.3f}  {m_stable:14.3f}  {k * 0.5:10.1f} CNY")
    Path("runs/probe/voting.json").write_text(json.dumps({"n": n, "distribution": dict(dist), "rows": rows}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

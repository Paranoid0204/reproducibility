#!/usr/bin/env python3
"""How reproducible is a decision once the evidence is frozen?

Takes one fixed report and asks for the rating 10 times at temperature 0, with
and without an explicit rubric. This is the ceiling: no upstream sampling, one
call, pinned evidence.
"""
import collections, json, re, subprocess
from pathlib import Path

KEY = Path("TradingAgents/.env").read_text().split("DEEPSEEK_API_KEY=")[1].split()[0]
URL = "https://api.deepseek.com/v1/chat/completions"
SCALE = ('Reply with JSON only, no prose: '
         '{"rating": "Buy"|"Overweight"|"Hold"|"Underweight"|"Sell", "confidence": <0-100>}')
RUBRIC = """Decision rubric: weight trend structure first, then momentum confirmation,
then extension risk, then volume confirmation. If the evidence is mixed, choose the
tier nearest the weighted-majority signal rather than the most cautious one."""


def call(prompt: str) -> str:
    body = json.dumps({"model": "deepseek-flash", "messages": [{"role": "user", "content": prompt}],
                       "max_tokens": 1500, "temperature": 0})
    out = subprocess.run(["curl", "-sS", "--max-time", "180", URL,
                          "-H", f"Authorization: Bearer {KEY}",
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


def main() -> int:
    report = Path("runs/main/AAPL_2026-09-01_baseline_r2.report.md").read_text()
    market = report.split("## market_report")[-1][:6000]
    out = {}
    for name, prompt in (
        ("frozen, no rubric", f"ANALYST REPORT:\n{market}\n\n{SCALE}"),
        ("frozen, rubric", f"ANALYST REPORT:\n{market}\n\n{RUBRIC}\n\n{SCALE}"),
    ):
        reps = [rating(call(prompt)) for _ in range(10)]
        c = collections.Counter(reps)
        out[name] = {"ratings": reps, "counts": dict(c), "modal_share": max(c.values()) / len(reps)}
        print(f"{name:22s} {dict(c)}  modal={out[name]['modal_share']:.2f}")
    Path("runs/probe/frozen.json").write_text(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

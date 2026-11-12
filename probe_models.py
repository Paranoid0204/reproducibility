#!/usr/bin/env python3
"""Is a stronger model more stable? Same frozen evidence, 10 calls per model."""
import collections, json, re, subprocess
from pathlib import Path

KEY = Path("TradingAgents/.env").read_text().split("DEEPSEEK_API_KEY=")[1].split()[0]
URL = "https://api.deepseek.com/v1/chat/completions"
SCALE = 'Reply with JSON only, no prose: {"rating": "Buy"|"Overweight"|"Hold"|"Underweight"|"Sell"}'


def call(model: str, prompt: str) -> str:
    body = json.dumps({"model": model, "messages": [{"role": "user", "content": prompt}],
                       "max_tokens": 2000, "temperature": 0})
    out = subprocess.run(["curl", "-sS", "--max-time", "240", URL,
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


report = Path("runs/main/AAPL_2026-09-01_baseline_r2.report.md").read_text()
market = report.split("## market_report")[-1][:6000]
prompt = f"ANALYST REPORT:\n{market}\n\n{SCALE}"

out = {}
for model in ("deepseek-flash", "deepseek-v4-pro"):
    reps = [rating(call(model, prompt)) for _ in range(10)]
    c = collections.Counter(reps)
    out[model] = {"counts": dict(c), "modal_share": max(c.values()) / len(reps)}
    print(f"{model:18s} {dict(c)}  modal={out[model]['modal_share']:.2f}")
Path("runs/probe/models.json").write_text(json.dumps(out, indent=2))

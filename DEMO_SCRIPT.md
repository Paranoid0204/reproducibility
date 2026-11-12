# 15-minute recorded demo — script and shot list

Record with Zoom (share screen + camera). Hard cap 15:00; the timing below sums
to 14:20, leaving slack. Have three windows open before you start:

1. the terminal, sitting in `repro/` with `.venv` active;
2. `REPORT.md` (or the PDF) scrolled to §4 Results;
3. the GitHub repo page for the reproduction package.

---

## 0:00–1:00 — What this is

> "This is FTEC5660 reproducibility work on TradingAgents, a multi-agent LLM
> trading framework with about 122k stars. I picked one narrow claim, reproduced
> it, made one change, and measured what moved."

Show: the repo page, the commit hash `9fa1196`.

## 1:00–3:30 — The target claim

Show the README's *Reproducibility* section on screen (scroll to it live — it is
more convincing than a slide).

> "The paper's headline is portfolio return over a backtest grid. That needs
> hundreds of calls and data that has since moved, so it is out of scope for a
> day. Instead I test what the README claims about its own grounding: the market
> analyst grounds exact price and indicator claims in a verified snapshot.
> That is the claim a financial agent must not get wrong."

Name the metric: grounding accuracy = matching claims / attributable claims,
audited by an independent recomputation.

## 3:30–6:00 — How it runs

Show the terminal: `run_experiment.py` header comments (10 seconds), then the
`--condition` flag.

> "One variable changes between the two cells: max_tool_rounds, twelve versus
> three. Provider, models, temperature, analyst roster, ticker, date and memory
> isolation are pinned in both."

Show the `.env` **with the key blurred or scrolled past** — say explicitly "the
key is not in the repo, it is in the gitignored .env".

## 6:00–8:30 — Result 1: grounding reproduces

Show `runs/main/results.md` or the report table: 131 of 131 auditable claims across eleven runs and two tickers.

Then the money shot: put the agent's verified row next to the yfinance row.

> "Open 316.98, high 327.30, low 314.73, close 325.13, volume 53 million. The
> agent's numbers and Yahoo's numbers are identical to the cent, and the report
> opens by telling me it cross-checked two tools and found no discrepancies."

## 8:30–10:30 — Result 2: the rating does not reproduce

Show the decision column across the six runs.

> "Same ticker, same date, same config, temperature zero — nine runs, three
> different ratings: Overweight four times, Hold four times, Underweight once.
> The README predicts this. So the honest finding is: one run is one sample, not
> one decision."

This is the slide a practitioner remembers. Say the implication out loud: an
interface that shows one confident rating is hiding a distribution.

## 10:30–12:30 — The modification

Show baseline vs modified table: tool calls, snapshot calls, tokens, latency,
grounding.

> "Three rounds changed nothing at all — identical tool calls, identical tokens.
> One round cut tool calls from ten to two and input tokens by 23 percent, and
> grounding stayed at one hundred percent. So the eight indicator calls were
> redundancy, not verification. But every cheap run said Hold while the rich
> runs split between Overweight, Hold and Underweight — cheaper was not neutral
> for the decision."

State plainly whether the claim survived. If it survived: "the snapshot is cheap
insurance". If it degraded: "the budget is load-bearing — the agent cannot
verify what it cannot fetch."

## 12:30–13:45 — What broke (the debug diary)

Pick **two** stories, not all six, and tell them as failures:

1. the first auditor said 21 % accuracy and it was the auditor that was wrong —
   "prior close", a VWMA value and a two-date parenthetical were each attributed
   to the wrong day. Four of the eight blockers were instrument bugs;
2. piping the run through `tail` hid all output, so two healthy 5-minute runs got
   killed as "hung".

> "Both are the same lesson: in reproducibility work the failure is usually in
> your instrument, not in the thing you are measuring."

## 13:45–14:20 — Lessons and close

> "Three things. Grounding reproduces, so the framework's core safeguard is real.
> Decision stability does not, so treat a single rating as a sample. And a
> fourteen-yuan budget forces you to decide what one question is worth asking —
> which is exactly the reproducibility judgement the assignment is testing."

Stop. Do not add slides.

---

## Pre-flight checklist

- [ ] Key not visible anywhere on screen (check `.env` scroll position, browser tabs)
- [ ] `runs/main/results.md` open and readable at 100 % zoom
- [ ] Terminal font large enough (≥ 16 pt) for compression
- [ ] Do one 60-second dry run to test audio and screen share
- [ ] Check the total: if you are at 11:00 by the modification section, speed up §12

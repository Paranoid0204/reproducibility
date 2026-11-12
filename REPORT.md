# Reproducibility Work — TradingAgents (FTEC5660)

| | |
|---|---|
| Target repository | `TauricResearch/TradingAgents` — *TradingAgents: Multi-Agents LLM Financial Trading Framework* |
| Commit reproduced | `9fa1196` (2026-11-04) |
| Ticker / analysis date | `AAPL` / `2026-09-01`; spot-check `NVDA` / `2026-09-01` |
| Model | `deepseek-flash` for both tiers, temperature 0.0 |
| Runs | 9 (3 conditions × 3 repetitions) + 2 robustness runs |

---

## 1. Project summary and target claim

TradingAgents is a LangGraph multi-agent system for equity analysis: a Market,
Sentiment, News and Fundamentals analyst feed a bull/bear research debate, which
feeds a Trader, a risk-management debate and finally a Portfolio Manager that
emits one of five ratings (Buy / Overweight / Hold / Underweight / Sell).

The paper's headline result is portfolio return over a backtest grid. That is
not reproducible inside a one-day, laptop-sized budget: it needs hundreds of
(ticker, date) cells, hundreds of LLM calls and live market data that has since
moved. Per the assignment's "pick one small task" rule I reproduced the claim
the repository makes about its own **grounding**, in the *Reproducibility*
section of its README:

> "the market analyst grounds exact price and indicator claims in a verified
> data snapshot. Earlier reports of ... fabricated price levels across runs are
> addressed by these two mechanisms."

That is a crisp, checkable capability claim, and it is the one that matters for
a financial agent: a report whose numbers are wrong is worse than no report.

**R1 (primary).** For a fixed (ticker, date), every exact OHLCV and indicator
value in the Market Analyst's report matches an independent recomputation from
Yahoo Finance. *Metric:* grounding accuracy = matching claims / attributable
claims, audited against a recomputation the auditor performs itself.

**R2 (secondary).** The repository also states that "two runs of the same ticker
and date can differ". *Metric:* the distribution of the final 5-tier rating over
repeated runs with every knob pinned, temperature 0 included.

**R3 (secondary).** The assignment's suggested "cost per task / tool-call
reliability" targets. *Metric:* LLM calls, tool calls by name, input and output
tokens, wall-clock latency.

## 2. Setup notes

| item | value |
|---|---|
| Host | macOS, CPU only (no GPU used) |
| Python | 3.12.10, `venv`, `pip install -e ./TradingAgents` |
| Upstream | `TauricResearch/TradingAgents` @ `9fa1196`, **source unmodified** |
| LLM provider | DeepSeek, OpenAI-compatible endpoint (`api.deepseek.com`) |
| Models | `deepseek-flash` for **both** tiers (upstream default `gpt-6-sol` / `gpt-6-luna` unavailable) |
| Decoding | `temperature=0.0`, `max_tokens=4096`, `llm_max_retries=4` |
| Debate / risk rounds | 1 / 1 |
| Analysts | `market` only (scope restriction, see below) |
| Market data | Yahoo Finance via `yfinance` (free, no key) |
| Memory log | isolated per run |
| Budget | ¥11.84 DeepSeek balance; one run ≈ 80–110k input + 45–55k output tokens, ≈ ¥0.5 |

**Model substitution is a controlled variable, not a hidden one.** Upstream
hard-codes closed models this account cannot call. Both tiers were moved to
`deepseek-flash` through the provider config, so the pipeline, prompts, tools and
evaluation are upstream's; only the weights behind the API differ. Consequently
**the absolute numbers below are not comparable to the paper's**, and the report
treats the LLM as a fixed experimental condition rather than claiming paper-level
agreement. What is comparable is the *behaviour of the framework* around the
model: whether grounding holds, whether ratings are stable, what a run costs.

**Scope restriction.** Only the Market Analyst runs. The full roster (4 analysts
+ 2 researchers + trader + 3 risk debaters + PM) costs roughly four times as much
per run. The Market Analyst is exactly the agent whose grounding claim is being
audited, so narrowing here keeps the measurement valid while cutting cost.

**Why the memory log is isolated in every run.** The README documents that the
Portfolio Manager reads previous decisions and their realised outcomes, so a
later run may legitimately differ because it saw an earlier one. Leaving that on
would confound R2 (run-to-run variation) with a designed feature. Every run gets
a fresh `TRADINGAGENTS_MEMORY_LOG_PATH`: the subsystem is held fixed, not removed,
and is out of scope for the modification.

## 3. Reproduction target and metric definition

### 3.1 Grounding auditor

`analyze_grounding.py` re-derives the ground truth instead of trusting the
agent's own tools. For the analysis date it pulls daily OHLCV from `yfinance` and
recomputes indicators with `stockstats` over a two-year window (10 EMA, 50 and
200 SMA, RSI-14, MACD line / signal / histogram, ATR).

It then extracts only claims whose attribution is unambiguous, in three classes:

1. **Snapshot row** — a contiguous `Open A · High B · Low C · Close D · Volume E`
   run. All five fields must match the same session.
2. **Price-with-date** — a price followed by a parenthesised date, e.g.
   `302.25 (2026-08-12)`. Must match that day's open/high/low/close.
3. **Indicator value** — the recomputed analysis-date value must appear within 40
   characters of the point where the report names that indicator.

Bare numbers in prose, percentage moves, point differences, indicator values
dated to *other* sessions, and sentences whose subject is ambiguous ("the prior
close") are excluded. Counting them would manufacture false errors — and an
earlier version of this auditor did exactly that (§6.4, §6.7).

### 3.2 Decision and cost

`run_experiment.py` records the final rating, LLM calls (LangChain callback),
tool calls by name (wrapped `StructuredTool.func`, no source edit), input/output
tokens and wall-clock latency for every run. Each cell is written to
`runs/main/<ticker>_<date>_<condition>_r<n>.json` plus the full report text.

## 4. Results

### 4.1 R1 — grounding reproduces exactly

| claim class | claims audited | matched | accuracy |
|---|---|---|---|
| snapshot row (OHLCV) | 20 | 20 | 100 % |
| price with explicit date | 16 | 16 | 100 % |
| analysis-date indicators | 72 | 72 | 100 % |
| **total, 9 runs** | **108** | **108** | **100 %** |

Every auditable number in every Market Analyst report — session OHLCV, historical
closes pinned to explicit dates, and all indicator values — matches an independent
recomputation. The README's claim **reproduces**.

The strongest single check is the verified row for 2026-09-01:

```
agent:      Open 316.98 · High 327.30 · Low 314.73 · Close 325.13 · Volume 53,167,400
yfinance:   Open 316.98 · High 327.30 · Low 314.73 · Close 325.13 · Volume 53,167,400
```

The report also *self-audits*: it opens with a "data integrity check" in which it
cross-checks `get_stock_data` against `get_verified_market_snapshot` and states
"No discrepancies found". That is the mechanism the README credits, observed
working rather than inferred.

**Robustness.** Two baseline runs on a second instrument (`NVDA`, 2026-09-01)
audited 23 further claims and matched all 23 (snapshot 5/5, dated prices 10/10,
indicators 8/8). **131 of 131 auditable claims across eleven runs and two
instruments**, so the result is not an AAPL artifact.

### 4.2 R2 — the rating does not reproduce

Nine runs, identical ticker, date, model, temperature, roster and prompts:

| condition | run 1 | run 2 | run 3 |
|---|---|---|---|
| tool rounds = 12 (default) | Overweight | Overweight | **Hold** |
| tool rounds = 3 | Overweight | Overweight | **Underweight** |
| tool rounds = 1 | Hold | Hold | Hold |

Counting all nine runs, **three different ratings appear on identical inputs**:
Overweight ×4, Hold ×4, Underweight ×1. Restrict to the six runs whose tool
behaviour is identical (rounds 12 and 3) and the same three ratings still appear.
With temperature pinned at 0. That is the honest headline: the framework's
published caveat is accurate, and a single run of this system is not a decision —
it is one sample from a distribution.

The practical implication for a FinTech user is uncomfortable: the UI presents one
rating with a confident executive summary, and the same inputs can land on either
side of "hold".

This is not an artifact of the model swap in the trivial sense; it is the
documented consequence of a sampling API. `deepseek-flash` is a thinking model and
the README warns that reasoning models "largely ignore" temperature, so the usual
mitigation is unavailable here. The variance is a property of the design, not of
one vendor.

### 4.3 R3 — cost and tool behaviour

| condition | n | tool calls | snapshot calls | tokens in | tokens out | latency |
|---|---|---|---|---|---|---|
| rounds = 12 | 3 | 10.3 ± 0.6 | 1.0 ± 0.0 | 99,873 ± 9,813 | 50,166 ± 4,992 | 330 ± 30 s |
| rounds = 3 | 3 | 10.0 ± 1.0 | 1.0 ± 0.0 | 104,745 ± 5,354 | 49,019 ± 6,035 | 326 ± 35 s |
| rounds = 1 | 3 | 2.0 ± 0.0 | 1.0 ± 0.0 | 77,322 ± 9,093 | 47,701 ± 8,319 | 296 ± 52 s |

Per-run token counts are stable to about ±10 %, and a market-only analysis costs
roughly ¥0.5. Full per-run table: `runs/main/results.md`.

## 5. The modification and its measured effect

**Change (one variable, three levels):** `max_tool_rounds` 12 (upstream default)
→ 3 → 1. It is set by `--condition` in `run_experiment.py`; nothing else in the
repository is touched.

A "round" is one assistant message carrying tool calls (`graph/setup.py`). After
the cap, the analyst is told to write its report (`wrap_up`).

| measurement | 12 | 3 | 1 | 12 → 1 |
|---|---|---|---|---|
| tool calls per run | 10.3 ± 0.6 | 10.0 ± 1.0 | 2.0 ± 0.0 | **−81 %** |
| snapshot tool called | 1.0 | 1.0 | 1.0 | unchanged |
| `get_indicators` calls | 8.3 | 8.0 | 0.0 | −100 % |
| tokens in / out | 99.9k / 50.2k | 104.7k / 49.0k | 77.3k / 47.7k | −23 % / −5 % |
| latency | 330 s | 326 s | 296 s | −10 % |
| grounding accuracy | 100 % | 100 % | 100 % | **unchanged** |
| ratings observed | OW, OW, Hold | OW, OW, UW | **Hold, Hold, Hold** | — |

**Finding 1 — the shipped default is about four times more budget than the agent
uses.** At three rounds the behaviour is *identical* to twelve: same tool count,
same tools, same tokens, and the framework's `wrap_up` warning never fires. The
analyst batches its eight indicator calls into one or two rounds. A cap of 3 is
therefore a no-op, and the modification as originally planned produced no
measurable difference at all.

**Finding 2 — at one round the cap binds, and grounding survives.** The wrap-up
message fires every time (`Market Analyst used its 1 tool rounds (get_stock_data
x1, get_verified_market_snapshot x1)`), tool calls fall from 10.3 to 2, input
tokens fall 23 % and latency 10 % — and grounding stays at **100 %**.

That combination is the interesting part. The eight `get_indicators` calls in the
baseline are **redundant**, because `get_verified_market_snapshot` already returns
the indicator set; the agent was fetching the same numbers twice from two tools
and then cross-checking them. Spending a quarter of the tool budget therefore
buys no extra accuracy — it buys the cross-check itself, which is what §4.1
observed the agent performing.

**Finding 3 — cheaper is not neutral for the decision.** Every one-round run
returned **Hold**, while the richer runs split between Overweight, Hold and
Underweight. Removing the redundant calls did not damage any number in the
report, but it changed what the system concluded. A cost optimisation that looks
free on an accuracy metric is not free on the output the user reads — which is
exactly the kind of claim a reproducibility study exists to surface.

## 6. Debug diary

Eight blockers, in the order they appeared. This section is the part a reader
cannot get from the repository's README.

### 6.1 The default data home is not writable (and would leak state anyway)

First launch died immediately:

```
PermissionError: [Errno 1] Operation not permitted: '/Users/.../.tradingagents'
```

Upstream writes results, cached prices and the memory log to `~/.tradingagents`.
Two fixes were needed at once: redirect `TRADINGAGENTS_RESULTS_DIR`,
`TRADINGAGENTS_CACHE_DIR` and `TRADINGAGENTS_MEMORY_LOG_PATH` into the run
directory, and isolate the memory log per run so repetitions are comparable. The
second matters for the experiment: without it run 2 would read run 1's decision.

### 6.2 The default models are not callable from this account

Upstream defaults to `gpt-6-sol` / `gpt-6-luna`. Probing `/v1/models` on the
DeepSeek endpoint returned only `deepseek-flash` and `deepseek-v4-pro`. Both tiers
were repointed through the provider config rather than by editing source, so the
change is visible in one place and recorded in every run JSON.

Two side effects were documented rather than hidden: `deepseek-flash` is a
thinking model, so it largely ignores `temperature` (the README predicts this),
and its thinking tokens count towards output cost. A third surfaced only in the
logs: the framework's *structured-output* agents (Research Manager, Trader)
occasionally answer in plain text instead of calling the schema tool, producing

```
structured-output invocation failed (structured output returned no parsed result);
retrying once as free text
```

in 7 of 9 runs. It is a **handled** degradation — the framework retries as free
text and the rating still parses — but it costs one extra call per occurrence and
is a direct consequence of the model swap, so it belongs in the record.

### 6.3 The framework's own stat handler under-reports tool calls

`cli/stats_handler.py` counts `on_tool_start`, but the graph does not pass its
callbacks into the tool nodes, so `tool_calls` read **0** on a run that had clearly
used tools. The tell: the first run reported `tool_calls: 0` while quoting prices
to the cent, which is impossible without a data call.

Rather than edit upstream source (which would contaminate the baseline), the
driver wraps `StructuredTool.func` for the market tools and counts invocations
outside the framework, after verifying the wrapper against a direct invoke.

### 6.4 The first ground-truth auditor was wrong, not the agent

The initial auditor reported "grounding accuracy 21 %" with 75 unsupported
numbers. Every failure was an artifact:

- `close 333.143` was attributed to 2026-07-31, but the sentence says "prior
  close", which belongs to the previous session;
- `307.62 (2026-08-19)` is a **VWMA** value, not that day's print;
- the 200-SMA "error" (recomputed 284.28 vs reported 282.63) was my own fault: my
  history window began 2026-01-01, so a 200-day average could not be formed.

Fixes: require a contiguous snapshot row, ignore table rows and numbers preceded
by an indicator name, drop ambiguous "prior close" sentences from the headline
metric, and extend the history window to two years.

### 6.5 Silent runs: output buffering made a five-minute run look hung

Piping the driver through `tail`/`grep` in a background shell swallowed every line
until process exit; two healthy runs were killed as "hung". Fixed by writing
unbuffered (`python -u`) logs to per-run files plus a heartbeat on every LLM
completion (`[llm] calls=… in=… out=… tools=… t=…s`). Cost of this mistake:
about 25 minutes and one wasted run.

### 6.6 The tool budget was not a cost lever — the first modification failed

The planned modification (`max_tool_rounds` 12 → 3) produced **no effect at all**:
identical tool counts, identical tokens, no `wrap_up` warning. The hypothesis
"less tool budget saves money" was simply false above the batching factor. The
response was to keep the same variable and extend it to a level that binds (1),
turning a failed experiment into a dose–response curve. Recording this matters:
as pre-registered, the modification would have been reported as a null result.

### 6.7 The auditor was wrong a second, third and fourth time

After the model fix, one run still showed 0.958 grounding. Both remaining
mismatches were again the auditor:

- the report wrote `MACD 1.267 vs signal −0.238`, and the label table only knew
  `MACD signal` / `signal line`;
- another report put the value *before* the label, in a table row
  (`` `macds`  | −0.2381 | ... | MACD above signal``), while the check only
  searched forward from the label;
- a robustness run on NVDA wrote `$220.653 (08-26 close to 08-27 low)`, and the
  auditor anchored the price to the first date inside the parenthesis — the
  value was the *second* date's low.

Fixes: accept `signal` without the `MACD` prefix, search ±40 characters around
the label, and skip any parenthetical naming more than one date. After that,
131/131 claims match. **Four of this study's eight blockers were bugs in the
measuring instrument** — which is itself the main methodological lesson.

### 6.8 Budget arithmetic

The account held ¥7.28 at the start; a market-only run costs ≈ ¥0.5, so the first
design (n=6) hit the floor at ¥1.88 and had to be topped up before the third
condition could run. The design was shaped by that constraint at every step: one
analyst instead of four, three levels of one variable instead of several
variables, and a written record of what was cut (§8).

## 7. Conclusions

**What reproduces.**

1. **Grounding.** 131 of 131 auditable numeric claims, across eleven runs and two
   instruments, match an independent recomputation; all five OHLCV fields of the
   analysis session match to the cent. The verified-snapshot mechanism is real,
   the agent visibly performs its own cross-check, and the "fabricated price
   levels" bug the README describes as fixed does not reappear in this sample.
2. **Cost profile.** A market-only analysis is ~5 minutes of wall clock and
   ~100k input + 50k output tokens, ≈ ¥0.5. Cheap enough for research, expensive
   enough that per-ticker daily sweeps need caching.

**What does not reproduce.**

1. **Decision stability.** Identical inputs produced Overweight, Hold and
   Underweight across nine runs with temperature 0. The repository predicts this,
   so the finding confirms rather than contradicts it — but it means one rating is
   one sample, not one decision.
2. **The cost hypothesis behind the modification.** Cutting the tool budget does
   not reduce cost proportionally until the cap binds, and the default cap never
   binds. The lever is the *number of distinct tools the agent decides to call*,
   not the cap the framework imposes.

**What the modification teaches.** The eight redundant `get_indicators` calls are
free insurance *for accuracy* (grounding is identical without them) and not free
*for the decision* (every cheap run said Hold). A practitioner who optimises on
tokens alone would ship a system that is just as accurate and materially more
conservative, without noticing.

**Recommendations to future users.**

1. Do not treat one run as one decision. Run 3–5 times and report the
   distribution, exactly as this study does.
2. If you need grounding only, one tool round is enough — `get_verified_market_snapshot`
   already carries the indicators. If you need the rating the baseline produces,
   keep the redundant calls; they act as a second opinion, not as waste.
3. Pin the analysis date, and keep the memory log out of comparative experiments.
4. Budget ≈ ¥0.5 and ≈ 5 minutes per market-only analysis, and multiply by the
   analyst roster before planning a sweep.

## 8. Limitations

- **One ticker, one date, one model, n=3 per condition.** The grounding result is
  a property of the tools and was spot-checked on a second ticker, but the rating
  distribution is a sample, not an estimate.
- **The paper's portfolio numbers are not reproduced.** Out of scope by design;
  no claim is made about them in either direction.
- **Model substitution.** Absolute quality is not comparable to the paper's
  GPT-6-based runs; only framework behaviour is.
- **Claims audited vary per run** (8–20), because report layout varies; the metric
  is accuracy over attributable claims, not a fixed checklist.
- **The auditor is mine.** It was wrong three times before it was right, and its
  thresholds are documented rather than hidden.

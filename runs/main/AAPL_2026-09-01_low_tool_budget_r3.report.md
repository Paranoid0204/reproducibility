## instrument_context

The instrument to analyze is `AAPL`. The tools serve this instrument; refer to it by this exact ticker in every report and recommendation, preserving any exchange suffix (e.g. `.TO`, `.L`, `.HK`, `.T`, `-USD`). Resolved identity: Company: Apple Inc. (its current name, given only to identify it; on 2026-09-01 it may have been named differently). Do not substitute a different company or ticker unless a tool result explicitly disproves this resolved identity.

## market_report

# AAPL — Technical Analysis Report
**Analysis date: 2026-09-01 (Tuesday) | Last verified close: $325.13**

---

## 1. Data Provenance & Verification Notes

All exact OHLCV and indicator values below come from the **verified market snapshot** for AAPL dated 2026-09-01, which matches the underlying indicator series exactly (e.g., `close_10_ema` 315.7769 → 315.777; `macd` 1.26742; `atr` 7.61732). **No conflicts were found** between the snapshot and the `get_indicators` output.

**What I could NOT retrieve:**
- **`vwma`** — the volume-weighted moving average was not pulled; volume analysis below is based on raw volume from the price CSV.
- **Historical series for `boll`, `boll_ub`, `boll_lb`, and `atr`** — only the latest (2026-09-01) values are available from the snapshot. I therefore cannot state when price first closed above the upper band or how ATR has evolved; I only use the current values.

**Latest verified OHLCV (2026-09-01):** Open 316.98 · High 327.30 · Low 314.73 · **Close 325.13** · Volume 53,167,400.

---

## 2. Price Structure: Three Distinct Regimes Since December 2025

**Phase 1 — Correction (Dec 2025 → Mar 2026).** AAPL fell from 282.331 (2025-12-01) to a closing low of 246.030 on 2026-01-20 (intraday 242.759), then made a slightly lower closing low of 246.191 on 2026-03-30 (intraday 245.073). This was a ~13% drawdown regime with the 50-SMA above the 200-SMA the whole time but price oscillating around/below both.

**Phase 2 — Trend re-acceleration (Apr → Jul 2026).** A sustained advance carried price from 258.399 (2026-04-06) to 339.787 (2026-07-28 close), with the intraday period high of **342.595 on 2026-07-28**. The move was orderly, stair-stepping through 270s (late April), 300s (late May), and 330s (late July).

**Phase 3 — The 2026-07-31 shock and August repair.** This is the single most important structural fact in the dataset:
- 2026-07-30: close **333.143**
- 2026-07-31: opened **304.547**, closed **308.644** — a one-day decline of **−7.35%** on volume of **132.5M** vs. 74.8M the prior session.
- Critically, the 2026-07-31 high was **310.422** while the 2026-07-30 low was **329.306** — meaning a **true downside gap between ~310.42 and ~329.31 was created and remains unfilled.**

Price then spent all of August building a base: closing low **302.25 on 2026-08-12** (intraday 300.57), repeatedly stalling in the 308–311 zone (2026-08-10 through 2026-08-25 closes: 308.26, 304.91, 302.25, 305.26, 305.93, 305.59, 310.03, 316.83, 311.30, 309.35, 310.34, 309.90).

**The current signal:** The breakout began 2026-08-28 (close 319.70, high 322.37), paused 2026-08-31 (316.85), and resumed decisively on **2026-09-01 with a close of 325.13** at the upper end of the day's range (high 327.30, low 314.73). This is the highest close since 2026-07-30, and it places price **inside the 07-31 gap** (310.42 / 329.31) — i.e., price is actively repairing the shock.

---

## 3. Trend Analysis (Moving Averages)

| MA | 2026-09-01 Value | Price vs. MA | Read |
|---|---:|---:|---|
| `close_10_ema` | 315.777 | **+2.96%** | Short-term momentum positive |
| `close_50_sma` | 312.761 | **+3.96%** | Medium-term trend bullish |
| `close_200_sma` | 282.626 | **+15.04%** | Long-term uptrend firmly intact |

- **Long-term (`close_200_sma`):** The 200-SMA has risen *monotonically* in every reading from 270.464 (2026-07-06) to 282.626 (2026-09-01). Price at 325.13 is 15% above it. This is a textbook long-term uptrend — not a market in structural distribution.
- **Medium-term (`close_50_sma`):** The 50-SMA bottomed at 309.2327 on 2026-07-31 (the gap day) and has crept up to 312.761. Notably, the flat stretch from 2026-08-03 (309.256) to 2026-08-21 (309.994) shows the 50-SMA was essentially horizontal during the base — and it has now **turned up over the last seven sessions** (311.02 → 311.33 → 311.81 → 312.19 → 312.76). A rising 50-SMA under price is the cleanest confirmation of trend resumption.
- **Short-term (`close_10_ema`):** The 10-EMA collapsed from 331.02 (2026-07-30) to a trough near 308.67 (2026-08-17), then ramped hard to **315.777**. Price is 2.96% above it — a supportive but not yet over-extended spread.
- **Golden cross status:** The 50-SMA (312.76) sits **~30.1 points above** the 200-SMA (282.63), and has been above it throughout the retrieved window. The trend stack is fully bullish: **price > 10-EMA > 50-SMA > 200-SMA**, and the 10-EMA (315.78) crossed back above the 50-SMA (312.76) on **2026-08-20** (10-EMA 310.53 vs. 50-SMA 309.63) after being below it in early August — a fresh short-term bullish crossover.

**Caution:** All three averages are lagging constructs. The 200-SMA at 282.63 is now ~13% below price, which means a routine mean-reversion to the 50-SMA would be a −3.8% move without breaking anything structural.

---

## 4. Momentum

**RSI (14): 61.16.** The RSI path tells the recovery story cleanly:
- 2026-07-28: **68.90** (near-overbought, immediately before the −7.35% day)
- 2026-07-31: 43.25 (shock)
- 2026-08-12: **40.36** (August low point in momentum)
- 2026-08-21: 47.40 (still below 50)
- 2026-08-27: 52.67 → 2026-08-28: 57.48 → 2026-09-01: **61.16**

The RSI has pushed **above 60 for the first time since the July shock**, in tandem with price making a higher high. This is momentum *confirming* price — not diverging. There is **room before the 70 threshold**, roughly 9 RSI points, so the move is not yet statistically overbought. The important nuance: in July, RSI 67–69 proved to be the danger zone, so a push into the high 60s should be treated as a place to reduce risk, not chase.

**MACD: 1.26742 | Signal: −0.23811 | Histogram: +1.50553.**
- The **MACD/signal bullish crossover occurred on 2026-08-26** (MACD −1.0307 vs. signal −1.1851), with the histogram flipping positive at +0.154 on that date.
- The histogram has since expanded every single session: +0.154 (08-26) → +0.416 (08-27) → +0.894 (08-28) → +0.973 (08-31) → **+1.506 (09-01)**. Expanding histogram = *accelerating* upside momentum, not a fading bounce.
- **The MACD line crossed above zero on 2026-09-01** (−0.614 signal on 08-31 → +1.267 on 09-01), a higher-quality confirmation than the signal crossover alone. The signal line at −0.238 will likely cross zero within a session or two if the advance holds.
- Context: MACD was 9.60 on 2026-07-29 and only reached zero-crossing territory now — this is a *fresh* cyclical upturn, roughly one month old, which in MACD terms is early-to-mid cycle rather than late.

**Momentum verdict:** RSI (61, rising, not extended) + MACD (fresh signal cross, expanding histogram, zero-line cross) is a **constructive, early-stage alignment**. The one blemish is that both are measured against a stock that just printed a violent shock; momentum re-accelerations after gap-downs are common and can fail at the gap's upper boundary.

---

## 5. Volatility & Bollinger Positioning

| Measure | Value | Interpretation |
|---|---:|---|
| `boll` (20-SMA) | 311.28 | Price 4.45% above the mean |
| `boll_ub` | 322.338 | **Price closed $2.79 (0.87%) above the upper band** |
| `boll_lb` | 300.221 | +8.30% below price |
| Bandwidth | 22.117 | **7.11% of the mid-band** |
| `atr` | 7.617 | **2.34% of the 325.13 close** |

**The key volatility observation:** AAPL closed at 325.13, **above the upper Bollinger Band at 322.338**. Two readings are possible and both must be respected:
1. *Breakout interpretation:* A close outside the band on expanding volume (53.2M vs. ~39.3M August average) is a legitimate volatility-expansion breakout signal. Bands will widen, and the mid-band at 311.28 will rise to meet price.
2. *Extension interpretation:* A downside gap shock compressed the bands (the 20-SMA at 311.28 is now *below* the 50-SMA at 312.76, indicating August's chop pulled the mean down), so a re-expansion higher mechanically pushes price outside the band. Closing above the upper band is by itself **not** proof of sustainable strength — prices "ride the band" in strong trends but mean-revert to the mid-band ~4.5% lower.

The honest synthesis: **the band break is real but unconfirmed.** A second consecutive close above ~322.34 would validate it; a close back inside (below 322.34) would flag a failed breakout.

**ATR 7.617 (2.34% of price)** is elevated relative to a normal large-cap tape, and it is *the* number that should drive position sizing. A single average day's range now equals about $7.62.

---

## 6. Volume Analysis

- **2026-09-01: 53,167,400** — roughly **35% above the August 4–31 average of ~39.3M** (computed from the sixteen available August sessions). Expanding volume on the breakout day is a positive confirmation.
- **2026-08-28: 38,649,400** on the first breakout push — only average. The confirmation therefore rests mostly on the 09-01 session.
- **The elephant in the room: 2026-07-31 at 132,489,100** (vs. 74.8M on 07-30). That is the distribution/capitulation day that created the unfilled gap. Until price reclaims 329–333, that volume bar represents overhead supply.
- **2026-06-26 at 261,775,500** and **2026-06-25 at 107,013,700** mark a separate high-volume event (a −7.1% day from 295.695 on 06-24 to 274.913 on 06-25). Both of these volume spikes sit **above** current price in the 273–296 zone? No — 06-25/06-26 closed at 274.913/283.535, **below** current price, meaning that supply has been absorbed. The July 07-31 gap supply in the 310–333 zone is the only unresolved overhead.
- Without `vwma`, I cannot quantify whether money flow is accumulating *into* the advance versus price drifting up on thin participation. This is a genuine gap in the analysis.

---

## 7. Actionable Levels & Scenarios

### Resistance (overhead supply)
| Level | Source |
|---:|---|
| **327.30** | 2026-09-01 intraday high — immediate |
| **329.31** | 2026-07-30 low = **bottom edge of the unfilled gap** |
| **333.14** | 2026-07-30 close = gap top / prior breakdown close |
| **337.90 / 339.79** | 2026-07-29 / 2026-07-28 closes |
| **342.60** | 2026-07-28 intraday high = period high |

### Support
| Level | Source |
|---:|---|
| **315.78** | `close_10_ema` — first dynamic support |
| **312.76** | `close_50_sma` — trend defense line |
| **311.28** | `boll` mid-band |
| **302.25 / 300.57** | 2026-08-12 closing low / intraday low — base floor |
| **282.63** | `close_200_sma` — structural bull/bear line |

### Scenario A — Gap fill continues (base case, ~60% weight)
Price is already inside the 310.42–329.31 gap. A hold above the 10-EMA (315.78) keeps the MACD/RSI alignment intact and targets **329.31 → 333.14** first, then 337.90. **Trigger:** two consecutive closes above 322.34 (upper band). **Invalidation:** a close below 312.76 (50-SMA).

### Scenario B — Failed breakout / return to base (bear case, ~40% weight)
Closing above the upper band while still *inside* a gap-down zone is exactly the setup where trapped buyers exit. A daily close back below **322.34** (upper band) would be the first warning; below **315.78** (10-EMA) the 08-28 breakout is failed; a close below **311–313** (mid-band / 50-SMA cluster) reopens the 302–305 August base and puts the 300.57 low in play.

**Why I do not weight Scenario A higher:** the July 28 RSI peak at 68.90 was followed within one session by a −7.35% gap on 132.5M shares. Nothing in the data proves that overhead seller is gone — the drawdown from 342.595 (07-28 high) to 300.57 (08-12 low) was −12.27%, and price has recovered only +7.57% from the 08-12 close (302.25 → 325.13). This is a recovery, not yet a new high.

---

## 8. Risk Management

- **Stop placement:** A volatility-appropriate stop sits at **313.50–315.00** — just below the 10-EMA (315.78) and above the 50-SMA (312.76), roughly **1.3–1.5 × ATR** below the 325.13 close. A wider structural stop at **310.00** (below the 08-31 low of 312.80 and the mid-band) gives 1.98 × ATR of room and risks 4.66% from entry.
- **Position sizing:** With ATR at 2.34% of price, size positions so that 2×ATR (≈$15.23) equals no more than your per-trade risk budget. A 1%-of-portfolio risk budget implies roughly 6.5% of portfolio in notional for a 2-ATR stop — half the size you would use if ATR were 1.1%.
- **Do not chase 325.** The risk/reward at current price is poor: upside to gap top 333.14 is +2.46%, downside to 50-SMA 312.76 is −3.80%. A better entry is either (a) a pullback to 315–317 that holds the 10-EMA, or (b) a decisive close above 329.31 with volume, where the gap fill becomes confirmed and 337.90 becomes the target.
- **Event risk:** I have **no news or fundamental data** from these tools. The 2026-07-31 −7.35% gap and the 2026-06-25 −7.1% drop with extreme volume are unexplained by the price data alone — these are almost certainly event-driven and imply **elevated headline risk** around any forward catalyst.

---

## 9. Indicator Selection Rationale

I selected **8 complementary indicators** spanning trend, momentum, volatility, and band positioning — deliberately avoiding redundancy:

| Indicator | Why it fits this context |
|---|---|
| `close_200_sma` | Establishes that the long-term uptrend is intact despite the July shock (+15% above it). |
| `close_50_sma` | Captures the exact inflection: it flatlined during the August base and has now turned up — the cleanest trend-resumption evidence. |
| `close_10_ema` | Fast support for entry/stop placement and confirmation of the 08-20 short-term crossover above the 50-SMA. |
| `macd` | Confirms the cyclical upturn via the **zero-line cross on 09-01**, a higher-quality signal than a signal-line cross alone. |
| `macds` | Defines the 08-26 crossover date and shows the signal line still negative (−0.238) — i.e., the turn is fresh, not extended. |
| `rsi` | At 61.16, rising and *not* overbought, quantifying remaining headroom while flagging the 67–69 danger zone seen in late July. |
| `boll_ub` | Essential here: price closed **above** 322.34, which is the single most important binary signal (breakout vs. extension) in this setup. |
| `atr` | At 7.617 (2.34%), it is the correct basis for stops and position size in a post-gap, high-ATR regime. |

*Excluded:* `macdh` (redundant with `macd`/`macds`, though its expansion pattern is cited as supporting context), `boll`/`boll_lb` (mid-band and lower band are not decision-relevant for a price above the upper band), `vwma` (not retrieved).

---

## 10. Summary Table

| Dimension | Evidence (2026-09-01) | Signal |
|---|---|---|
| **Long-term trend** | Close 325.13 vs. `close_200_sma` 282.626 (+15.04%); 200-SMA rose every reading since 270.464 (07-06) | **Bullish** |
| **Medium-term trend** | Close vs. `close_50_sma` 312.761 (+3.96%); 50-SMA turned up last 7 sessions | **Bullish** |
| **Short-term trend** | Close vs. `close_10_ema` 315.777 (+2.96%); 10-EMA crossed above 50-SMA on 08-20 | **Bullish** |
| **Momentum (RSI)** | 61.16, up from 40.36 (08-12); below 70 | **Bullish, not overbought** |
| **Momentum (MACD)** | MACD 1.267 above signal −0.238; histogram expanding +0.154→+1.506; zero cross on 09-01 | **Bullish, accelerating** |
| **Volatility bands** | Close 325.13 vs. `boll_ub` 322.338 (+0.87%); bandwidth 7.11% | **Breakout, UNCONFIRMED** |
| **Volatility (risk)** | `atr` 7.617 = 2.34% of price | **Elevated — size down** |
| **Volume** | 53.17M on 09-01, ~35% above ~39.3M August avg | **Confirms breakout day** |
| **Key structure** | Price inside unfilled 310.42–329.31 gap from 07-31 | **Overhead supply** |
| **Immediate resistance** | 327.30 → **329.31** → 333.14 → 337.90 → 342.60 | — |
| **Immediate support** | 315.78 → 312.76 → 311.28 → 302.25 / 300.57 | — |
| **Suggested stop** | 313.50–315.00 (1.3–1.5×ATR); structural 310.00 | — |
| **Net bias** | Recovery inside a gap; trend + momentum aligned, but band break unconfirmed and R:R poor at 325 | **Constructive but do not chase — buy pullbacks to 315–317 or breakout above 329.31** |

**Bottom line for AAPL:** The trend stack (price > 10-EMA > 50-SMA > 200-SMA), a rising RSI at 61, and a freshly zero-crossed MACD with an expanding histogram all point the same way — the August base is resolving higher. But AAPL is doing so *inside the unfilled gap* left by the 2026-07-31 −7.35% session, and it just closed above its upper Bollinger Band. The trade is not the current price; it is either a disciplined pullback entry near 315–317 with a stop under 312.76, or a volume-confirmed close above 329.31 that opens 333.14 and then 337.90.

## investment_plan

**Recommendation**: Underweight

**Rationale**: The bear case wins on the actionable issue: AAPL at **325.13** is still inside the unfilled **310.42–329.31** gap, only about **1.3%** below the gap top, and just **0.87%** above the upper Bollinger Band at **322.338**. That is a poor entry point, and the bull implicitly concedes it by recommending waiting for **315–317** or a confirmed close above **329.31** rather than buying now. The volume evidence is also not decisive: **53.17M** shares is constructive versus the August average, but far below the **132.5M** July 31 distribution day, so absorption of overhead supply is not proven. Near-term risk/reward is unfavorable: upside to **329.31** is roughly **1.3%**, while downside to the 50-SMA at **312.76** is roughly **3.8%**, and downside to the August base near **302.25** is roughly **7.1%**. I am not choosing Sell because the long-term trend stack remains positive—AAPL is above its 10-EMA, 50-SMA, and 200-SMA—and momentum is improving with RSI at **61.16** and MACD crossing above zero. But the upper-band close is unconfirmed, the gap remains overhead resistance, and there is no fundamentals/news/sentiment evidence in this run to validate the qualitative moat argument. That supports trimming/avoiding new money, not exiting outright.

**Strategic Actions**: Treat “standard allocation” as the neutral AAPL weight. If currently at or above standard allocation, trim AAPL to roughly **70–75% of standard allocation** and do not add at **325.13**. Keep the remaining core position for the still-intact long-term trend. Use **322.34** as the first warning line; a daily close below it should prompt another trim toward **60–65% of standard allocation**. A close below **315.78** fails the recent breakout attempt and should reduce AAPL to **50% or less** of standard allocation. A close below **312.76** would signal structural damage and justify cutting to a minimal residual position, with the next referenced downside levels at **311.28**, then **302.25/300.57**, and ultimately **282.63**. Only re-risk toward standard allocation or better on a daily close above **329.31** with convincing volume expansion, with further confirmation above **333.14**; alternatively, a pullback that holds **315.78** and reverses cleanly can justify a small add, but with a hard stop below **312.76**.

## trader_investment_plan

**Action**: Sell (partial trim — Underweight)

**Reasoning**

The plan calls for Underweight, and under my sizing convention an Underweight research call maps to a Sell, expressed as a reduction in exposure rather than a full liquidation. The technical report's own risk/reward arithmetic supports cutting now:

- AAPL at **325.13** sits inside the unfilled **310.42–329.31** gap left by the 2026-07-31 −7.35% session, with the gap top only **1.3%** above. The 132.5M-share distribution day that created that gap is unabsorbed; the 53.17M-share breakout day is 35% above the August average but only 40% of that supply bar. Overhead supply is therefore not proven cleared.
- The instrument closed **325.13 vs. `boll_ub` 322.338** — $2.79 (0.87%) above the upper band — and the band break is explicitly labeled *unconfirmed* in the report. A second close above 322.34 is required; a close back inside flags a failed breakout.
- Asymmetry is unfavorable at the current price: upside to 329.31 is ~1.3%, while downside to the 50-SMA at **312.76** is ~3.8% and to the August base at **302.25** is ~7.1%. The report itself says "do not chase 325."
- Volatility is elevated: `atr` **7.617** = 2.34% of price, so a single average session is ~$7.62. This argues for smaller gross exposure regardless of direction.

Why not a full exit (and why not Hold): the trend stack is intact — price > `close_10_ema` 315.777 > `close_50_sma` 312.761 > `close_200_sma` 282.626, the 200-SMA has risen monotonically, RSI is 61.16 and not overbought, and MACD crossed above zero on 2026-09-01 with an expanding histogram (+0.154 → +1.506). That is a constructive, early-stage upturn, so the long-term core should be retained. But no fundamentals, news, or `vwma`/money-flow evidence was retrievable, and the two −7%+ volume events remain unexplained event risk — insufficient grounds to add or to hold full weight.

**Entry Price**: 325.13 (reduce at market near the 2026-09-01 close; do not initiate new long exposure here)

**Stop Loss**: 329.31 — the bottom edge of the 2026-07-31 gap. This is the invalidation level for the reduction thesis: a daily close above 329.31 with convincing volume expansion means the gap is being repaired, at which point the trimmed exposure should be re-established (with a second confirmation above 333.14). For the retained core position, the structural line is 312.76 (50-SMA); a close below it justifies cutting to a minimal residual.

**Position Sizing**: Trim to **70–75% of the caller's standard AAPL allocation**; add nothing at 325.13. Escalation ladder from the plan: daily close below 322.34 → trim toward 60–65%; close below 315.78 → 50% or less; close below 312.76 → minimal residual (next referenced downside 311.28, then 302.25/300.57, ultimately 282.63). Re-risk toward standard or above only on a daily close above 329.31 with volume, confirmed above 333.14. With ATR at 2.34% of price, cap incremental risk so that 2×ATR (~$15.23) stays within the per-trade risk budget — roughly half the notional you would carry at a 1.1% ATR; the remaining core should be sized so a full retest of 302.25 (−7.1%) is tolerable. Current holdings and cash were not provided, so apply these as fractions of your own standard weight rather than absolute share counts.

## final_trade_decision

**Rating**: Underweight

**Executive Summary**: Trim AAPL to roughly 70% of standard allocation (65-75% band; use 65% if the position is oversized or event-risk-sensitive) and add nothing at 325.13. De-risk on close-based triggers — 322.34, then 315.78 (cap ~60% or less), then 312.76 (minimal residual) — and re-risk only in tranches after a daily close above 329.31 on volume expanding across more than one session, with a second confirmation above 333.14. Size the retained core so 2xATR (~$15.23) stays inside the per-trade risk budget and a retest of 302.25 (-7.1%) is comfortably absorbable rather than merely tolerable.

**Investment Thesis**: The bear case wins on the actionable issue: entry price. AAPL at 325.13 sits inside the unfilled 310.42-329.31 gap from the 2026-07-31 -7.35% session, only ~1.3% below the gap top and 0.87% above the upper Bollinger Band at 322.338 — a break the technical work itself calls unconfirmed. The volume evidence does not clear the overhead seller: 53.17M shares on 2026-09-01 is ~35% above the August average but only ~40% of the 132.5M July 31 distribution bar. Payoff asymmetry is negative at full weight: ~1.3% upside to 329.31 versus ~3.8% downside to the 50-SMA at 312.76 and ~7.1% to the August base near 302.25, with ATR at 7.617 (2.34% of price) making a routine two-ATR week (~$15.23) cost more than the trim saves. The aggressive analyst's own framing concedes the point — you cannot refuse to stand in front of the largest seller of the last two months and then defend 70-75% as a position instead of a ceiling. The bull case is nonetheless strong enough to defeat the conservative seat's 50-60% (or 40-50%) proposal: price sits above the 10-EMA 315.78 > 50-SMA 312.76 > 200-SMA 282.63, the 50-SMA has turned up over the last seven sessions, the 200-SMA has risen monotonically from 270.46 (Jul 6) to 282.63, MACD crossed the zero line on 2026-09-01 with an expanding histogram (+0.154 to +1.506), and RSI at 61.16 is not overbought. Cutting to near-half weight before any close-based trigger has fired front-runs a failed breakout that has not happened; the conservative's valid complaint that the ladder is reactive is answered by trimming now and by making every subsequent trigger close-based rather than intraday. The neutral's "hold full weight, don't chase" is internally contradictory — it accepts full downside on an unconfirmed band break to preserve optionality it is not using. Two mechanical fixes are adopted from the debate: 329.31 is a re-risk/invalidation level, not a protective stop (it sits above the market), and the genuine structural line for the retained core is a daily close below 312.76. Protective puts or a collar make sense only if the position is mandate-constrained, but no options data or portfolio context was provided, so that cannot be the default prescription. Fundamentals, news, sentiment and vwma/money-flow were not retrievable in this run, and the two unexplained -7%+ volume events remain un-underwritten — which argues for carrying below standard weight and for staged rather than binary re-risking. What would change the call: a daily close above 329.31 with volume expanding over more than one session, confirmed above 333.14, restores standard allocation and opens 337.90/342.60; a pullback that holds 315.78 and reverses cleanly justifies a small add with a hard stop below 312.76; a daily close below 312.76 warrants a minimal residual with 311.28, then 302.25/300.57, and ultimately 282.63 as referenced downside.

**Price Target**: 312.76

**Time Horizon**: 1-3 months (tactical trim; core retained through the trend)

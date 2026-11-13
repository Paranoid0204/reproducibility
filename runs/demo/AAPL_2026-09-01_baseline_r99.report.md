## instrument_context

The instrument to analyze is `AAPL`. The tools serve this instrument; refer to it by this exact ticker in every report and recommendation, preserving any exchange suffix (e.g. `.TO`, `.L`, `.HK`, `.T`, `-USD`). Resolved identity: Company: Apple Inc. (its current name, given only to identify it; on 2026-09-01 it may have been named differently). Do not substitute a different company or ticker unless a tool result explicitly disproves this resolved identity.

## market_report

# AAPL — Technical Analysis Report
**Analysis date: 2026-09-01** | Instrument: **AAPL** (Apple Inc.) | Last verified close: **$325.13**

---

## 1. Data verification note

All exact price and indicator values below are taken from the **verified market snapshot for 2026-09-01**, which used the **2026-09-01** trading row (Open 316.98 / High 327.30 / Low 314.73 / Close 325.13 / Volume 53,167,400). The `get_indicators` output matched the snapshot **exactly** on every overlapping field (RSI 61.1599, 50-SMA 312.7607, 200-SMA 282.6264, 10-EMA 315.7770, Boll middle 311.2796, upper 322.3384, lower 300.2209, MACD 1.2674, signal −0.2381, histogram 1.5055, ATR 7.6173). **No discrepancies to flag.**

One housekeeping note: AAPL went ex-dividend on **2026-05-11** and **2026-08-10** ($0.27 each, per the price file). The 200-SMA and all long lookbacks therefore absorb small dividend-related price gaps; this is a normal, non-signal event.

---

## 2. Market context and regime classification

AAPL is in a **primary uptrend that experienced a violent mid-cycle shakeout, and is now re-accelerating out of a six-week base.** The sequence, all from tool data:

| Phase | Dates | Move (close-to-close) |
|---|---|---|
| Q1 drawdown | 2026-03-02 close 264.248 → 2026-03-30 close 246.191 | −6.83% |
| Spring leg up | 2026-03-30 → 2026-07-28 close 339.787 | +38.02% |
| Distribution shock | 2026-07-30 close 333.143 → 2026-07-31 close 308.644 | **−7.35% on 132.5M shares** |
| Base / repair | 2026-08-03 close 303.159 → 2026-08-27 close 314.58 | chop, RSI 40–57 |
| Breakout attempt | 2026-08-28 319.70 → 2026-09-01 **325.13** | +1.70% on 9/1 alone **+2.61%** |

The regime is best classified as **"trend continuation, early-stage re-acceleration, with overhead supply directly above."** This is not a low-risk trend-following entry (price is stretched vs. its short averages), nor is it a reversal setup (trend stack is fully bullish). It is a **momentum-confirmation / breakout-retest regime**, which dictates a specific indicator mix: trend filters for direction, momentum oscillators for exhaustion control, volatility bands for extension/squeeze detection, and volume-weighting for conviction.

---

## 3. Indicator selection (8 chosen) and rationale

| # | Indicator | Value (2026-09-01) | Why it is the right tool here |
|---|---|---|---|
| 1 | **close_10_ema** | 315.777 | Responsive read on the newly-turning short-term momentum; also the first line of defense for a breakout retest. |
| 2 | **close_50_sma** | 312.761 | The medium-term trend spine *and* the level the August base was built around. It is rising (311.81 on 8/28 → 312.76 on 9/1), which matters more than its absolute level. |
| 3 | **close_200_sma** | 282.626 | Strategic bull/bear arbiter. Price is 15% above it and it is still rising; this removes any argument for a short-the-trend bias. |
| 4 | **macd** | 1.2674 | Captures the regime *shift* — MACD was deeply negative through August and has just reclaimed zero. |
| 5 | **macds** | −0.2381 | The signal line is still below zero, which is precisely why the current signal is "early" rather than "late." |
| 6 | **macdh** | 1.5055 | Best single visualization of momentum *acceleration*; five consecutive sessions of expansion. |
| 7 | **rsi** | 61.16 | Exhaustion check. Tells us the breakout is NOT yet overbought — the single most important nuance in this setup. |
| 8 | **atr** | 7.6173 | Mandatory in a name that just printed a −7.35% day and a +2.61% day inside five weeks. Drives stop distance and position size. |

**Deliberately excluded, with reasons:**
- **`boll_ub` / `boll_lb` / `boll`** — I reviewed all three (values used in the analysis below) but capped the formal list at eight. If forced to drop one of the eight, the 10-EMA is the redundant one; the Bollinger envelope at 322.34/311.28/300.22 is currently doing more work than the 10-EMA because price has closed *outside* the upper band.
- **`vwma`** — Reviewed (312.494) and used as a confluence check in §7, but it currently sits within $0.27 of the 50-SMA, so as a standalone selection it duplicates rather than diversifies. Its genuine value today is confirming the **311–313 cost-basis shelf**.
- **`macd` ↔ `macds` ↔ `macdh`** are mathematically linked, so this trio is the maximum acceptable overlap; I would not add a fourth momentum oscillator (e.g., Stochastic) on top of RSI.

---

## 4. Trend structure — fully aligned, but price is extended

The stack is unambiguously bullish and properly ordered:

**Close 325.13 > 10-EMA 315.78 > 50-SMA 312.76 > 200-SMA 282.63**

- **200-SMA (282.626):** rising every session (282.15 on 8/28 → 282.36 on 8/31 → 282.63 on 9/1). The 50-SMA has been above the 200-SMA continuously across the entire visible window (on 2026-05-04: 50-SMA 260.998 vs. 200-SMA 254.784), so the golden-cross regime is long-established, not fresh. This is a **strategic bull-market backdrop**, and it means pullbacks should be treated as buyable until proven otherwise.
- **50-SMA (312.761):** this is the most informative line on the chart right now. It flattened into the August chop — 309.44 (8/10), 309.03 (8/13), 308.90 (8/18), 309.21 (8/19) — and has now **turned up**: 309.99 (8/21) → 310.67 (8/25) → 311.33 (8/27) → 311.81 (8/28) → 312.19 (8/31) → 312.76 (9/1). A flattening-then-rising 50-SMA after a shock is a classic "trend repairs" signature.
- **10-EMA (315.777):** inflected hard off the 8/21–8/25 trough (310.32 → 310.24 → 310.83 → 311.51 → 313.00 → 313.70 → **315.78**). Five consecutive up-days on this average is the cleanest short-term momentum evidence in the dataset.

**The caution:** close is **+2.96%** above the 10-EMA, **+3.96%** above the 50-SMA, and **+15.04%** above the 200-SMA. That is a healthy but extended posture. Historically, entries taken this far above the 10-EMA have poorer risk/reward than retests — which is why the plan in §9 favors a retest/scale approach over a full-size chase at 325.

---

## 5. Momentum — the strongest part of the story

**MACD (1.2674) / Signal (−0.2381) / Histogram (1.5055)**

The MACD complex has produced a textbook **bearish-then-bullish transition within 26 sessions**:

- **Bearish crossover 2026-07-31:** histogram flipped from +0.641 (7/30) to **−1.365** (7/31) — same session as the −7.35% price break and the 132.5M-share volume spike. Momentum and distribution confirmed each other.
- **Histogram trough:** −3.632 on **2026-08-05**, gradually improving to −2.261 (8/17), then turning.
- **Bullish crossover 2026-08-26:** MACD −1.0307 crossed above signal −1.1851, histogram **+0.154** (prior session, 8/25, was −0.143).
- **Expansion since:** +0.416 (8/27) → +0.894 (8/28) → +0.973 (8/31) → **+1.506 (9/1)**. Five straight sessions of a widening histogram is momentum *acceleration*, not just a crossover.

Crucially, **MACD has now crossed above zero** (1.2674 vs. 0.3585 on 8/31), while the **signal line is still below zero** (−0.2381). This configuration — MACD > 0 > signal — describes a trend that has just flipped positive but has not yet been "confirmed" by the lagging signal. It is the earliest, highest-upside phase of a momentum cycle, and simultaneously the phase most vulnerable to a fake-out. The correct response is participation with a tight, ATR-anchored invalidation, not conviction sizing.

**RSI (61.16)** — this is the nuance that separates a good read from a naive one. Price closed **today at its highest level since 2026-07-30**, yet RSI is **61.16**, well short of the 70 overbought threshold. For comparison:
- RSI peak in the July top: **71.66 (2026-07-17)**, with 68.90 (7/28) and 67.29 (7/27).
- RSI low in the August correction: **40.34 (2026-08-03)** and **40.36 (2026-08-12)** — note it **never reached oversold (<30)**. That is a mild, orderly correction, not capitulation, which is consistent with a continuation pattern rather than a top.
- RSI recovery path: 43.55 (8/17) → 48.01 (8/18) → 53.99 (8/19) → 47.40 (8/21, dip) → 47.93 (8/25) → 51.54 (8/26) → 52.67 (8/27) → 57.48 (8/28) → 54.18 (8/31) → **61.16 (9/1)**.

**Interpretation:** there is **no bearish RSI divergence** to point to (price has not made a new high above 339.787, so no divergence condition exists), and there is **~9 points of RSI headroom before overbought**. That gives the breakout room to run toward the 330s before the oscillator becomes a headwind.

---

## 6. Volatility — a squeeze that just resolved upward

Although not in the final eight, the Bollinger geometry is the most actionable structural insight in this dataset, so I am reporting it explicitly:

| Date | Upper | Middle | Lower | Bandwidth ((UB−LB)/Mid) |
|---|---|---|---|---|
| 2026-08-12 | 346.89 | 320.98 | 295.07 | **16.14%** |
| 2026-08-19 | 341.52 | 315.87 | 290.23 | 16.24% |
| 2026-08-25 | 329.37 | 311.39 | 293.41 | 11.55% |
| 2026-08-28 | 318.79 | 309.79 | 300.80 | **5.81% (tightest)** |
| 2026-09-01 | **322.34** | **311.28** | **300.22** | **7.11%** |

That is a **textbook volatility compression followed by directional expansion.** The bands collapsed from ~16% width in mid-August to 5.81% on 2026-08-28, then began widening on 9/1 concurrently with price closing **$2.79 above the upper band (325.13 vs. 322.34)**. A close outside the upper band after a squeeze is a breakout signal, not a mean-reversion signal — but it carries the standard caveat that in strong trends price can "walk the band," so it must be confirmed (see §8).

Also note the middle band (20-SMA, 311.28) has turned up: 309.24 (8/27) → 309.79 (8/28) → 310.48 (8/31) → 311.28 (9/1). **Three consecutive rises after a month of decline** — the short-term mean has re-sloped upward.

**ATR (7.6173)** = **2.34% of the $325.13 close**, and it **rose** on 9/1 (from 7.236 on 8/31) after compressing through late August (7.094 on 8/27, 7.144 on 8/28). Read together with the band widening, this says **realized volatility is re-expanding in the direction of the breakout** — supportive of the move, but a warning that stops must be wider in dollar terms than a mid-August setup would have required. The ATR was as high as **9.86 on 2026-07-31** (the −7.35% day) and 9.82 on 8/3, so the current 7.62 sits below the post-shock peak but above the August lull.

---

## 7. Volume / price confirmation — the one soft spot

The 2026-09-01 volume of **53,167,400** is the **highest since 2026-08-19** (50.5M) and represents ~1.27× my computed average of **~41.9M** across the 21 sessions from 2026-08-04 through 2026-09-01 (derived by summing the daily volumes in the price file). That is *adequate* confirmation, not *overwhelming* confirmation. For context, the 7/31 breakdown day traded **132.5M** and the 6/25–6/26 flush traded **107.0M then 261.8M** — so the bulls have not yet demonstrated institutional-scale accumulation on this leg.

**VWMA (312.494)** adds a genuine insight: it sits **$0.267 below the 50-SMA (312.761)**. In other words, the **volume-weighted average price of the recent past and the simple 50-day average are converging on the same level — a 311.3–312.8 confluence shelf.** VWMA has also inflected sharply upward (309.10 on 8/27 → 309.99 on 8/28 → 310.80 on 8/31 → **312.49 on 9/1**), its fastest four-day rise since mid-July. That shelf is the most defensible "the breakout has failed" line on the chart.

The other side of the VWMA coin: price is **+4.04% above VWMA** ($12.64). Recent buyers are sitting on meaningful unrealized gains, which raises the odds of supply emerging on any stall.

**Tape quality on 9/1** was strong: Open 316.98 (a slight gap up from the 316.85 prior close), traded to a **low of only 314.73**, then closed at 325.13 — **82.7% of the day's 12.57-point range**, near the highs, with the high at 327.30. Buying pressure persisted through the session rather than fading. That is exactly the intraday signature you want on a breakout day.

---

## 8. Key levels map (all derived from tool data)

**Resistance / overhead supply**
| Level | Source | Note |
|---|---|---|
| **327.30** | 2026-09-01 intraday high | Immediate hurdle; today's rejection point on the high |
| **329.31** | 2026-07-30 low | First level of the 7/31 gap |
| **333.14** | 2026-07-30 close | Bottom edge of the pre-gap congestion |
| **334.70** | 2026-07-17 high | Swing high in the July top |
| **339.79 / 344.27** | 2026-07-28 close / 2026-07-29 high | Cycle high close and cycle high intraday |

**Critical structural caveat — the unfilled 2026-07-31 gap:** On 7/31 AAPL opened at **304.547** against a 7/30 range of 329.306–334.462, and the 7/31 high was only **310.422**. That leaves a **price void between roughly 310.42 and 329.31** that has never been traded through on a closing basis until today's advance entered it. **AAPL is currently trading *inside* that gap at 325.13.** Gap zones function as low-liquidity, high-friction territory where prior holders are motivated to exit at breakeven. This is a *conditional* caution, not a proven resistance claim — but it materially raises the risk of chop or rejection between 325 and 333, and it argues for scaling rather than a single full-size entry.

**Support**
| Level | Source | Distance from 325.13 |
|---|---|---|
| **322.34** | Bollinger upper band | −0.86% |
| **315.78** | 10-EMA | −2.88% |
| **314.73** | 2026-09-01 low | −3.20% |
| **312.76 / 312.49** | 50-SMA / VWMA | −3.80% / −3.88% |
| **311.28** | Bollinger middle (20-SMA) | −4.26% |
| **309.88** | Close − 2×ATR | −4.69% |
| **300.22** | Bollinger lower band | −7.66% |

---

## 9. Actionable trade plans

### Plan A — Bullish continuation (primary, base case)
**Trigger:** a daily close **above 327.30** (today's high) with volume ≥ ~53M, ideally after a shallow hold of 322–325.
**Rationale:** MACD zero-line reclaim + histogram expansion + RSI 61 (room to 70) + squeeze expansion + rising 50-SMA.
**Entry:** scale — 1/2 on a confirmed close above 327.30, 1/2 on a successful retest of 322–325 that holds on a closing basis.
**Stop:** **313.70** (1.5×ATR below close) for a swing position; **309.90** (2×ATR) for a wider, lower-turnover position. Both sit beneath the 311.3–315.8 confluence shelf, so the stop is placed where the *thesis* is wrong, not where the noise is.
**Targets:** T1 **329.31**, T2 **333.14**, T3 **339.79**; stretch **344.27**. Partial-scale at each, trail the remainder behind the 10-EMA.

### Plan B — Retest-and-hold (highest risk/reward)
**Setup:** price stalls or pulls back into **315.8–312.5** (10-EMA → 50-SMA/VWMA confluence) *without* a close below 311.28 (Boll middle).
**Entry:** at the reversal candle off that shelf, confirmed by RSI holding above ~45 and MACD histogram staying positive.
**Stop:** **308.50**, below the 2×ATR line and the 8/31–9/1 lows region. Risk ≈ 4.5%.
**Why this is preferable to chasing:** it removes the +3.96% extension above the 50-SMA and the overhead gap friction, and gets you long at the volume-weighted cost basis instead of $12.64 above it.

### Plan C — Breakdown / invalidation
**Trigger:** a daily close **back below 322.34** (upper band) that is followed by a close **below 315.78** (10-EMA), or any close **below 311.28** (Boll middle) regardless of sequence.
**Meaning:** the squeeze resolves as a false breakout; MACD's below-zero signal line reasserts.
**Action:** exit longs. Do **not** short the primary uptrend (price 15% above a rising 200-SMA) — favor standing aside. Only a close below **300.22** (lower band) would justify a tactical short, and even then against the 200-SMA trend.

### Position sizing
With ATR at **7.62 (2.34% of price)**, a 1%-of-equity risk budget permits roughly **1.3% of equity per 1 ATR of stop distance**. Using the Plan A stop of 313.70 (an $11.43 risk, 1.5 ATR), a 1%-risk position is about **0.875× a full unit**. In practical terms: **size at ~75–85% of normal**, because both realized volatility (rising ATR) and structural uncertainty (trading inside an unfilled gap) are elevated.

---

## 10. Risk register — what would falsify this read

1. **Volume is good, not great.** 53.2M at ~1.27× the ~41.9M recent average does not match the 132.5M distribution print of 7/31. If the next up-day comes on declining volume, treat the breakout as suspect.
2. **The 7/31 gap (310.42–329.31) is untested overhead.** Price at 325.13 is inside it. Expect friction; do not assume a straight line to 333.
3. **MACD signal is still negative (−0.2381).** The bullish crossover is 4 sessions old and unconfirmed. A histogram roll-over — from +1.506 back toward +0.90 (the 8/28 level) — would be the first yellow flag.
4. **Extension risk.** +2.96% vs. 10-EMA and +4.04% vs. VWMA. Mean-reversion toward the 315.8–312.5 shelf is a normal, healthy outcome and should not be read as a trend break — unless it closes below 311.28.
5. **The base was shallow, not washed out.** RSI only reached 40.34/40.36 in August; there was no capitulation. This supports continuation, but it also means there is no "clean" accumulation floor under the market beyond the 311–313 confluence.
6. **Event risk is unknown to me.** I have no earnings, guidance, product, or macro calendar in these tools. Any such event can invalidate every technical level above. Do not carry full size through an unknown catalyst.

---

## 11. Summary table

| Dimension | Indicator | Value (2026-09-01) | Signal | Conviction |
|---|---|---|---|---|
| **Price** | Close / O / H / L / Vol | 325.13 / 316.98 / 327.30 / 314.73 / 53.17M | Closed 82.7% up the day's range; +2.61% d/d | Bullish |
| **Long-term trend** | close_200_sma | 282.626 (rising) | Price +15.04% above; strategic bull intact | Strong bullish |
| **Medium trend** | close_50_sma | 312.761 (turned up) | Flattened in August, now rising 5 straight sessions | Bullish |
| **Short trend** | close_10_ema | 315.777 | Price +2.96% above; 10-EMA inflecting sharply | Bullish but extended |
| **Momentum (level)** | macd | 1.2674 | Just reclaimed zero (from 0.3585 on 8/31) | Bullish, early |
| **Momentum (confirmation)** | macds | −0.2381 | Signal still < 0 → crossover not yet confirmed | Neutral / caution |
| **Momentum (thrust)** | macdh | 1.5055 | 5 straight expansions since the 8/26 bullish cross | Strong bullish |
| **Overbought check** | rsi | 61.16 | 9 pts of headroom to 70; no bearish divergence | Bullish, not exhausted |
| **Volatility (regime)** | atr | 7.6173 (2.34% of price) | Re-expanding off the 8/27 low of 7.09 | Two-sided / size down |
| **Volatility (structure)** | boll / boll_ub / boll_lb | 311.280 / 322.338 / 300.221 | Squeeze to 5.81% on 8/28 → 7.11% on 9/1; close $2.79 ABOVE upper band | Breakout confirmed |
| **Volume confirmation** | vwma | 312.494 (rising fast) | Price +4.04% above; confluent with 50-SMA → 311.3–312.8 shelf | Supportive |
| **Overhead friction** | Unfilled gap | 310.42 (7/31 high) → 329.31 (7/30 low) | Price at 325.13 is *inside* the void | Warning |

### Bottom line

**Directional bias: LONG, with reduced size and staged entries.** Four independent evidence streams agree: the trend stack is perfectly ordered and re-sloping (10-EMA > 50-SMA > 200-SMA, all rising), MACD has crossed its signal and reclaimed zero with an accelerating histogram, RSI at 61.16 has room before overbought, and a Bollinger squeeze resolved upward with price closing outside the upper band on above-average volume.

Three things temper the conviction and argue against a full-size chase at 325.13: price is ~4% above both the 50-SMA and the volume-weighted average, the MACD signal line is still below zero (an unconfirmed crossover), and AAPL is currently trading **inside an untested price gap from 310.42 to 329.31** that will supply sellers in the 325–333 band.

The disciplined play is a **half-size starter above 327.30 with the balance added either on a clean 322–325 retest that holds, or on a pullback into the 315.8–312.5 confluence** — with invalidation at **313.70** (1.5×ATR) or **309.90** (2×ATR) for swing risk, and a hard "stand aside" trigger on any close below **311.28** (Bollinger middle). Upside targets are **329.31 → 333.14 → 339.79**, with **344.27** as the stretch.

## investment_plan

**Recommendation**: Underweight

**Rationale**: The bear case wins on the actionable question for AAPL at $325.13, even though the bull wins the broad trend argument. AAPL is above a rising 200-SMA and 50-SMA, and MACD has reclaimed zero, so a Sell/short call is not supported; the bear conceded direction and did not recommend shorting. But the bull’s trade plan lacks an edge at the current price. The 9/1 breakout was 53.17M shares versus 132.5M on the 7/31 −7.35% distribution day—less than half—so upthrust risk is unresolved. The upside targets 329.31/333.14/339.79/344.27 sit in the July buyer supply/breakeven zone. The bull’s own R:R is poor: about 1.28:1 to T3 using a 313.70 stop, about 1.06:1 using the stated 311.28 invalidation, and 0.37:1/0.70:1 to T1/T2. The 313.70 stop is only 1.5× ATR while ATR is expanding to 7.6173 and AAPL recently gapped −7.35%; below 311.28 there is an air pocket toward the 200-SMA at 282.63. The bull’s preferred Plan B entry at 315.8–312.5 implicitly concedes that 325.13 is not an attractive entry. No fundamentals/catalyst data were supplied, so the unexplained 7/31 distribution cannot be dismissed. This supports trimming/avoiding new AAPL exposure, not a full bearish short.

**Strategic Actions**:
- Do not initiate or add to AAPL at $325.13. Treat 327.30–333.14 as a trim/supply zone, not a chase zone.
- If holding a standard AAPL allocation: trim roughly one-third into 327.30–333.14; if 339.79 is reached, trim another 15–20% of the original position. Target residual exposure around 50–70% of standard allocation, i.e., underweight.
- If flat: stay at 0–25% of standard allocation; no new long until a confirmed retest or a volume-confirmed breakout.
- Risk controls: a close below 322.34 is a warning against any adds; a close below 311.28 invalidates the tactical long setup and should cut residual tactical exposure to zero/minimal, because the next major reference is the 200-SMA at 282.63. Do not treat 313.70 as a reliable hard stop for a full position given ATR and recent gap risk.
- Re-entry/upgrade triggers: only consider rebuilding toward neutral on a 311–313 retest that holds with a confirmed reversal candle and volume >60M. Only consider upgrading beyond Underweight if AAPL closes above 333.14 and then 339.79 with volume expanding toward/above the 132.5M distribution day, which would neutralize the bear’s volume-asymmetry objection. Otherwise, use strength to reduce.

## trader_investment_plan

**Action**: Sell

**Reasoning**: The research plan’s Underweight recommendation maps to a Sell/trim call, not a short. The bullish trend is real — AAPL closed at 325.13 above a rising 200-SMA at 282.63 and a rising 50-SMA at 312.76, and MACD has reclaimed zero — but the actionable risk/reward at 325.13 is poor. AAPL is extended versus short-term structure: +2.96% above the 10-EMA at 315.78, +3.96% above the 50-SMA at 312.76, and +4.04% above VWMA at 312.49. It is also trading inside the unfilled 310.42–329.31 gap, with overhead supply at 327.30, 329.31, 333.14, and 339.79. The 9/1 breakout volume of 53.17M was only about 1.27× the recent average and less than half the 132.5M distribution day on 7/31, so conviction is not strong enough to chase. The plan’s own reward/risk is weak: about 1.28:1 to T3 using the 313.70 stop, only about 1.06:1 using 311.28, and 0.37:1/0.70:1 to T1/T2. With ATR at 7.62 and a recent −7.35% gap, the 313.70 stop is too tight for a full position. Plan B’s preferred entry at 315.8–312.5 implicitly concedes that 325.13 is not attractive. I would not short AAPL because the primary uptrend remains intact, but I would reduce/avoid new exposure and use strength to sell.

**Entry Price**: 327.30 for the initial trim; additional trim levels are 329.31 and 333.14. If strength does not materialize, 325.13 is the current-market reduction reference.

**Stop Loss**: 311.28 — a close below this level invalidates the tactical long setup and should cut residual tactical exposure to zero/minimal. A close below 322.34 is a warning against any adds.

**Position Sizing**: For holders, trim roughly one-third into 327.30, trim another 15–20% of the original position if 339.79 is reached, and target residual exposure of 50–70% of standard allocation. If flat, stay at 0–25% of standard allocation and do not initiate a new long until a 311–313 retest holds with a confirmed reversal and volume above 60M, or AAPL closes above 333.14 and then 339.79 with volume expanding toward the 132.5M distribution day. Do not short the primary uptrend.

## final_trade_decision

**Rating**: Underweight

**Executive Summary**: Trim AAPL into strength — do not short and do not add at $325.13. Sell roughly one-third into $327.30, another 10–15% into $329.31–$333.14, and target residual exposure of ~50–60% of standard allocation; if flat, stay at 0–15% and force no entry until a held $311–$313 retest (reversal candle, RSI back above ~45, volume >60M) or a close above $333.14 followed by confirmation through $339.79. Hard invalidation is a close below $311.28 (cut tactical residual to minimal); a close below $322.34 is a no-add warning. Horizon is tactical, roughly one to three months, with upside participation preserved via the residual and dry powder rather than full exposure at a poor entry.

**Investment Thesis**: All three analysts converged on trimming; the real debate was how much residual to keep, and that decided the size. The trend case rules out Sell/short: AAPL is 15% above a rising 200-SMA ($282.63), above a rising 50-SMA ($312.76), MACD has reclaimed zero (1.2674, histogram 1.5055), RSI is 61.16, and the Bollinger squeeze resolved upward — the bear conceded direction and never recommended shorting. But the entry is poor: reward/risk is ~1.28:1 to T3 on the $313.70 stop, only ~1.06:1 on $311.28, and 0.37:1/0.70:1 to T1/T2 — and the conservative's correction is decisive, since those ratios assume stops fill at the stop while AAPL gapped from a $333.14 close to $308.64 (−7.35% on 132.5M shares) five weeks ago, roughly doubling realized risk and pushing the true payoff toward ~0.8:1. Supporting evidence: the 9/1 breakout printed 53.17M shares, ~1.27× the ~41.9M average and less than half the 132.5M distribution day; price sits inside the unfilled 310.42–329.31 gap with supply at 327.30/329.31/333.14/339.79; ATR is 7.62 (2.34%) and expanding; and no sentiment, news, or fundamentals data were supplied, so the unexplained 7/31 distribution and event risk cannot be dismissed. The aggressive analyst's "aggressive, high-reward" framing loses on specifics: his full-size re-entry at 311–313 targets the exact shelf (50-SMA/VWMA 312.5–312.8, Bollinger middle 311.28, gap-fill top 310.42) where the thesis is designed to be abandoned, and his 132.5M volume benchmark is a distribution print, so volume alone is directionless; buying above $339.79 with invalidation below $327.30–$322.34 is $12–$17 of risk against a 7.62 ATR. The conservative's gap-risk point is the best argument in the debate, but his 40–50% residual plus blanket hedges implicitly assumes the gap repeats before the intact uptrend can express itself. Hence the neutral's 50–60% residual with confirmation-gated, halved re-adds: it prices the gap risk without converting de-risking into near-liquidation. What would change the call: a close above $333.14 then $339.79 on volume expanding toward/above 132.5M with a strong close and multi-session follow-through (upgrade toward Hold/Overweight), or a close below $311.28 (cut residual to minimal, next reference the 200-SMA at $282.63). No price target is set — no valuation or catalyst inputs were supplied, so only technical reference levels are defensible, and that data gap is itself part of why full exposure is not warranted.

**Price Target**: not provided

**Time Horizon**: 1-3 months (tactical)

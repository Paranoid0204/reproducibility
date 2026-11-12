## instrument_context

The instrument to analyze is `AAPL`. The tools serve this instrument; refer to it by this exact ticker in every report and recommendation, preserving any exchange suffix (e.g. `.TO`, `.L`, `.HK`, `.T`, `-USD`). Resolved identity: Company: Apple Inc. (its current name, given only to identify it; on 2026-09-01 it may have been named differently). Do not substitute a different company or ticker unless a tool result explicitly disproves this resolved identity.

## market_report

## AAPL — Multi-Timeframe Technical Report (analysis date: 2026-09-01)

### 1. Data integrity check (done first)

I cross-checked `get_stock_data` against `get_verified_market_snapshot` before writing anything. **No discrepancies found.** Both sources return the same 2026-09-01 OHLCV row, and every indicator value returned by `get_indicators` matches the verified snapshot to the reported precision (e.g. MACD 1.2674205 → 1.26742; RSI 61.1599; ATR 7.61732; 50-SMA 312.7607 → 312.761). The signal line (−0.23811) was not separately fetched but reconciles exactly: MACD − histogram = 1.26742 − 1.50553 = −0.23811. All figures below are anchored to the verified snapshot.

**Verified row, 2026-09-01:** Open 316.98 · High 327.30 · Low 314.73 · Close **325.13** · Volume 53,167,400.

---

### 2. Regime assessment: bullish trend, mid-cycle re-acceleration

The moving-average stack is in a textbook bullish configuration, and it is *ordered*, which is the important nuance:

| Layer | Value (verified) | Price vs. layer |
|---|---:|---:|
| Close | 325.13 | — |
| 10 EMA | 315.777 | +2.96% above |
| 50 SMA | 312.761 | +3.96% above |
| 200 SMA | 282.626 | +15.04% above |

10 EMA > 50 SMA > 200 SMA, with the 50 SMA sitting **10.66% above** the 200 SMA. That wide positive spread is the signature of a mature, well-established uptrend rather than an emerging one — the golden-cross work is long since done, and what matters now is whether the *fast* layers are re-accelerating. They are: price reclaimed the 10 EMA, the 10 EMA itself has turned up (310.32 on 2026-08-24 → 312.998 on 08-28 → 315.777 on 09-01), and the 50 SMA has rolled from a flat 308.84 on 2026-08-17 to 312.761.

One caution on the 50 SMA: it was *falling* in spirit during late July (309.23 on 07-31 versus 308.32 on 07-29 — essentially flat) while price collapsed beneath it. Its current upward slope is only a few sessions old. It is a supporting layer, not yet a proven launchpad.

---

### 3. The context that matters most: the 2026-07-31 break and the August base

This is where the current setup gets interesting, and it is fully documented in the price data:

- **2026-07-28:** close 339.787 — the swing high of the sample.
- **2026-07-29:** intraday high 344.273 — the highest print in the dataset.
- **2026-07-31:** open **304.547** versus the prior close of 333.143, on volume of **132,489,100** — roughly 3.3× the 10-day average and the largest volume in the sample outside the 261.8M outlier on 2026-06-26. Close 308.644.
- Measured from the 07-28 close to the 07-31 close, that is **−31.143 points, or −9.17%**, in three sessions.

That single session created an unfilled overhead gap between the 07-30 low (329.306) and the 07-31 open (304.547). **Today's close of 325.13 sits inside that gap**, roughly 4.3 points below its upper boundary. This is the single most important structural observation in the report: the stock is not merely "going up," it is retracing a specific disruption, and the 329.3–339.8 zone is the supply shelf it must absorb.

Between 07-31 and 08-31 the stock built a base: closes ranged from 302.25 (2026-08-12) to 316.83 (2026-08-19), with intraday extremes at 300.57 (08-12 low) and 320.28 (08-20 high). **A 300.5–320.3 box, about 6.5% wide.**

The 2026-09-01 session **closed above the entire box** (325.13 > 320.28), on volume 1.33× the 10-session average. That is a range breakout, not a drift. Note the measured-move arithmetic: box height 19.71 points projected off the 320.28 ceiling implies ~340 — which coincides with the 07-28 close (339.787). This is arithmetic, not a prediction, but the coincidence is worth stating.

For scale on the larger trend: close on 2025-09-02 was 228.875 versus 325.13 today (**+42.05%**), and 2025-12-31 was 271.122 (**+19.92% year to date**). The stock remains **4.3% below its 2026-07-28 close** and **5.9% below the 07-29 intraday high of 344.273**.

---

### 4. Momentum: fresh, confirmed, and still accelerating

MACD is the cleanest signal on the board:

- MACD line **1.26742**, signal **−0.23811**, histogram **+1.506**.
- The histogram crossed from negative on 2026-08-25 (−0.143) to positive on 2026-08-26 (+0.154) — **a bullish MACD crossover six sessions ago** — and has expanded monotonically every session since: 0.154 → 0.416 (08-27) → 0.894 (08-28) → 0.973 (08-31) → 1.506 (09-01).
- Critically, the MACD line had fallen from **+9.604 on 2026-07-29 to −2.603 on 2026-08-17** before this turn. That is a full momentum reset. The current crossover is therefore a *second-leg* signal coming off a washed-out reading, which historically carries better follow-through than a crossover from elevated levels.

**RSI at 61.16** — up from 54.18 on 08-31 and from a trough of **40.34 on 2026-08-03**. It is not overbought. There are roughly nine RSI points of headroom before the 70 threshold.

But the July episode is instructive and should temper enthusiasm: RSI printed **71.66 (07-17) and 68.90 (07-28)** immediately before the −9.17% three-session break. In this instrument over this sample, sustained RSI readings near 70 have preceded air pockets rather than extensions. Treat 70 as a *de-risking alert level*, not a hold signal.

Note also that the RSI reading of 61.16 is not confirmed by a divergence — price made a higher high today while RSI sits well below its July peak. On the strict definition that is a mild negative divergence against the July high, but since the July high was an impulsive blow-off and today is a base breakout, I weight the MACD acceleration more heavily. Divergence matters more when both highs are of similar character.

---

### 5. Volatility: breakout above the upper band, with ATR contracting underneath

Two opposing forces are at work:

**Bollinger bands (20-period):** middle **311.28**, upper **322.338**, lower **300.221**, width 22.117 points (7.11% of the middle). The close of 325.13 is **2.792 points, or 0.87%, above the upper band.** This is a genuine band breakout, and in a healthy uptrend it is exactly what "walking the band" looks like at the start. It also means short-term mean-reversion risk is elevated — the mechanical pullback target is the 20-SMA at ~311.3.

**ATR at 7.61732 (2.34% of price):** contracting decisively. It peaked at **9.863 on 2026-07-31** (the gap day), ran at 8.5–8.9 through 2026-08-10/12, and has since compressed to 7.09–7.24 (08-27 to 08-31) before ticking up to 7.617 today on the wider breakout range. The pattern is volatility contraction *into* a breakout — the classic setup, and far healthier than a breakout on expanding, chaotic ranges.

Practical translation: a 1× ATR stop from 325.13 is 317.51; 1.5× is 313.70; 2× is 309.90. Any stop closer than ~8 points to entry is inside normal daily noise for this name right now.

---

### 6. Volume: accumulation confirmed, but only modestly

VWMA is **312.494** — price is 4.03% above it, and VWMA has clearly inflected: it bottomed at 307.62 (2026-08-19) and has risen every session since: 308.30 (08-20) → 309.09 (08-25) → 309.99 (08-28) → 310.80 (08-31) → 312.494 (09-01). A rising VWMA with price above it means the volume-weighted participant is profitable and adding. That is a confirming signal, not a leading one.

Breakout-day volume: **53,167,400** versus a 10-session average of approximately **39.86M** — about **1.33×**. Constructive, and the highest volume since 2026-08-19 (50.5M). But I want to be precise about its limits: 1.33× is adequate confirmation, not institutional-scale conviction. For comparison, the 07-31 breakdown traded at 132.5M and the 06-26 session at 261.8M. If this breakout is real, follow-through volume over the next 2–3 sessions should hold above ~45M.

The residual negative on volume: the 07-31 distribution day was never answered by a comparable accumulation day. Today is a start, not an answer.

---

### 7. Level map (all prices from verified 2026-09-01 and prior rows)

**Resistance / supply overhead**
- **327.30** — 2026-09-01 high (immediate, one day old)
- **329.31** — 2026-07-30 low; upper boundary of the unfilled 07-31 gap
- **333.14** — 2026-07-30 close
- **333.45** — 2026-07-17 close
- **339.79** — 2026-07-28 close (swing high close)
- **344.27** — 2026-07-29 intraday high (sample high)

**Support / demand beneath**
- **316.83–316.98** — 2026-08-19 close and 2026-09-01 open; first shelf
- **315.78** — 10 EMA
- **312.76** — 50 SMA (the key structural line)
- **312.49** — VWMA (nearly coincident with the 50 SMA — that confluence is meaningful)
- **311.28** — Bollinger middle / 20-SMA
- **300.57–302.30** — August floor (2026-08-12 low 300.57; 2026-08-03 low 302.299) and near the Bollinger lower band at 300.221

I want to be explicit: nothing in the tool output *validates* that price has previously bounced from these levels. They are levels defined by prior closes, highs, lows, and computed averages. They should be treated as decision points, not proven floors.

---

### 8. Actionable playbook

**Bias: constructive long, but staged — not a full-size chase at 325.**

The setup is a valid base breakout with fresh MACD momentum, above-band strength, contracting ATR, and rising VWMA. The two things keeping this from a high-conviction "buy everything" call are (a) the close is 0.87% above the upper Bollinger band and 15% above the 200 SMA, both of which raise short-term reversion odds, and (b) the 329.3–339.8 gap zone is unabsorbed supply directly overhead.

**Entry approach — three tranches:**
1. **Starter now (⅓):** at market near 325.13. Accept you are buying an extended band tag; the trend and momentum justify a toehold.
2. **Add on a hold (⅓):** if price closes a session above **329.31** (gap top) without giving back the breakout, confirming the August range was truly vacated.
3. **Add on a retest (⅓):** if price pulls back into **312.5–316.8** (50 SMA / VWMA / first shelf confluence) and holds on contracting volume, that is the higher-quality entry and it also doubles as the trend-failure test.

**Risk management:**
- **Primary stop: 309.90** — 2× ATR below today's close, and below the Bollinger middle (311.28) and 50 SMA (312.76). A close under 311.28 breaks the structural read outright.
- **Tighter alternative for the starter tranche: 313.70** (1.5× ATR) if position sizing demands a smaller nominal risk; expect a higher stop-out frequency.
- **Position size:** with ATR at 2.34% of price, a 2× ATR stop is a ~4.7% adverse move. Size so that 4.7% of the position equals your per-trade risk budget.
- **Do not** use a stop inside 317.5 — that is inside one ATR of noise.

**Targets / management:**
- **T1: 329.31** — gap top; trim a portion, expect a decision point.
- **T2: 333.14–333.45** — prior 07-30 and 07-17 closes.
- **T3: 339.79** — July swing-high close, and the measured-move objective (~340) derived from the 19.71-point August box.
- **T4 (stretch): 344.27** — sample high.
- **Trail:** once price closes above 333, raise the stop to the 10 EMA (currently 315.78 and rising ~1.5–2 points/session). That converts the trade to a trend-follow with defined downside.

**What would invalidate the thesis:**
1. A close back below **311.28** (Bollinger middle) — the breakout is then a failed band tag inside a range.
2. A close below **300.57** — August floor broken; the July high becomes a completed double-top and the trend structure is damaged.
3. MACD histogram rolling back over (a print below ~0.97, i.e. the 08-31 value) within two to three sessions — that would mark the crossover as a head-fake.
4. A high-volume down day (>60M) that erases the 09-01 gain — direct evidence the breakout was distribution into strength.
5. 50 SMA turning back down while price is beneath it — the medium-term trend layer failing.

**Event risk to respect:** the 2026-07-31 session behaved like a scheduled-catalyst repricing (gap open, 132.5M volume). The next comparable scheduled event for this name will carry the same gap risk in both directions; reduce size into it rather than carrying full exposure through.

---

### 9. Why these eight indicators

- **close_10_ema / close_50_sma / close_200_sma** — three separated time horizons establish *regime* before anything else. Using only fast averages would have flagged the August drift as bearish; the 200 SMA confirms the primary trend never broke. All three are non-redundant because they answer different questions (entry timing / trend support / strategic bias).
- **macd + macdh** — the line gives the crossover, the histogram gives its *rate of change*. The histogram's five-session monotonic expansion is what distinguishes this from a stalled crossover, and it isn't visible from the MACD line alone. I used the signal line only from the verified snapshot to avoid a third, partially redundant fetch.
- **rsi** — the independent check on whether the breakout is overbought. It disagrees with the Bollinger read (61 is not stretched), and that disagreement is itself informative: momentum has room even though price is band-tagged.
- **atr** — converts every price level into a *risk* quantity. Without it, "stop at 311" is arbitrary; with ATR at 7.62, we know a 14-point stop is 1.8× ATR and appropriately sized.
- **vwma** — the only volume-aware price measure here. It confirms the breakout with participation rather than price alone, and its nine-session rise from 307.62 is a genuine accumulation tell the SMAs cannot show.

I deliberately excluded Bollinger upper/lower as separate fetches (the verified snapshot supplies all three band values, so a separate call would be pure redundancy) and excluded any stochastic/RSI pairing as duplicative momentum measurement. `macds` was obtained from the snapshot rather than a separate call, which I verified arithmetically.

---

### 10. Summary table

| Dimension | Verified reading (2026-09-01) | Interpretation | Actionable implication |
|---|---|---|---|
| Close / OHLCV | 316.98 / 327.30 / 314.73 / **325.13**, vol 53.17M | Strong close, upper half of range | Breakout session, not a fade |
| Trend stack | 10 EMA 315.777 < Close; 50 SMA 312.761; 200 SMA 282.626 | Bullish ordered stack; price +15.04% over 200 SMA | Primary trend intact; extended vs. long-term mean |
| 50 vs 200 SMA | Spread +10.66% | Mature uptrend | Strategic long bias, not early-cycle |
| MACD | Line 1.26742, signal −0.23811, hist +1.506 | Bullish crossover 2026-08-26; hist expanding 5 sessions | Momentum confirming — the strongest signal on the board |
| RSI | 61.16 (from 40.34 on 2026-08-03) | Rising, not overbought | ~9 points headroom to 70; July showed 68–72 precedes risk |
| Bollinger | Mid 311.28 / UB 322.338 / LB 300.221 | Close 0.87% **above** upper band | Strength + short-term reversion risk to ~311.3 |
| ATR | 7.61732 (2.34% of price) | Contracted from 9.863 (2026-07-31) | 1×ATR stop 317.51; 2×ATR stop 309.90 |
| VWMA | 312.494, rising from 307.62 (2026-08-19) | Price 4.03% above; accumulation confirmed | Volume-weighted holder in profit; supports the breakout |
| Breakout volume | 53.17M vs ~39.86M 10-day avg (1.33×) | Adequate, not institutional-scale | Want >45M follow-through in next 2–3 sessions |
| Structural context | 07-31 gap: 304.547 open vs 333.143 prior close; −9.17% in 3 sessions | Unfilled overhead gap 304.55–329.31 | 329.31 is the pivotal level |
| August base | Box 300.57–320.28 (~6.5% wide) | Closed above the whole box today | Range breakout; measured move ≈ 340 |
| Position sizing | 2× ATR = 4.7% of price | — | Size 4.7% of position = risk budget |
| Stance | **Constructive long, staged** | Trend + momentum bullish; extension + overhead supply constrain | ⅓ now, ⅓ over 329.31, ⅓ on 312.5–316.8 retest; stop 309.90 |

---

**Bottom line for AAPL:** the verified data supports a *constructive* posture, not a euphoric one. The 2026-09-01 close of 325.13 cleared a six-week base on 1.33× volume, with a six-session-old MACD crossover whose histogram is still widening, RSI at a non-extreme 61.16, VWMA inflecting upward, and ATR contracting into the move. Against that, price closed above the upper Bollinger band, sits 15% above its 200 SMA, and is pressing into an unfilled 304.55–329.31 gap left by a violent 2026-07-31 repricing that was never answered by comparable accumulation. The correct expression is a staged long with a hard structural stop at 309.90, a decisive level at 329.31, and staged objectives at 333.14, 339.79, and 344.27 — while treating 70 on RSI and any sub-311.28 close as reasons to reduce rather than add.

## investment_plan

**Recommendation**: Underweight

**Rationale**: The bear case wins on risk-adjusted entry and confirmation, not because the bull’s technical work is invalid. I accept the bull’s verified trend/momentum facts for AAPL: price is above the 10 EMA, 50 SMA, and 200 SMA; MACD has crossed up from a washed-out reading; the histogram is expanding; and VWMA is rising. That is enough to reject a Sell or outright short.

But at AAPL’s $325.13 close, the bear made the stronger actionable argument:
- The breakout above the 320.28 box top is only ~1.5%, and AAPL is still below the 329.31 gap-top resistance.
- Breakout volume of 53.17M vs. ~39.86M average is only 1.33×, and it is far below the 07-31 distribution day of 132.49M. That is not decisive confirmation.
- The risk/reward at the current price is poor: stop 309.90 risks 15.23 points, or 4.68%, while T3 at 339.79 offers 14.66 points, or 4.51%. To T1/T2 the math is worse. The bull’s own staged plan concedes the first tranche is “mediocre” and that the best entry requires a pullback.
- AAPL is 15.04% above its 200 SMA and closed ~0.87% above the upper Bollinger band. That is an extended, mature-trend condition, not a low-risk new-money entry.
- The packet contains no sentiment, news, or fundamentals report. I have not invented them. For a mega-cap investment call at an extended level, the burden of proof sits with the buyer, and the technical packet alone does not clear that bar.

So the bull’s trend evidence justifies not abandoning AAPL entirely, but the bear’s confirmation and risk/reward critique justifies trimming exposure and refusing to add at $325.13.

**Strategic Actions**:
- Treat “standard AAPL allocation” as 1.0× the normal target weight. If currently at full target, trim 25–33% of the AAPL position into the 325–329.31 area, moving toward ~0.67–0.75× standard allocation. If at benchmark/neutral, move to ~0.5–0.75× standard.
- Do not initiate a new full-size AAPL position at 325.13. No chasing between 325 and 329.31 without volume confirmation.
- For remaining AAPL exposure, use 311.28 as the first warning level and 309.90 as the hard invalidation/stop area on a closing basis. A close below 300.57 should trigger exiting the residual core. Because gap risk is real, size the position so a slip through 309.90 is tolerable rather than pretending the stop is gap-proof.
- Rebuild only on one of two setups:
  1. **Confirmation:** a daily close above 329.31 on >60M shares, followed by a 2–3 session hold. Then rebuild in 1/3 tranches toward 0.75–1.0× standard allocation, with targets 333.14–333.45, 339.79, and 344.27.
  2. **Pullback:** a retest of 312.5–316.8 that holds on contracting volume. That can justify a tactical add of up to 1/3 standard allocation, with 309.90 as the stop and total AAPL exposure kept at or below standard until the breakout confirms.
- If AAPL rallies into 329.31–339.79 without the required volume confirmation, use that strength to trim further toward 0.5× standard allocation. If it closes above 344.27 on strong volume, reassess the Underweight stance, but not before confirmation.
- Do not short AAPL outright: the primary trend is still intact, and this is an Underweight/trim call, not a Sell call.

## trader_investment_plan

**Action**: Sell

**Reasoning**: The plan is an Underweight call, and the price structure supports acting on it rather than waiting: AAPL closed 325.13, only ~1.3 points under the 329.31 gap top, 0.87% above the upper Bollinger band at 322.34, and 15.04% above its 200 SMA at 282.63 — an extended, mature-trend entry point. Risk/reward is inverted at this price: the plan's hard stop at 309.90 risks 15.23 points (4.7%) while the T3 objective at 339.79 offers only 14.66 points, and breakout volume of 53.17M (1.33× the ~39.86M average) is far short of the 132.49M distribution day on 2026-07-31 that created the unfilled 304.55–329.31 gap. Because the primary trend is intact (price above the 10 EMA 315.78, 50 SMA 312.76, 200 SMA 282.63, with MACD histogram expanding and VWMA rising to 312.49), this is a trim/underweight, not an outright short: sell into strength, do not chase between 325 and 329.31, and rebuild only on a close above 329.31 on >60M shares or a held retest of 312.5–316.8. Note explicitly: the packet contains no sentiment, news, or fundamentals data, so this decision rests solely on the technical structure above.

**Entry Price**: 325.13

**Stop Loss**: 340.0

**Position Sizing**: Trim 25–33% of an existing AAPL position into the 325.13–329.31 zone, taking exposure to ~0.67–0.75× standard allocation (or ~0.5–0.75× if currently at benchmark/neutral); no new full-size position at 325.13. Hard invalidation of the underweight stance is a decisive move above 339.79, so size the residual core and the trim so a squeeze to ~340 (2× ATR of 7.62 above today's close, just over the July swing-high close) is tolerable; if instead AAPL closes below 311.28, cut further, and exit the residual core on a close below 300.57.

FINAL TRANSACTION PROPOSAL: **SELL**

## final_trade_decision

**Rating**: Underweight

**Executive Summary**: Trim AAPL 30–33% of the existing position into the 325.13–329.31 zone and hold a residual core of roughly 0.60–0.70x standard allocation (lower, 0.50–0.60x, if the caller is concentrated; if already underweight, just maintain or trim 25% and do not force more). Do not initiate or add at 325.13 and do not chase size between 325 and 329.31. Place the residual core's hard de-risk at a close below 311.28, first alert at 316.8–315.8, and stress-test the position against a repeat of the 2026-07-31 gap to 300.57 — if that stress loss exceeds the caller's name-level risk budget, trim more than 33%. Rebuild only on (1) a close above 329.31 on >60M shares followed by a held retest/follow-through, or (2) a held retest of 312.5–316.8 on contracting volume with a higher low; re-add in thirds toward 0.75–1.0x with targets 333.14–333.45, 339.79, 344.27.

**Investment Thesis**: All three analysts converged on the same direction, and the debate was properly about how much to sell, not whether to sell — which makes Underweight, not Sell, the correct rating. The bear/risk-control case wins on position sizing, but the bull's trend facts are unrefuted and take an outright Sell (or short) off the table.

Why the reduction case wins: (1) Payoff is inverted at the current price — the hard stop at 309.90 risks 15.23 points (4.68%) while T3 at 339.79 pays only 14.66 points (4.51%), and the math is worse to T1/T2. (2) The extension is measurable: AAPL at 325.13 sits 15.04% above its 200 SMA (282.63) and ~0.87% above the upper Bollinger band (322.34). (3) The 2026-07-31 gap from 304.55 to 329.31 was created on 132.49M shares of distribution and remains unanswered; today's 53.17M breakout is only 1.33x the ~39.86M average — adequate, not conviction. (4) There is demonstrated air-pocket behavior: RSI 71.66 on 07-17 and 68.90 on 07-28 preceded a 9.17% drop from 333.14 to 308.64 within three sessions. (5) The packet contains no sentiment, news, or fundamentals data, so event risk around the next catalyst is unknown and un-hedged by any narrative.

Why not Sell: the trend stack is intact and ordered — price above the 10 EMA (315.78), 50 SMA (312.76), and 200 SMA (282.63); MACD has crossed up from a washed-out reading with the histogram expanding from 0.154 to 1.506; VWMA is rising to 312.49; RSI at 61.16 is not overbought; and AAPL closed above the entire 300.57–320.28 August box. Abandoning or shorting a constructively-stacked primary trend is not supported.

Where I sided between the analysts: the conservative analyst is right that 309.90 is not gap protection — a 2x ATR stop would not have saved anyone from the 28.6-point, ~3.75x ATR gap on 07-31 — and that the 312.5–316.8 confluence is a decision zone, not a validated floor. That justifies the harder constraints: first alert at 316.8–315.8, hard de-risk on a close below 311.28 rather than waiting for 300.57, and explicit stress-test-to-300.57 sizing. But the conservative call to cut below 0.5–0.65 by default overcorrects: with a fresh MACD crossover, expanding histogram, and a close above the whole August box, defaulting to the worst-case size risks converting a tactical underweight into a trend exit and re-entering higher. The aggressive analyst's 0.67–0.75 core is defensible at benchmark but too generous for a concentrated or unknown book, and his single-close-on-60M rebuild trigger is too permissive given the unanswered 132.49M supply shelf. The neutral framing — staged trim now, stricter re-add rules, gap-stress-tested residual size — is the strongest synthesis, and I execute it at the higher end of the trim range given the inverted payoff.

What would change this view: a daily close above 329.31 on >60M shares held for 2–3 sessions, or a held retest of 312.5–316.8 on contracting volume with a higher low, moves this toward Hold/Overweight and justifies rebuilding in thirds. A decisive close above 344.27 on strong volume would retire the Underweight stance. Conversely, a close below 311.28 triggers further reduction, and a close below 300.57 is structural damage requiring exit of the residual core. Identification of a scheduled catalyst before confirmation argues for hedging or trimming the residual rather than carrying the binary event at size.

**Price Target**: 339.79

**Time Horizon**: 1-3 months (trim now; reassess on confirmation above 329.31 or a held retest of 312.5-316.8)

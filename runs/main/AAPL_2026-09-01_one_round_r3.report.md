## instrument_context

The instrument to analyze is `AAPL`. The tools serve this instrument; refer to it by this exact ticker in every report and recommendation, preserving any exchange suffix (e.g. `.TO`, `.L`, `.HK`, `.T`, `-USD`). Resolved identity: Company: Apple Inc. (its current name, given only to identify it; on 2026-09-01 it may have been named differently). Do not substitute a different company or ticker unless a tool result explicitly disproves this resolved identity.

## market_report

# AAPL — Technical Analysis Report (analysis date 2026-09-01)

## 1. Data provenance and discrepancies

- **Price data:** 128 daily rows from 2026-03-01 → 2026-09-01 (`get_stock_data`).
- **Verified snapshot (`get_verified_market_snapshot`, 2026-09-01):** latest row Open 316.98 / High 327.30 / Low 314.73 / **Close 325.13** / Volume **53,167,400**.
- **Reconciliation:** the snapshot's 2026-09-01 OHLCV row matches the CSV row **exactly, field for field** (316.98 / 327.30 / 314.73 / 325.13 / 53,167,400). **No discrepancy to flag.** All exact price and indicator values below come from the verified snapshot.
- **Limitations — data I could not retrieve:**
  - `vwma` (volume-weighted moving average) — **not available**. Volume commentary below is derived from the raw CSV volume column, not from a verified volume indicator.
  - **Historical indicator series** — only the *latest-row* values were verified. I therefore **cannot** assert measured divergences (e.g., RSI at the July peak vs. today) or backtested indicator performance. Any such claim would be invented, so it is omitted.
  - No intraday, options, news, or fundamental data was available. Two large one-day gaps in the window imply event/headline risk I cannot characterize.

---

## 2. Regime summary

AAPL is in a **primary uptrend that suffered a violent mid-summer air-pocket and is now re-asserting itself**. The structure is: persistent March–July advance → one-day distribution shock on 2026-07-31 → five weeks of basing between roughly 300 and 320 → a fresh breakout attempt on 2026-09-01 that closed at 325.13, *above* the upper Bollinger Band.

The long-term trend is intact; the medium-term trend has turned back up from a corrective phase; the short-term state is **extended but unconfirmed-negative**. Momentum is early-cycle bullish (MACD just crossed its signal and the zero line) while price is stretched versus its short-term mean — a combination that favors buy-the-dip or breakout-with-tight-risk over chasing.

---

## 3. Trend structure (moving averages)

| Reading | Value | Price vs. level | Interpretation |
|---|---:|---:|---|
| close_200_sma | 282.626 | **+15.04%** | Long-term uptrend decisively intact |
| close_50_sma | 312.761 | **+3.95%** | Medium-term trend has flipped back in the bulls' favor |
| close_10_ema | 315.777 | **+2.96%** | Short-term momentum positive but price is stretched |

- **Golden-cross configuration is live:** 50 SMA (312.761) sits **10.66% above** the 200 SMA (282.626). This is a strategic bullish backdrop, not a timing signal — the 200 SMA lags badly and is 42.50 points below spot.
- **The 50 SMA is the key pivot of the whole thesis.** Price spent most of the 2026-08-10 → 2026-08-27 stretch *below* or hugging it, and only in the final three sessions (2026-08-28 close 319.70, 2026-08-31 close 316.85, 2026-09-01 close 325.13) has it cleared meaningfully. A daily close back under 312.76 would neutralise the current breakout.
- **The 10 EMA (315.777) is the first line of defense.** At 325.13 the close is 9.35 points above it. In a healthy trending tape price rides this average; a close below it would be the first warning that this week's push is a failed breakout rather than a trend resumption.

### Trend timeline (all figures computed from verified closes/OHLC in the retrieved data)

- **Advance leg:** 2026-03-30 close **246.191** → 2026-07-29 intraday high **344.273** = **+39.9%** (period low 245.073 on 2026-03-30).
- **Distribution shock:** 2026-07-30 close 333.143 → 2026-07-31 open **304.547**, close **308.644** on **132.5M** shares. That open-to-prior-close gap is **−8.58%** in one session.
- **Correction:** 2026-07-29 high 344.273 → 2026-08-12 low **300.570** = **−12.69%**.
- **Base:** closes of 304.91 (08-11), 302.25 (08-12), 305.26 (08-13), 305.93 (08-14), 305.59 (08-17) establish a repeat-tested shelf at **~302–306**.
- **Recovery:** 2026-08-12 close 302.25 → 2026-09-01 close 325.13 = **+7.57%** (from the 08-12 low of 300.57 it is **+8.17%**).
- **Still below the July peak:** 325.13 is **−4.31%** under the 2026-07-28 close of 339.787 and **−5.56%** under the 2026-07-29 intraday high of 344.273.

**Crucially, the June low is a higher low relative to today's structure.** On 2026-06-25 AAPL closed 274.913 (down **−6.12%** from the 2026-06-24 close of 292.827) on 107.0M shares; the next session, 2026-06-26, traded as low as 273.974 on **261.8M** shares and closed 283.535 (**+3.14%**). From that 274.913 close, price rallied to the 344.273 high by 2026-07-29 (**+25.2%**). The August low at 300.57 is therefore a **higher low within a rising sequence**, which is the textbook signature of trend continuation rather than a top.

---

## 4. Momentum (MACD family, RSI)

- **macd = 1.26742**, **macds = −0.23811**, **macdh = 1.50553**. The MACD line has **crossed above its signal line** and has **just crossed above zero**, while the signal line is still negative. That is the *early* phase of a bullish momentum regime — constructive, but it is a fresh turn, not an extended one. The positive histogram (MACD minus signal = 1.50553, internally consistent with the two published values) means momentum is currently **accelerating in the bulls' favor**.
- **Context caveat:** the absolute MACD reading of 1.27 against a 325 share price is small — this is a *nascent* momentum recovery off a deeply negative July/August reading, not a thrust of the kind the July advance would have produced. It argues for confirmation before aggressive size.
- **rsi = 61.1599.** Firmly above 50, comfortably below 70 — a "trend-healthy" reading with **no overbought constraint on further upside**. It is also far from oversold, so it offers **no mean-reversion edge** in either direction. In strong trends RSI can stay elevated for weeks; treat 61 as permission to be long, not as a signal to add aggressively.

---

## 5. Volatility and band positioning (Bollinger, ATR)

- **boll (middle, 20 SMA) = 311.28**; **boll_ub = 322.338**; **boll_lb = 300.221**.
- **The 2026-09-01 close of 325.13 is 2.79 points (+0.87%) ABOVE the upper band.** Band width is 22.117 points, or **7.11% of the middle band** — a moderately compressed range, meaning a band contact carries more information than it would in a wide, whipsawing band.
- Interpretation — **breakout, with a mean-reversion tax.** Riding/closing above the upper band in an uptrend is a legitimate continuation signal, especially with volume expansion. But statistically it is a two-standard-deviation event: the *first* target on any failure is the 20-day mean at **311.28**, which is **−4.26%** away. This asymmetry is the single most important tactical fact in the report.
- **The lower band at 300.221** is now effectively the boundary of the August base — it sits within 0.35 points of the 2026-08-12 low of 300.570, a useful confluence for the "trend has broken" scenario.
- **atr = 7.61732 = 2.34% of price.** This is the sizing and stop anchor. Note the asymmetry risk: the 2026-07-31 gap alone (−8.58%) was **~3.7× the current ATR** in a single open. **Standing stops do not protect against that class of event on this name.** Position size must assume gap risk, not merely ATR risk.

---

## 6. Volume (raw CSV — `vwma` unavailable)

- **2026-09-01 volume = 53,167,400.** That is the **highest daily volume since 2026-08-18 (53,424,500)** and roughly **27% above** the ~41.9M average of the 21 sessions from 2026-08-04 to 2026-09-01 (my own calculation from the retrieved volume column). Up-day volume expansion supporting a band breakout is a genuinely constructive tell.
- **The August base was built on drying volume:** the window's low was **25,869,800 on 2026-08-25**, right before the 2026-08-26/27/28 sequence of 34.0M / 32.4M / 38.6M and then 41.2M (08-31) and 53.2M (09-01). Rising price on rising volume from a low-volume base is the ideal accumulation profile.
- **But the tape has a history of violent volume events:** 261,775,500 on 2026-06-26 and 132,489,100 on 2026-07-31. These are 5–6× normal. Any trend-following framework on AAPL must be sized for headline-driven single-session repricing.

---

## 7. Key levels map

| Level | Price | Source | Role |
|---|---:|---|---|
| Period high | 344.273 | 2026-07-29 high | Ultimate resistance / breakout objective |
| Record close (period) | 339.787 | 2026-07-28 close | Resistance |
| Gap upper edge | 333.143 | 2026-07-30 close | **Primary upside target — top of the 07-31 gap** |
| Intraday trigger | 327.30 | 2026-09-01 high | Breakout confirmation trigger |
| **Spot** | **325.13** | 2026-09-01 close | — |
| Bollinger upper | 322.338 | Verified | Now reclaimed; becomes first support |
| 10 EMA | 315.777 | Verified | Short-term trend line |
| **50 SMA** | **312.761** | Verified | **Thesis pivot** |
| Bollinger middle | 311.28 | Verified | Mean-reversion magnet |
| Gap lower edge | 310.422 | 2026-07-31 high | Structural support |
| 07-31 close | 308.644 | 2026-07-31 | Support |
| Base shelf | 300.570 – 306.00 | 08-12 low / 08-11–08-17 closes | Major support |
| Bollinger lower | 300.221 | Verified | Base boundary |
| 200 SMA | 282.626 | Verified | Strategic trend floor |

**Note on the gap:** the 2026-07-31 break left an unfilled zone between the 2026-07-31 high of 310.422 and the 2026-07-30 close of 333.143. Price has now retraced **most** of it — the remaining unfilled portion is roughly **327.30 (today's high) to 333.143**. The most natural path for a continued advance is a grind into 333.14, which is also the level at which sellers were last in control.

---

## 8. Actionable plan

**Bias: moderately bullish, but tactically patient.** Trend, MACD turn, RSI room and volume all point up; band extension and the unfilled gap cap the reward-to-risk on a chase at 325.13.

**Scenario A — Breakout continuation (primary).**
- Trigger: a daily close **above 327.30** (2026-09-01 high), ideally on volume ≥ 53M.
- Initial stop: **1.5 × ATR ≈ 11.4 points** below entry, i.e. ~315.9 (coincides with the 10 EMA at 315.777) — a tight, meaningful stop.
- Targets: **333.143** (gap fill, +~2%) → **339.787** (July record close) → **344.273**.
- Avoid entering mid-range between 325 and 327; you would be paying up while sitting directly on the upper band.

**Scenario B — Pullback accumulation (preferred risk/reward).**
- Entry zone: **315.78 (10 EMA) down to 312.76 (50 SMA)**.
- Stop: **~306.0** (below the August shelf) — a 1.1× ATR cushion under the 50 SMA that also clears the 2026-08-17 close of 305.59.
- This offers roughly 19 points of upside to 333.14 against ~7–10 points of downside from the zone.

**Scenario C — Invalidation.**
- A daily close **below 312.76 (50 SMA)** converts the 09-01 breakout into a bull trap and shifts the tactical bias to neutral.
- A close **below 300.221/300.570** (lower band + 08-12 low confluence) breaks the August higher-low sequence and puts the 200 SMA at 282.626 in play.

**Position sizing (ATR-based).** With ATR = 7.617 (2.34%), a 2×ATR stop is **15.23 points**. On a $100,000 account risking 1% ($1,000), that permits **~65 shares**. If you instead use the 1.5×ATR breakout stop (11.43 points), size is **~87 shares**. **Discount size by 25–40% versus a pure-ATR calculation** because of demonstrated gap risk: 2026-07-31 gapped −8.58% at the open, and 2026-06-25 closed −6.12% with an intraday low of 273.514.

**What would make me wrong on the bullish case:** MACD histogram rolling back to zero while price holds under 322.34; a close back below the 10 EMA *and* the 50 SMA in the same week; or a heavy-volume down day (>100M) swallowing 2026-09-01's range — that pattern would echo the 2026-07-31 distribution day.

---

## 9. Indicator selection rationale

| # | Indicator | Value (2026-09-01) | Why it is the right tool here | Redundancy avoided |
|---|---|---:|---|---|
| 1 | close_10_ema | 315.777 | Fast trend/entry anchor for a fresh breakout; defines the first invalidation of the 09-01 thrust | Distinct timescale from 50/200 |
| 2 | close_50_sma | 312.761 | The actual battleground of the Aug–Sep transition; dynamic support for the pullback plan | Not duplicated by 10 EMA (itself a distinct horizon) |
| 3 | close_200_sma | 282.626 | Confirms the strategic uptrend and verifies the 50 > 200 golden-cross backdrop | Long-horizon only; no overlap with 10 EMA |
| 4 | macd | 1.26742 | Identifies the regime shift — zero-line + signal-line cross just completed | Complements MAs (momentum, not level) |
| 5 | macdh | 1.50553 | Measures whether that shift is *accelerating* — currently yes | macds omitted: histogram already encodes the signal relationship |
| 6 | rsi | 61.1599 | Confirms trend health without an overbought constraint; guardrail against chasing a >70 blow-off | No stochrsi/other oscillators (redundant) |
| 7 | boll_ub | 322.338 | Directly quantifies today's two-sigma extension — the report's core tactical risk | Paired conceptually with boll (311.28) / boll_lb (300.221), not a duplicate of them |
| 8 | atr | 7.61732 | Required to set stops (1.5×/2× = 11.43/15.23) and size positions in a gap-prone name | Volatility-based; orthogonal to all price-level tools |

*Supplemental readings used but not in the core eight:* **boll (311.28)** as the mean-reversion magnet and **boll_lb (300.221)** as the base boundary — cited as context, not as separate signals; **macds (−0.238)** referenced only to describe the crossover phase.

---

## 10. Bottom line

AAPL closed at **325.13 on 2026-09-01 (+2.61% from 316.85 on 2026-08-31)** on **53.17M shares**, above a **rising 50 SMA (312.761)**, **firmly above the 200 SMA (282.626, +15.04%)**, with **RSI 61.16**, a **fresh MACD bullish cross (1.267 vs. signal −0.238, histogram +1.506)**, and above the **upper Bollinger Band (322.338)**. The trend is up and the momentum turn is genuine but early. The single tactical objection is statistical extension: the **20-day mean is at 311.28, 4.26% below spot**. Conclusion: **buy strength only above 327.30 with a 10-EMA stop, or buy the 315.78–312.76 pullback with a ~306 stop; hard invalidation at a close below 312.76, trend break below 300.57.** Size down for gap risk — the −8.58% open on 2026-07-31 proves ATR-based stops alone are insufficient on this instrument.

## investment_plan

**Recommendation**: Hold

**Rationale**: Let me be straight with you — this one is genuinely close, and the reason it lands on Hold is not timidity, it's that the two sides largely agree on the facts and disagree only on what time horizon matters.

Where the bull won: the strategic trend is unambiguously intact and the bear conceded it. AAPL at 325.13 sits above the 50 SMA (312.761) and far above the 200 SMA (282.626), with the 50 SMA 10.66% above the 200 SMA and price 15.04% above the 200. The August low at 300.57 is a higher low versus the June low around 274.9, and the move off that low is +8.17% on rising volume (41.2M on 08-31, 53.17M on 09-01, roughly 27% above the ~41.9M 21-session average). MACD at 1.267 versus signal −0.238 with a +1.506 histogram is a genuine fresh cross above zero, and RSI at 61.16 sits in healthy trend territory with room below 70. The bear's "higher low isn't a completed uptrend" and "golden cross is lagging" points are technically true but they describe why the trend is early, not why it's broken. The bear also never produced any evidence of distribution, deterioration, or a failed structure — it argued only that the stock is extended and that overhead supply exists. Extension is a timing issue, not a thesis.

Where the bear won, and this is what decides it: the risk/reward at the current price is objectively poor, and the bull's own action plan concedes it. From 325.13 the first upside target (333.143) is +2.46% away while the 20-day mean (311.28) is −4.26% and the 50 SMA (312.761) is −3.80%. The bear's arithmetic on the bull's breakout plan holds up: entry above 327.30 with a stop near 315.9 is roughly 11.4 points of risk against ~5.8 points to the first target, under 0.5:1, and only about 1.1:1 even to the July close at 339.787. That is a chase with a tight leash. And the bull's own "preferred" entry at 315.78–312.76 is 3–4% below spot — which is an admission that today's price isn't where the edge lives. The unfilled gap supply at roughly 327.30–333.143, created on a 132.5M-share, −8.58% gap session, has not been tested, and 53.17M shares is only about 40% of that distribution print, so "absorption" is an inference, not a demonstrated fact. The bear's point that ATR-based stops are unreliable given a demonstrated 3.7×-ATR gap is also correct and reduces, rather than eliminates, the risk.

So: the bull has the better trend argument, the bear has the better entry-price argument, and there is no fundamentals, sentiment, or news data in this run to break the tie — the bull expressly declined to invent it, and the bear correctly noted its absence cuts against underwriting a 325 price. Neither side produced evidence the other's structure has failed. With a constructive primary trend but a first supply zone directly overhead and sub-1:1 reward-to-risk on the front leg, the honest call is to maintain the position rather than add at resistance or sell into an intact uptrend. I'm not manufacturing a direction here; I'd flip to Overweight/Buy on a decisive close above 333.143 on 100M+ volume, and to Underweight/Sell on a close below 312.761.

**Strategic Actions**: Against a standard full allocation for AAPL, hold the existing position at roughly current size — do not add at 325.13 and do not trim into an intact primary trend. Concretely:

1) CORE HOLD (approx. 100% of the standard allocation kept in place): no new buying at market while AAPL is pinned between the 20-day mean at 311.28 and the unfilled gap supply at 327.30–333.143. No stop is triggered at current levels.

2) ADD TRANCHE A — BREAKOUT CONFIRMATION (deploy up to +25% of a standard allocation, i.e. take the position to ~1.25x standard): only on a daily close above 333.143 — not 327.30, since 327.30–333.143 is the actual supply zone — with volume at 100M+ shares. That is the level both sides agreed would break the bear case. Initial stop near 315.9 (10 EMA); targets 339.787 then 344.273. Size this tranche at 60–75% of a normal ATR-based add given the demonstrated 3.7×-ATR gap risk on 2026-07-31.

3) ADD TRANCHE B — PULLBACK ENTRY (deploy up to +25% of a standard allocation, same 1.25x cap): buy the 315.78–312.76 zone (10 EMA to 50 SMA) if reached, with a hard stop just below 306.0 under the August shelf. This is the bull's better-risk entry and the more likely one to be filled. If both Tranche A and Tranche B triggers present themselves, use only one — do not stack to 1.5x.

4) DE-RISK TRIGGERS: on a daily close below 312.761, cancel all standing add orders and cut the core back to ~50% of a standard allocation (Underweight). On a daily close below 300.57, exit to zero or a token position — that breaks the higher-low sequence and puts the 200 SMA at 282.626 in play as the next reference.

5) RISK NOTE: no fundamentals, sentiment, or news report exists in this run. Position sizing above is technical-only and should be reduced or reconsidered if fundamental data arrives that contradicts the uptrend. Do not use tight intraday stops on AAPL — size down instead, given the gap risk.

## trader_investment_plan

- **Action**: Hold

- **Reasoning**: The plan's Hold is warranted, but it should be read as "hold what you own, do not commit new capital at 325.13" — not as indifference. The trend evidence is genuinely constructive: price 325.13 sits +3.95% above the 50 SMA (312.761) and +15.04% above the 200 SMA (282.626) with the 50 > 200 spread at 10.66%; MACD has just crossed both its signal (−0.238) and zero with a +1.506 histogram; RSI 61.16 is trend-healthy with no overbought cap; and 53.17M shares is ~27% above the 21-session average on an up day. Nothing in the structure has failed — no distribution day, no lost higher low (300.57 > June 274.9). What blocks a Buy is pure price location: spot closed 0.87% *above* the upper Bollinger Band (322.338), the 20-day mean sits at 311.28 (−4.26%) and the 50 SMA at 312.761 (−3.80%), while the first objective — the 333.143 gap-fill — is only +2.46% away. That is roughly 5.8 points of reward against 11.4 points of stop risk (<0.5:1) on the report's own breakout trigger above 327.30, and the unfilled supply band 327.30–333.143 was created on a 132.5M-share, −8.58% gap session that 53.17M shares has not demonstrably absorbed. The better-risk entry the report itself prefers (10 EMA 315.78 down to 50 SMA 312.76) is 3–4% below spot — an admission that today's price is not where the edge is. Against a demonstrated 3.7×-ATR single-session gap risk, I will not pay up for sub-1:1. I would upgrade to Buy on a daily close above 333.143 on 100M+ shares, or on a tag of the 315.78–312.76 zone with the trend structure intact; I would downgrade to Sell on a daily close below 312.761. Note explicitly: `vwma` was unavailable and no fundamental, sentiment, or news data exists in this run — this is a technical-only judgment, and sizing should be revisited if fundamental data contradicts the uptrend.

- **Entry Price**: No entry at market. Conditional adds only: pullback entry **315.78** (10 EMA); alternative breakout entry **333.14**, taken only after a daily close above that level on ≥100M shares (do not enter the 327.30–333.14 supply band mid-range).

- **Stop Loss**: **306.00** on the pullback entry (just below the August base shelf, the report's structural stop); **315.90** on the breakout entry (10 EMA).

- **Position Sizing**: Keep the existing core at ~100% of standard allocation; adds are capped so total never exceeds ~1.25× standard. Account size and current holdings were not provided, so size by risk: risk ~1% of account per add. On a $100,000 account ($1,000 risk), the pullback tranche (9.78 pts to stop at 306.00) permits ~102 shares raw; apply a 25–40% gap-risk haircut for the 2026-07-31 −8.58% open and 2026-06-25 −6.12% close → **~65 shares**. The breakout tranche (17.24 pts from 333.14 to 315.90) permits ~58 shares raw → **~40 shares** after the same haircut. Use only one tranche, never stack both. On a daily close below 312.761, cancel all add orders and cut the core to ~50% of standard; on a close below 300.57, exit to zero or a token position, with the 200 SMA at 282.626 as the next reference. Do not use tight intraday stops on AAPL — reduce size instead.

## final_trade_decision

**Rating**: Hold

**Executive Summary**: Hold AAPL at standard allocation size and commit no new capital at 325.13 — the primary uptrend is intact but price is pinned directly under the 327.30–333.143 supply band with sub-1:1 reward-to-risk on the front leg. Keep the core (~100% of a standard allocation) in place, and pre-commit only conditional adds: a pullback tag of 315.78–312.76 with the 50 SMA at 312.761 holding (hard stop 306.00), or a daily close above 333.143 on 100M+ shares (stop 315.90). Size those adds small enough to survive an 8.58%-style gap — roughly 25–35 shares per $100,000 of account, one tranche only, never stacked, no total above ~1.25x standard. Cancel all adds and cut the core on a daily close below 312.761; exit to zero or a token position below 300.57. Time horizon 3–6 months, technical-only.

**Investment Thesis**: The bull case wins the trend question and the bear case wins the price question; because the two are settled on different inputs and the run has no fundamentals, sentiment, or news to break the tie, the honest output is a maintained position rather than a forced direction.

Where the trend evidence is decisive for not selling: AAPL at 325.13 sits above the 50 SMA (312.761) and 15.04% above the 200 SMA (282.626), with the 50/200 spread at 10.66%. The August low of 300.57 is a higher low versus the June low near 274.9, and the +8.17% move off that low came on rising volume (41.2M on 08-31, 53.17M on 09-01, ~27% above the ~41.9M 21-session average). MACD at 1.267 against a signal of −0.238 with a +1.506 histogram is a genuine fresh cross above zero, and RSI at 61.16 is trend-healthy with room to 70. Neither the conservative nor the neutral analyst produced a failed structure, a distribution day inside the August base, or a lost higher low; the conservative conceded the tape is constructive and argued only about sizing and location. Extension and nascent momentum are timing objections, not reasons to exit a live uptrend.

Where the bear case is decisive for not adding at market: spot closed 0.87% above the upper Bollinger Band (322.338), the 20-day mean is 4.26% below at 311.28 and the 50 SMA 3.80% below at 312.761, while the first objective — the 333.143 gap fill — is only 2.46% higher. The trader's own breakout arithmetic (entry 327.30, stop 315.90) is 11.4 points of risk against ~5.8 points of reward, under 0.5:1, and only ~1.1:1 even to the July close at 339.787. The 327.30–333.143 band was created by a 132.5M-share, −8.58% gap session; 53.17M shares is about 40% of that print, so "absorption" is an inference, not a demonstrated fact, and the aggressive analyst's claim that volume expansion proves the supply is gone overstates the evidence.

The gap-risk dispute is where the conservative analyst clearly wins on the numbers, and it decides the sizing. From a 315.78 pullback entry, another 8.58% gap is roughly 288.6, so the trader's 65-share tranche would lose ~$1,760 on a $100,000 account rather than the $1,000 (1%) budget — the aggressive analyst's 1.8:1 to 2.9:1 pullback math assumes a 306 fill that AAPL's own history shows cannot be relied on, and his 100M-share breakout case leans on "blue-sky" continuation, which is not a measurable target for a 17.24-point stop. But the conservative overcorrects: 25 shares risks only ~$245 to the stop and ~$680 in the gap scenario, which underuses the risk budget and is effectively ceremonial, and his demand for a full retest of 327.30–333.143 after a 100M-share close above 333.143 adds delay that the evidence does not require. The neutral analyst's compromise — roughly 35 shares on the pullback and 30–35 on the breakout, standard core, one tranche, and a staged de-risk (trim to ~75% of standard on the first close below 312.761, then 50% if 311.28 or the 310.42 gap edge also breaks) — is the better-calibrated synthesis and is what I am adopting.

What changes the rating: a daily close above 333.143 on 100M+ shares flips me to Overweight (with the stop at 315.90 and targets 339.787 then 344.273), because that is the level both sides agreed breaks the bear case. A tag of 315.78–312.76 that holds on declining volume is the better-risk add and also supports Overweight. A daily close below 312.761 cancels all adds and moves the core toward Underweight; a close below 300.57 breaks the higher-low sequence and puts the 200 SMA at 282.626 in play, which is Sell. Explicitly missing in this run: any fundamental, sentiment, or news data, and `vwma` was unavailable — this is a technical-only judgment, and position sizing should be reduced or reversed if fundamental data contradicts the uptrend. No portfolio context was provided, so all sizing is expressed relative to the caller's own standard allocation and risk budget.

**Price Target**: not provided

**Time Horizon**: 3-6 months (reassess on any daily close outside 312.76-333.14)

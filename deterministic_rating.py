#!/usr/bin/env python3
"""A decision rule that is reproducible by construction.

No LLM in the decision path: the rating comes from a fixed score over the same
indicator snapshot the analyst sees. Same inputs -> same rating, always.

This is the reference point for the study: it measures how much of the agent's
answer is "the evidence" and how much is "the sampler".

Rule (fixed before looking at any rating)
-----------------------------------------
  trend      close > 50 SMA > 200 SMA                    +1
             10 EMA > 50 SMA                             +1
  momentum   MACD > signal, histogram rising             +1
             RSI-14 in 50..70 (momentum without froth)   +1
  extension  close above the upper Bollinger band        -1
             close more than 15 % above the 200 SMA      -1
  volume     volume > 1.2 x 20-day average               +1

  score >= 3 -> Buy; 2 -> Overweight; 1 -> Hold; 0 -> Underweight; <= -1 -> Sell
"""
from __future__ import annotations

import argparse
import json
import sys

import yfinance as yf
from stockstats import StockDataFrame


def rating_for(ticker: str, date: str, lookback_start: str = "2024-06-01") -> dict:
    hist = yf.Ticker(ticker).history(start=lookback_start, end=date)
    hist.index = hist.index.tz_localize(None)
    df = StockDataFrame.retype(hist[["Open", "High", "Low", "Close", "Volume"]].copy())

    last = hist.index[-1]
    close = float(hist["Close"].iloc[-1])
    sma50 = float(df["close_50_sma"].iloc[-1])
    sma200 = float(df["close_200_sma"].iloc[-1])
    ema10 = float(df["close_10_ema"].iloc[-1])
    macd = float(df["macd"].iloc[-1])
    signal = float(df["macds"].iloc[-1])
    hist_now = float(df["macdh"].iloc[-1])
    hist_prev = float(df["macdh"].iloc[-2])
    rsi = float(df["rsi_14"].iloc[-1])
    boll_ub = float(df["boll_ub"].iloc[-1])
    vol = float(hist["Volume"].iloc[-1])
    vol_avg = float(hist["Volume"].iloc[-21:-1].mean())

    score = 0
    reasons = []
    if close > sma50 > sma200:
        score += 1
        reasons.append("close > 50 SMA > 200 SMA")
    if ema10 > sma50:
        score += 1
        reasons.append("10 EMA > 50 SMA")
    if macd > signal and hist_now > hist_prev:
        score += 1
        reasons.append("MACD > signal with rising histogram")
    if 50 <= rsi <= 70:
        score += 1
        reasons.append(f"RSI {rsi:.1f} in 50-70")
    if close > boll_ub:
        score -= 1
        reasons.append("close above upper Bollinger band")
    if close > sma200 * 1.15:
        score -= 1
        reasons.append(f"close {100 * (close / sma200 - 1):.1f}% above 200 SMA")
    if vol > 1.2 * vol_avg:
        score += 1
        reasons.append(f"volume {vol / vol_avg:.2f}x 20-day average")

    tier = ("Buy" if score >= 3 else "Overweight" if score == 2 else "Hold" if score == 1
            else "Underweight" if score == 0 else "Sell")
    return {"ticker": ticker, "date": str(last.date()), "score": score, "rating": tier,
            "reasons": reasons,
            "inputs": {"close": round(close, 3), "sma50": round(sma50, 3),
                       "sma200": round(sma200, 3), "ema10": round(ema10, 3),
                       "macd": round(macd, 4), "signal": round(signal, 4),
                       "macd_hist": round(hist_now, 4), "rsi": round(rsi, 2),
                       "boll_ub": round(boll_ub, 3), "volume": int(vol),
                       "volume_avg20": int(vol_avg)}}


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--ticker", default="AAPL")
    p.add_argument("--date", default="2026-09-02")
    args = p.parse_args()
    print(json.dumps(rating_for(args.ticker, args.date), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

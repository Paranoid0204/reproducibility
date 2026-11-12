#!/usr/bin/env python3
"""Grounding check: do the numbers a report cites match the real market data?

Only claims whose attribution is unambiguous are counted, so that a correct
report is not penalised for writing several dated figures in one sentence.

Claim patterns accepted
-----------------------
1. SNAPSHOT ROW  - "Open A · High B · Low C · Close D · Volume E" on a line that
   also names the analysis date. All five fields must match that date's OHLCV.
2. PRICE-DATE    - a price immediately followed by a parenthesised date,
   e.g. "302.25 (2026-08-12)", "316.83 (08-19)". Must match O/H/L/C of that day.
3. DATE-CLOSE    - "2026-07-28: close 339.787" / "on 2026-08-12 the close was X" -
   a date immediately followed (within 60 chars) by a close/price label and value.
4. INDICATORS    - MACD / RSI / SMA / EMA / ATR values are recomputed with
   stockstats over the same history and compared to any occurrence of that
   indicator label in the report, within the printed precision.

Anything else (bare numbers in prose, percentages, points-differences) is
ignored: those cannot be attributed automatically without guessing.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import pandas as pd
import yfinance as yf
from stockstats import StockDataFrame

FULL_DATE = r"(20\d{2})-(\d{2})-(\d{2})"
DATE_ANY = r"(?:(20\d{2})-)?(\d{2})-(\d{2})"


def load_ohlcv(ticker: str, start: str, end: str) -> pd.DataFrame:
    hist = yf.Ticker(ticker).history(start=start, end=end)
    hist.index = hist.index.tz_localize(None)
    return hist[["Open", "High", "Low", "Close", "Volume"]]


def indicators(hist: pd.DataFrame) -> dict[str, float]:
    df = StockDataFrame.retype(hist.copy())
    last = hist.index[-1].strftime("%Y-%m-%d")
    out = {}
    for key, label in (("close_10_ema", "ema10"), ("close_50_sma", "sma50"),
                       ("close_200_sma", "sma200"), ("rsi_14", "rsi"),
                       ("macd", "macd"), ("macds", "macd_signal"),
                       ("macdh", "macd_hist"), ("atr", "atr")):
        try:
            series = df[key]
            out[label] = float(series.loc[hist.index[-1]])
        except Exception:  # noqa: BLE001 - indicator unavailable for short windows
            continue
    out["date"] = last
    return out


def resolve_date(match: re.Match, default_year: int) -> str:
    year = match.group(1) or str(default_year)
    return f"{year}-{match.group(2)}-{match.group(3)}"


def near(claimed: float, actual: float, rel: float) -> bool:
    return actual != 0 and abs(claimed - actual) / abs(actual) <= rel


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--report", required=True)
    p.add_argument("--ticker", required=True)
    p.add_argument("--start", required=True)
    p.add_argument("--end", required=True)
    p.add_argument("--year", type=int, default=None, help="year for short dates")
    p.add_argument("--include-ambiguous", action="store_true",
                   help="also audit 'date ... close value' sentences with ambiguous attribution")
    args = p.parse_args()

    text = Path(args.report).read_text()
    market = text.split("## market_report")[-1] if "## market_report" in text else text
    hist = load_ohlcv(args.ticker, args.start, args.end)
    rows = {i.strftime("%Y-%m-%d"): i for i in hist.index}
    default_year = args.year or int(sorted(rows)[-1][:4])

    claims: list[dict] = []

    # ---- 1. snapshot row: one contiguous "Open X <sep> High Y <sep> Low Z <sep>
    # Close W <sep> Volume V" run, so that values from other sentences cannot leak in.
    ROW = re.compile(
        r"open[^\d]{0,8}([\d,]+(?:\.\d+)?)[^\w]{1,10}high[^\d]{0,8}([\d,]+(?:\.\d+)?)"
        r"[^\w]{1,10}low[^\d]{0,8}([\d,]+(?:\.\d+)?)[^\w]{1,10}close[^\d]{0,8}([\d,]+(?:\.\d+)?)"
        r"[^\w]{1,10}volume[^\d]{0,8}([\d,]+(?:\.\d+)?)", re.I)
    for m in ROW.finditer(market):
        # the date governing the row: nearest full date before the row, else the analysis date
        before = market[:m.start()]
        dates = re.findall(FULL_DATE, before)
        date = "-".join(dates[-1]) if dates else sorted(rows)[-1]
        if date not in rows:
            continue
        row = hist.loc[rows[date]]
        for field, value in zip(("Open", "High", "Low", "Close", "Volume"), m.groups()):
            claimed = float(value.replace(",", ""))
            actual = float(row[field])
            claims.append({"kind": "snapshot", "date": date, "field": field.lower(),
                           "claimed": claimed, "actual": round(actual, 3),
                           "ok": near(claimed, actual, 1e-3)})

    # ---- 2. price followed by a parenthesised date
    IND_WORDS = re.compile(
        r"(EMA|SMA|RSI|MACD|ATR|VWMA|VWAP|BOLL|BB|MFI|signal|histogram|band|stoch|"
        r"volume[- ]weighted|moving average)", re.I)
    for m in re.finditer(r"([\d]{3}\.\d+)\s*\((?:on\s+)?(" + DATE_ANY + r")[^)]*\)", market):
        price = float(m.group(1))
        line_start = market.rfind("\n", 0, m.start()) + 1
        prefix = market[line_start:m.start()]
        if prefix.strip().startswith("|") or IND_WORDS.search(prefix):
            # table rows and indicator mentions carry indicator values, not
            # session prints (e.g. "200 SMA rose from 279.12 (2026-08-10)")
            continue
        dm = re.match(DATE_ANY, f"{m.group(2)}-{m.group(3)}" if m.group(2) else f"{m.group(3)}-{m.group(4)}")
        date = resolve_date(re.match(r"(?:(20\d{2})-)?(\d{2})-(\d{2})", dm.group(0)), default_year)
        if date not in rows:
            continue
        row = hist.loc[rows[date]]
        ohlc = [float(row[c]) for c in ("Open", "High", "Low", "Close")]
        claims.append({"kind": "price_date", "date": date, "claimed": price,
                       "actual": [round(v, 3) for v in ohlc],
                       "ok": any(near(price, v, 2e-3) for v in ohlc)})

    # ---- 3. date followed by a close label (diagnostic only: a sentence may
    # legitimately mean "the prior close", so this is excluded from the headline
    # metric unless --include-ambiguous is passed)
    for m in (re.finditer(FULL_DATE + r"[^\n]{0,60}?(?:close|closed|closing|price)[^\d]{0,24}([\d,]{3,}(?:\.\d+)?)",
                          market, re.I) if args.include_ambiguous else []):
        date = m.group(0)[:10]
        if len(re.findall(FULL_DATE, m.group(0))) > 1:
            continue  # several dates in the same span -> attribution ambiguous
        if date not in rows:
            continue
        claimed = float(m.group(4).replace(",", ""))
        actual = float(hist.loc[rows[date], "Close"])
        claims.append({"kind": "date_close", "date": date, "claimed": claimed,
                       "actual": actual, "ok": near(claimed, actual, 2e-3)})

    # ---- 4. indicators: recall of the independently recomputed values.
    # For each indicator, accept it as reproduced if the report states the
    # recomputed analysis-date value (within printed precision) anywhere it
    # names that indicator. Historical mentions on other dates are ignored.
    ind = indicators(hist)
    label_map = {"ema10": r"10[- ]?EMA|EMA\s*\(?10", "sma50": r"50[- ]?SMA|SMA\s*\(?50",
                 "sma200": r"200[- ]?SMA|SMA\s*\(?200", "rsi": r"\bRSI\b",
                 "macd": r"\bMACD\b", "macd_signal": r"(?:MACD\s*)?signal\b(?!\s*(?:line|cross|crossover|line-up))",
                 "macd_hist": r"MACD\s*hist(?:ogram)?|histogram", "atr": r"\bATR\b"}
    VALUE_RE = re.compile(r"([−-]?\d+(?:\.\d+)?)")
    ind_claims = []
    for key, pattern in label_map.items():
        if key not in ind:
            continue
        hit = False
        for m in re.finditer("(?:" + pattern + ")", market, re.I):
            # the value may sit either side of the label: "signal −0.238" or a
            # table row "`macds` | −0.2381 | ...". 40 chars each way is enough
            # to reach the neighbouring cell but not a neighbouring row.
            window = market[max(0, m.start() - 40):m.end() + 80]
            for token in VALUE_RE.findall(window):
                try:
                    claimed = float(token.replace("−", "-"))
                except ValueError:
                    continue
                actual = ind[key]
                if actual and abs(claimed - actual) / abs(actual) <= 1e-3:
                    hit = True
                    break
            if hit:
                break
        ind_claims.append({"indicator": key, "actual": round(ind[key], 5), "ok": hit})

    def summarize(items):
        total = len(items)
        hits = sum(1 for c in items if c["ok"])
        return {"n": total, "matched": hits, "accuracy": round(hits / total, 4) if total else None,
                "failures": [c for c in items if not c["ok"]][:10]}

    result = {
        "report": args.report,
        "ticker": args.ticker,
        "analysis_date": ind.get("date"),
        "snapshot_row": summarize([c for c in claims if c["kind"] == "snapshot"]),
        "price_date": summarize([c for c in claims if c["kind"] == "price_date"]),
        "date_close": summarize([c for c in claims if c["kind"] == "date_close"]),
        "indicators": summarize(ind_claims),
        "indicator_values": {k: (round(v, 5) if isinstance(v, float) else v) for k, v in ind.items()},
    }
    all_claims = [c for c in claims if c["kind"] != "date_close"] + ind_claims
    result["total_claims"] = len(all_claims)
    result["total_matched"] = sum(1 for c in all_claims if c["ok"])
    result["grounding_accuracy"] = (round(result["total_matched"] / result["total_claims"], 4)
                                    if all_claims else None)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""
Beats Wireless Speaker Survey — Descriptive Analysis
- Loads raw CSV from ./data/Survey_responses.csv
- Cleans columns
- Computes descriptive summaries
- Saves figures to ./figures/
- Uses matplotlib (no seaborn), one chart per figure.
"""

import os, re, json
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
FIG_DIR = ROOT / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

def clean_col(c):
    c = c.strip()
    c = re.sub(r"\s+", " ", c)
    c = c.replace("/", " or ")
    c = c.replace("?", "")
    c = c.lower().strip().replace(" ", "_")
    c = re.sub(r"[^a-z0-9_]+", "", c)
    return c

def value_counts_percent(s):
    vc = s.dropna().value_counts()
    pct = (vc / vc.sum() * 100).round(1)
    return pd.DataFrame({"count": vc, "percent": pct})

def extract_numeric_midpoint(val):
    if pd.isna(val):
        return np.nan
    text = str(val).replace(",", "")
    m_less = re.search(r"[Ll]ess\s+than\s*\$?(\d+(?:\.\d+)?)", text)
    m_more = re.search(r"[Mm]ore\s+than\s*\$?(\d+(?:\.\d+)?)", text)
    if m_less:
        return float(m_less.group(1)) * 0.8
    if m_more:
        return float(m_more.group(1)) * 1.2
    m_range = re.findall(r"\$?(\d+(?:\.\d+)?)", text)
    if len(m_range) == 2:
        lo, hi = map(float, m_range)
        return (lo + hi) / 2.0
    if len(m_range) == 1:
        return float(m_range[0])
    return np.nan

def likert_to_numeric(s):
    mapping = {
        "very_unimportant": 1, "unimportant": 2, "neutral": 3,
        "important": 4, "very_important": 5,
        "1": 1, "2": 2, "3": 3, "4": 4, "5": 5
    }
    def map_one(x):
        if pd.isna(x):
            return np.nan
        key = str(x).strip().lower().replace(" ", "_")
        return mapping.get(key, np.nan)
    return s.apply(map_one)

def find_cols(cols, keywords):
    pat = re.compile("|".join([re.escape(k) for k in keywords]), flags=re.IGNORECASE)
    return [c for c in cols if pat.search(c)]

def main():
    csv_path = DATA_DIR / "Survey_responses.csv"
    df = pd.read_csv(csv_path)
    df.columns = [clean_col(c) for c in df.columns]
    
    cols = df.columns.tolist()
    ownership_cols = find_cols(cols, ["own", "wireless_speaker"])
    use_freq_cols = find_cols(cols, ["how_often", "use_your_wireless_speaker"])
    sound_quality_cols = find_cols(cols, ["sound_quality"])
    price_cols = find_cols(cols, ["price", "pay", "spend", "willing"])
    gender_cols = find_cols(cols, ["gender"])
    age_cols = find_cols(cols, ["age"])
    income_cols = find_cols(cols, ["income"])
    factor_cols = find_cols(cols, ["how_important", "decision", "factors", "brand_reputation", "reviews", "advertising"])

    # Usage frequency chart
    if use_freq_cols:
        plt.figure()
        df[use_freq_cols[0]].dropna().value_counts().plot(kind="bar")
        plt.title("Usage Frequency Distribution")
        plt.xlabel("Response")
        plt.ylabel("Count")
        plt.tight_layout()
        plt.savefig(FIG_DIR / "usage_frequency.png", dpi=150)

    # Price histogram (first numeric proxy)
    price_numeric_cols = []
    for c in price_cols:
        numeric_series = df[c].apply(extract_numeric_midpoint)
        if numeric_series.notna().mean() > 0.2:
            colname = f"{c}__numeric"
            df[colname] = numeric_series
            price_numeric_cols.append(colname)
    if price_numeric_cols:
        plt.figure()
        df[price_numeric_cols[0]].dropna().plot(kind="hist", bins=15)
        plt.title("Price Distribution")
        plt.xlabel("USD")
        plt.ylabel("Count")
        plt.tight_layout()
        plt.savefig(FIG_DIR / "price_distribution.png", dpi=150)

    # Demographics
    if gender_cols:
        plt.figure()
        df[gender_cols[0]].dropna().value_counts().plot(kind="bar")
        plt.title("Gender Distribution")
        plt.xlabel("Response")
        plt.ylabel("Count")
        plt.tight_layout()
        plt.savefig(FIG_DIR / "gender_distribution.png", dpi=150)

    if age_cols:
        plt.figure()
        df[age_cols[0]].dropna().value_counts().plot(kind="bar")
        plt.title("Age Distribution")
        plt.xlabel("Response")
        plt.ylabel("Count")
        plt.tight_layout()
        plt.savefig(FIG_DIR / "age_distribution.png", dpi=150)

    if income_cols:
        plt.figure()
        df[income_cols[0]].dropna().value_counts().plot(kind="bar")
        plt.title("Income Distribution")
        plt.xlabel("Response")
        plt.ylabel("Count")
        plt.tight_layout()
        plt.savefig(FIG_DIR / "income_distribution.png", dpi=150)

    # Importance factors
    likert_means = {}
    for c in factor_cols:
        scores = likert_to_numeric(df[c])
        if scores.notna().mean() > 0.2:
            likert_means[c] = scores.mean()
    if likert_means:
        likert_df = pd.DataFrame.from_dict(likert_means, orient="index", columns=["mean_score"]).sort_values("mean_score", ascending=False)
        plt.figure()
        likert_df.plot(kind="bar", legend=False)
        plt.title("Importance Factors — Mean Scores (1..5)")
        plt.xlabel("Factor")
        plt.ylabel("Mean score")
        plt.tight_layout()
        plt.savefig(FIG_DIR / "importance_factors_means.png", dpi=150)

    # Also dump a quick JSON summary
    summary = {
        "n_rows": int(df.shape[0]),
        "n_cols": int(df.shape[1]),
        "columns": cols,
        "detected": {
            "ownership_cols": ownership_cols,
            "use_freq_cols": use_freq_cols,
            "sound_quality_cols": sound_quality_cols,
            "price_cols": price_cols,
            "gender_cols": gender_cols,
            "age_cols": age_cols,
            "income_cols": income_cols,
            "factor_cols": factor_cols
        }
    }
    (FIG_DIR / "summary.json").write_text(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()

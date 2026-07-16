# Trader Performance vs Market Sentiment Analysis

## Overview

This project analyzes the relationship between Bitcoin market sentiment (Fear & Greed Index) and historical trader performance.

The objective is to determine whether market sentiment affects trading performance and trader behavior.

---

## Dataset

### 1. Fear & Greed Index
- Date
- Classification
- Market Sentiment

### 2. Historical Trading Data
- Account
- Coin
- Side
- Closed PnL
- Trade Size
- Timestamp
- Fees
- etc.

---

## Libraries Used

- Python
- Pandas
- Matplotlib

---

## Methodology

1. Load datasets
2. Clean data
3. Convert timestamps
4. Merge datasets using date
5. Calculate trading metrics
6. Generate charts
7. Analyze results

---

## Metrics

- Total PnL
- Average PnL
- Win Rate
- Trade Count
- Long vs Short Ratio
- Average Trade Size

---

## Output

Charts generated:

- Average PnL by Market Sentiment
- Win Rate by Market Sentiment
- Trade Count by Market Sentiment
- Long vs Short Distribution
- Average Trade Size by Market Sentiment

---

## How to Run

```bash
pip install pandas matplotlib
python main.py
```
# Quantitative SMA Crossover Strategy & Backtester

## 📌 Executive Summary
This repository implements a Trend-Following algorithmic trading strategy based on **Simple Moving Average (SMA) Crossover** using `yfinance` data. The strategy mitigates **Look-ahead Bias** by lagging trade execution and calculates key risk-adjusted metrics such as **Sharpe Ratio** and **Max Drawdown (MDD)**.

---

## 🛠️ Tech Stack & Dependencies
* **Language:** Python 3.10+
* **Libraries:** `pandas`, `numpy`, `yfinance`, `matplotlib`

---

## 📊 Methodology & Key Concepts

### 1. SMA Crossover Signal
* **Golden Cross (Buy Signal):** $SMA_{50} > SMA_{200}$ $\rightarrow$ Position = 1
* **Death Cross (Sell/Cash Signal):** $SMA_{50} \le SMA_{200}$ $\rightarrow$ Position = 0

### 2. Look-ahead Bias Prevention
To simulate real-world execution without future information leakage:
$$\text{Position}_t = \text{Signal}_{t-1}$$

### 3. Risk-Adjusted Metrics
* **Sharpe Ratio:** 
  $$S = \frac{R_p - R_f}{\sigma_p}$$
* **Max Drawdown (MDD):**
  $$MDD = \min_t \left( \frac{X_t - P_t}{P_t} \right)$$
  *(where $P_t$ is the peak value up to time $t$, and $X_t$ is the current portfolio value)*

---

## 🚀 How to Run
```bash
git clone [https://github.com/tobeaperformanceanaylst/quant-portfolio.git](https://github.com/tobeaperformanceanaylst/quant-portfolio.git)
cd quant-portfolio
python main.py
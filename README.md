# Quantitative SMA Crossover Strategy & Backtester

## 📌 Executive Summary
This repository features an algorithmic trend-following strategy implementation using **Simple Moving Average (SMA) Crossover** on historical equity data via `yfinance`. To ensure quantitative rigor, the pipeline handles multi-index data structures, eliminates **Look-ahead Bias**, and evaluates strategy performance through risk-adjusted metrics like **Sharpe Ratio** and **Max Drawdown (MDD)**.

---

## 🛠️ Tech Stack & Dependencies
* **Language:** Python 3.10+
* **Libraries:** `pandas`, `numpy`, `yfinance`, `matplotlib`

---

## 📊 Methodology & Key Formulas

### 1. Trading Signals & Execution Lag
* **Golden Cross (Long Signal):** $SMA_{50} > SMA_{200} \implies \text{Signal}_t = 1$
* **Death Cross (Cash/Flat):** $SMA_{50} \le SMA_{200} \implies \text{Signal}_t = 0$
* **Execution Lag (Look-ahead Bias Prevention):**
  $$\text{Position}_t = \text{Signal}_{t-1}$$

### 2. Risk-Adjusted Metrics
* **Logarithmic Daily Return:** $r_t = \ln(P_t / P_{t-1})$
* **Sharpe Ratio:**
  $$S = \frac{R_{\text{annualized}} - R_f}{\sigma_{\text{annualized}}}$$
* **Max Drawdown (MDD):**
  $$MDD = \min_t \left( \frac{X_t - \max_{\tau \le t} X_\tau}{\max_{\tau \le t} X_\tau} \right)$$

---

## 🚀 How to Run
```bash
# Clone repository
git clone [https://github.com/tobeaperformanceanaylst/quant-portfolio.git](https://github.com/tobeaperformanceanaylst/quant-portfolio.git)
cd quant-portfolio

# Run backtest
python main.py
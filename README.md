# Quantitative Financial Data Pipeline with Python & yfinance

## 📌 Executive Summary
This repository contains a robust data ingestion and processing pipeline for financial time-series analysis. It retrieves historical price data using `yfinance`, calculates continuous **logarithmic returns**, and derives cumulative performance and **annualized volatility** for benchmark equity indices (e.g., S&P 500 / SPY).

---

## 🛠️ Tech Stack & Dependencies
* **Language:** Python 3.10+
* **Core Libraries:** `pandas`, `numpy`, `yfinance`, `matplotlib`

---

## 📊 Methodology & Key Formulas

### 1. Daily Log Return
Rather than simple arithmetic return, continuous log returns are used to preserve additive properties over time horizons:
$$r_t = \ln\left(\frac{P_t}{P_{t-1}}\right)$$

### 2. Annualized Volatility
Daily standard deviation of log returns is scaled by the square root of annual trading days ($\approx 252$ days):
$$\sigma_{\text{annual}} = \sigma_{\text{daily}} \times \sqrt{252}$$

---

## 🚀 How to Run
```bash
# Clone the repository
git clone [https://github.com/tobeaperformanceanaylst/quant-portfolio.git](https://github.com/tobeaperformanceanaylst/quant-portfolio.git)
cd quant-portfolio

# Install required packages
pip install pandas numpy yfinance matplotlib

# Execute the pipeline
python main.py
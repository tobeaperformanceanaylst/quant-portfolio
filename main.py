import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf


def fetch_and_process_data(
    ticker: str, start_date: str, end_date: str
) -> pd.DataFrame:
    print(f"[{ticker}] 데이터를 {start_date}부터 {end_date}까지 수집 중...")
    df = yf.download(ticker, start=start_date, end=end_date)

    if df.empty:
        raise ValueError("데이터를 불러오지 못했습니다. Ticker를 확인하세요.")

    if isinstance(df.columns, pd.MultiIndex):
        df = df['Close'].to_frame(name='Close')

    df['Log_Return'] = np.log(df['Close'] / df['Close'].shift(1))
    df['Cumulative_Return'] = df['Log_Return'].cumsum().apply(np.exp) - 1
    df.dropna(inplace=True)

    return df


if __name__ == "__main__":
    TICKER = "SPY"
    START = "2023-01-01"
    END = datetime.date.today().strftime("%Y-%m-%d")

    data = fetch_and_process_data(TICKER, START, END)

    print("\n--- 상위 5개 데이터 ---")
    print(data.head())

    daily_vol = data["Log_Return"].std()
    annual_vol = daily_vol * np.sqrt(252)
    print(f"\n[{TICKER}] 연율화 변동성(Annualized Volatility): {annual_vol:.2%}")
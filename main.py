import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf


def run_sma_crossover_backtest(
    ticker: str, start_date: str, end_date: str, short_window: int = 50, long_window: int = 200
) -> pd.DataFrame:
    """
    yfinance 데이터 기반 이동평균 교차(SMA Crossover) 백테스터를 실행합니다.
    Look-ahead Bias를 방지하기 위해 신호(Signal) 발생 다음 날(Shift=1) 포지션을 잡습니다.
    """
    print(f"[{ticker}] 데이터를 수집하고 백테스트를 진행합니다...")
    df = yf.download(ticker, start=start_date, end=end_date)

    if df.empty:
        raise ValueError("데이터를 불러오지 못했습니다. Ticker를 확인하세요.")

    if isinstance(df.columns, pd.MultiIndex):
        df = df['Close'].to_frame(name='Close')

    # 1. 이동평균선(SMA) 계산
    df['SMA_Short'] = df['Close'].rolling(window=short_window).mean()
    df['SMA_Long'] = df['Close'].rolling(window=long_window).mean()

    # 2. 매수/매도 신호 생성 (단기 SMA > 장기 SMA 일 때 1, 아니면 0)
    df['Signal'] = np.where(df['SMA_Short'] > df['SMA_Long'], 1, 0)

    # 3. Look-ahead Bias 방지: t일의 신호로 t+1일에 매매 진행 (Shift 1)
    df['Position'] = df['Signal'].shift(1)

    # 4. 일별 로그 수익률 계산
    df['Log_Return'] = np.log(df['Close'] / df['Close'].shift(1))

    # 5. 전략 수익률(Strategy Return) 및 누적 수익률 계산
    df['Strategy_Return'] = df['Position'] * df['Log_Return']
    df['Benchmark_Cum'] = df['Log_Return'].cumsum().apply(np.exp) - 1
    df['Strategy_Cum'] = df['Strategy_Return'].cumsum().apply(np.exp) - 1

    df.dropna(inplace=True)
    return df


def calculate_performance_metrics(df: pd.DataFrame, risk_free_rate: float = 0.02):
    """Sharpe Ratio 및 Max Drawdown (MDD)을 산출합니다."""
    # 연율화 전략 수익률 및 변동성
    trading_days = 252
    mean_daily_return = df['Strategy_Return'].mean()
    annualized_return = mean_daily_return * trading_days
    annualized_vol = df['Strategy_Return'].std() * np.sqrt(trading_days)

    # Sharpe Ratio (무위험 수익률 2% 가정)
    sharpe_ratio = (annualized_return - risk_free_rate) / annualized_vol if annualized_vol != 0 else 0

    # Max Drawdown (MDD) 계산
    cum_wealth = (1 + df['Strategy_Return']).cumprod()
    peak = cum_wealth.cummax()
    drawdown = (cum_wealth - peak) / peak
    mdd = drawdown.min()

    return annualized_return, annualized_vol, sharpe_ratio, mdd


if __name__ == "__main__":
    TICKER = "SPY"
    START = "2018-01-01"
    END = datetime.date.today().strftime("%Y-%m-%d")

    # 백테스트 실행 (50일/200일 이동평균선)
    data = run_sma_crossover_backtest(TICKER, START, END, short_window=50, long_window=200)

    # 성과 평가 지표 출력
    ann_ret, ann_vol, sharpe, mdd = calculate_performance_metrics(data)

    print("\n" + "="*40)
    print(f"📊 [{TICKER}] SMA Crossover Strategy Performance")
    print("="*40)
    print(f"Annualized Return    : {ann_ret:.2%}")
    print(f"Annualized Volatility: {ann_vol:.2%}")
    print(f"Sharpe Ratio         : {sharpe:.2f}")
    print(f"Max Drawdown (MDD)   : {mdd:.2%}")
    print("="*40)
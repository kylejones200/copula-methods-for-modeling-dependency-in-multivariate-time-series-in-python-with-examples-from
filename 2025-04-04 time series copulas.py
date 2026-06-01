"""Generated from Jupyter notebook: 2025-04-04 time series copulas

Magics and shell lines are commented out. Run with a normal Python interpreter."""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import requests
import scipy.stats as stats
import seaborn as sns
import yfinance as yf
from copulas.bivariate import Clayton, StudentT
from copulas.multivariate import GaussianMultivariate


def simulate_stock_returns_and_interest_rates() -> None:
    np.random.seed(42)
    time_steps = 500
    stock_returns = np.random.normal(0, 1, time_steps)
    interest_rates = 0.5 * stock_returns + np.random.normal(0, 1, time_steps)
    data = pd.DataFrame(
        {"Stock Returns": stock_returns, "Interest Rates": interest_rates}
    )
    u = stats.rankdata(data["Stock Returns"]) / (time_steps + 1)
    v = stats.rankdata(data["Interest Rates"]) / (time_steps + 1)
    copula = Clayton()
    copula.fit(pd.DataFrame({"u": u, "v": v}))
    u_future = np.random.uniform(size=100)
    v_future = copula.inverse_transform(pd.DataFrame({"u": u_future}))
    returns_forecast = np.quantile(data["Stock Returns"], u_future)
    rates_forecast = np.quantile(data["Interest Rates"], v_future["v"])
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=returns_forecast, y=rates_forecast, alpha=0.5)
    plt.xlabel("Forecasted Stock Returns")
    plt.ylabel("Forecasted Interest Rates")
    plt.title("Stock Returns vs. Interest Rates (Copula Forecast)")
    plt.savefig("copula_forecast_stock_interest.png")
    plt.show()
    np.random.seed(42)
    inflation = np.random.normal(2, 1, time_steps)
    unemployment = -0.7 * inflation + np.random.normal(0, 1, time_steps)
    data = pd.DataFrame({"Inflation": inflation, "Unemployment": unemployment})
    u = stats.rankdata(data["Inflation"]) / (time_steps + 1)
    v = stats.rankdata(data["Unemployment"]) / (time_steps + 1)
    copula = StudentT()
    copula.fit(pd.DataFrame({"u": u, "v": v}))
    u_future = np.random.uniform(size=100)
    v_future = copula.inverse_transform(pd.DataFrame({"u": u_future}))
    inflation_forecast = np.quantile(data["Inflation"], u_future)
    unemployment_forecast = np.quantile(data["Unemployment"], v_future["v"])
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=inflation_forecast, y=unemployment_forecast, alpha=0.5)
    plt.xlabel("Forecasted Inflation")
    plt.ylabel("Forecasted Unemployment")
    plt.title("Inflation vs. Unemployment (t-Copula Forecast)")
    plt.savefig("copula_forecast_inflation_unemployment.png")
    plt.show()


def simulate_stock_returns_and_interest_rates_2() -> None:
    np.random.seed(42)
    time_steps = 500
    stock_returns = np.random.normal(0, 1, time_steps)
    interest_rates = 0.5 * stock_returns + np.random.normal(0, 1, time_steps)
    data = pd.DataFrame(
        {"Stock Returns": stock_returns, "Interest Rates": interest_rates}
    )
    u = stats.rankdata(data["Stock Returns"]) / (time_steps + 1)
    v = stats.rankdata(data["Interest Rates"]) / (time_steps + 1)
    copula = Clayton()
    copula.fit(np.column_stack((u, v)))
    simulated_copula_data = copula.sample(100)
    returns_forecast = np.quantile(data["Stock Returns"], simulated_copula_data[:, 0])
    rates_forecast = np.quantile(data["Interest Rates"], simulated_copula_data[:, 1])
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=returns_forecast, y=rates_forecast, alpha=0.5)
    plt.xlabel("Forecasted Stock Returns")
    plt.ylabel("Forecasted Interest Rates")
    plt.title("Stock Returns vs. Interest Rates (Clayton Copula Forecast)")
    plt.savefig("copula_forecast_stock_interest.png")
    plt.show()
    np.random.seed(42)
    inflation = np.random.normal(2, 1, time_steps)
    unemployment = -0.7 * inflation + np.random.normal(0, 1, time_steps)
    data = pd.DataFrame({"Inflation": inflation, "Unemployment": unemployment})
    u = stats.rankdata(data["Inflation"]) / (time_steps + 1)
    v = stats.rankdata(data["Unemployment"]) / (time_steps + 1)
    copula = GaussianMultivariate()
    copula.fit(pd.DataFrame({"Inflation": u, "Unemployment": v}))
    simulated_copula_data = copula.sample(100).to_numpy()
    inflation_forecast = np.quantile(data["Inflation"], simulated_copula_data[:, 0])
    unemployment_forecast = np.quantile(
        data["Unemployment"], simulated_copula_data[:, 1]
    )
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=inflation_forecast, y=unemployment_forecast, alpha=0.5)
    plt.xlabel("Forecasted Inflation")
    plt.ylabel("Forecasted Unemployment")
    plt.title("Inflation vs. Unemployment (Gaussian Copula Forecast)")
    plt.savefig("copula_forecast_inflation_unemployment.png")
    plt.show()


def download_daily_data_for_s_p_500() -> None:
    start_date = "1994-01-01"
    end_date = "2019-09-01"
    sp500
    _daily = yf.download("^GSPC", start=start_date, end=end_date, interval="1d")
    sp500
    _monthly = sp500_daily["Adj Close"].resample("M").last()
    sp500
    _returns = sp500_monthly.pct_change().dropna()
    fedfunds = web.DataReader("FEDFUNDS", "fred", start_date, end_date)
    fedfunds_monthly = fedfunds.resample("M").last()
    data = pd.merge(
        sp500_returns, fedfunds_monthly, left_index=True, right_index=True, how="inner"
    )
    data.columns = ["S&P 500 Returns", "Federal Funds Rate"]
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data["S&P 500 Returns"], label="S&P 500 Returns")
    plt.title("S&P 500 Monthly Returns")
    plt.xlabel("Date")
    plt.ylabel("Returns")
    plt.legend()
    plt.show()
    plt.figure(figsize=(12, 6))
    plt.plot(
        data.index,
        data["Federal Funds Rate"],
        label="Federal Funds Rate",
        color="orange",
    )
    plt.title("Federal Funds Rate")
    plt.xlabel("Date")
    plt.ylabel("Rate (%)")
    plt.legend()
    plt.show()
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x="Federal Funds Rate", y="S&P 500 Returns", data=data)
    plt.title("S&P 500 Returns vs. Federal Funds Rate")
    plt.xlabel("Federal Funds Rate (%)")
    plt.ylabel("S&P 500 Returns")
    plt.show()


def define_the_fmp_api_endpoint() -> None:
    start_date = "1994-01-01"
    end_date = "2019-09-01"
    api_key = "key"
    fmp_url = f"https://financialmodelingprep.com/api/v3/historical-price-full/%5EGev?from={start_date}&to={end_date}&apikey={api_key}"
    response = requests.get(fmp_url)
    data = response.json()
    sp500
    _daily = pd.DataFrame(data["GSPC"])
    sp500_daily["date"] = pd.to_datetime(sp500_daily["date"])
    sp500_daily.set_index("date", inplace=True)
    sp500_daily.sort_index(inplace=True)
    sp500
    _monthly = sp500_daily["close"].resample("M").last()
    sp500
    _returns = sp500_monthly.pct_change().dropna()
    fedfunds = web.DataReader("FEDFUNDS", "fred", start_date, end_date)
    fedfunds_monthly = fedfunds.resample("M").last()
    data = pd.merge(
        sp500_returns, fedfunds_monthly, left_index=True, right_index=True, how="inner"
    )
    data.columns = ["S&P 500 Returns", "Federal Funds Rate"]
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data["S&P 500 Returns"], label="S&P 500 Returns")
    plt.title("S&P 500 Monthly Returns")
    plt.xlabel("Date")
    plt.ylabel("Returns")
    plt.legend()
    plt.show()
    plt.figure(figsize=(12, 6))
    plt.plot(
        data.index,
        data["Federal Funds Rate"],
        label="Federal Funds Rate",
        color="orange",
    )
    plt.title("Federal Funds Rate")
    plt.xlabel("Date")
    plt.ylabel("Rate (%)")
    plt.legend()
    plt.show()
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x="Federal Funds Rate", y="S&P 500 Returns", data=data)
    plt.title("S&P 500 Returns vs. Federal Funds Rate")
    plt.xlabel("Federal Funds Rate (%)")
    plt.ylabel("S&P 500 Returns")
    plt.show()


def notebook_step_006() -> None:
    data


def main() -> None:
    simulate_stock_returns_and_interest_rates()
    simulate_stock_returns_and_interest_rates_2()
    download_daily_data_for_s_p_500()
    define_the_fmp_api_endpoint()
    notebook_step_006()


if __name__ == "__main__":
    main()

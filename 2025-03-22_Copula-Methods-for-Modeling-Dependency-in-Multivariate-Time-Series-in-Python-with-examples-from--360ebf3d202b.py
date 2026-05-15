# Description: Short example for Copula Methods for Modeling Dependency in Multivariate Time Series in Python with examples from.


import logging

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import scipy.stats as stats
import yfinance as yf
from copulas.bivariate import Bivariate


def main():
    np.random.seed(42)

    logger = logging.getLogger(__name__)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )


    # Retrieve interest rates from FRED
    interest_rate_data = web.DataReader(
        "MORTGAGE30US", "fred", start="2000-01-01", end="2025-01-01"
    ).dropna()
    # Retrieve S&P 500 returns from Yahoo Finance
    stock_data = yf.download("^GSPC", start="2000-01-01", end="2025-01-01")
    stock_returns = stock_data["Close"].pct_change().dropna()
    # Align datasets
    aligned_data = pd.concat(
        [stock_returns, interest_rate_data], axis=1, join="inner"
    ).dropna()
    aligned_data.columns = ["Stock Returns", "Interest Rates"]
    # Uniform transformation
    n = len(aligned_data)
    u = stats.rankdata(aligned_data["Stock Returns"]) / (n + 1)
    v = stats.rankdata(aligned_data["Interest Rates"]) / (n + 1)
    uv = np.column_stack((u, v))
    # Automatically select the best copula
    best_copula = Bivariate.select_copula(uv)
    logger.info(f"Selected Copula: {best_copula.copula_type.name}")
    # Fit the selected copula
    best_copula.fit(uv)
    # Simulate future dependencies
    simulated_samples = best_copula.sample(100)
    u_future, v_future = simulated_samples[:, 0], simulated_samples[:, 1]
    # Back-transform to original scale
    returns_forecast = np.quantile(aligned_data["Stock Returns"], u_future)
    rates_forecast = np.quantile(aligned_data["Interest Rates"], v_future)
    # Visualization
    plt.figure(figsize=(10, 7))
    plt.scatter(returns_forecast, rates_forecast, alpha=0.5, edgecolors="k", linewidths=0.5)
    plt.xlabel("Forecasted Stock Returns")
    plt.ylabel("Forecasted Interest Rates")
    plt.title(
        f"Forecasted Stock Returns vs. Interest Rates ({best_copula.copula_type.name.capitalize()} Copula)"
    )
    plt.savefig("copula_forecast_stock_interest_real_data.png")
    plt.show()


    # Set seed for reproducibility

    # Fetch real macroeconomic data from FRED
    inflation = web.DataReader(
        "FPCPITOTLZGUSA", "fred", start="2000-01-01", end="2025-01-01"
    )
    unemployment = web.DataReader("UNRATE", "fred", start="2000-01-01", end="2025-01-01")

    # Clean and align data
    data = pd.concat([inflation, unemployment], axis=1, join="inner").dropna()
    data.columns = ["Inflation", "Unemployment"]

    # Transform data to uniform scale (probabilities)
    n = len(data)
    u = stats.rankdata(data["Inflation"]) / (n + 1)
    v = stats.rankdata(data["Unemployment"]) / (n + 1)
    uv = np.column_stack((u, v))

    # Automatically select the best copula
    best_copula = Bivariate.select_copula(uv)
    logger.info(f"Best copula selected: {best_copula.copula_type.name}")

    # Fit the best copula
    best_copula.fit(uv)

    # Simulate future dependencies
    samples = best_copula.sample(100)
    u_future = samples[:, 0]
    v_future = samples[:, 1]

    # Transform simulated dependencies back to original data scale
    inflation_forecast = np.quantile(data["Inflation"], u_future)
    unemployment_forecast = np.quantile(data["Unemployment"], v_future)

    # Visualization of forecasts
    plt.figure(figsize=(10, 7))
    plt.scatter(
        inflation_forecast, unemployment_forecast, alpha=0.6, edgecolors="k", linewidths=0.5
    )
    plt.xlabel("Forecasted Inflation Rate (%)")
    plt.ylabel("Forecasted Unemployment Rate (%)")
    plt.title(
        f"Inflation vs. Unemployment Forecast ({best_copula.copula_type.name.capitalize()} Copula Model)"
    )
    plt.savefig(
        f"{best_copula.copula_type.name.lower()}_copula_forecast_inflation_unemployment.png"
    )
    plt.show()


if __name__ == "__main__":
    main()

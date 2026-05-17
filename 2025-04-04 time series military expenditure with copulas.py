"""Generated from Jupyter notebook: 2025-04-04 time series military expenditure with copulas

Magics and shell lines are commented out. Run with a normal Python interpreter."""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import gumbel_r
from sklearn.preprocessing import QuantileTransformer


def simulate_gumbel_copula(n, theta=1.5):
    u1 = gumbel_r.rvs(loc=0, scale=1, size=n)
    u2 = gumbel_r.rvs(loc=0, scale=1, size=n)
    u1_copula = gumbel_r.cdf(u1)
    u2_copula = gumbel_r.cdf(u2)
    return np.column_stack([u1_copula, u2_copula])


def main() -> None:
    data = pd.read_csv("data/NMC_Documentation-6.0/NMC-60-abridged/NMC-60-abridged.csv")

    data_clean = data[["milex", "upop"]].dropna()

    scaler = QuantileTransformer()

    data_scaled = scaler.fit_transform(data_clean)

    simulated_data_copula = simulate_gumbel_copula(len(data_scaled))

    simulated_data_original = scaler.inverse_transform(simulated_data_copula)

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)

    plt.scatter(data_clean["milex"], data_clean["upop"], color="blue", alpha=0.5)

    plt.title("Original Data: Military Expenditure vs. Urban Population")

    plt.xlabel("Military Expenditure")

    plt.ylabel("Urban Population")

    plt.subplot(1, 2, 2)

    plt.scatter(
        simulated_data_original[:, 0],
        simulated_data_original[:, 1],
        color="red",
        alpha=0.5,
    )

    plt.title("Simulated Data from Gumbel Copula")

    plt.xlabel("Military Expenditure")

    plt.ylabel("Urban Population")

    plt.tight_layout()

    plt.show()

    data_clean = data[["milex", "upop", "year"]].dropna()

    scaler = QuantileTransformer()

    data_scaled = scaler.fit_transform(data_clean[["milex", "upop"]])

    simulated_data_copula = simulate_gumbel_copula(len(data_scaled))

    simulated_data_original = scaler.inverse_transform(simulated_data_copula)

    fig = plt.figure(figsize=(12, 6))

    ax1 = fig.add_subplot(121, projection="3d")

    ax1.scatter(
        data_clean["milex"],
        data_clean["upop"],
        data_clean["year"],
        color="blue",
        alpha=0.5,
    )

    ax1.set_title("Original Data: Military Expenditure vs. Urban Population")

    ax1.set_xlabel("Military Expenditure")

    ax1.set_ylabel("Urban Population")

    ax1.set_zlabel("Year")

    ax2 = fig.add_subplot(122, projection="3d")

    ax2.scatter(
        simulated_data_original[:, 0],
        simulated_data_original[:, 1],
        data_clean["year"],
        color="red",
        alpha=0.5,
    )

    ax2.set_title("Simulated Data from Gumbel Copula")

    ax2.set_xlabel("Military Expenditure")

    ax2.set_ylabel("Urban Population")

    ax2.set_zlabel("Year")

    plt.tight_layout()

    plt.show()

    data_clean = data[["milex", "upop", "year"]].dropna()

    scaler = QuantileTransformer()

    data_scaled = scaler.fit_transform(data_clean[["milex", "upop"]])

    simulated_data_copula = simulate_gumbel_copula(len(data_scaled))

    simulated_data_original = scaler.inverse_transform(simulated_data_copula)

    fig = plt.figure(figsize=(12, 6))

    ax1 = fig.add_subplot(121, projection="3d")

    ax1.scatter(
        data_clean["milex"],
        data_clean["upop"],
        data_clean["year"],
        color="blue",
        alpha=0.5,
    )

    ax1.set_title("Original Data: Military Expenditure vs. Urban Population")

    ax1.set_xlabel("Military Expenditure")

    ax1.set_ylabel("Urban Population")

    ax1.set_zlabel("Year")

    plt.tight_layout()

    plt.show()


if __name__ == "__main__":
    main()

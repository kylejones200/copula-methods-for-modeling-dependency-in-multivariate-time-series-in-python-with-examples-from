"""Copula prep — rank/uniform transforms via DuckDB window functions."""

import numpy as np
import duckdb
import polars as pl


def generate_stock_interest_data(time_steps: int = 500, seed: int = 42) -> pl.DataFrame:
    rng = np.random.default_rng(seed)
    stock = rng.normal(0, 1, time_steps)
    rates = 0.5 * stock + rng.normal(0, 1, time_steps)
    return pl.DataFrame(
        {"stock_returns": stock.tolist(), "interest_rates": rates.tolist()}
    )


def transform_to_uniform(data: pl.Series) -> pl.Series:
    """Rank-based uniform marginals — replaces scipy.stats.rankdata / n."""
    pl.DataFrame({"x": data, "idx": list(range(data.len()))})
    return duckdb.sql("""
        SELECT (RANK() OVER (ORDER BY x) - 1.0) / NULLIF(COUNT(*) OVER () - 1, 0) AS u
        FROM df
        ORDER BY idx
    """).pl()["u"]


def pairwise_rank_correlation(df: pl.DataFrame, col_x: str, col_y: str) -> float:
    pl.DataFrame(
        {
            "u": transform_to_uniform(df[col_x]),
            "v": transform_to_uniform(df[col_y]),
        }
    )
    return float(duckdb.sql("SELECT CORR(u, v) FROM df").pl()[0, 0])

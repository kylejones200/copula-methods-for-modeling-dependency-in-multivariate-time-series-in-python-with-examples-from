"""Column-wise Pearson correlation matrix (row-major flat storage)."""

from __future__ import annotations

import numpy as np


def rank_correlation_matrix(data: np.ndarray, n_rows: int, n_cols: int) -> np.ndarray:
    m = np.asarray(data, dtype=float).reshape(n_rows, n_cols)
    if n_rows < 2:
        return np.zeros((n_cols, n_cols), dtype=float).ravel()
    corr = np.zeros((n_cols, n_cols), dtype=float)
    for i in range(n_cols):
        for j in range(n_cols):
            xi = m[:, i]
            xj = m[:, j]
            mx, my = xi.mean(), xj.mean()
            a, b = xi - mx, xj - my
            num = float((a * b).sum())
            dx, dy = float((a * a).sum()), float((b * b).sum())
            corr[i, j] = 0.0 if dx <= 1e-18 or dy <= 1e-18 else num / (dx * dy) ** 0.5
    return corr.ravel(order="C")

#!/usr/bin/env python3
"""Python vs Rust kernel benchmark."""

from __future__ import annotations

import time
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
from compute_kernel import rank_correlation_matrix  # noqa: E402

def main() -> None:
    n_rows, n_cols = 200, 5
    data = np.ascontiguousarray(
        np.random.default_rng(0).standard_normal((n_rows, n_cols))
    ).ravel()
    t0 = time.perf_counter()
    for _ in range(200):
        rank_correlation_matrix(data, n_rows, n_cols)
    py_s = time.perf_counter() - t0
    try:
        import copula_methods_for_modeling_dependency_in_multivariate_time_series_in_python_with_examples_from_rs as rs
    except ImportError:
        print("Build: maturin develop --release -m rust/py/Cargo.toml")
        print(f"Python {py_s:.3f}s")
        return
    rs_s = rs.bench_kernel_py(data, n_rows, n_cols, 200)
    print(f"Python {py_s:.3f}s Rust {rs_s:.3f}s speedup {py_s / max(rs_s, 1e-9):.1f}x")
    np.testing.assert_allclose(
        rank_correlation_matrix(data, n_rows, n_cols),
        np.asarray(rs.rank_correlation_matrix_py(data, n_rows, n_cols)),
        rtol=1e-10,
    )
    print("Correctness: OK")

if __name__ == "__main__":
    main()

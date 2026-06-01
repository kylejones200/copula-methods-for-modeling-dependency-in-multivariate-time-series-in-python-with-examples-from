# Copula Methods for Multivariate Time Series

This project demonstrates copula methods for modeling dependencies in multivariate time series.

## Business context

Forecasting multivariate time series requires accurately modeling dependencies between variables. Traditional methods rely on correlation, which fails when relationships shift during different market conditions or economic events. Copulas separate dependency modeling from marginal distributions, allowing more flexible and realistic forecasting. This approach significantly improves forecasts by capturing non-linear relationships and tail dependencies.

Traditional vector autoregression (VAR) assumes linear dependencies. Each variable is modeled as a function of its past values and past values of other variables. Gaussian assumptions simplify calculations but collapse in extreme market conditions or financial crises. Static correlation structures miss dynamic shifts, leading to poor predictions when conditions change.

Copulas overcome these limitations by replacing fixed correlations with dynamic, flexible dependencies. Instead of forcing a single distribution onto data, copulas adapt, capturing changes over time. This flexibility is particularly beneficial for financial and economic forecasting.

## Article

Medium article: [Copula Methods for Modeling Dependency in Multivariate Time Series](https://medium.com/@kylejones_47003/copula-methods-for-modeling-dependency-in-multivariate-time-series-in-python-with-examples-from-360ebf3d202b)

## Project Structure

```
.
├── README.md           # This file
├── main.py            # Main entry point
├── config.yaml        # Configuration file
├── requirements.txt   # Python dependencies
├── src/               # Core functions
│   ├── core.py        # Copula analysis functions
│   └── plotting.py    # Tufte-style plotting utilities
├── tests/             # Unit tests
├── data/              # Data files
├── images/            # Generated plots and figures
├── rust/                   # Rust port (core + PyO3 + CLI bench)
├── benchmark_rust.py       # Python vs Rust benchmark
├── src/compute_kernel.py   # Python/numpy reference kernel
```

## Configuration

Edit `config.yaml` to customize:
- Data generation parameters (time_steps, seed)
- Copula types (Clayton, Student-t)
- Forecast sample sizes
- Output settings

## Copula Methods

### Clayton Copula
- Asymmetric dependence structure
- Lower tail dependence
- Useful for modeling joint extremes

### Student-t Copula
- Symmetric dependence
- Tail dependence in both directions
- More flexible than Gaussian copula

## Caveats

- By default, generates synthetic data for demonstration.
- Copula fitting requires sufficient data for reliable parameter estimation.
- Forecasts preserve dependence structure but may not capture all dynamics.

## Rust performance port

Side-by-side **Python vs Rust** implementation of the numeric hot loop — rank correlation matrix. Reference PyO3 benchmark: **see `benchmark_rust.py`** on a release build (local machine; run `benchmark_rust.py` to reproduce).

| Path | Role |
|------|------|
| `src/compute_kernel.py` | Python/numpy reference kernel |
| `rust/core/` | Pure Rust library |
| `rust/py/` | PyO3 bindings |
| `rust/bench/` | Standalone CLI benchmark |
| `benchmark_rust.py` | Python vs Rust timing + correctness check |

```bash
# Rust-only CLI benchmark
cd rust && cargo run --release -p copula_methods_for_modeling_dependency_in_multivariate_time_series_in_python_with_examples_from_bench

# Python vs Rust (PyO3)
pip install maturin numpy
maturin develop --release -m rust/py/Cargo.toml
python benchmark_rust.py
```

Python ML training, solvers, and orchestration stay in Python; Rust targets the numeric hot loops. Stochastic generators validate output shapes; deterministic kernels match at tight floating-point tolerance.


## Disclaimer

Educational/demo code only. Not financial, safety, or engineering advice. Use at your own risk. Verify results independently before any production or operational use.

## License

MIT — see [LICENSE](LICENSE).
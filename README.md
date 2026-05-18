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
└── images/            # Generated plots and figures
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

## Disclaimer

Educational/demo code only. Not financial, safety, or engineering advice. Use at your own risk. Verify results independently before any production or operational use.

## License

MIT — see [LICENSE](LICENSE).
# CLI for Techtonique

This a **Command Line Interface** (CLI) for [Techtonique](https://www.techtonique.net)'s [API](https://www.techtonique.net/docs). 

## Installation

In a virtual environment, run the following command:

```bash
pip install techtonique_cli
```

If you want to avoid providing a token each time you run the CLI, you can set the `TECHTONIQUE_API_TOKEN` environment variable (for 30 minutes).


## Examples

```bash
techtonique --help

techtonique forecasting --help

techtonique forecasting univariate --help

techtonique ml --help

techtonique ml classification --help

techtonique reserving --help

techtonique survival --help

#  Univariate forecasting
techtonique forecasting univariate /Users/t/Documents/datasets/time_series/univariate/a10.csv --base_model RidgeCV --h 3

# Multivariate forecasting

techtonique forecasting multivariate /Users/t/Documents/datasets/time_series/multivariate/ice_cream_vs_heater.csv --lags 25 --h 10

# Classification
techtonique ml classification /Users/t/Documents/datasets/tabular/classification/iris_dataset2.csv --base_model RandomForestRegressor

# Regression
techtonique ml regression /Users/t/Documents/datasets/tabular/regression/mtcars2.csv --base_model ElasticNet

# Chain Ladder
techtonique reserving chainladder /Users/t/Documents/datasets/tabular/triangle/abc.csv

# Mack Chain Ladder
techtonique reserving mack /Users/t/Documents/datasets/tabular/triangle/abc.csv

# Survival Analysis
techtonique survival /Users/t/Documents/datasets/tabular/survival/kidney.csv --model coxph
```
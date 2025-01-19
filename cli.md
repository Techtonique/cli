# Techtonique CLI Tool


**Techtonique CLI** is a command-line tool that interacts with the Techtonique API for various machine learning, forecasting, reserving, and survival analysis tasks. It simplifies sending POST requests to the API by wrapping the curl commands you provided in a user-friendly interface.

## Key Features

### **Forecasting**
- Supports **univariate** and **multivariate** forecasting.
- Configurable parameters such as:
  - Base model type (e.g., `RidgeCV`).
  - Number of lags.
  - Number of replications.
  - Prediction interval type (e.g., `kde`).


### **Machine Learning**
- Handles **classification** and **regression** tasks.
- Configurable parameters such as:
  - Base model type (e.g., `RandomForest`, `ElasticNet`).
  - Number of hidden features.


### **Reserving**
- Supports reserving methods such as:
  - **Chain Ladder**.
  - **Mack Chain Ladder**.

### **Survival Analysis**
- Performs survival regression using models like:
  - **Cox Proportional Hazards Model** (`coxph`).

## Benefits
1. **Automation**: 
   - Replaces manual `curl` commands with simple CLI commands.
   
2. **Security**: 
   - Reads API tokens from environment variables (`TECHTONIQUE_API_TOKEN`), reducing the risk of exposing sensitive information.
   
3. **Ease of Use**:
   - Validates parameters and provides clear error messages.
   - Includes comprehensive `--help` options for all commands and subcommands.

4. **Flexibility**:
   - Allows customization of parameters like model types, lags, and replications.


## Installation

1. Create a new Python package:
\```bash
mkdir techtonique-cli
cd techtonique-cli
\```

2. Create the following file structure:
\```
techtonique-cli/
├── setup.py
├── requirements.txt
└── techtonique_cli/
    └── __init__.py
    └── cli.py  # The main CLI code goes here
\```

3. Create `setup.py`:
\```python
from setuptools import setup, find_packages

setup(
    name="techtonique-cli",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click>=8.0.0",
        "requests>=2.25.0",
    ],
    entry_points={
        "console_scripts": [
            "techtonique=techtonique_cli.cli:cli",
        ],
    },
)
\```

4. Install the package:
\```bash
pip install -e .
\```

## Usage Guide

After installation, the `techtonique` command will be available in your terminal. The CLI tool provides access to four main categories of functionality:

### 1. Forecasting

#### Univariate Forecasting
\```bash
techtonique forecasting univariate data.csv \
    --base-model RidgeCV \
    --n-hidden-features 5 \
    --lags 25 \
    --type-pi kde \
    --replications 4 \
    --h 3
\```

#### Multivariate Forecasting
\```bash
techtonique forecasting multivariate data.csv \
    --base-model RidgeCV \
    --n-hidden-features 5 \
    --lags 25 \
    --h 3
\```

### 2. Machine Learning

#### Classification
\```bash
techtonique ml classification data.csv \
    --base-model RandomForestRegressor \
    --n-hidden-features 5
\```

#### Regression
\```bash
techtonique ml regression data.csv \
    --base-model ElasticNet \
    --n-hidden-features 5
\```

### 3. Reserving

#### Chain Ladder
\```bash
techtonique reserving chainladder data.csv
\```

#### Mack Chain Ladder
\```bash
techtonique reserving mack data.csv
\```

### 4. Survival Analysis
\```bash
techtonique survival data.csv --model coxph
\```

## Authentication

The tool supports two methods for providing your API token:

1. Environment variable:
\```bash
export TECHTONIQUE_API_TOKEN="your-token-here"
\```

2. Command-line option:
\```bash
techtonique --token "your-token-here" [command]
\```

## Command Structure

The CLI uses a nested command structure:

\```
techtonique
├── forecasting
│   ├── univariate
│   └── multivariate
├── ml
│   ├── classification
│   └── regression
├── reserving
│   ├── chainladder
│   └── mack
└── survival
\```

Each command supports the `--help` option to show available options and usage:
\```bash
techtonique --help
techtonique forecasting --help
techtonique forecasting univariate --help
\```
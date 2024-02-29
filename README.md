# LPM.fidelity

## Disclaimer
This is pre-alpha software. We are currently testing it in real-world scenarios. In its present state, we discourage users from trying it.

## Overview over fidelity component

![schematic](images/fidelity-schematic.png)

## Installation

This library is packaged with [Nix Flakes](https://nixos.wiki/wiki/Flakes).
Include this as a Python module in your Flakes file or use the CLI directly (see
examples below).

## Usage

:warning: this currently only works with categorical CSV files.

### Using fidelity as a Python library

```python
# Get dependencies.
import polars as pl

from lpm_fidelity.distances import bivariate_distances_in_data
from lpm_fidelity.distances import univariate_distances_in_data
from lpm_fidelity.two_sample_testing import univariate_two_sample_testing_in_data

# Read in two csv files.
df_foo = pl.read_csv("foo.csv")
df_bar = pl.read_csv("bar.csv")

# Compute univariate distance.
df_univariate_distance = univariate_distances_in_data(df_foo, df_bar, distance_metric="tvd")

# Compute bivariate distance.
df_bivariate_distance = bivariate_distances_in_data(df_foo, df_bar, distance_metric="tvd")

# Compute univariate two-sample hypothesis tests (currently only Chi^2).
df_univariate_two_sample_test = univariate_two_sample_testing_in_data(df_foo, df_bar)
```

### Fidelity CLI

Usage information for the CLI can be printed with the following command.
```shell
nix run . -- --help
```

Assess univariate probabilistic distance metrics.
```shell
nix run . -- --data-1 foo.csv --data-2 bar.csv
```

Assess bivariate probabilistic distance metrics.
```shell
nix run . -- --data-1 foo.csv --data-2 bar.csv --bivariate
```

Assess fidelity with two-sample testing.
```shell
nix run .#assess-statistics -- --data-1 foo.csv --data-2 bar.csv 
```

## Test

Tests are automatically run through the flakes file.

During development, uses can either add Pytest to the flakes output and use the Nix shell:
```shell
nix develop -c  pytest tests/ -vvv
```
or they install the library globally.
```shell
python -m pip install --upgrade --force-reinstall  . && pytest tests/ -vvv
```
The latter worflow depends on pip and pytest being available globablly, too.

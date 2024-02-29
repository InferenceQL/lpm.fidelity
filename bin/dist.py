import argparse
import polars as pl

from lpm_fidelity.distances import bivariate_distances_in_data
from lpm_fidelity.distances import univariate_distances_in_data


def main():
    """Main function for computing distances."""
    description = (
        "Compute column-wise probabilstic distance measure between two csv files."
    )
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument("-a", "--data-1", type=str, help="Path to a CSV.")
    parser.add_argument("-b", "--data-2", type=str, help="Path to a CSV.")
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="Path to output CSV - prints to stdout if not set.",
        default=None,
    )
    parser.add_argument(
        "--main-metric", type=str, help="Main metric to order result by", default="tvd"
    )
    parser.add_argument(
        "--bivariate",
        action="store_true",
        default=False,
        help="compute bivariate distance metrics",
    )

    args = parser.parse_args()

    df_a = pl.read_csv(args.data_1)
    df_b = pl.read_csv(args.data_2)

    if args.bivariate:
        result = bivariate_distances_in_data(
            df_a, df_b, distance_metric=args.main_metric
        )
    else:
        result = univariate_distances_in_data(
            df_a, df_b, distance_metric=args.main_metric
        )
    if args.output is None:  # Print to stdout.
        print(result.write_csv(args.output))
    else:
        result.write_csv(args.output)


if __name__ == "__main__":
    main()

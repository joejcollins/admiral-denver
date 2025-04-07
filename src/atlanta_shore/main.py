"""Entry point for console access to the package."""

import argparse

from atlanta_shore.handlers import create_dataset
from atlanta_shore.handlers.gpx_parser import create_gpx_observations


def create_datasets():
    """Recreate the datasets for analysis."""
    create_dataset.create_observations()
    create_dataset.create_records()
    # Process GPX files
    create_gpx_observations()
    print("Data files for analysis recreated.")


def perform_analysis():
    """Do some analysis."""
    create_dataset.create_records()
    print("Analysis was rerun.")


def main():
    """Entry point for repeating analytical operations."""
    parser = argparse.ArgumentParser(
        description="Beavers and Botany Analysis Command Line Interface"
    )
    parser.add_argument(
        "-a", "--analysis", action="store_true", help="Rerun the analysis."
    )
    parser.add_argument(
        "-c",
        "--create",
        action="store_true",
        help="Recreate the datasets.",
    )

    args = parser.parse_args()

    if args.create:
        create_datasets()
    elif args.analysis:
        perform_analysis()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

"""Global settings for the project."""

import datetime
import json
import re
from pathlib import Path
from typing import Any

from atlanta_shore import file_finder_service


def date_from_file(file_path: str) -> datetime.date:
    """Extract the survey date from the survey file path"""
    split_path = file_path.split("-")
    year = int(split_path[-4])
    month = int(split_path[-3])
    day = int(split_path[-2])
    return datetime.date(year, month, day)


def date_from_gpx_file(file_path: str) -> datetime.date:
    """Extract the survey date from the gpx file path, handling both formats."""
    # Format 1: spains-hall-waypoints-survey-YYYY-MM-DD.gpx
    match1 = re.search(r"(\d{4})-(\d{2})-(\d{2})", file_path)
    if match1:
        year, month, day = map(int, match1.groups())
        return datetime.date(year, month, day)

    # Format 2: Waypoints_DD-MMM-YY.gpx
    match2 = re.search(r"Waypoints_(\d{2})-([A-Z]{3})-(\d{2})\.gpx", file_path)
    if match2:
        day, month_str, year_short = match2.groups()
        day = int(day)
        year = 2000 + int(year_short)  # Assuming 21st century

        # Convert month string to month number
        month_dict = {
            "JAN": 1,
            "FEB": 2,
            "MAR": 3,
            "APR": 4,
            "MAY": 5,
            "JUN": 6,
            "JUL": 7,
            "AUG": 8,
            "SEP": 9,
            "OCT": 10,
            "NOV": 11,
            "DEC": 12,
        }
        month = month_dict.get(month_str, None)

        if month:
            return datetime.date(year, month, day)
        else:
            raise ValueError(f"Invalid month in file path: {file_path}")

        raise ValueError(f"Could not extract date from file path: {file_path}")


class AtlantaShoreSettings:
    """Settings for the Atlanta Shore Project."""

    def __init__(
        self, file_finder=file_finder_service.FileFinderService(), file_opener=open
    ):
        """Load the file finder, file opener and local settings."""
        self.file_finder = file_finder
        self.open = file_opener
        self.load_local_settings()

    # region Static settings which can be over ridden with the `settings.json` file.
    log_format: str = (
        "[%(asctime)s] [%(levelname)s] %(message)s. "
        "%(pathname)s:%(lineno)d, in %(funcName)s()"
    )
    log_level: str = "WARN"  # as a string so it can be read and set in settings.json.

    # endregion

    def load_local_settings(self) -> None:
        """Load custom settings from the local settings.json file."""
        if settings_path := self.file_finder.find_file_upwards("settings.json"):
            with self.open(settings_path, "r", encoding="utf-8") as file:
                content = file.read()
                settings = json.loads(content)
                for key, value in settings.items():
                    if hasattr(self, key):
                        setattr(self, key, value)

    # region Properties
    @property
    def observations_files(self, pattern="data-plant*.csv") -> Any:
        """Get the list of file names."""
        return self.file_finder.find_data_files(pattern=pattern)

    @property
    def gpx_files(self) -> Any:
        """Get the list of GPX file names."""
        pattern1 = "spains-hall-waypoints-survey-*.gpx"
        pattern2 = "Waypoints_*.gpx"

        files1 = self.file_finder.find_data_files(pattern=pattern1)
        files2 = self.file_finder.find_data_files(pattern=pattern2)

        return sorted(files1 + files2)

    @property
    def processed_data(self) -> Any:
        """Get the directory for processed data."""
        root = self.file_finder.find_root()
        return Path(root) / "data/processed"

    # endregion


ATLANTA_SHORE = AtlantaShoreSettings()

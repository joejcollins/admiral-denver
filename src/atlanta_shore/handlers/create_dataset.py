"""Create the main observations data file by merging the observations files."""

import csv
import re
from typing import Any

from atlanta_shore.data.csv.observation_file_reader import ObservationFileReader
from atlanta_shore.logger import setup_logger
from atlanta_shore.models.sample_point_observation import SamplePointObservation
from atlanta_shore.settings import ATLANTA_SHORE, date_from_file

LOG = setup_logger(__name__)


def _get_field_names(first_observations_file) -> Any:
    """Get the field names from the first observations file."""
    survey_file_reader = ObservationFileReader(first_observations_file)
    first_record = next(survey_file_reader)
    sample_point_observation = SamplePointObservation.set_values_from_observation_csv(
        first_record
    )
    return sample_point_observation.headers()


def create_observations() -> None:
    """Create the observations dataset."""
    # Get the headers from the first file.
    first_observations_file = ATLANTA_SHORE.observations_files[0]
    fieldnames = _get_field_names(first_observations_file)

    with open(
        "./data/processed/observations.csv", "w+", newline=""
    ) as observations_file:
        record_writer = csv.DictWriter(
            observations_file,
            fieldnames=fieldnames,
        )
        record_writer.writeheader()
        for observations_file in ATLANTA_SHORE.observations_files:
            LOG.info(f"observations_file: {observations_file}")
            observation_date = date_from_file(observations_file)
            survey_file_reader = ObservationFileReader(observations_file)
            for record in survey_file_reader:
                LOG.debug(f"record: {record}")
                sample_point_observation = (
                    SamplePointObservation.set_values_from_observation_csv(record)
                )
                sample_point_observation.observation_date = observation_date
                record_writer.writerow(sample_point_observation.model_dump())


def create_records() -> None:
    """Transform all the survey files into a records list

    Create a records for each waypoint with the date and species identified.
    """
    with open("./data/processed/records.csv", "w+", newline="") as records_file:
        record_writer = csv.DictWriter(
            records_file,
            fieldnames=[
                "date",
                "quadrat",
                "waypoint",
                "grid_reference",
                "photo_up",
                "photo_down",
                "wetness",
                "canopy",
                "species",
                "comments",
            ],
        )
        record_writer.writeheader()

        for survey_file_path in ATLANTA_SHORE.observations_files:
            print(survey_file_path)
            with open(survey_file_path, newline="") as survey_file:
                survey_file_reader = csv.reader(survey_file, delimiter=",")
                # Prepare an empty record with the file date
                record = {
                    "date": date_from_file(survey_file_path).isoformat(),
                    "comments": "",
                }
                waypoint_comments = ""  # to collect waypoint comments
                for row in survey_file_reader:
                    # Read the waypoint information into the record.
                    while "species" not in row[0]:
                        record[row[0]] = row[1]  # so just add it to the record
                        if row[2]:  # there is a comment
                            waypoint_comments = waypoint_comments + row[2]
                        row = next(survey_file_reader)
                    # Get the individual species records
                    while True:
                        record["comments"] = waypoint_comments
                        record["species"] = row[1]
                        if row[2]:  # there is a comment
                            record["comments"] = record["comments"] + " - " + row[2]
                        # write a species record
                        record_writer.writerow(record)
                        try:
                            row = next(survey_file_reader)
                        except StopIteration:
                            break  # at the end of the file
                        if re.match(r"species|^$", row[0]) is None:
                            # Next waypoint so add the read row to the record
                            record[row[0]] = row[1]
                            waypoint_comments = row[2] or ""
                            break  # at the end of the species list

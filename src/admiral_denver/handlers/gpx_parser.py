"""Equivalent of create_dataset.py for importing gox data (for height and location check)."""

import csv
import os
import xml.etree.ElementTree as ET
from typing import Any

from admiral_denver.logger import setup_logger
from admiral_denver.settings import admiral_denver, date_from_gpx_file

LOG = setup_logger(__name__)


class GPXFileReader:
    """Class to read GPX files and extract waypoints."""

    def __init__(self, gpx_file_path):
        """Initialize the GPXFileReader with the path to a GPX file."""
        self.tree = ET.parse(gpx_file_path)
        self.root = self.tree.getroot()
        self.ns = {"gpx": "http://www.topografix.com/GPX/1/1"}
        self.waypoints = self.root.findall(".//gpx:wpt", namespaces=self.ns)
        self.waypoint_iter = iter(self.waypoints)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.waypoint_iter)
        except StopIteration as e:
            raise StopIteration from e


def _get_gpx_field_names(first_gpx_file) -> Any:
    gpx_file_reader = GPXFileReader(first_gpx_file)
    first_waypoint = next(gpx_file_reader)
    fields = ["lat", "lon", "ele", "time", "name", "sym", "cmt", "date"]
    return fields


def create_gpx_observations() -> None:
    first_gpx_file = admiral_denver.gpx_files[0]
    fieldnames = _get_gpx_field_names(first_gpx_file)

    output_path = os.path.join(admiral_denver.processed_data, "gpx_observations.csv")

    with open(output_path, "w", newline="", encoding="utf-8") as observations_file:
        record_writer = csv.DictWriter(observations_file, fieldnames=fieldnames)
        record_writer.writeheader()

        for gpx_file in admiral_denver.gpx_files:
            LOG.info(f"GPX file: {gpx_file}")
            gpx_file_reader = GPXFileReader(gpx_file)
            observation_date = date_from_gpx_file(gpx_file)

            for waypoint in gpx_file_reader:
                lat = waypoint.get("lat")
                lon = waypoint.get("lon")
                ele = (
                    waypoint.find("gpx:ele", namespaces=gpx_file_reader.ns).text
                    if waypoint.find("gpx:ele", namespaces=gpx_file_reader.ns)
                    is not None
                    else None
                )
                time = (
                    waypoint.find("gpx:time", namespaces=gpx_file_reader.ns).text
                    if waypoint.find("gpx:time", namespaces=gpx_file_reader.ns)
                    is not None
                    else None
                )
                name = (
                    waypoint.find("gpx:name", namespaces=gpx_file_reader.ns).text
                    if waypoint.find("gpx:name", namespaces=gpx_file_reader.ns)
                    is not None
                    else None
                )
                sym = (
                    waypoint.find("gpx:sym", namespaces=gpx_file_reader.ns).text
                    if waypoint.find("gpx:sym", namespaces=gpx_file_reader.ns)
                    is not None
                    else None
                )
                cmt = (
                    waypoint.find("gpx:cmt", namespaces=gpx_file_reader.ns).text
                    if waypoint.find("gpx:cmt", namespaces=gpx_file_reader.ns)
                    is not None
                    else None
                )

                record_writer.writerow(
                    {
                        "lat": lat,
                        "lon": lon,
                        "ele": ele,
                        "time": time,
                        "name": name,
                        "sym": sym,
                        "cmt": cmt,
                        "date": observation_date.isoformat(),
                    }
                )

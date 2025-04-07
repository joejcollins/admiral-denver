""" Transform GPX

View Ranger doesn't read the gpx extensions so in order
to identify sample sites the id element is transformed into
a gpx field. """
import csv
import os

import lxml.etree as ET
from OSGridConverter import (
    latlong2grid,  # Accurate enough, probably matches ViewRanger and Garmin
)

FILES = ["spains-hall-waypoints-regular-30m-with-name-edited.gpx"]


def main():
    """Transform all the files"""
    for gpx_file in FILES:
        transform(gpx_file)


def transform(gpx_file):
    """Convert to CSV"""
    dir_path = os.path.dirname(os.path.realpath(__file__))
    gpx_file_name = os.path.join(dir_path, "../../data/raw/" + gpx_file)
    dom = ET.parse(gpx_file_name)
    namespaces = {"gpx": "http://www.topografix.com/GPX/1/1"}
    sites = dom.xpath("//gpx:wpt", namespaces=namespaces)
    output_file_name = gpx_file_name.replace(".gpx", ".csv")
    with open(output_file_name, "w+", newline="") as output_file:
        site_writer = csv.DictWriter(
            output_file,
            fieldnames=["name", "lat", "lon", "eastings", "northings", "grid_ref"],
        )
        site_writer.writeheader()
        for site in sites:
            lat = site.attrib["lat"]
            lon = site.attrib["lon"]
            name = site.find("gpx:name", namespaces=namespaces).text
            grid_ref = latlong2grid(float(lat), float(lon))
            eastings = grid_ref.E
            northings = grid_ref.N

            site = {
                "name": name,
                "lat": lat,
                "lon": lon,
                "eastings": eastings,
                "northings": northings,
                "grid_ref": str(grid_ref),
            }
            site_writer.writerow(site)


if __name__ == "__main__":
    main()

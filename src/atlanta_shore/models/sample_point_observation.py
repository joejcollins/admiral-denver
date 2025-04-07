"""Schema for an observation at a sampling point."""

import csv
from datetime import date
from typing import Any, Dict, List

from pydantic import BaseModel, Field


class SamplePointObservation(BaseModel):
    """The point observations are all recorded in the yellow field book.  And are
    entered into a csv file using the same layout as the field book.  The field
    booklets use a different naming convention to the data tables, because the field
    booklets were created in a hurry."""

    sample_point_id: int = Field(alias="quadrat")
    observation_date: date = date(1970, 1, 1)
    garmin_waypoint_id: int = Field(alias="waypoint")  # Garmin Waypoints file.
    garmin_grid_ref: str = Field(alias="grid_reference")  # If the Garmin file fails.
    photo_up_id: str = Field(alias="photo_up")
    photo_down_id: str = Field(alias="photo_down")
    wetness_estimate: float = Field(alias="wetness")  # estimated wetness of the ground.
    canopy_cover_estimate: int = Field(alias="canopy")  # estimated percentage cover.
    species_identified: List[str] = Field(alias="species")  # list of species found.

    @classmethod
    def set_values_from_observation_csv(
        cls, observation_csv: str
    ) -> "SamplePointObservation":
        """Set the values of the model from the csv observation record."""
        csv_data = csv.reader(observation_csv.splitlines())
        data: Dict[Any, Any] = {}
        for row in csv_data:
            csv_field_name = row[0]
            csv_field_value = row[1]
            # The species list is a special case, because it is a list of values.
            if csv_field_name in ["species", ""]:
                # Create a list for the species if it is not there then add.
                if "species" not in data:
                    data["species"] = []
                data["species"].append(csv_field_value)
            else:
                data[csv_field_name] = csv_field_value

        return cls(**data)

    def to_csv(self) -> str:
        """Output as csv"""
        field_values = []
        for field_name, field_value in self.__dict__.items():
            if field_name == "observation_date":
                field_value = field_value.isoformat()
            elif isinstance(field_value, list):
                field_value = "|".join(map(str, field_value))
            field_values.append(str(field_value))
        return ", ".join(field_values)

    def headers(self) -> List[str]:
        """Return the headers for the csv file"""
        return [field_name for field_name, _ in self.__dict__.items()]

    def csv_headers(self) -> str:
        """Return the headers for a csv file"""
        field_names = [field_name for field_name, _ in self.__dict__.items()]
        return ", ".join(field_names)

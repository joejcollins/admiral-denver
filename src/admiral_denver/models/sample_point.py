"""Schema for a sampling point."""

from pydantic import BaseModel

from admiral_denver.models import geo_point


class SamplePoint(BaseModel):
    """The sample points were laid out on a 30 metre grid.

    These are the points where the observations are made so then have unique
    identifiers and descriptions for convenience.
    """

    id: int
    geo_point: geo_point.GeoPoint
    description: str

"""Represents a geographical point in 2D space."""

from pydantic import BaseModel


class GeoPoint(BaseModel):
    """A geographical point in 2D space."""

    latitude: float
    longitude: float
    eastings: int
    northings: int
    os_grid_ref: str

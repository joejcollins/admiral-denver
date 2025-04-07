"""Static parameters for the whole site."""

from typing import List

from pydantic import BaseModel


class Site(BaseModel):
    """Site parameters."""

    area: float  # Area of the site in hectares.
    fence_length: float  # Length of the fence in metres.

    fence_points: List

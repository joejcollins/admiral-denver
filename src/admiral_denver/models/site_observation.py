"""Schema for observations relating to the whole site."""

from datetime import date

from pydantic import BaseModel


class SiteObservation(BaseModel):
    """The site observations are largely the number of beavers."""

    beaver_females: int
    beaver_males: int
    beaver_kits: int
    observation_date: date = date(1970, 1, 1)

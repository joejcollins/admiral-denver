"""Test the Sample Point Observation class."""

from datetime import date

from atlanta_shore.models.sample_point_observation import SamplePointObservation

OBSERVATION_STRING = """quadrat,49,
waypoint,1,
grid_reference,TL6796833089,
photo_up,P6240001,
photo_down,P6240002,
wetness,3,"Averaged, range 1-5 due to beaver canal entering sample point"
canopy,80,mainly Tilia cordata and Populus x
species,Veronica beccabunga,
,Glechoma hederacea,
,Sambucus nigra,
,Urtica dioica,
,Galium aparine,
,Rorippa nasturtium-aquaticum,
,Adoxa moschatellina,
,Populus x canadensis,sucker
,Carex sp,seedling
,Anthriscus sylvestris,
,Silene dioica,
,Arum maculatum,
"""


def test_set_values_from_observation_string() -> None:
    """Confirm that properties are correctly set from an observation string."""
    # Act
    observation = SamplePointObservation.set_values_from_observation_csv(
        OBSERVATION_STRING
    )
    # Assert
    assert observation.canopy_cover_estimate == 80
    assert observation.garmin_grid_ref == "TL6796833089"
    assert len(observation.species_identified) == 12


def test_as_csv() -> None:
    """Confirm that correct string comes back from the as_csv method."""
    # Arrange
    observation = SamplePointObservation.set_values_from_observation_csv(
        OBSERVATION_STRING
    )
    observation.observation_date = date(2023, 6, 23)
    # Act
    csv = observation.to_csv()
    # Assert
    assert csv.startswith("49, 2023-06-23, 1, TL6796833089, P6240001,")


def test_csv_headers() -> None:
    """Confirm that the correct headers are returned."""
    # Arrange
    observation = SamplePointObservation.set_values_from_observation_csv(
        OBSERVATION_STRING
    )
    # Act
    headers = observation.csv_headers()
    # Assert
    assert headers.startswith("sample_point_id, observation_date, garmin_waypoint_id")

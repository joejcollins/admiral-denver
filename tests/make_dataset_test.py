"""Test the functions using for making the dataset."""
from admiral_denver import settings
from admiral_denver.handlers import create_dataset


def test_get_field_names() -> None:
    """Test that the field names are correct."""
    # ARRANGE
    first_observations_file = settings.admiral_denver.observations_files[0]
    # ACT
    field_names = create_dataset._get_field_names(first_observations_file)
    # ASSERT
    assert field_names == [
        "sample_point_id",
        "observation_date",
        "garmin_waypoint_id",
        "garmin_grid_ref",
        "photo_up_id",
        "photo_down_id",
        "wetness_estimate",
        "canopy_cover_estimate",
        "species_identified",
    ]

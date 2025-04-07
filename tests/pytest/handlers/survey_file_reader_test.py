"""Confirm that the survey file reader can iterate through a file."""

from atlanta_shore.data.csv.observation_file_reader import ObservationFileReader


def test_read_first_record() -> None:
    """Confirm that the first record can be read."""
    # Arrange
    survey_file_reader = ObservationFileReader("tests/pytest/dummy_survey_file.csv")
    # Act
    record = next(survey_file_reader)
    # Assert
    assert record.startswith("quadrat,63,\nwaypoint,1,\ngrid_reference,TL6769933268,")
    assert record.endswith(",Kindbergia praelonga,\n")


def test_read_second_record() -> None:
    """Confirm that the second record can be read."""
    # Arrange
    survey_file_reader = ObservationFileReader("tests/pytest/dummy_survey_file.csv")
    # Act
    record = next(survey_file_reader)
    record = next(survey_file_reader)
    # Assert
    assert record.startswith("quadrat,1,\nwaypoint,2,\ngrid_reference,TL6772733270,")
    assert record.endswith(",Ranunculus repens,\n")


def test_read_last_record() -> None:
    """Confirm that the last record can be read."""
    # Arrange
    survey_file_reader = ObservationFileReader("tests/pytest/dummy_survey_file.csv")
    # Act
    record = None
    for record in survey_file_reader:
        pass
    # Assert
    assert record.startswith("quadrat,16,\nwaypoint,3,\ngrid_reference,TL6769833299,")

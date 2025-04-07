"""Confirm that the settings module is working as expected.

This was written as a demonstration of using dependency injection in place of
monkey patching.  Dependency injection is favoured because it makes dependencies
explicit and they can then be mocked without monkey patching.  These dependencies
should are things that we know work and don't need to test.  Things like path.isfile or
builtin.open.  Where we need one of our own methods to behave differently it is more
convenient to monkey patch it instead.  It should be tested elsewhere so doesn't need
further testing.
"""

from _pytest.monkeypatch import MonkeyPatch
from atlanta_shore import file_finder_service, settings

from tests.pytest import mock_builtin_file


def test_date_from_file() -> None:
    """Confirm date parsing from file name."""
    # ARRANGE
    test_file_path = "/data/raw/2019-02/data-plant-2019-02-01-JJC.csv"
    # ACT
    file_date = settings.date_from_file(test_file_path)
    # ASSERT
    assert file_date.year == 2019
    assert file_date.month == 2


def test_static_settings() -> None:
    """Test that the static settings are correct."""
    # ARRANGE
    # Make sure that any `settings.json` file that might be there is not found.
    mock_file_finder = file_finder_service.FileFinderService(isfile=lambda path: False)
    # ACT
    the_settings = settings.AtlantaShoreSettings(mock_file_finder)
    # ASSERT
    assert the_settings.log_level == "WARN"


def test_overriding_static_settings() -> None:
    """Ensure that the static settings are overridden with a `settings.json` file."""
    # ARRANGE
    # Make sure a dummy settings file is found and returned, even it there is not
    # `settings.json` file at all.
    mock_file_finder = file_finder_service.FileFinderService(isfile=lambda path: True)

    def mock_file_open(
        file: str, mode: str, encoding: str
    ) -> mock_builtin_file.MockFile:
        """Return a mock file with some dummy content."""
        return mock_builtin_file.MockFile('{ "log_level": "CRITICAL" }')

    # ACT
    the_settings = settings.AtlantaShoreSettings(
        file_finder=mock_file_finder, file_opener=mock_file_open
    )
    # ASSERT
    assert the_settings.log_level == "CRITICAL"


def test_processed_data_path(monkeypatch: MonkeyPatch) -> None:
    """Confirm the path to the processed data."""
    # ARRANGE
    # Patch over the find_root() method to ensure that the dummy root is found.
    monkeypatch.setattr(
        file_finder_service.FileFinderService,
        "find_root",
        lambda self: "/somewhere/on/the/file/system",
    )
    # ACT
    the_settings = settings.AtlantaShoreSettings()
    processed_data_path = str(the_settings.processed_data)
    # ACT
    assert processed_data_path == "/somewhere/on/the/file/system/data/processed"

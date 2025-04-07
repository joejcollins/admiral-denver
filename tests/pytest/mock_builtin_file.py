"""Mock file class for testing which has the same features at the built in file."""


class MockFile:
    """Mock file class for testing which has the same features at the built in file."""

    def __init__(self, content: str) -> None:
        """Initialise the mock file with the content for the test."""
        self.content = content

    def __enter__(self):
        """Make sure the mock supports the context manager."""
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Make sure the mock supports the context manager."""
        pass

    def read(self) -> str:
        """Return the content of the dummy content."""
        return self.content

    def readlines(self) -> list:
        """Return the content of the dummy content."""
        return self.content.splitlines()

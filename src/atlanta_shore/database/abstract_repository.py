"""Abstract Repository."""
import abc


class AbstractRepository(abc.ABC):
    """ """

    @abc.abstractmethod
    def create(self, record: dict) -> None:
        """Create a record from a dict."""
        raise NotImplementedError

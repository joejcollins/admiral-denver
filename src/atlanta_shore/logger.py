"""Standard logger for the project."""
import logging

from atlanta_shore.settings import ATLANTA_SHORE


def setup_logger(name: str = __name__) -> logging.Logger:
    """Create a standard logger and log to stdout for convenience."""
    logger = logging.getLogger(name)
    logger.setLevel(ATLANTA_SHORE.log_level)

    # Create a formatter for the log messages
    formatter = logging.Formatter(ATLANTA_SHORE.log_format)

    # Create a StreamHandler to write log messages to stdout
    stdout_handler = logging.StreamHandler()
    stdout_handler.setLevel(ATLANTA_SHORE.log_level)
    stdout_handler.setFormatter(formatter)

    # Add the stdout handler to the logger
    logger.addHandler(stdout_handler)

    return logger

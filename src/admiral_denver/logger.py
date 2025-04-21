"""Standard logger for the project."""

import logging

from admiral_denver.settings import admiral_denver


def setup_logger(name: str = __name__) -> logging.Logger:
    """Create a standard logger and log to stdout for convenience."""
    logger = logging.getLogger(name)
    logger.setLevel(admiral_denver.log_level)

    # Create a formatter for the log messages
    formatter = logging.Formatter(admiral_denver.log_format)

    # Create a StreamHandler to write log messages to stdout
    stdout_handler = logging.StreamHandler()
    stdout_handler.setLevel(admiral_denver.log_level)
    stdout_handler.setFormatter(formatter)

    # Add the stdout handler to the logger
    logger.addHandler(stdout_handler)

    return logger

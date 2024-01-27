"""Main module."""

from __future__ import annotations

import logging

from .const import DATE_FORMAT, LOG_FORMAT

_LOGGER = logging.getLogger(__name__)


def init_logger(log_level: int = logging.INFO) -> None:
    """Initialize python logger."""
    fmt = LOG_FORMAT
    datefmt = DATE_FORMAT

    # set the application logger
    logging.basicConfig(level=log_level, format=fmt, datefmt=datefmt)

    # stdout handler
    logging.getLogger().handlers[0].setFormatter(
        logging.Formatter(fmt, datefmt=datefmt)
    )


def main() -> None:
    """Entry point for the application script."""
    # initialize logger
    init_logger()

    # application code here
    _LOGGER.info("Hello World!")


if __name__ == "__main__":
    main()

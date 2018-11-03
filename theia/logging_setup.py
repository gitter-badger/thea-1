"""Functions to setup loggers."""

import logging
import os
from logging.config import fileConfig
import __main__

LOGGING_CONFIG_LOCATION = "logging.ini"


def main_logger():
    """Sets-up main logger from configuration file."""

    # Logger setup
    try:
        # Create logs directory
        if not os.path.exists("logs"):
            os.makedirs("logs")

        # Setup log name
        log_file = os.path.basename(__main__.__file__.split(".")[0])
        logging.log_location = f"logs\\{log_file}.log"
        logger = fileConfig(LOGGING_CONFIG_LOCATION)
    except KeyError:
        raise FileNotFoundError(f"Could not find {LOGGING_CONFIG_LOCATION}.")
    else:
        logger = logging.getLogger(__name__)

    # Print name of main before imports
    logger.info("Launched Python script: {}.".format(__main__.__file__))

    return logger


def aux_logger():
    """Setup auxiliary logger."""

    logger = logging.getLogger(__name__)
    return logger


def vebosity(logger, verbose=False):
    """Adjusts verbosity of the printing to console"""

    if verbose is True:
        logger.parent.handlers[0].setLevel(logging.DEBUG)
    else:
        logger.parent.handlers[0].setLevel(logging.INFO)


# Setup main logger upon first import
main_logger()
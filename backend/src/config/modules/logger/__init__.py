"""Logging"""
import sys
from logging.config import dictConfig

from src.config.manager import get_configuration


def setup_logger(config):
    """
    Initialize the logger with the configured settings
    :param config: Flask config dict
    :return: None
    """
    try:
        dictConfig(get_configuration(
            config['NAME'],
            config['LOG_CONSOLE_LEVEL'],
            config['LOG_DEBUG_FILE_LEVEL'],
            config['LOG_DEBUG_FILE_TO'],
            config['LOG_ERROR_FILE_LEVEL'],
            config['LOG_ERROR_FILE_TO']
        ))
    except Exception as error:
        print(error)
        sys.exit(1)

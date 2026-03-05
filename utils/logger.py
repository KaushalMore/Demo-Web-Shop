import logging
import os
from logging.handlers import RotatingFileHandler


def get_logger(name):
    logger = logging.getLogger(name)

    if logger.hasHandlers():
        logger.handlers.clear()

    logger.setLevel(logging.DEBUG)
    os.makedirs("logs", exist_ok=True)

    console_handler = logging.StreamHandler()
    file_handler = RotatingFileHandler("logs/test_log.log", maxBytes=3000000, backupCount=3)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

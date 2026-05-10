"""
logger_config.py — ECRIO_BMS Mini Project 2
─────────────────────────────────────────────
Centralised logging configuration.
Import `get_logger` in any module to obtain a named logger that writes
both to the console and to a rotating log file.
"""

import logging
import os
from logging.handlers import RotatingFileHandler

# ── Constants ─────────────────────────────────────────────────────────────────
LOG_DIR = os.path.join(os.path.dirname(__file__), "logs")
LOG_FILE = os.path.join(LOG_DIR, "transactions.log")
LOG_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def get_logger(name: str = "ecrio_bms") -> logging.Logger:
    """
    Return a configured Logger instance.

    Args:
        name: Logger namespace (typically the module name).

    Returns:
        logging.Logger: Ready-to-use logger with console + file handlers.
    """
    # Ensure log directory exists
    os.makedirs(LOG_DIR, exist_ok=True)

    logger = logging.getLogger(name)

    # Prevent adding duplicate handlers on repeated calls
    if logger.handlers:
        return logger

    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT)

    # ── Console handler (INFO and above) ──────────────────────────────────────
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # ── Rotating file handler (DEBUG and above, max 1 MB × 3 backups) ─────────
    file_handler = RotatingFileHandler(
        LOG_FILE, maxBytes=1_000_000, backupCount=3, encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

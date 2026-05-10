"""
custom_exceptions.py — ECRIO_BMS Mini Project 4
─────────────────────────────────────────────────
Custom exception hierarchy for the Advanced Data Processing module.
Using custom exceptions makes error handling more expressive and
allows callers to catch specific error categories.
"""


class ECRIOBaseError(Exception):
    """Root exception for all ECRIO_BMS errors."""
    pass


class FileProcessingError(ECRIOBaseError):
    """Raised when a file cannot be read or processed."""
    pass


class EmptyFileError(FileProcessingError):
    """Raised when a file exists but contains no usable data."""
    pass


class DataValidationError(ECRIOBaseError):
    """Raised when data fails a validation check."""
    pass


class StackUnderflowError(ECRIOBaseError):
    """Raised when pop() is called on an empty stack."""
    pass


class QueueUnderflowError(ECRIOBaseError):
    """Raised when dequeue() is called on an empty queue."""
    pass

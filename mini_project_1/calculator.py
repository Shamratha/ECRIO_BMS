"""
calculator.py
─────────────
Core arithmetic operations for the ECRIO_BMS Calculator.
Each function accepts two numbers and returns the result.
Divide-by-zero is handled with a custom error message.
"""


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return a minus b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float | str:
    """
    Return a divided by b.
    Returns an error string when b is zero instead of raising an exception,
    so the caller can display the message directly.
    """
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


# ── Mapping: menu choice → (label, function) ──────────────────────────────────
OPERATIONS: dict[str, tuple[str, callable]] = {
    "1": ("Addition       (+)", add),
    "2": ("Subtraction    (-)", subtract),
    "3": ("Multiplication (*)", multiply),
    "4": ("Division       (/)", divide),
}

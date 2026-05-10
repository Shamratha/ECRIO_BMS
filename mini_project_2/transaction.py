"""
transaction.py — ECRIO_BMS Mini Project 2
───────────────────────────────────────────
Defines the Transaction base class and its Income / Expense subclasses.

Class hierarchy:
    Transaction
    ├── Income
    └── Expense
"""

from datetime import date as Date
from logger_config import get_logger

logger = get_logger(__name__)


# ──────────────────────────────────────────────────────────────────────────────
# Base class
# ──────────────────────────────────────────────────────────────────────────────

class Transaction:
    """
    Represents a financial transaction.

    Attributes:
        amount   (float)  : Monetary value — must be positive.
        category (str)    : E.g. 'Salary', 'Groceries'.
        date     (Date)   : Transaction date (defaults to today).
    """

    def __init__(self, amount: float, category: str, date: Date = None) -> None:
        """
        Initialise a Transaction.

        Args:
            amount   : Must be a positive number.
            category : Short label for the transaction type.
            date     : Defaults to today's date.

        Raises:
            ValueError: If amount is not positive.
            TypeError : If category is not a string.
        """
        # ── Validate amount ────────────────────────────────────────────────────
        try:
            amount = float(amount)
        except (TypeError, ValueError) as exc:
            logger.error("Invalid amount value: %s", amount)
            raise ValueError(f"Amount must be a number, got: {amount!r}") from exc

        if amount <= 0:
            logger.error("Negative/zero amount rejected: %.2f", amount)
            raise ValueError(f"Amount must be positive, got: {amount}")

        # ── Validate category ──────────────────────────────────────────────────
        if not isinstance(category, str) or not category.strip():
            logger.error("Invalid category: %r", category)
            raise TypeError(f"Category must be a non-empty string, got: {category!r}")

        self.amount: float = amount
        self.category: str = category.strip()
        self.date: Date = date or Date.today()

        logger.debug("Transaction created — %s", self)

    # ── Dunder helpers ────────────────────────────────────────────────────────

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"amount={self.amount:.2f}, "
            f"category='{self.category}', "
            f"date={self.date})"
        )

    def __str__(self) -> str:
        return (
            f"[{self.__class__.__name__}] "
            f"₹{self.amount:>10.2f}  |  {self.category:<20}  |  {self.date}"
        )

    # ── Public interface ──────────────────────────────────────────────────────

    def display_info(self) -> None:
        """Print a formatted summary of the transaction."""
        print(f"  {'─' * 50}")
        print(f"  Type     : {self.__class__.__name__}")
        print(f"  Amount   : ₹{self.amount:,.2f}")
        print(f"  Category : {self.category}")
        print(f"  Date     : {self.date}")
        print(f"  {'─' * 50}")
        logger.info("Displayed transaction: %s", self)


# ──────────────────────────────────────────────────────────────────────────────
# Subclasses
# ──────────────────────────────────────────────────────────────────────────────

class Income(Transaction):
    """A positive cash inflow (salary, freelance, etc.)."""

    def __init__(self, amount: float, category: str, date: Date = None,
                 source: str = "Unknown") -> None:
        """
        Args:
            source: Where the income came from (e.g. 'Employer', 'Client').
        """
        super().__init__(amount, category, date)
        self.source: str = source
        logger.info("Income recorded — ₹%.2f from %s", amount, source)

    def display_income(self) -> None:
        """Print income-specific details."""
        self.display_info()
        print(f"  Source   : {self.source}")
        print(f"  {'─' * 50}")


class Expense(Transaction):
    """A cash outflow (bills, groceries, travel, etc.)."""

    def __init__(self, amount: float, category: str, date: Date = None,
                 vendor: str = "Unknown") -> None:
        """
        Args:
            vendor: Where the money was spent (e.g. 'Amazon', 'Supermarket').
        """
        super().__init__(amount, category, date)
        self.vendor: str = vendor
        logger.info("Expense recorded — ₹%.2f at %s", amount, vendor)

    def display_expense(self) -> None:
        """Print expense-specific details."""
        self.display_info()
        print(f"  Vendor   : {self.vendor}")
        print(f"  {'─' * 50}")

"""
tests/test_logging.py — ECRIO_BMS Mini Project 2
──────────────────────────────────────────────────
Mock tests that verify logging behaviour without writing to disk.

Run:
    python -m pytest tests/test_logging.py -v
"""

import sys
import os
import unittest
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from transaction import Income, Expense


class TestIncomeLogging(unittest.TestCase):
    """Verify that Income logs the expected messages."""

    @patch("transaction.logger")
    def test_income_logs_info_on_creation(self, mock_logger: MagicMock):
        """Income.__init__ should call logger.info once."""
        Income(5000, "Freelance", source="Client")
        mock_logger.info.assert_called()

    @patch("transaction.logger")
    def test_income_logs_error_on_negative_amount(self, mock_logger: MagicMock):
        """Negative amount should trigger logger.error."""
        with self.assertRaises(ValueError):
            Income(-100, "Bad")
        mock_logger.error.assert_called()

    @patch("transaction.logger")
    def test_income_logs_debug_on_creation(self, mock_logger: MagicMock):
        """Transaction base should call logger.debug."""
        Income(1000, "Salary")
        mock_logger.debug.assert_called()


class TestExpenseLogging(unittest.TestCase):
    """Verify that Expense logs the expected messages."""

    @patch("transaction.logger")
    def test_expense_logs_info_on_creation(self, mock_logger: MagicMock):
        """Expense.__init__ should call logger.info once."""
        Expense(2000, "Rent", vendor="Landlord")
        mock_logger.info.assert_called()

    @patch("transaction.logger")
    def test_expense_logs_error_on_bad_category(self, mock_logger: MagicMock):
        """Empty category should trigger logger.error."""
        with self.assertRaises(TypeError):
            Expense(500, "")
        mock_logger.error.assert_called()


if __name__ == "__main__":
    unittest.main(verbosity=2)

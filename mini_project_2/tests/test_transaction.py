"""
tests/test_transaction.py — ECRIO_BMS Mini Project 2
──────────────────────────────────────────────────────
Unit tests for the Transaction, Income, and Expense classes.

Run:
    python -m pytest tests/          (pytest)
    python -m unittest discover tests (unittest)
"""

import sys
import os
import unittest
from datetime import date

# Allow imports from the parent directory
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from transaction import Transaction, Income, Expense


class TestTransaction(unittest.TestCase):
    """Tests for the Transaction base class."""

    def test_valid_creation(self):
        """A valid transaction should store all attributes correctly."""
        t = Transaction(amount=500, category="Test", date=date(2024, 1, 1))
        self.assertEqual(t.amount, 500.0)
        self.assertEqual(t.category, "Test")
        self.assertEqual(t.date, date(2024, 1, 1))

    def test_amount_is_float(self):
        """Amount should always be stored as float."""
        t = Transaction(100, "Salary")
        self.assertIsInstance(t.amount, float)

    def test_default_date_is_today(self):
        """If no date is given, it should default to today."""
        t = Transaction(200, "Misc")
        self.assertEqual(t.date, date.today())

    def test_negative_amount_raises(self):
        """Negative amounts must raise ValueError."""
        with self.assertRaises(ValueError):
            Transaction(-100, "Bad")

    def test_zero_amount_raises(self):
        """Zero amount must raise ValueError."""
        with self.assertRaises(ValueError):
            Transaction(0, "Bad")

    def test_non_numeric_amount_raises(self):
        """Non-numeric amount must raise ValueError."""
        with self.assertRaises(ValueError):
            Transaction("not_a_number", "Bad")

    def test_empty_category_raises(self):
        """Empty category must raise TypeError."""
        with self.assertRaises(TypeError):
            Transaction(100, "")

    def test_whitespace_category_raises(self):
        """Whitespace-only category must raise TypeError."""
        with self.assertRaises(TypeError):
            Transaction(100, "   ")

    def test_category_stripped(self):
        """Leading/trailing whitespace should be stripped from category."""
        t = Transaction(100, "  Salary  ")
        self.assertEqual(t.category, "Salary")

    def test_str_representation(self):
        """__str__ should include the class name, amount, and category."""
        t = Transaction(1000, "Rent")
        s = str(t)
        self.assertIn("Transaction", s)
        self.assertIn("1000.00", s)
        self.assertIn("Rent", s)


class TestIncome(unittest.TestCase):
    """Tests for the Income subclass."""

    def test_income_creation(self):
        """Income should inherit Transaction and add source attribute."""
        inc = Income(80_000, "Salary", source="Employer")
        self.assertEqual(inc.amount, 80_000.0)
        self.assertEqual(inc.source, "Employer")

    def test_income_is_transaction(self):
        """Income must be an instance of Transaction."""
        inc = Income(5000, "Bonus")
        self.assertIsInstance(inc, Transaction)

    def test_income_invalid_amount(self):
        """Income with negative amount should raise ValueError."""
        with self.assertRaises(ValueError):
            Income(-100, "Salary")


class TestExpense(unittest.TestCase):
    """Tests for the Expense subclass."""

    def test_expense_creation(self):
        """Expense should inherit Transaction and add vendor attribute."""
        exp = Expense(1500, "Groceries", vendor="Big Basket")
        self.assertEqual(exp.amount, 1500.0)
        self.assertEqual(exp.vendor, "Big Basket")

    def test_expense_is_transaction(self):
        """Expense must be an instance of Transaction."""
        exp = Expense(500, "Travel")
        self.assertIsInstance(exp, Transaction)

    def test_expense_default_vendor(self):
        """Default vendor should be 'Unknown'."""
        exp = Expense(200, "Misc")
        self.assertEqual(exp.vendor, "Unknown")


if __name__ == "__main__":
    unittest.main(verbosity=2)

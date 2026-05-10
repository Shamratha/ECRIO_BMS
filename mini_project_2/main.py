"""
main.py — ECRIO_BMS Mini Project 2
────────────────────────────────────
Demonstrates the Transaction management system:
  • Creates Income and Expense objects
  • Displays formatted output
  • Shows logging in action
  • Demonstrates error handling for invalid data

Run:
    python main.py
"""

from datetime import date
from transaction import Income, Expense
from logger_config import get_logger

logger = get_logger("main")


def demo_valid_transactions() -> None:
    """Create and display a set of valid transactions."""
    print("\n" + "=" * 55)
    print("  💰  ECRIO_BMS Transaction Management System")
    print("=" * 55)

    # ── Income examples ───────────────────────────────────────────────────────
    print("\n  📈  INCOME TRANSACTIONS")
    salary = Income(
        amount=75_000,
        category="Salary",
        date=date(2024, 5, 1),
        source="Tech Corp Pvt Ltd",
    )
    salary.display_income()

    freelance = Income(
        amount=12_500,
        category="Freelance",
        date=date(2024, 5, 15),
        source="Upwork Client",
    )
    freelance.display_income()

    # ── Expense examples ──────────────────────────────────────────────────────
    print("\n  📉  EXPENSE TRANSACTIONS")
    rent = Expense(
        amount=18_000,
        category="Rent",
        date=date(2024, 5, 5),
        vendor="Landlord",
    )
    rent.display_expense()

    groceries = Expense(
        amount=3_450.75,
        category="Groceries",
        date=date(2024, 5, 10),
        vendor="Big Basket",
    )
    groceries.display_expense()

    # ── Summary ───────────────────────────────────────────────────────────────
    total_income = salary.amount + freelance.amount
    total_expense = rent.amount + groceries.amount
    net = total_income - total_expense

    print("\n  📊  MONTHLY SUMMARY")
    print(f"  {'─' * 50}")
    print(f"  Total Income  : ₹{total_income:>10,.2f}")
    print(f"  Total Expense : ₹{total_expense:>10,.2f}")
    print(f"  Net Balance   : ₹{net:>10,.2f}  {'✅' if net >= 0 else '❌'}")
    print(f"  {'─' * 50}")


def demo_error_handling() -> None:
    """Show how invalid data is handled gracefully."""
    print("\n  ⚠️   ERROR HANDLING DEMO")
    print("  " + "─" * 50)

    test_cases = [
        {"amount": -500,   "category": "Bad Amount", "label": "Negative amount"},
        {"amount": "abc",  "category": "Bad Amount", "label": "Non-numeric amount"},
        {"amount": 1000,   "category": "",            "label": "Empty category"},
        {"amount": 0,      "category": "Zero",        "label": "Zero amount"},
    ]

    for case in test_cases:
        label = case.pop("label")
        try:
            t = Income(**case, source="Test")
            t.display_info()
        except (ValueError, TypeError) as exc:
            print(f"  [{label}] → Caught: {exc}")


def main() -> None:
    """Entry point."""
    logger.info("Application started")
    demo_valid_transactions()
    demo_error_handling()
    print("\n  ✅  All done. Check logs/transactions.log for full details.\n")
    logger.info("Application finished")


if __name__ == "__main__":
    main()

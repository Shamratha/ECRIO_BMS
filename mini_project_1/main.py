"""
main.py — ECRIO_BMS Mini Project 1
────────────────────────────────────
A beginner-friendly terminal calculator with:
  • Four arithmetic operations
  • Robust input validation
  • Looping menu until the user exits
  • Divide-by-zero protection

Run:
    python main.py
"""

from calculator import OPERATIONS


# ──────────────────────────────────────────────────────────────────────────────
# Helper utilities
# ──────────────────────────────────────────────────────────────────────────────

def print_banner() -> None:
    """Print a welcome banner."""
    print("\n" + "=" * 45)
    print("       🧮  ECRIO_BMS CALCULATOR  🧮")
    print("=" * 45)


def print_menu() -> None:
    """Print the operations menu."""
    print("\n  Select an operation:")
    for key, (label, _) in OPERATIONS.items():
        print(f"    [{key}] {label}")
    print("    [5] Exit")
    print("-" * 45)


def get_number(prompt: str) -> float:
    """
    Prompt the user for a number and keep asking until a valid
    integer or float is entered.
    """
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print(f"  ⚠️  '{raw}' is not a valid number. Please try again.")


def get_menu_choice() -> str:
    """Return a valid menu choice (1-5)."""
    valid = set(OPERATIONS.keys()) | {"5"}
    while True:
        choice = input("  Your choice: ").strip()
        if choice in valid:
            return choice
        print(f"  ⚠️  Please enter a number between 1 and 5.")


# ──────────────────────────────────────────────────────────────────────────────
# Main application loop
# ──────────────────────────────────────────────────────────────────────────────

def main() -> None:
    """Entry point — runs the calculator loop."""
    print_banner()
    print("  Welcome! This calculator supports +, -, *, /")

    while True:
        print_menu()
        choice = get_menu_choice()

        # Exit condition
        if choice == "5":
            print("\n  👋  Thanks for using ECRIO_BMS Calculator. Goodbye!\n")
            break

        # Retrieve the chosen operation
        label, operation = OPERATIONS[choice]
        print(f"\n  ── {label} ──")

        # Collect operands
        num1 = get_number("  Enter first number : ")
        num2 = get_number("  Enter second number: ")

        # Perform calculation
        result = operation(num1, num2)

        # Display result (result may be a string for divide-by-zero)
        if isinstance(result, str):
            print(f"\n  ❌  {result}")
        else:
            # Format: remove trailing '.0' for whole numbers
            display = int(result) if result == int(result) else round(result, 6)
            print(f"\n  ✅  Result: {num1} {label[16]} {num2} = {display}")


# ──────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()

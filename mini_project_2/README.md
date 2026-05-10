# Mini Project 2 — OOP + Logging + Unit Testing 💼

A transaction management system demonstrating Object-Oriented Programming,
Python's built-in logging module, and unit testing with unittest and mocks.

---

## 📁 Structure
```
mini_project_2/
├── main.py               ← Entry point & demo
├── transaction.py        ← Transaction, Income, Expense classes
├── logger_config.py      ← Centralised logging setup
├── tests/
│   ├── __init__.py
│   ├── test_transaction.py   ← Unit tests for classes
│   └── test_logging.py       ← Mock tests for logging
├── README.md
├── requirements.txt
└── sample_output.txt
```

---

## 🧠 Concepts Covered
| Concept | Where |
|---------|-------|
| Class with `__init__` | `transaction.py → Transaction` |
| Inheritance | `Income(Transaction)`, `Expense(Transaction)` |
| `display_info()` method | `transaction.py` |
| `logging.basicConfig` equivalent | `logger_config.py` |
| `logger.error()` on bad input | `transaction.py` |
| `try/except` validation | `transaction.py → __init__` |
| `unittest.TestCase` | `tests/test_transaction.py` |
| `unittest.mock.patch` | `tests/test_logging.py` |

---

## ▶️ How to Run

```bash
cd mini_project_2

# Run the demo
python main.py

# Run all unit tests
python -m unittest discover tests -v
```

---

## 🖼 Screenshot Placeholder
> _Add a screenshot of your terminal output here_

![MP2 Screenshot](../docs/mp2_screenshot.png)

---

## 📦 Dependencies
No third-party packages — pure Python 3.10+ stdlib.

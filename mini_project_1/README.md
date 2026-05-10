# Mini Project 1 — Python Calculator 🧮

A terminal-based calculator that covers the fundamental Python building blocks:
data types, functions, loops, input validation, and error handling.

---

## 📁 Structure
```
mini_project_1/
├── main.py           ← Entry point & menu loop
├── calculator.py     ← Pure arithmetic functions
├── README.md
├── requirements.txt
└── sample_output.txt
```

---

## 🧠 Concepts Covered
| Concept | Where |
|---------|-------|
| `int`, `float`, `str` data types | `calculator.py`, `main.py` |
| Separate functions per operation | `calculator.py` |
| Input validation with `try/except` | `main.py → get_number()` |
| Looping menu with `while True` | `main.py → main()` |
| Divide-by-zero guard | `calculator.py → divide()` |
| Dictionary for dispatch table | `calculator.py → OPERATIONS` |

---

## ▶️ How to Run
```bash
cd mini_project_1
python main.py
```

---

## 🖼 Screenshot Placeholder
> _Add a screenshot of your terminal output here_

![Calculator Screenshot](../docs/mp1_screenshot.png)

---

## 📦 Dependencies
No third-party packages required — pure Python 3.10+.

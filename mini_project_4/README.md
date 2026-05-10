# Mini Project 4 — Advanced Data Processing ⚙️

Demonstrates file I/O, all major Python data structures, custom exceptions,
assertions, and logging — all wired together in a clean, modular design.

---

## 📁 Structure
```
mini_project_4/
├── main.py                ← Entry point & all demos
├── utils.py               ← List/Tuple/Set/Dict/Stack/Queue helpers
├── custom_exceptions.py   ← Custom exception hierarchy
├── logger_config.py       ← Rotating file + console logger
├── data/
│   └── sample_data.txt    ← Auto-created on first run
├── logs/
│   └── data_processing.log
├── README.md
├── requirements.txt
└── sample_output.txt
```

---

## 🧠 Concepts Covered
| Concept | Where |
|---------|-------|
| Line-by-line file reading | `utils.read_file_line_by_line()` |
| List ops (append, sort, slice) | `utils.demonstrate_list_ops()` |
| Tuple ops (count, index, slice) | `utils.demonstrate_tuple_ops()` |
| Set ops (union, intersect, diff) | `utils.demonstrate_set_ops()` |
| Dict ops (frequency, comprehension) | `utils.demonstrate_dict_ops()` |
| Stack (LIFO) | `utils.Stack` |
| Queue (FIFO with deque) | `utils.Queue` |
| Custom exceptions | `custom_exceptions.py` |
| `assert` statements | `main.demo_assertions()` |
| Rotating file logging | `logger_config.py` |

---

## ▶️ How to Run
```bash
cd mini_project_4
python main.py
```
The `data/sample_data.txt` file is auto-created on the first run.

---

## 🖼 Screenshot Placeholder
> _Add a screenshot here_

![MP4 Screenshot](../docs/mp4_screenshot.png)

---

## 📦 Dependencies
No third-party packages — pure Python 3.10+ stdlib.

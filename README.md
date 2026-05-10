# ECRIO_BMS 🐍

> **E**ducational **C**ode **R**epository for **I**ntermediate to **O**riginal **B**eginner **M**entored **S**tudies

A collection of **7 end-to-end Python mini-projects** covering core programming,
OOP, data analysis, file processing, data normalisation, web development, and IoT messaging —
all following professional coding standards and ready to push to GitHub.

---

## 📁 Repository Structure

```
ECRIO_BMS/
│
├── README.md
├── requirements.txt
├── .gitignore
├── datasets/               ← Shared raw datasets
├── docs/
│   └── GITHUB_GUIDE.md    ← Step-by-step GitHub push guide
├── screenshots/            ← Add your screenshots here
│
├── mini_project_1/         ← Python Calculator
├── mini_project_2/         ← OOP + Logging + Unit Testing
├── mini_project_3/         ← Titanic Dataset Analysis (Pandas)
├── mini_project_4/         ← Advanced Data Processing
├── mini_project_5/         ← Normalisation + Pivot Tables
├── mini_project_6/         ← Flask To-Do Web Application
└── mini_project_7/         ← MQTT Publisher & Subscriber
```

---

## 🗂 Mini Projects Overview

| # | Project | Key Concepts | Run Command |
|---|---------|-------------|-------------|
| 1 | Python Calculator | Data types, functions, loops, validation | `python main.py` |
| 2 | Transaction Management | OOP, inheritance, logging, unittest | `python main.py` |
| 3 | Titanic Analysis | Pandas, CSV I/O, filtering, groupby | `python main.py` |
| 4 | Advanced Data Processing | File I/O, Stack, Queue, custom exceptions | `python main.py` |
| 5 | Normalisation & Pivot Tables | Min-Max, Z-score, pivot tables | `python main.py` |
| 6 | Flask To-Do App | Flask, Jinja2, routes, HTML/CSS | `python app.py` |
| 7 | MQTT Pub/Sub | paho-mqtt, IoT messaging, broker | `python publisher.py` / `python subscriber.py` |

---

## 🚀 Quick Start

### 1 — Clone the repository
```bash
git clone https://github.com/<your-username>/ECRIO_BMS.git
cd ECRIO_BMS
```

### 2 — Create & activate a virtual environment
```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3 — Install dependencies per project
```bash
# Mini Project 6 (Flask)
cd mini_project_6
pip install -r requirements.txt
python app.py

# Mini Project 7 (MQTT) — open TWO terminals
cd mini_project_7
pip install -r requirements.txt
python subscriber.py   # Terminal 1
python publisher.py    # Terminal 2
```

### 4 — Titanic dataset (Projects 3 & 5)
```bash
curl -o mini_project_3/datasets/titanic.csv \
  https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv

cp mini_project_3/datasets/titanic.csv mini_project_5/datasets/titanic.csv
```

---

## 🛠 Tech Stack

| Tool | Used In |
|------|---------|
| Python 3.10+ | All projects |
| Pandas, NumPy | Projects 3, 5 |
| Flask, Jinja2 | Project 6 |
| paho-mqtt | Project 7 |
| logging, unittest | Projects 2, 4 |

---

## 📤 Pushing to GitHub

```bash
git init
git add .
git commit -m "Initial commit — ECRIO_BMS all 7 projects"
git branch -M main
git remote add origin https://github.com/<your-username>/ECRIO_BMS.git
git push -u origin main
```

See `docs/GITHUB_GUIDE.md` for the full step-by-step guide.

---

## 📜 License
MIT — free to use and learn from.

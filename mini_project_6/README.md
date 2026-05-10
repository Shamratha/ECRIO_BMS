# Mini Project 6 — Flask To-Do Web Application 🌐

A clean, beginner-friendly web app built with **Flask** and **Jinja2** templates.
Add, complete, and delete tasks — all in your browser, no database needed.

---

## 📁 Structure
```
mini_project_6/
├── app.py                  ← Flask app, all routes
├── static/
│   └── style.css           ← Responsive CSS styling
├── templates/
│   ├── base.html           ← Shared layout (navbar, flash, footer)
│   └── index.html          ← Task list page
├── README.md
├── requirements.txt
└── sample_output.txt
```

---

## 🧠 Concepts Covered
| Concept | Where |
|---------|-------|
| `Flask(__name__)` app setup | `app.py` |
| `@app.route()` decorators | `app.py` |
| `render_template()` | `index` route |
| `redirect()` + `url_for()` | All POST routes |
| `flash()` messages | `add_task`, `delete_task`, `toggle_task` |
| `request.form.get()` | `add_task` route |
| Jinja2 `{% extends %}` | `index.html` |
| Jinja2 `{% for %}` loop | `index.html` task list |
| Jinja2 `{% if %}` condition | Empty state, done/pending |
| CSS variables & responsive | `style.css` |

---

## ▶️ Setup & Run

```bash
# 1 — Go to project folder
cd mini_project_6

# 2 — Create virtual environment
python -m venv venv
source venv/bin/activate        # Mac / Linux
venv\Scripts\activate           # Windows

# 3 — Install Flask
pip install -r requirements.txt

# 4 — Run the app
python app.py

# 5 — Open in browser
# http://127.0.0.1:5000
```

---

## 🌐 Routes

| Route | Method | Purpose |
|-------|--------|---------|
| `/` | GET | Show all tasks |
| `/add` | POST | Add a new task |
| `/delete/<id>` | POST | Delete a specific task |
| `/toggle/<id>` | POST | Mark done / undone |
| `/clear` | POST | Delete all tasks |

---

## 🖼 Screenshot Placeholder
> _Add a screenshot here_

![MP6 Screenshot](../screenshots/mp6_screenshot.png)

---

## 📦 Dependencies
```
Flask>=3.0.0
```

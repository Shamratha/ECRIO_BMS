"""
app.py — ECRIO_BMS Mini Project 6
───────────────────────────────────
Flask To-Do Web Application.

Features:
  • Add tasks with validation
  • View all tasks in a clean UI
  • Delete tasks individually
  • Flash messages for user feedback
  • In-memory task storage (Python list)

Run:
    python app.py
Then open: http://127.0.0.1:5000
"""

from flask import Flask, render_template, request, redirect, url_for, flash

# ── App Initialisation ────────────────────────────────────────────────────────
app = Flask(__name__)

# Secret key is required for Flask's flash (session) messaging system
app.secret_key = "ecrio_bms_secret_key_2024"

# ── In-memory task storage ────────────────────────────────────────────────────
# Each task is a dict: {"id": int, "text": str, "done": bool}
tasks = []
next_id = 1  # auto-incrementing ID counter


# ── Helper ────────────────────────────────────────────────────────────────────

def find_task(task_id: int):
    """Return the task dict matching task_id, or None if not found."""
    return next((t for t in tasks if t["id"] == task_id), None)


# ── Routes ────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    """
    Home page — display all tasks.
    Passes the task list to the Jinja2 template.
    """
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    """
    Handle the Add Task form submission (POST only).
    Validates input and appends a new task to the list.
    Redirects back to home after processing.
    """
    global next_id

    # Get task text from the submitted form
    task_text = request.form.get("task", "").strip()

    # Validation — do not allow empty tasks
    if not task_text:
        flash("⚠️  Task cannot be empty. Please type something!", "warning")
        return redirect(url_for("index"))

    if len(task_text) > 200:
        flash("⚠️  Task is too long. Keep it under 200 characters.", "warning")
        return redirect(url_for("index"))

    # Add task to the in-memory list
    tasks.append({"id": next_id, "text": task_text, "done": False})
    next_id += 1

    flash(f'✅  Task "{task_text}" added successfully!', "success")
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id: int):
    """
    Delete a task by its ID.
    Uses a POST request (not GET) to prevent accidental deletion via URL.
    """
    task = find_task(task_id)

    if task:
        tasks.remove(task)
        flash(f'🗑️  Task "{task["text"]}" deleted.', "info")
    else:
        flash("❌  Task not found.", "danger")

    return redirect(url_for("index"))


@app.route("/toggle/<int:task_id>", methods=["POST"])
def toggle_task(task_id: int):
    """
    Toggle a task's completion status (done / not done).
    """
    task = find_task(task_id)

    if task:
        task["done"] = not task["done"]
        status = "completed" if task["done"] else "reopened"
        flash(f'🔄  Task marked as {status}.', "info")
    else:
        flash("❌  Task not found.", "danger")

    return redirect(url_for("index"))


@app.route("/clear", methods=["POST"])
def clear_all():
    """Delete ALL tasks at once."""
    global tasks, next_id
    count = len(tasks)
    tasks = []
    next_id = 1
    flash(f"🧹  Cleared all {count} task(s).", "info")
    return redirect(url_for("index"))


# ── Entry Point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("  🚀  ECRIO_BMS Flask To-Do App")
    print("  📌  Open: http://127.0.0.1:5000")
    print("=" * 50 + "\n")
    # debug=True enables auto-reload on file save (development only)
    app.run(debug=True)

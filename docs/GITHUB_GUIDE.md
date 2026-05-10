# 🚀 How to Push ECRIO_BMS to GitHub

A step-by-step guide for beginners.

---

## Step 1 — Create a GitHub Repository

1. Go to https://github.com and sign in.
2. Click the **+** icon → **New repository**.
3. Name it exactly: `ECRIO_BMS`
4. Set visibility: **Public** (or Private).
5. ⚠️ **Do NOT** check "Add a README" — we already have one.
6. Click **Create repository**.

---

## Step 2 — Open VS Code Terminal

Open VS Code, then open the terminal:
- **Windows/Linux**: `Ctrl + `` ` ``
- **macOS**: `Cmd + `` ` ``

Navigate to your project folder:
```bash
cd path/to/ECRIO_BMS
```

---

## Step 3 — Initialise Git

```bash
git init
git add .
git commit -m "Initial commit — ECRIO_BMS complete project"
```

---

## Step 4 — Connect to GitHub

Copy the remote URL from your GitHub repository page, then:

```bash
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ECRIO_BMS.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

---

## Step 5 — Verify

Visit `https://github.com/YOUR_USERNAME/ECRIO_BMS` — you should see all files!

---

## 🔄 Future Updates

After making changes:
```bash
git add .
git commit -m "Your descriptive commit message"
git push
```

---

## 💡 Useful Git Commands

| Command | Purpose |
|---------|---------|
| `git status` | See changed files |
| `git log --oneline` | See commit history |
| `git diff` | See exact changes |
| `git branch` | List branches |

---

## 🐍 Virtual Environment (Recommended)

```bash
# Create
python -m venv venv

# Activate — macOS/Linux
source venv/bin/activate

# Activate — Windows
venv\Scripts\activate

# Install all dependencies
pip install -r requirements.txt

# Deactivate when done
deactivate
```

> The `venv/` folder is already in `.gitignore` — it won't be pushed to GitHub.

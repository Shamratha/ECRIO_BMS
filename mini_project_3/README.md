# Mini Project 3 — Titanic Dataset Analysis 🚢

Full exploratory data analysis on the Titanic dataset using **Pandas**.
Covers loading, filtering, grouping, age binning, and CSV export.

---

## 📁 Structure
```
mini_project_3/
├── main.py           ← Runs the full analysis pipeline
├── analysis.py       ← All analysis functions (modular)
├── datasets/
│   └── titanic.csv   ← Place dataset here (see below)
├── output/
│   └── cleaned_titanic.csv   ← Auto-generated after run
├── README.md
├── requirements.txt
└── sample_output.txt
```

---

## 📥 Getting the Dataset

```bash
# Option 1 — curl
curl -o datasets/titanic.csv \
  https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv

# Option 2 — wget
wget -O datasets/titanic.csv \
  https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
```

---

## 🧠 Concepts Covered
| Concept | Function |
|---------|----------|
| Load CSV | `load_dataset()` |
| `.head()` preview | `show_first_rows()` |
| `groupby` + `count` | `passengers_by_class_and_gender()` |
| Boolean filtering | `female_survival_percentage()` |
| `.mean()` per group | `survival_rate_by_gender()` |
| `.median()` per group | `median_age_by_gender()` |
| Filter rows | `passengers_above_age()` |
| `pd.cut()` binning | `add_age_group()` |
| Multi-condition filter | `survivors_first_class()` |
| `fillna`, `dropna` | `clean_dataset()` |
| Export CSV | `export_cleaned()` |

---

## ▶️ How to Run

```bash
cd mini_project_3
pip install -r requirements.txt
python main.py
```

---

## 🖼 Screenshot Placeholder
> _Add a screenshot of your terminal output here_

![MP3 Screenshot](../docs/mp3_screenshot.png)

---

## 📦 Dependencies
```
pandas>=2.0.0
```

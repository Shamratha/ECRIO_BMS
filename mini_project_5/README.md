# Mini Project 5 — Normalisation & Pivot Tables 📈

Advanced data preprocessing on the Titanic dataset:
Min-Max normalisation, Z-score normalisation, feature engineering,
grouped aggregations, and pivot tables.

---

## 📁 Structure
```
mini_project_5/
├── main.py              ← Full pipeline entry point
├── preprocessing.py     ← All transform & normalisation functions
├── visualization.py     ← Terminal pretty-printing helpers
├── datasets/
│   └── titanic.csv      ← Place dataset here (see below)
├── output/
│   └── titanic_processed.csv   ← Auto-generated
├── README.md
├── requirements.txt
└── sample_output.txt
```

---

## 📥 Getting the Dataset

```bash
curl -o datasets/titanic.csv \
  https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
```

---

## 🧠 Concepts Covered
| Concept | Function |
|---------|----------|
| Fill missing with mean | `fill_missing_age()` |
| Fill missing with mode | `fill_missing_embarked()` |
| Numeric encoding | `add_sex_code()` |
| Boolean feature | `add_child_adult_column()` |
| Min-Max normalisation | `min_max_normalise()` |
| Z-score normalisation | `zscore_normalise()` |
| Grouped aggregation | `group_by_pclass()`, `group_by_sex_code()` |
| `pd.pivot_table` | `pivot_pclass_sexcode()`, `pivot_survival_by_child()` |

---

## ▶️ How to Run
```bash
cd mini_project_5
pip install -r requirements.txt
python main.py
```

---

## 🖼 Screenshot Placeholder
> _Add a screenshot here_

![MP5 Screenshot](../docs/mp5_screenshot.png)

---

## 📦 Dependencies
```
pandas>=2.0.0
numpy>=1.24.0
```

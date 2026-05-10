"""
main.py — ECRIO_BMS Mini Project 5
────────────────────────────────────
Data Analysis + Normalisation + Pivot Tables using the Titanic dataset.

Pipeline:
  1. Load & clean data
  2. Handle missing values
  3. Feature engineering (SexCode, IsChild)
  4. Min-Max & Z-score normalisation on Age
  5. Group-by analysis (Pclass, SexCode)
  6. Pivot tables
  7. Export results

Run:
    python main.py

Dataset:
    Place titanic.csv inside the datasets/ folder.
    Download: https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
"""

import os
import pandas as pd

from preprocessing import (
    fill_missing_age,
    fill_missing_embarked,
    add_sex_code,
    add_child_adult_column,
    min_max_normalise,
    zscore_normalise,
    group_by_pclass,
    group_by_sex_code,
    pivot_pclass_sexcode,
    pivot_survival_by_child,
)
from visualization import (
    section_header,
    print_dataframe,
    print_series,
    print_normalisation_preview,
    print_pivot,
    print_summary_stats,
)

# ── Paths ──────────────────────────────────────────────────────────────────────
BASE_DIR     = os.path.dirname(__file__)
DATASET_PATH = os.path.join(BASE_DIR, "datasets", "titanic.csv")
OUTPUT_DIR   = os.path.join(BASE_DIR, "output")


def load_data() -> pd.DataFrame:
    """Load the raw Titanic CSV."""
    if not os.path.exists(DATASET_PATH):
        raise FileNotFoundError(
            f"Dataset not found: {DATASET_PATH}\n"
            "Download: https://raw.githubusercontent.com/datasciencedojo/"
            "datasets/master/titanic.csv"
        )
    df = pd.read_csv(DATASET_PATH)
    print(f"  ✅  Loaded {len(df)} rows × {len(df.columns)} columns")
    return df


def export_results(df: pd.DataFrame) -> None:
    """Export the fully preprocessed DataFrame to CSV."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_path = os.path.join(OUTPUT_DIR, "titanic_processed.csv")
    df.to_csv(out_path, index=False)
    print(f"  ✅  Exported processed data → {out_path}")


def main() -> None:
    print("\n" + "=" * 62)
    print("  📈  ECRIO_BMS — Normalisation & Pivot Table Analysis")
    print("=" * 62)

    # ── 1. Load ────────────────────────────────────────────────────────────────
    section_header("Loading Dataset")
    df = load_data()

    # ── 2. Handle missing values ──────────────────────────────────────────────
    section_header("Handling Missing Values")
    df = fill_missing_age(df)
    df = fill_missing_embarked(df)
    print(f"  Remaining nulls:\n{df.isnull().sum()[df.isnull().sum() > 0]}")

    # ── 3. Feature engineering ────────────────────────────────────────────────
    section_header("Feature Engineering")
    df = add_sex_code(df)
    df = add_child_adult_column(df)
    print(f"  SexCode distribution:\n{df['SexCode'].value_counts().to_string()}")
    print(f"\n  IsChild distribution:\n{df['IsChild'].value_counts().to_string()}")

    # ── 4. Group by Pclass ────────────────────────────────────────────────────
    pclass_stats = group_by_pclass(df)
    print_dataframe(pclass_stats, "Group By Pclass — Avg Age & Survival Rate")

    # ── 5. Normalisation ──────────────────────────────────────────────────────
    section_header("Applying Normalisation to 'Age'")
    df = min_max_normalise(df, "Age")
    df = zscore_normalise(df, "Age")
    print_normalisation_preview(df, "Age")

    # ── 6. Summary stats after normalisation ──────────────────────────────────
    print_summary_stats(df, "Age_MinMax")
    print_summary_stats(df, "Age_ZScore")

    # ── 7. Group by SexCode ───────────────────────────────────────────────────
    sex_stats = group_by_sex_code(df)
    print_dataframe(sex_stats, "Group By SexCode — Survivor Count")

    # ── 8. Pivot: Pclass × SexCode ────────────────────────────────────────────
    pivot1 = pivot_pclass_sexcode(df)
    print_pivot(pivot1, "Pivot Table — Avg Survival Rate by Pclass × SexCode")
    print("  SexCode: 0 = Female, 1 = Male")

    # ── 9. Pivot: Pclass × IsChild ────────────────────────────────────────────
    pivot2 = pivot_survival_by_child(df)
    print_pivot(pivot2, "Pivot Table — Avg Survival Rate by Pclass × Age Group")

    # ── 10. Export ────────────────────────────────────────────────────────────
    section_header("Exporting Processed Dataset")
    export_results(df)

    print(f"\n{'=' * 62}")
    print("  ✅  Mini Project 5 complete!")
    print(f"{'=' * 62}\n")


if __name__ == "__main__":
    main()

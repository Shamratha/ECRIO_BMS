"""
main.py — ECRIO_BMS Mini Project 3
────────────────────────────────────
Titanic Dataset Analysis using Pandas.
Runs a full analysis pipeline and exports a cleaned CSV.

Run:
    python main.py

Dataset:
    Place titanic.csv inside the datasets/ folder.
    Download: https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
"""

import os
from analysis import (
    load_dataset,
    show_first_rows,
    passengers_by_class_and_gender,
    female_survival_percentage,
    survival_rate_by_gender,
    median_age_by_gender,
    avg_age_survivors_vs_not,
    passengers_above_age,
    add_age_group,
    survivors_first_class,
    average_fare,
    clean_dataset,
    export_cleaned,
)

# ── Paths ──────────────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(__file__)
DATASET_PATH = os.path.join(BASE_DIR, "datasets", "titanic.csv")
OUTPUT_PATH  = os.path.join(BASE_DIR, "output", "cleaned_titanic.csv")

DIVIDER = "  " + "─" * 55


def section(title: str) -> None:
    """Print a section header."""
    print(f"\n{DIVIDER}")
    print(f"  📌  {title}")
    print(DIVIDER)


def main() -> None:
    print("\n" + "=" * 60)
    print("   🚢  ECRIO_BMS — Titanic Dataset Analysis")
    print("=" * 60)

    # ── 1. Load ────────────────────────────────────────────────────────────────
    section("Loading Dataset")
    df = load_dataset(DATASET_PATH)

    # ── 2. Preview ────────────────────────────────────────────────────────────
    section("First 5 Rows")
    show_first_rows(df, 5)

    # ── 3. Passengers by class and gender ─────────────────────────────────────
    section("Passenger Count by Class & Gender")
    counts = passengers_by_class_and_gender(df)
    print(f"\n{counts.to_string()}")

    # ── 4. Female survival percentage ─────────────────────────────────────────
    section("Female Survival Percentage")
    pct = female_survival_percentage(df)
    print(f"\n  Female passengers who survived: {pct}%")

    # ── 5. Survival rate by gender ────────────────────────────────────────────
    section("Survival Rate by Gender")
    rates = survival_rate_by_gender(df)
    for gender, rate in rates.items():
        print(f"  {gender.capitalize():<8} : {rate * 100:.1f}%")

    # ── 6. Median age by gender ───────────────────────────────────────────────
    section("Median Age by Gender")
    medians = median_age_by_gender(df)
    for gender, age in medians.items():
        print(f"  {gender.capitalize():<8} : {age} years")

    # ── 7. Average age: survivors vs non-survivors ────────────────────────────
    section("Average Age — Survivors vs Non-Survivors")
    avg_ages = avg_age_survivors_vs_not(df)
    for group, age in avg_ages.items():
        print(f"  {group:<15} : {age} years")

    # ── 8. Passengers above age 40 ────────────────────────────────────────────
    section("Passengers Above Age 40")
    older = passengers_above_age(df, 40)
    print(f"\n  Found {len(older)} passengers older than 40.")
    print(older[["Name", "Age", "Sex", "Pclass", "Survived"]].head(5).to_string(index=False))

    # ── 9. Age groups ─────────────────────────────────────────────────────────
    section("Age Group Distribution (Child / Adult / Senior)")
    df_grouped = add_age_group(df)
    group_counts = df_grouped["AgeGroup"].value_counts().sort_index()
    for grp, cnt in group_counts.items():
        print(f"  {grp:<8} : {cnt} passengers")

    # ── 10. First-class survivors ─────────────────────────────────────────────
    section("First-Class Survivors")
    fc_survivors = survivors_first_class(df)
    print(f"\n  {len(fc_survivors)} first-class passengers survived.")
    print(fc_survivors[["Name", "Age", "Sex", "Fare"]].head(5).to_string(index=False))

    # ── 11. Average fare ──────────────────────────────────────────────────────
    section("Average Ticket Fare")
    fare = average_fare(df)
    print(f"\n  Average fare across all passengers: £{fare}")

    # ── 12. Export cleaned dataset ────────────────────────────────────────────
    section("Cleaning & Exporting Dataset")
    df_clean = clean_dataset(df)
    print(f"  Rows after cleaning : {len(df_clean)}")
    print(f"  Columns             : {list(df_clean.columns)}")
    export_cleaned(df_clean, OUTPUT_PATH)

    print(f"\n{'=' * 60}")
    print("  ✅  Analysis complete!")
    print(f"{'=' * 60}\n")


if __name__ == "__main__":
    main()

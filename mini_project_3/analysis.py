"""
analysis.py — ECRIO_BMS Mini Project 3
────────────────────────────────────────
All Titanic dataset analysis functions.
Each function is self-contained, accepts a DataFrame, and returns results.
"""

import pandas as pd
import os


# ──────────────────────────────────────────────────────────────────────────────
# Data Loading
# ──────────────────────────────────────────────────────────────────────────────

def load_dataset(filepath: str) -> pd.DataFrame:
    """
    Load the Titanic CSV dataset.

    Args:
        filepath: Path to titanic.csv

    Returns:
        pd.DataFrame with raw data.

    Raises:
        FileNotFoundError: If the CSV file does not exist.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(
            f"Dataset not found at: {filepath}\n"
            "Download from: https://raw.githubusercontent.com/datasciencedojo/"
            "datasets/master/titanic.csv"
        )
    df = pd.read_csv(filepath)
    print(f"  ✅  Dataset loaded — {len(df)} rows, {len(df.columns)} columns")
    return df


# ──────────────────────────────────────────────────────────────────────────────
# Exploration
# ──────────────────────────────────────────────────────────────────────────────

def show_first_rows(df: pd.DataFrame, n: int = 5) -> None:
    """Display the first n rows of the dataset."""
    print(f"\n  📋  First {n} rows:\n")
    print(df.head(n).to_string(index=False))


def passengers_by_class_and_gender(df: pd.DataFrame) -> pd.DataFrame:
    """
    Count male and female passengers in each passenger class.

    Returns:
        A pivot table: rows = Pclass, columns = Sex, values = count.
    """
    result = df.groupby(["Pclass", "Sex"])["PassengerId"].count().unstack(fill_value=0)
    result.columns.name = None
    result.index.name = "Pclass"
    return result


# ──────────────────────────────────────────────────────────────────────────────
# Survival Analysis
# ──────────────────────────────────────────────────────────────────────────────

def female_survival_percentage(df: pd.DataFrame) -> float:
    """Return the percentage of female passengers who survived."""
    females = df[df["Sex"] == "female"]
    if len(females) == 0:
        return 0.0
    return round((females["Survived"].sum() / len(females)) * 100, 2)


def survival_rate_by_gender(df: pd.DataFrame) -> pd.Series:
    """Return survival rate (0–1) grouped by gender."""
    return df.groupby("Sex")["Survived"].mean().round(4)


def survivors_first_class(df: pd.DataFrame) -> pd.DataFrame:
    """Return all first-class survivors."""
    return df[(df["Pclass"] == 1) & (df["Survived"] == 1)]


# ──────────────────────────────────────────────────────────────────────────────
# Age Analysis
# ──────────────────────────────────────────────────────────────────────────────

def median_age_by_gender(df: pd.DataFrame) -> pd.Series:
    """Return median age for males and females (NaN excluded)."""
    return df.groupby("Sex")["Age"].median().round(1)


def avg_age_survivors_vs_not(df: pd.DataFrame) -> pd.Series:
    """Return average age of survivors vs non-survivors."""
    return df.groupby("Survived")["Age"].mean().round(2).rename(
        index={0: "Non-Survivor", 1: "Survivor"}
    )


def passengers_above_age(df: pd.DataFrame, age: int = 40) -> pd.DataFrame:
    """Filter passengers older than the given age."""
    return df[df["Age"] > age]


def add_age_group(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add an 'AgeGroup' column:
        Child  : Age < 18
        Adult  : 18 <= Age < 60
        Senior : Age >= 60
    Missing ages are filled with the column median before binning.
    """
    df = df.copy()
    df["Age"] = df["Age"].fillna(df["Age"].median())
    bins = [0, 17, 59, 120]
    labels = ["Child", "Adult", "Senior"]
    df["AgeGroup"] = pd.cut(df["Age"], bins=bins, labels=labels)
    return df


# ──────────────────────────────────────────────────────────────────────────────
# Fare Analysis
# ──────────────────────────────────────────────────────────────────────────────

def average_fare(df: pd.DataFrame) -> float:
    """Return the average ticket fare across all passengers."""
    return round(df["Fare"].mean(), 2)


# ──────────────────────────────────────────────────────────────────────────────
# Data Cleaning & Export
# ──────────────────────────────────────────────────────────────────────────────

def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply basic cleaning steps:
      1. Fill missing Age with median.
      2. Fill missing Embarked with mode.
      3. Drop Cabin column (too many NaNs).
      4. Add AgeGroup column.
      5. Drop remaining NaN rows.

    Returns:
        Cleaned DataFrame.
    """
    df = df.copy()

    # Fill Age with median
    age_median = df["Age"].median()
    df["Age"] = df["Age"].fillna(age_median)

    # Fill Embarked with mode
    embarked_mode = df["Embarked"].mode()[0]
    df["Embarked"] = df["Embarked"].fillna(embarked_mode)

    # Drop Cabin (77% missing)
    if "Cabin" in df.columns:
        df.drop(columns=["Cabin"], inplace=True)

    # Add AgeGroup
    bins = [0, 17, 59, 120]
    labels = ["Child", "Adult", "Senior"]
    df["AgeGroup"] = pd.cut(df["Age"], bins=bins, labels=labels)

    # Drop any remaining NaN rows
    df.dropna(inplace=True)

    return df


def export_cleaned(df: pd.DataFrame, output_path: str) -> None:
    """Export the cleaned DataFrame to a CSV file."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"  ✅  Cleaned dataset exported → {output_path}")

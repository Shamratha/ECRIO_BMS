"""
preprocessing.py — ECRIO_BMS Mini Project 5
─────────────────────────────────────────────
All data preprocessing and normalisation functions:
  • Missing value handling
  • Min-Max normalisation
  • Z-score normalisation
  • SexCode encoding
  • Child/Adult column
  • Groupby aggregations
  • Pivot tables
"""

import pandas as pd
import numpy as np


# ──────────────────────────────────────────────────────────────────────────────
# Missing Value Handling
# ──────────────────────────────────────────────────────────────────────────────

def fill_missing_age(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fill missing Age values with the column mean.
    This is the most common strategy for continuous numerical features.
    """
    df = df.copy()
    age_mean = df["Age"].mean()
    missing_count = df["Age"].isna().sum()
    df["Age"] = df["Age"].fillna(age_mean)
    print(f"  Filled {missing_count} missing Age values with mean: {age_mean:.2f}")
    return df


def fill_missing_embarked(df: pd.DataFrame) -> pd.DataFrame:
    """Fill missing Embarked values with the mode (most frequent port)."""
    df = df.copy()
    mode_val = df["Embarked"].mode()[0]
    df["Embarked"] = df["Embarked"].fillna(mode_val)
    return df


# ──────────────────────────────────────────────────────────────────────────────
# Feature Engineering
# ──────────────────────────────────────────────────────────────────────────────

def add_sex_code(df: pd.DataFrame) -> pd.DataFrame:
    """
    Encode Sex as a numeric column:
        female → 0
        male   → 1
    Machine learning models require numeric input, so this is
    a common preprocessing step.
    """
    df = df.copy()
    df["SexCode"] = df["Sex"].map({"female": 0, "male": 1})
    return df


def add_child_adult_column(df: pd.DataFrame, age_threshold: int = 18) -> pd.DataFrame:
    """
    Add a 'IsChild' boolean column:
        True  → Age < age_threshold (Child)
        False → Age >= age_threshold (Adult)
    """
    df = df.copy()
    df["IsChild"] = df["Age"] < age_threshold
    return df


# ──────────────────────────────────────────────────────────────────────────────
# Normalisation
# ──────────────────────────────────────────────────────────────────────────────

def min_max_normalise(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Apply Min-Max normalisation to a column.

    Formula:  X_norm = (X - X_min) / (X_max - X_min)

    Result range: [0, 1]
    New column name: <column>_MinMax
    """
    df = df.copy()
    col_min = df[column].min()
    col_max = df[column].max()

    if col_max == col_min:
        df[f"{column}_MinMax"] = 0.0    # avoid division by zero
    else:
        df[f"{column}_MinMax"] = (df[column] - col_min) / (col_max - col_min)

    df[f"{column}_MinMax"] = df[f"{column}_MinMax"].round(6)
    print(f"  Min-Max normalised '{column}' → '{column}_MinMax'  "
          f"(min={col_min:.2f}, max={col_max:.2f})")
    return df


def zscore_normalise(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Apply Z-score (standard score) normalisation to a column.

    Formula:  Z = (X - μ) / σ

    Result: mean ≈ 0, std ≈ 1
    New column name: <column>_ZScore
    """
    df = df.copy()
    mean = df[column].mean()
    std  = df[column].std()

    if std == 0:
        df[f"{column}_ZScore"] = 0.0
    else:
        df[f"{column}_ZScore"] = (df[column] - mean) / std

    df[f"{column}_ZScore"] = df[f"{column}_ZScore"].round(6)
    print(f"  Z-score normalised '{column}' → '{column}_ZScore'  "
          f"(μ={mean:.2f}, σ={std:.2f})")
    return df


# ──────────────────────────────────────────────────────────────────────────────
# Group-by Analysis
# ──────────────────────────────────────────────────────────────────────────────

def group_by_pclass(df: pd.DataFrame) -> pd.DataFrame:
    """
    Group by Pclass and compute:
      • Average Age
      • Survival Rate (mean of Survived)
      • Passenger Count
    """
    return (
        df.groupby("Pclass")
        .agg(
            Avg_Age=("Age", "mean"),
            Survival_Rate=("Survived", "mean"),
            Passenger_Count=("PassengerId", "count"),
        )
        .round(4)
    )


def group_by_sex_code(df: pd.DataFrame) -> pd.DataFrame:
    """
    Group by SexCode and count survivors.
    SexCode must already exist (call add_sex_code first).
    """
    return (
        df.groupby("SexCode")["Survived"]
        .agg(["sum", "count", "mean"])
        .rename(columns={"sum": "Survivors", "count": "Total", "mean": "Survival_Rate"})
        .round(4)
    )


# ──────────────────────────────────────────────────────────────────────────────
# Pivot Tables
# ──────────────────────────────────────────────────────────────────────────────

def pivot_pclass_sexcode(df: pd.DataFrame) -> pd.DataFrame:
    """
    Pivot table: rows = Pclass, columns = SexCode, values = average Survived.
    Shows survival rate for each class × gender combination.
    """
    return pd.pivot_table(
        df,
        index="Pclass",
        columns="SexCode",
        values="Survived",
        aggfunc="mean",
    ).round(4)


def pivot_survival_by_child(df: pd.DataFrame) -> pd.DataFrame:
    """
    Pivot table: rows = Pclass, columns = IsChild, values = average Survived.
    Shows how survival differs for children vs adults per class.
    """
    return pd.pivot_table(
        df,
        index="Pclass",
        columns="IsChild",
        values="Survived",
        aggfunc="mean",
    ).round(4).rename(columns={False: "Adult", True: "Child"})

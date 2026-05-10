"""
visualization.py — ECRIO_BMS Mini Project 5
─────────────────────────────────────────────
Pretty terminal printing helpers for DataFrames and analysis results.
No external plotting libraries required — output is text-based
and suitable for beginners who haven't set up matplotlib yet.
"""

import pandas as pd


DIVIDER = "  " + "─" * 58


def section_header(title: str) -> None:
    """Print a clearly visible section title."""
    print(f"\n{DIVIDER}")
    print(f"  📊  {title}")
    print(DIVIDER)


def print_dataframe(df: pd.DataFrame, title: str = "", max_rows: int = 10) -> None:
    """Print a DataFrame with an optional title and row limit."""
    if title:
        section_header(title)
    print()
    print(df.head(max_rows).to_string())
    if len(df) > max_rows:
        print(f"  ... ({len(df) - max_rows} more rows not shown)")
    print()


def print_series(s: pd.Series, title: str = "") -> None:
    """Print a Series with an optional title."""
    if title:
        section_header(title)
    print()
    print(s.to_string())
    print()


def print_normalisation_preview(df: pd.DataFrame, original: str) -> None:
    """Show a side-by-side preview of original vs normalised columns."""
    section_header(f"Normalisation Preview — '{original}'")
    cols = [c for c in [original, f"{original}_MinMax", f"{original}_ZScore"]
            if c in df.columns]
    print()
    print(df[cols].head(8).to_string(index=False))
    print()


def print_pivot(pivot: pd.DataFrame, title: str) -> None:
    """Print a pivot table with a descriptive title."""
    section_header(title)
    print()
    print(pivot.to_string())
    print()


def print_summary_stats(df: pd.DataFrame, column: str) -> None:
    """Print basic descriptive statistics for a column."""
    section_header(f"Summary Statistics — '{column}'")
    stats = df[column].describe().round(4)
    for stat, val in stats.items():
        print(f"  {stat:<10} : {val}")
    print()

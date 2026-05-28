"""Reusable summary-statistics helpers for the public health notebook.

These functions mirror notebook helpers and are provided for future script
separation. The notebook remains the main report for now.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats


def format_number(value):
    """Format numeric table values with one decimal place."""
    if pd.isna(value):
        return ""
    return f"{value:.1f}"


def format_percentage(value):
    """Format percentage table values with one decimal place."""
    if pd.isna(value):
        return ""
    return f"{value:.1f}"


def format_p_value(p_value):
    """Format p-values for report tables and figure annotations."""
    if pd.isna(p_value):
        return ""
    if p_value < 0.001:
        return "<0.001"
    return f"{p_value:.3f}"


def continuous_stats(series, stat_names, not_applicable_marker="--"):
    """Calculate formatted continuous summary statistics."""
    numeric_series = pd.to_numeric(series, errors="coerce").dropna()
    if numeric_series.empty:
        return {stat_name: "" for stat_name in stat_names}
    return {
        "Mean": format_number(numeric_series.mean()),
        "SD": format_number(numeric_series.std(ddof=1)),
        "Median": format_number(numeric_series.median()),
        "25th percentile": format_number(numeric_series.quantile(0.25)),
        "75th percentile": format_number(numeric_series.quantile(0.75)),
        "%": not_applicable_marker,
    }


def percentage_stats(series, positive_value, stat_names, not_applicable_marker="--"):
    """Calculate formatted percentage summary statistics."""
    valid_series = series.dropna()
    if valid_series.empty:
        return {stat_name: "" for stat_name in stat_names}
    percent = valid_series.eq(positive_value).mean() * 100
    return {
        "Mean": not_applicable_marker,
        "SD": not_applicable_marker,
        "Median": not_applicable_marker,
        "25th percentile": not_applicable_marker,
        "75th percentile": not_applicable_marker,
        "%": format_percentage(percent),
    }


def mann_whitney_p_value(data, column_name, group_variable="sex_label", group_order=("Male", "Female")):
    """Compare two group distributions using the Mann-Whitney U test."""
    group_values = [
        pd.to_numeric(
            data.loc[data[group_variable].eq(group), column_name],
            errors="coerce",
        ).dropna()
        for group in group_order
    ]
    if any(values.empty for values in group_values):
        return np.nan
    return stats.mannwhitneyu(group_values[0], group_values[1], alternative="two-sided").pvalue


def chi_square_p_value(data, column_name, positive_value, group_variable="sex_label", group_order=("Male", "Female")):
    """Compare two group percentages using a chi-square test."""
    subset = data.loc[data[group_variable].isin(group_order), [group_variable, column_name]].dropna()
    if subset.empty:
        return np.nan
    subset = subset.copy()
    subset["is_positive"] = subset[column_name].eq(positive_value)
    contingency_table = pd.crosstab(subset[group_variable], subset["is_positive"])
    contingency_table = contingency_table.reindex(index=list(group_order), columns=[False, True], fill_value=0)
    if (contingency_table.sum(axis=1) == 0).any() or (contingency_table.sum(axis=0) == 0).any():
        return np.nan
    return stats.chi2_contingency(contingency_table, correction=False).pvalue

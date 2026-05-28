"""Reusable plotting helpers for future notebook refactoring."""

from __future__ import annotations

import numpy as np
import pandas as pd


def p_value_label(format_p_value, p_value):
    """Return a compact p-value label for plot annotations."""
    formatted = format_p_value(p_value)
    return "p = unavailable" if formatted == "" else f"p = {formatted}"


def sex_grouped_values(data, column_name, group_variable="sex_label", group_order=("Male", "Female")):
    """Return numeric values by group for matplotlib boxplots."""
    return [
        pd.to_numeric(
            data.loc[data[group_variable].eq(group), column_name],
            errors="coerce",
        ).dropna()
        for group in group_order
    ]


def style_boxplot(boxplot, colors):
    """Apply simple publication-style formatting to a matplotlib boxplot."""
    for patch, color in zip(boxplot["boxes"], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.75)
        patch.set_edgecolor("#333333")
    for median in boxplot["medians"]:
        median.set_color("#111111")
        median.set_linewidth(1.6)
    for whisker in boxplot["whiskers"]:
        whisker.set_color("#333333")
    for cap in boxplot["caps"]:
        cap.set_color("#333333")


def cutoff_percentage_ci(data, column_name, group, group_variable="sex_label"):
    """Return percent, 95% CI half-width, and n for a binary cutoff indicator."""
    values = data.loc[data[group_variable].eq(group), column_name].dropna()
    n = len(values)
    if n == 0:
        return np.nan, np.nan, 0
    p = values.eq(True).mean()
    se = np.sqrt(p * (1 - p) / n)
    return p * 100, 1.96 * se * 100, n


def save_figure(fig, figure_dir, filename, dpi=300):
    """Save a matplotlib figure to the configured figure directory."""
    figure_dir.mkdir(parents=True, exist_ok=True)
    figure_path = figure_dir / filename
    fig.savefig(figure_path, dpi=dpi, bbox_inches="tight", facecolor="white")
    return figure_path

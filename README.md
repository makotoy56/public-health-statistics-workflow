# Public Health Statistics Workflow

## Table of Contents

- [Repository Purpose](#repository-purpose)
- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Folder Structure](#folder-structure)
- [Technologies Used](#technologies-used)
- [Reproducibility](#reproducibility)
- [Set Up a Virtual Environment](#set-up-a-virtual-environment)
- [Install Requirements](#install-requirements)
- [Run the Notebook](#run-the-notebook)
- [HTML Export](#html-export)
- [Outputs Generated](#outputs-generated)
- [Project Status](#project-status)
- [Notes on Data](#notes-on-data)

## Repository Purpose

This repository demonstrates a reproducible public health statistics workflow using notebook-based reporting. It highlights statistical testing, exploratory visualization, and a styled Excel export workflow suitable for portfolio review and educational use.

## Project Overview

This project generates a public health summary statistics table and exploratory figures from a local raw dataset. The Jupyter notebook is the main report and produces a styled Excel workbook plus publication-style PNG figures.

The analysis includes:
- workbook loading and sheet inspection
- column mapping from the raw workbook to analysis names
- data cleaning and derived cutoff indicators
- overall and sex-stratified summary statistics
- statistical tests comparing Male and Female groups
- exploratory visualizations saved as PNG files

Raw data files are excluded from Git. Place the local raw workbook under `data/` before running the notebook.

## Key Features

- Reproducible notebook workflow with project-relative paths
- Overall and sex-stratified public health summary statistics
- Mann-Whitney U tests for continuous variables
- Chi-square tests for categorical and binary cutoff indicators
- Matplotlib-only exploratory visualizations
- Styled Excel export for reporting
- Preliminary `src/` modules prepared for future notebook refactoring
- Preliminary Quarto report template for future reporting work

## Folder Structure

```text
public-health-statistics-workflow/
├── data/                         # Raw data files, excluded from Git
├── notebooks/
│   └── generate_public_health_summary_table.ipynb
├── outputs/                      # Generated files, excluded from Git
│   ├── figures/
│   ├── reports/
│   └── public_health_summary_table.xlsx
├── reports/
│   └── public_health_summary_report.qmd
├── src/                          # Reusable helper modules for future refactoring
│   ├── excel_export.py
│   ├── plotting.py
│   └── summary_stats.py
├── README.md
└── requirements.txt
```

## Technologies Used

- Python
- pandas
- scipy
- matplotlib
- openpyxl
- Jupyter Notebook
- Quarto

## Reproducibility

The workflow is designed to be rerun from a clean clone after creating a virtual environment, installing `requirements.txt`, and placing the local raw workbook under `data/`. Analysis parameters, output paths, figure paths, group definitions, and export settings are defined near the top of the notebook.

Generated outputs are intentionally excluded from Git. Recreate them by running the notebook.

## Set Up a Virtual Environment

Create the virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

## Install Requirements

```bash
pip install -r requirements.txt
```

Register the virtual environment as a Jupyter kernel:

```bash
.venv/bin/python -m ipykernel install --user --name public-health-statistics --display-name "public-health-statistics"
```

## Run the Notebook

Launch Jupyter:

```bash
.venv/bin/jupyter notebook
```

Open and run:

```text
notebooks/generate_public_health_summary_table.ipynb
```

The notebook expects the raw workbook at:

```text
data/public_health_statistics_dataset.xlsx
```

## HTML Export

Export the notebook to HTML:

```bash
.venv/bin/jupyter nbconvert --to html notebooks/generate_public_health_summary_table.ipynb --output-dir outputs/reports
```

## Outputs Generated

Running the notebook generates:

```text
outputs/public_health_summary_table.xlsx
outputs/figures/fig1_bmi_by_sex.png
outputs/figures/fig2_blood_glucose_by_sex.png
outputs/figures/fig3_age_group_percentages.png
outputs/figures/fig4_cutoff_prevalence_by_sex.png
```

Optional HTML export writes to:

```text
outputs/reports/
```

## Project Status

Current status: active educational and portfolio project.

Future plans:
- regression modeling
- Quarto reporting
- expanded reusable modules

## Notes on Data

Raw data are intentionally excluded from Git. Keep raw workbooks in `data/` locally and avoid committing identifiable, restricted, or non-public raw data.

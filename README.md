# Public Health Statistics

## Project Overview

This project generates a public health summary statistics table and exploratory figures from a local raw dataset. The notebook is the main report and produces a styled Excel workbook plus publication-style PNG figures.

The analysis includes:
- workbook loading and sheet inspection
- column mapping from the raw workbook to analysis names
- data cleaning and derived cutoff indicators
- overall and sex-stratified summary statistics
- statistical tests comparing Male and Female groups
- exploratory visualizations saved as PNG files

Raw data files are excluded from Git. Place the local raw workbook under `data/` before running the notebook.

## Folder Structure

```text
public-health-statistics/
├── data/                         # Raw data files, excluded from Git
├── notebooks/
│   └── generate_public_health_summary_table.ipynb
├── outputs/
│   ├── figures/                  # Generated PNG figures
│   ├── reports/                  # Optional exported HTML reports
│   └── public_health_summary_table.xlsx
├── reports/
│   └── public_health_summary_report.qmd
├── scripts/
├── src/                          # Reusable helper modules for future refactoring
│   ├── excel_export.py
│   ├── plotting.py
│   └── summary_stats.py
├── README.md
└── requirements.txt
```

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

## Notes on Data

Raw data are intentionally excluded from Git. Keep raw workbooks in `data/` locally and avoid committing identifiable, restricted, or non-public raw data.

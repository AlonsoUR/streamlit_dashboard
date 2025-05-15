# 📊 Streamlit Data Viewer App

A lightweight Streamlit web application that lets you upload a CSV file, explore its contents, clean missing values, and visualize the data using interactive charts.

---

## 🚀 Features

- 📁 Upload a single CSV file
- 📋 View raw data in a scrollable table
- 🧼 Handle missing values per column:
  - Drop rows with NAs
  - Fill NAs with custom values
- 📊 Interactive visualizations:
  - Scatter Plot
  - Histogram
  - Bar Chart
- 🎛️ Dynamic column selection for plotting

---

## 🖼️ App Overview

1. Upload your CSV file via the sidebar.
2. Preview the raw data.
3. Optionally clean missing values using the NA Handler.
4. Choose two columns to visualize.
5. Select a chart type (scatter, histogram, or bar).
6. View the interactive chart rendered with Plotly.

---

## 📦 Requirements

- Python 3.8+
- Streamlit
- Pandas
- Plotly

Install them via pip:

```bash
pip install streamlit pandas plotly
```
## 🏁 Running the App

```bash
streamlit run app.py
```
## 📝 Notes

- If no CSV is uploaded, a default sample dataset will be used(vehicles_us.csv).
- Designed for quick inspection and lightweight analysis of tabular data.
- Page may freeze if columns with too many categories are choosen for the graphs legend

## Author
Made by AlonsoUR

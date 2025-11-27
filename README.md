# Iran Microeconomy Dashboard

A Streamlit dashboard for exploring Iran's microeconomic indicators using a hierarchical schema.

---

## Project Structure
```text
Iran_microeconomy_dash/
├─ GDP-dash.py
├─ IOD_Schema_Total.csv
├─ requirements.txt
└─ README.md
```

## Features
- Filter data by indicator (`sub0`)
- Automatic hierarchical filtering (`sub1` → `sub7`)
- Cleaned numeric values (thousands separators supported)
- Line chart with correct numeric axes
- Download filtered results as CSV


After launching, Streamlit will open automatically at:

[http://localhost:8501](https://aliranjipour-iran-microeconomics-data-dash.streamlit.app/)

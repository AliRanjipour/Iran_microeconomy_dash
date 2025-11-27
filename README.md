# Iran Microeconomy Dashboard

A Streamlit dashboard for exploring Iran's microeconomic indicators using a hierarchical schema (`sub0`–`sub7`).

---

## Project Structure
```text
Iran_microeconomy_dash/
├─ GDP-dash.py
├─ IOD_Schema_Total.csv
├─ requirements.txt
└─ README.md
'''
---

## Features

- Filter data by indicator (`sub0`)
- Automatic hierarchical filtering (`sub1` → `sub7`)
- Cleaned numeric values (thousands separators supported)
- Line chart with correct numeric axes
- Download filtered results as CSV

---

## Installation

Clone the repository:

```bash
git clone https://github.com/AliRanjipour/Iran_microeconomy_dash
cd Iran_microeconomy_dash

Install dependencies:
pip install -r requirements.txt

▶️ Run the Dashboard
streamlit run GDP-dash.py

http://localhost:8501

Data Details

The dataset includes:

sub0–sub7 (hierarchy)

Indicator

Source

Time

Value

Unit

Details

Value is parsed as numeric using comma clean-up or thousands=','.

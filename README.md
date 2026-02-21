\# 📈 Forecast Analytics Dashboard



An end-to-end analytics system that implements an ETL pipeline, data quality validation,

adaptive forecasting logic, and an interactive dashboard.



\## 🚀 Features

\- Upload CSV / Excel / JSON files

\- ETL pipeline with logging \& data quality checks

\- Automatic aggregation (daily / monthly)

\- Adaptive forecasting strategy

\- Uncertainty visualization

\- Interactive charts with hover tooltips

\- Professional tab-based UI



\## 🧠 Modeling Logic

\- Uses Linear Regression when data supports it

\- Falls back to Moving Average for small or noisy datasets

\- Avoids misleading trend extrapolation



\## 🛠 Tech Stack

\- Python

\- Streamlit

\- Pandas / NumPy

\- Scikit-learn

\- Plotly



\## ▶️ Run Locally

```bash

pip install -r requirements.txt

streamlit run app.py


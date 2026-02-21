# 📊 Universal Analytics Dashboard

A lightweight, extensible **data analytics dashboard** built using **Streamlit**, designed to help users quickly **upload datasets, explore data, visualize insights, and understand key trends** — all without writing code.

---

## 🚀 Features

### ✅ Current Features
- 📁 **CSV Upload**
- 🔍 **Data Preview & Profiling**
  - Row & column count
  - Missing value detection
  - Column data types
- 📈 **Interactive Visualizations**
  - Bar chart
  - Line chart
  - Box plot
  - Histogram
- 💡 **Executive Insights**
  - Automatic human-readable summary
  - Basic statistics and categorical dominance
- 🧩 **Modular Architecture**
  - Clean separation between UI (`app.py`) and logic (`intelligence.py`)
- 🧪 **Beginner-friendly & stable**
  - No broken imports
  - No experimental dependencies

---

## 🗂 Project Structure
Universal-Analysis/
│
├── app.py # Main Streamlit application
├── intelligence.py # Insights & summary logic
├── users.json # Placeholder for future authentication
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── venv/ # (Optional) Virtual environment
---

## 🖥️ Tech Stack

- **Python 3.9+**
- **Streamlit** – Web application framework
- **Pandas** – Data manipulation
- **Plotly** – Interactive visualizations

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/Universal-Analysis.git
cd Universal-Analysis
---

## 🖥️ Tech Stack

- **Python 3.9+**
- **Streamlit** – Web application framework
- **Pandas** – Data manipulation
- **Plotly** – Interactive visualizations

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/Universal-Analysis.git
cd Universal-Analysis

2️⃣ (Optional but Recommended) Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # macOS/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
streamlit run app.py

The app will be available at:

http://localhost:8501

📂 How to Use

Upload a CSV file using the sidebar.

Navigate through tabs:

🔍 Data Preview – Inspect dataset structure.

📈 Visualization – Create interactive charts.

💡 Insights – Read auto-generated summaries.

Change axes and chart types dynamically.

🧠 Insights Logic (Current)

The dashboard automatically generates:

Dataset size summary

Missing value detection

Mean of first numeric column

Most frequent value in first categorical column

These insights are intentionally simple and explainable.

🔒 Authentication (Planned)

Role-based authentication (Admin / Analyst / Viewer) is planned but not yet activated to ensure stability.

The users.json file is included as a placeholder for the next development phase.

🛣 Roadmap
🔜 Upcoming Enhancements

🔐 Role-based authentication (login system)

🗃 Multi-dataset support

💬 Natural language Q&A over data

📄 Export reports to PDF / PPT

🧠 Smarter insight narration

⚠ Data quality warnings

🎨 Improved UI themes

🧑‍🎓 Ideal For

Data Analytics students

Academic projects

Mini / Major projects

Streamlit learning

Rapid analytics demos

🤝 Contribution

Contributions are welcome:

Fork the repository

Create a feature branch

Commit changes

Open a pull request

📜 License

This project is open-source and intended for educational use.

📬 Support

If you face issues or want enhancements, feel free to raise an issue or discuss improvements.

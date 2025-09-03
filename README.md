# 📊 One-Click Dataset Visualizer

A **Streamlit-based** app that enables anyone (even non-technical users) to quickly upload datasets (CSV/XLSX) and interactively explore them — no coding required!  
It automatically generates **summaries**, **charts**, **insights**, **correlation heatmaps**, and allows **one-click export to PDF reports**.  

Works fully **offline** once dependencies are installed.

---

## 🚀 Features

- **📂 Easy Upload** – Drag & drop CSV or Excel files.
- **📑 Dataset Summary** – Automatically compute column stats, data types, and missing values.
- **📊 Interactive Visualizations** – Plotly-powered charts (bar, line, scatter, histogram, pie, box, heatmap).
- **💡 Automated Insights** – AI-style dataset observations.
- **📈 Correlation Analysis** – Detect numeric relationships via heatmaps.
- **📥 One-Click Report Export** – Generate styled PDF dataset reports (summary + insights + charts).
- **🌍 Offline Mode** – No internet required after setup.

---

### 🛠️ Quickstart

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Hassan-07-code/dataset_visualizer.git
   cd one_click_dataset_visualizer

2. **Install dependices**

pip install -r requirements.txt

### Run App

streamlit run app.py

### one_click_dataset_visualizer/

│
├── app.py                     # Main Streamlit entry point
├── assets/                    # Static assets (logo, images, etc.)
│
├── modules/                   # Core processing functions
│   ├── data_loader.py         # Handles dataset upload
│   ├── data_summary.py        # Generates summary/statistics
│   ├── visualization.py       # Creates Plotly charts
│   ├── export_report.py       # Builds styled PDF reports
│
├── pages/                     # Streamlit multi-page UI
│   ├── 1_🏠_Home.py           # Upload datasets
│   ├── 2_📑_Data_Summary.py   # Dataset overview
│   ├── 3_📊_Charts.py         # Interactive visualizations
│   ├── 4_💡_Insights.py       # Automated insights
│   ├── 5_📤_Export_Report.py  # Export as PDF
│
├── tests/                     # Unit & integration tests
│   ├── test_export_report.py
│   ├── test_visualization.py
│
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation

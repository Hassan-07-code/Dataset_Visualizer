# pages/2_Data_Summary.py
import streamlit as st
from modules.data_summary import generate_data_summary
from modules.data_loader import sample_preview

st.title("📋 Data Summary")

# ----------------------------
# Check dataset availability
# ----------------------------
if "df" not in st.session_state or st.session_state["df"] is None:
    st.info("⚠️ Please upload a dataset in Home first.")
    st.stop()

# ----------------------------
# Generate summary
# ----------------------------
df = st.session_state["df"]
summary = generate_data_summary(df)

# ----------------------------
# Overview
# ----------------------------
st.subheader("🔎 Overview")
shape = summary.get("shape", {})
rows = shape.get("rows", "N/A")
cols = shape.get("columns", "N/A")
st.write(f"**Rows:** {rows} — **Columns:** {cols}")

# ----------------------------
# Columns & Types
# ----------------------------
st.subheader("🧾 Columns & Types")
if "data_types" in summary:
    st.table(summary["data_types"])
else:
    st.write("_No column type info available._")

# ----------------------------
# Missing Values
# ----------------------------
st.subheader("❓ Missing Values")
if "missing_values" in summary:
    st.table(summary["missing_values"])
else:
    st.write("_No missing values info available._")

# ----------------------------
# Sample Data
# ----------------------------
st.subheader("📑 Sample Preview")
try:
    st.dataframe(sample_preview(df, 10))
except Exception:
    st.write("_Sample preview not available._")

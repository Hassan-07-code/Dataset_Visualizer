# pages/2_Data_Summary.py
import streamlit as st
from modules.data_summary import generate_data_summary
from modules.data_loader import sample_preview

st.title("Data Summary")
if 'df' not in st.session_state:
    st.info("Upload a dataset in Home first.")
else:
    df = st.session_state['df']
    summary = generate_data_summary(df)
    st.subheader("Overview")
    st.write(f"Rows: {summary['shape']['rows']} — Columns: {summary['shape']['columns']}")
    st.subheader("Columns & Types")
    st.table(summary['data_types'])
    st.subheader("Missing values")
    st.table(summary['missing_values'])
    st.subheader("Sample")
    st.dataframe(sample_preview(df, 10))

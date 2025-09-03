import streamlit as st
from pathlib import Path
from modules.data_loader import load_data
from modules.utils import fingerprint_df
from modules.data_summary import generate_data_summary
from modules.insights import generate_insights

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Dataset Visualizer",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------ HEADER ------------------
st.markdown(
    """
    <style>
        .main-title { font-size:40px !important; font-weight:800; color:#1f77b4; }
        .subtitle { font-size:18px !important; color:#555; margin-bottom:20px; }
        .upload-box {border:2px dashed #1f77b4; padding:20px; border-radius:10px; background:#f9f9f9;}
        .footer { font-size:14px; color:#777; text-align:center; margin-top:50px; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<p class="main-title">📊 One-Click Dataset Visualizer</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Upload → Explore → Export.</p>', unsafe_allow_html=True)

st.markdown("---")

# ------------------ SESSION PERSISTENCE ------------------
if "df" not in st.session_state:
    st.session_state.df = None
    st.session_state.meta = None
    st.session_state.uploaded_file = None
    st.session_state.fingerprint = None
    st.session_state.dataset_summary = None
    st.session_state.insights = None
    st.session_state.charts_png = {}

# ------------------ FILE UPLOAD ------------------
st.markdown("### 📂 Upload Your Dataset")
with st.container():
    uploaded = st.file_uploader("Upload CSV or Excel file", type=["csv", "xls", "xlsx"], label_visibility="collapsed")

    if uploaded:
        try:
            df, meta = load_data(uploaded)

            # Save only if new file OR first upload
            if st.session_state.df is None or st.session_state.meta['filename'] != meta['filename']:
                st.session_state.df = df
                st.session_state.meta = meta
                st.session_state.uploaded_file = uploaded
                st.session_state.fingerprint = fingerprint_df(df)

                # ✅ NEW: Save summary and insights for export
                st.session_state.dataset_summary = generate_data_summary(df)
                st.session_state.insights = generate_insights(df).get("bullets", [])
                st.session_state.charts_png = {}  # fill later from chart pages

            st.success(f"✅ Loaded **{st.session_state.meta['filename']}** — {st.session_state.meta['rows']} rows × {st.session_state.meta['cols']} columns")

            # Preview
            st.subheader("🔎 Data Preview (first 10 rows)")
            st.dataframe(st.session_state.df.head(10), use_container_width=True)

            # Reset button
            if st.button("🗑️ Clear Dataset"):
                for key in ["df", "meta", "uploaded_file", "fingerprint", "dataset_summary", "insights", "charts_png"]:
                    st.session_state[key] = None
                st.rerun()

        except Exception as e:
            st.error(f"❌ Error loading file: {e}")

    elif st.session_state.df is not None:
        st.success(f"✅ Using previously loaded dataset: **{st.session_state.meta['filename']}** — {st.session_state.meta['rows']} rows × {st.session_state.meta['cols']} columns")
        st.subheader("🔎 Data Preview (first 10 rows)")
        st.dataframe(st.session_state.df.head(10), use_container_width=True)

        if st.button("🗑️ Clear Dataset"):
            for key in ["df", "meta", "uploaded_file", "fingerprint", "dataset_summary", "insights", "charts_png"]:
                st.session_state[key] = None
            st.rerun()

# ------------------ FOOTER ------------------
st.markdown(
    "<div style='text-align: center; font-size: 13px; color: #999; margin-top: 40px;'>"
    "🕶️ Project by <b>Mysterious</b> | The name is <i>Hassan</i> "
    "</div>",
    unsafe_allow_html=True   
)

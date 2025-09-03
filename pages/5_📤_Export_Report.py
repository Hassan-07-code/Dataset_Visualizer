import streamlit as st
import io
from modules.export_html_report import render_html_report, make_download_link_html

st.set_page_config(page_title="Export Report", layout="wide")
st.title("📑 Export Report")

# ----------------------------
# Ensure dataset is available
# ----------------------------
if "df" not in st.session_state or st.session_state.df is None:
    st.warning("⚠️ Please upload a dataset first from the Home page.")
    st.stop()

df = st.session_state["df"]

# ----------------------------
# Load stored items
# ----------------------------
summary = st.session_state.get("dataset_summary", {})
bullets = st.session_state.get("insights", [])
charts_figs = st.session_state.get("charts_figs", {})  # IMPORTANT: store figures instead of PNGs

# ----------------------------
# Preview on screen
# ----------------------------
st.subheader("🔎 Preview")

# Dataset Shape
dataset_shape = summary.get("shape")
if dataset_shape:
    st.markdown(
        f"<div style='background:#EBF5FB;padding:10px;border-radius:6px;'>"
        f"<b>Dataset Shape:</b> <span style='color:#1F618D;'>{dataset_shape['rows']} rows × {dataset_shape['columns']} columns</span>"
        f"</div>",
        unsafe_allow_html=True,
    )
else:
    st.info("Dataset shape not available.")

# Columns
columns_list = summary.get("columns")
if columns_list:
    st.markdown(
        f"<div style='background:#FEF9E7;padding:10px;border-radius:6px;'>"
        f"<b>Columns:</b> <span style='color:#B9770E;'>{', '.join(columns_list)}</span>"
        f"</div>",
        unsafe_allow_html=True,
    )
else:
    st.info("Columns info not available.")

# Insights
if bullets:
    st.markdown("### ✨ Insights")
    for b in bullets:
        st.markdown(f"- ✅ {b}")
else:
    st.write("_No insights generated._")

# Charts Preview
if charts_figs:
    st.markdown("### 📊 Charts (Preview)")
    for name, fig in charts_figs.items():
        st.plotly_chart(fig, use_container_width=True)
else:
    st.write("_No charts available._")

# ----------------------------
# Export button
# ----------------------------
st.markdown("---")
st.subheader("📥 Export")

if st.button("📤 Generate HTML Report"):
    html_report = render_html_report(
        title="Dataset Report",
        summary=summary,
        bullets=bullets,
        charts_figs=charts_figs,
    )

    download_link = make_download_link_html(html_report, "dataset_report.html")
    st.markdown(
        f'<a href="{download_link}" download="dataset_report.html" '
        f'style="background-color:#28B463;color:white;padding:10px 18px;'
        f'font-size:16px;border-radius:6px;text-decoration:none;">⬇️ Download Report (HTML)</a>',
        unsafe_allow_html=True,
    )
st.markdown("For PDF downloading, it will update soon. Stay tuned! 🚀")
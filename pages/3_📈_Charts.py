# pages/3_📊_Charts.py
import streamlit as st
from modules.visualization import generate_chart
import pandas as pd

st.title("📊 Charts")

if "df" not in st.session_state or st.session_state["df"] is None:
    st.info("⚠️ Upload a dataset in Home first.")
else:
    df = st.session_state["df"]
    cols = df.columns.tolist()

    chart_type = st.selectbox(
        "Select Chart Type",
        ["line", "bar", "scatter", "histogram", "pie", "box", "heatmap"]
    )

    x = st.selectbox("X column (if applicable)", [None] + cols, index=0)
    y = None
    if chart_type in ["line", "scatter", "bar"]:
        y = st.selectbox("Y column", [None] + cols, index=1 if len(cols) > 1 else 0)

    if st.button("Generate Chart"):
        try:
            # ✅ generate_chart should return a Plotly figure
            fig, png_bytes = generate_chart(df, chart_type, x=x, y=y)

            # Show chart interactively
            st.plotly_chart(fig, use_container_width=True)

            # ✅ Store the FIGURE (for HTML export)
            st.session_state.setdefault("charts_figs", {})[
                f"{chart_type}_{x}_{y}"
            ] = fig

            # (Optional) still store PNGs if you want PDF fallback
            if png_bytes:
                st.session_state.setdefault("charts_png", {})[
                    f"{chart_type}_{x}_{y}"
                ] = png_bytes

            st.success("✅ Chart generated and saved for export.")

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

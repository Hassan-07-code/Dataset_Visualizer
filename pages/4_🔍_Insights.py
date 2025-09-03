# pages/4_Insights.py
import streamlit as st
from modules.insights import generate_insights

st.title("💡 Insights")

# ----------------------------
# Check dataset availability
# ----------------------------
if "df" not in st.session_state or st.session_state["df"] is None:
    st.info("⚠️ Please upload a dataset in Home first.")
    st.stop()

df = st.session_state["df"]

# ----------------------------
# Generate insights
# ----------------------------
with st.spinner("🔎 Generating insights..."):
    res = generate_insights(df)

if "error" in res:
    st.error(f"❌ {res['error']}")
    st.stop()

# ----------------------------
# Automated Insights (bullets)
# ----------------------------
st.subheader("📌 Key Insights")
bullets = res.get("bullets", [])
if bullets:
    for b in bullets:
        st.markdown(f"- ✅ {b}", unsafe_allow_html=True)
else:
    st.write("_No automated insights generated._")

# ----------------------------
# Numeric Summary
# ----------------------------
st.subheader("📊 Numeric Summary")
summary = res.get("summary")
if summary is not None and not summary.empty:
    st.dataframe(summary)
else:
    st.info("No numeric summary available.")

# ----------------------------
# Correlation Matrix
# ----------------------------
st.subheader("🔗 Correlation Matrix")
corr = res.get("correlation")
if corr is not None and not corr.empty:
    st.dataframe(corr.style.background_gradient(cmap="Blues"))
else:
    st.info("No correlations found.")

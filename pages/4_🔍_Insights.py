# pages/4_Insights.py
import streamlit as st
from modules.insights import generate_insights

st.title("Insights")
if 'df' not in st.session_state:
    st.info("Upload a dataset in Home first.")
else:
    df = st.session_state['df']
    res = generate_insights(df)
    if 'error' in res:
        st.error(res['error'])
    else:
        st.subheader("Automated bullets")
        for b in res['bullets']:
            st.markdown(f"- {b}", unsafe_allow_html=True)
        st.subheader("Numeric summary")
        if not res['summary'].empty:
            st.dataframe(res['summary'])
        else:
            st.write("No numeric summary available.")
        st.subheader("Correlation matrix")
        if not res['correlation'].empty:
            st.dataframe(res['correlation'])
        else:
            st.write("No correlation to show.")

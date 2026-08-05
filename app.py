import streamlit as st

st.set_page_config(
    page_title="InsightFlow AI",
    page_icon="📊",
    layout="wide"
)

st.title("📊 InsightFlow AI")

st.markdown(
    "### AI-Powered Multi-Agent Data Analytics Platform"
)

uploaded_file = st.file_uploader(
    "Upload your CSV dataset",
    type=["csv"]
)

if uploaded_file is None:
    st.info("📂 Upload a CSV file to begin analysis.")
import streamlit as st

from tools.loader import load_data
from tools.overview import show_overview


st.set_page_config(
    page_title="InsightFlow AI",
    page_icon="📊",
    layout="wide"
)

st.title("📊 InsightFlow AI")
st.markdown("### AI-Powered Multi-Agent Data Analytics Platform")

uploaded_file = st.file_uploader(
    "Upload your CSV dataset",
    type=["csv"]
)

if uploaded_file is not None:

    df = load_data(uploaded_file)

    st.success("✅ Dataset uploaded successfully!")

    show_overview(df)

    st.divider()

    st.subheader("📄 Dataset Preview")

    st.dataframe(
        df.head(10),
        use_container_width=True,
        height=350
    )

else:
    st.info("📂 Upload a CSV file to begin analysis.")
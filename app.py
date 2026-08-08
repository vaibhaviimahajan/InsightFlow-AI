import streamlit as st

from tools.loader import load_data
from tools.overview import show_overview
from tools.column_explorer import show_column_explorer
from tools.health_report import show_health_report


st.set_page_config(
    page_title="InsightFlow AI",
    page_icon="📊",
    layout="wide"
)


# Sidebar
with st.sidebar:

    st.title("📊 InsightFlow AI")

    st.caption("AI-Powered Data Analytics")

    st.divider()

    st.subheader("Analytics Pipeline")

    st.success("🟢 Data Upload")
    st.info("⚪ Data Cleaning")
    st.info("⚪ Exploratory Analysis")
    st.info("⚪ Visualization")
    st.info("⚪ AI Insights")
    st.info("⚪ Recommendations")

    st.divider()

    st.caption("Version 0.1.0")


# Main application
st.title("📊 InsightFlow AI")

st.markdown(
    "### Turn raw data into business insights with AI"
)

uploaded_file = st.file_uploader(
    "📂 Upload your CSV dataset",
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

    show_column_explorer(df)

    show_health_report(df)

else:

    st.info(
        "📂 Upload a CSV file to start the analytics pipeline."
    )
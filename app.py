import streamlit as st

from tools.loader import load_data
from tools.overview import show_overview
from tools.column_explorer import show_column_explorer
from tools.health_report import show_health_report

from agents.data_cleaning_agent import (
    clean_dataset
)


st.set_page_config(
    page_title="InsightFlow AI",
    page_icon="📊",
    layout="wide"
)


with st.sidebar:

    st.title("📊 InsightFlow AI")

    st.caption("AI-Powered Data Analytics")

    st.divider()

    st.subheader("Analytics Pipeline")

    st.success("🟢 Data Upload")
    st.success("🟢 Data Cleaning")
    st.info("⚪ Exploratory Analysis")
    st.info("⚪ Visualization")
    st.info("⚪ AI Insights")
    st.info("⚪ Recommendations")

    st.divider()

    st.caption("Version 0.2.0")


st.title("📊 InsightFlow AI")

st.markdown(
    "### Turn raw data into actionable business insights"
)


uploaded_file = st.file_uploader(
    "📂 Upload your CSV dataset",
    type=["csv"]
)


if uploaded_file is not None:

    df = load_data(uploaded_file)

    st.success(
        f"✅ Dataset uploaded: {uploaded_file.name}"
    )

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

    st.divider()

    st.subheader("🧹 Data Cleaning")

    st.write(
        "Automatically clean common data quality issues "
        "in the uploaded dataset."
    )

    if st.button(
        "🧹 Clean Dataset",
        type="primary"
    ):

        with st.spinner(
            "Cleaning dataset..."
        ):

            cleaned_df, cleaning_report = (
                clean_dataset(df)
            )

        st.session_state.cleaned_df = cleaned_df

        st.session_state.cleaning_report = (
            cleaning_report
        )

        st.success(
            "✅ Dataset cleaned successfully!"
        )


    # =========================
    # CLEANING REPORT
    # =========================

    if "cleaning_report" in st.session_state:

        st.divider()

        st.subheader(
            "📋 Cleaning Report"
        )

        report = (
            st.session_state
            .cleaning_report
        )

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Original Rows",
            report["original_rows"]
        )

        col2.metric(
            "Duplicates Removed",
            report["duplicates_removed"]
        )

        col3.metric(
            "Final Rows",
            report["final_rows"]
        )

        col4.metric(
            "Missing Remaining",
            report["missing_values_remaining"]
        )

else:

    st.info(
        "📂 Upload a CSV file to start the analytics pipeline."
    )
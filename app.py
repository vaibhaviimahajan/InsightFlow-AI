import streamlit as st

from tools.loader import load_data
from tools.overview import show_overview
from tools.column_explorer import show_column_explorer
from tools.health_report import show_health_report

from agents.data_cleaning_agent import clean_dataset

from agents.eda_agent import (
    generate_summary,
    generate_kpis
)


# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="InsightFlow AI",
    page_icon="📊",
    layout="wide"
)


# =========================
# SIDEBAR
# =========================

with st.sidebar:

    st.title("📊 InsightFlow AI")

    st.caption("AI-Powered Data Analytics")

    st.divider()

    st.subheader("Analytics Pipeline")

    st.success("🟢 Data Upload")
    st.success("🟢 Data Cleaning")
    st.success("🟢 Exploratory Analysis")
    st.info("⚪ Visualization")
    st.info("⚪ AI Insights")
    st.info("⚪ Recommendations")

    st.divider()

    st.caption("Version 0.3.0")


# =========================
# MAIN PAGE
# =========================

st.title("📊 InsightFlow AI")

st.markdown(
    "### Turn raw data into actionable business insights"
)


# =========================
# FILE UPLOAD
# =========================

uploaded_file = st.file_uploader(
    "📂 Upload your CSV dataset",
    type=["csv"]
)


if uploaded_file is not None:

    # =========================
    # LOAD DATA
    # =========================

    df = load_data(uploaded_file)

    st.success(
        f"✅ Dataset uploaded: {uploaded_file.name}"
    )


    # =========================
    # DATASET OVERVIEW
    # =========================

    show_overview(df)


    # =========================
    # DATASET PREVIEW
    # =========================

    st.divider()

    st.subheader("📄 Dataset Preview")

    st.dataframe(
        df.head(10),
        use_container_width=True,
        height=350
    )


    # =========================
    # COLUMN EXPLORER
    # =========================

    show_column_explorer(df)


    # =========================
    # DATASET HEALTH
    # =========================

    show_health_report(df)


    # ==================================================
    # DATA CLEANING
    # ==================================================

    st.divider()

    st.header("🧹 Data Cleaning")

    st.write(
        "Automatically detect and fix common "
        "data quality issues."
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


        # Store cleaned data
        st.session_state.cleaned_df = (
            cleaned_df
        )

        st.session_state.cleaning_report = (
            cleaning_report
        )


        st.success(
            "✅ Dataset cleaned successfully!"
        )


    # ==================================================
    # CLEANING REPORT
    # ==================================================

    if "cleaning_report" in st.session_state:

        report = (
            st.session_state.cleaning_report
        )


        st.subheader(
            "📋 Cleaning Report"
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


        # =========================
        # CLEANING OPERATIONS
        # =========================

        st.subheader(
            "📝 Cleaning Operations"
        )


        st.write(
            f"🗑️ Removed "
            f"**{report['duplicates_removed']}** "
            f"duplicate rows."
        )


        st.write(
            f"🔧 Filled "
            f"**{report['missing_values_filled']}** "
            f"missing values."
        )


        standardized = (
            report["standardized_columns"]
        )


        if standardized:

            st.write(
                "🔤 Standardized categorical columns:"
            )

            st.write(
                ", ".join(standardized)
            )

        else:

            st.write(
                "🔤 No categorical "
                "standardization required."
            )


        st.success(
            "✅ Cleaning pipeline completed successfully."
        )


        # =========================
        # BEFORE VS AFTER
        # =========================

        cleaned_df = (
            st.session_state.cleaned_df
        )


        st.divider()

        st.subheader(
            "🔄 Before vs After Cleaning"
        )


        before_missing = int(
            df.isnull().sum().sum()
        )


        after_missing = int(
            cleaned_df.isnull().sum().sum()
        )


        before_duplicates = int(
            df.duplicated().sum()
        )


        after_duplicates = int(
            cleaned_df.duplicated().sum()
        )


        col1, col2 = st.columns(2)


        with col1:

            st.markdown("### 🔴 Before")

            st.metric(
                "Rows",
                len(df)
            )

            st.metric(
                "Missing Values",
                before_missing
            )

            st.metric(
                "Duplicates",
                before_duplicates
            )


        with col2:

            st.markdown("### 🟢 After")

            st.metric(
                "Rows",
                len(cleaned_df)
            )

            st.metric(
                "Missing Values",
                after_missing
            )

            st.metric(
                "Duplicates",
                after_duplicates
            )


        # =========================
        # CLEANED DATA PREVIEW
        # =========================

        st.divider()

        st.subheader(
            "🧹 Cleaned Dataset Preview"
        )


        st.dataframe(
            cleaned_df.head(10),
            use_container_width=True,
            height=350
        )


        # =========================
        # DOWNLOAD CLEANED DATA
        # =========================

        st.subheader(
            "📥 Download Cleaned Dataset"
        )


        csv_data = (
            cleaned_df
            .to_csv(index=False)
            .encode("utf-8")
        )


        st.download_button(
            label="📥 Download Cleaned CSV",
            data=csv_data,
            file_name="cleaned_dataset.csv",
            mime="text/csv"
        )


    # ==================================================
    # EXPLORATORY DATA ANALYSIS
    # ==================================================

    st.divider()

    st.header("🔎 Exploratory Data Analysis")

    st.write(
        "Automatically analyze the dataset "
        "and identify important patterns."
    )


    # =========================
    # EDA SUMMARY
    # =========================

    eda_summary = generate_summary(df)


    st.success(
        "✅ EDA analysis completed!"
    )


    # =========================
    # KPI CARDS
    # =========================

    st.subheader(
        "📊 Key Performance Indicators"
    )


    kpis = generate_kpis(df)


    if kpis:

        kpi_columns = list(
            kpis.keys()
        )


        # Show maximum 4 KPI cards
        display_columns = kpi_columns[:4]


        cols = st.columns(
            len(display_columns)
        )


        for col, column in zip(
            cols,
            display_columns
        ):

            with col:

                st.metric(
                    label=f"Total {column}",
                    value=f"{kpis[column]['sum']:,.2f}"
                )


    else:

        st.info(
            "No numerical columns available "
            "for KPI generation."
        )


else:

    st.info(
        "📂 Upload a CSV file to start "
        "the analytics pipeline."
    )
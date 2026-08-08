import streamlit as st


def show_health_report(df):

    st.divider()

    st.subheader("🩺 Dataset Health Report")

    memory_usage = df.memory_usage(deep=True).sum() / 1024

    numeric_cols = len(
        df.select_dtypes(include="number").columns
    )

    categorical_cols = len(
        df.select_dtypes(include="object").columns
    )

    missing_percentage = (
        df.isnull().sum().sum()
        / (df.shape[0] * df.shape[1])
    ) * 100

    duplicate_percentage = (
        df.duplicated().sum()
        / df.shape[0]
    ) * 100

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Memory Usage",
        f"{memory_usage:.2f} KB"
    )

    col2.metric(
        "Numeric Columns",
        numeric_cols
    )

    col3.metric(
        "Categorical Columns",
        categorical_cols
    )

    col4, col5 = st.columns(2)

    col4.metric(
        "Missing %",
        f"{missing_percentage:.2f}%"
    )

    col5.metric(
        "Duplicate %",
        f"{duplicate_percentage:.2f}%"
    )

    if missing_percentage < 5 and duplicate_percentage < 2:
        st.success("🟢 Dataset Quality: Good")
    else:
        st.warning("🟡 Dataset Quality: Needs Cleaning")
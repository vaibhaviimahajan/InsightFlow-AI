import streamlit as st


def show_overview(df):
    total_rows = df.shape[0]
    total_columns = df.shape[1]
    missing_values = df.isnull().sum().sum()
    duplicate_rows = df.duplicated().sum()

    st.subheader("📈 Dataset Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Rows", total_rows)
    col2.metric("Columns", total_columns)
    col3.metric("Missing Values", missing_values)
    col4.metric("Duplicate Rows", duplicate_rows)
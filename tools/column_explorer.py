import streamlit as st
import pandas as pd


def show_column_explorer(df):

    st.divider()

    st.subheader("📋 Column Explorer")

    column_info = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str).values,
        "Missing Values": df.isnull().sum().values,
        "Unique Values": df.nunique().values
    })

    st.dataframe(
        column_info,
        use_container_width=True
    )
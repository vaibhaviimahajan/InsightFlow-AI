import streamlit as st
import pandas as pd

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

    df = pd.read_csv(uploaded_file)

    st.success("✅ Dataset uploaded successfully!")

    st.subheader("📈 Dataset Overview")

    total_rows = df.shape[0]
    total_columns = df.shape[1]
    missing_values = df.isnull().sum().sum()
    duplicate_rows = df.duplicated().sum()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Rows", total_rows)
    col2.metric("Columns", total_columns)
    col3.metric("Missing Values", missing_values)
    col4.metric("Duplicates", duplicate_rows)

    st.divider()

    st.subheader("📄 Dataset Preview")
    st.dataframe(df.head(10), use_container_width=True)
    st.divider()

    st.subheader("📋 Column Explorer")

    column_info = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str),
        "Missing Values": df.isnull().sum().values,
        "Unique Values": df.nunique().values
    })

    st.dataframe(column_info, use_container_width=True)


else:
    st.info("📂 Upload a CSV file to begin analysis.")
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="InsightFlow AI",
    page_icon="📊",
    layout="wide"
)
with st.sidebar:

    st.title("📊 InsightFlow AI")

    st.divider()

    st.header("Pipeline")

    st.success("🟢 Upload")

    st.info("⚪ Cleaning")

    st.info("⚪ EDA")

    st.info("⚪ Visualization")

    st.info("⚪ Insights")

    st.info("⚪ Recommendations")

    st.divider()

    st.caption("Version 0.1")

st.title("📊 InsightFlow AI")
st.markdown("### AI-Powered Multi-Agent Data Analytics Platform")

uploaded_file = st.file_uploader(
    "Upload your CSV dataset",
    type=["csv"]
)

if uploaded_file is not None:

    from tools.loader import load_data

    df = load_data(uploaded_file)

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
    st.dataframe(df.head(10), use_container_width=True, height=350)
    st.divider()

    st.subheader("📋 Column Explorer")

    column_info = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str),
        "Missing Values": df.isnull().sum().values,
        "Unique Values": df.nunique().values
    })

    st.dataframe(column_info, use_container_width=True)
    st.divider()

    st.subheader("🩺 Dataset Health Report")

    memory_usage = df.memory_usage(deep=True).sum() / 1024

    numeric_cols = len(df.select_dtypes(include="number").columns)

    categorical_cols = len(df.select_dtypes(include="object").columns)

    missing_percentage = (
        df.isnull().sum().sum()
        / (df.shape[0] * df.shape[1])
    ) * 100

    duplicate_percentage = (
        df.duplicated().sum()
        / df.shape[0]
    ) * 100

    st.write(f"**Memory Usage:** {memory_usage:.2f} KB")
    st.write(f"**Numeric Columns:** {numeric_cols}")
    st.write(f"**Categorical Columns:** {categorical_cols}")
    st.write(f"**Missing Percentage:** {missing_percentage:.2f}%")
    st.write(f"**Duplicate Percentage:** {duplicate_percentage:.2f}%")

    if missing_percentage < 5 and duplicate_percentage < 2:
        st.success("🟢 Dataset Quality: Good")
    else:
        st.warning("🟡 Dataset Quality: Needs Cleaning")

else:
    st.info("📂 Upload a CSV file to begin analysis.")
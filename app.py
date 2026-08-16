import streamlit as st
import plotly.express as px
from tools.loader import load_data
from tools.overview import show_overview
from tools.column_explorer import show_column_explorer
from tools.health_report import show_health_report
from agents.visualization_agent import generate_charts
from agents.data_cleaning_agent import clean_dataset
from agents.insight_agent import generate_ai_insights
from agents.dataset_chat import ask_dataset_question


from agents.eda_agent import (
    generate_summary,
    generate_kpis,
    generate_statistics,
    generate_correlations,
    generate_category_analysis
)

from agents.insight_agent import (
    generate_insight_summary,
    find_top_bottom_performers,
    detect_trends
)

from agents.insight_agent import (
    generate_ai_insights,
    generate_executive_summary
)

from agents.insight_agent import (
    generate_ai_insights,
    generate_executive_summary
)

from agents.recommendation_agent import (
    generate_recommendations
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
    st.subheader("🤖 AI Analyst Team")

    st.info("🧹 Data Cleaning Agent")
    st.info("🔎 EDA Agent")
    st.info("📈 Visualization Agent")
    st.info("💡 Insight Agent")
    st.info("🎯 Recommendation Agent")

    st.divider()

    st.subheader("Analytics Pipeline")

    st.success("🟢 Data Upload")
    st.success("🟢 Data Cleaning")
    st.success("🟢 Exploratory Analysis")
    st.info("⚪ Visualization")
    st.info("⚪ AI Insights")
    st.info("⚪ Recommendations")

    st.divider()

    st.caption("Version 0.3.1")


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
    
        # ==================================================
    # CHAT WITH DATASET
    # ==================================================

    st.divider()

    st.header("💬 Chat With Your Dataset")

    st.write(
        "Ask questions about your uploaded dataset "
        "using natural language."
    )

    question = st.text_input(
        "Ask a question",
        placeholder="Example: Which category has the highest sales?"
    )

    if st.button("💬 Ask AI") and question:

        with st.spinner(
            "Mistral AI is analyzing your dataset..."
        ):

            answer = ask_dataset_question(
                df,
                question
            )

        st.markdown("### 🤖 AI Answer")

        st.write(answer)
        
    # =========================
    # PIPELINE STATUS
    # =========================

    st.divider()

    st.subheader("⚙️ Analysis Pipeline")

    pipeline_col1, pipeline_col2, pipeline_col3, pipeline_col4, pipeline_col5 = st.columns(5)

    with pipeline_col1:
        st.success("🟢 Upload")

    with pipeline_col2:
        st.success("🟢 Cleaning")

    with pipeline_col3:
        st.success("🟢 EDA")

    with pipeline_col4:
        st.success("🟢 Visualization")

    with pipeline_col5:
        st.success("🟢 AI Analysis")

    # =========================
    # DATASET INFORMATION
    # =========================

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


    # =========================
    # CLEANING
    # =========================

    st.divider()

    st.header("🧹 Data Cleaning")

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

        cleaned_df = (
            st.session_state.cleaned_df
        )

        st.subheader(
            "🧹 Cleaned Dataset Preview"
        )

        st.dataframe(
            cleaned_df.head(10),
            use_container_width=True
        )

        csv_data = (
            cleaned_df
            .to_csv(index=False)
            .encode("utf-8")
        )

        st.download_button(
            "📥 Download Cleaned CSV",
            data=csv_data,
            file_name="cleaned_dataset.csv",
            mime="text/csv"
        )


    # =========================
    # EDA
    # =========================

    st.divider()

    st.header(
        "🔎 Exploratory Data Analysis"
    )

    st.write(
        "Automatically analyze numerical "
        "and categorical patterns."
    )


    eda_summary = generate_summary(df)

    kpis = generate_kpis(df)

    statistics = generate_statistics(df)


    st.success(
        "✅ EDA analysis completed!"
    )


    # =========================
    # KPI CARDS
    # =========================

    st.subheader(
        "📊 Key Performance Indicators"
    )


    if kpis:

        display_columns = list(
            kpis.keys()
        )[:4]

        cols = st.columns(
            len(display_columns)
        )

        for col, column in zip(
            cols,
            display_columns
        ):

            with col:

                st.metric(
                    f"Total {column}",
                    f"{kpis[column]['sum']:,.2f}"
                )

    else:

        st.info(
            "No numerical columns found."
        )


    # =========================
    # STATISTICAL SUMMARY
    # =========================

    st.subheader(
        "📐 Statistical Summary"
    )


    if not statistics.empty:

        st.dataframe(
            statistics,
            use_container_width=True
        )

    else:

        st.info(
            "No numerical columns available."
        )


else:

    st.info(
        "📂 Upload a CSV file to start."
    )

# =========================
# CORRELATION ANALYSIS
# =========================

st.subheader(
    "🔥 Correlation Analysis"
)

correlations = generate_correlations(df)

if not correlations.empty:

    fig = px.imshow(
        correlations,
        text_auto=True,
        aspect="auto",
        title="Numerical Feature Correlations"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

else:

    st.info(
        "At least two numerical columns "
        "are required for correlation analysis."
    )
    
# =========================
# CATEGORY ANALYSIS
# =========================

st.subheader(
    "📊 Category Analysis"
)

category_results = (
    generate_category_analysis(df)
)

if category_results:

    for column, analysis in (
        category_results.items()
    ):

        st.markdown(
            f"### {column}"
        )

        st.dataframe(
            analysis,
            use_container_width=True
        )

else:

    st.info(
        "No suitable categorical columns found."
    )

# ==================================================
# VISUALIZATION
# ==================================================

st.divider()

st.header(
    "📈 Automated Visualizations"
)

st.write(
    "InsightFlow AI automatically selects "
    "charts based on your dataset."
)


charts = generate_charts(df)


if charts:

    for chart in charts:

        st.plotly_chart(
            chart,
            use_container_width=True
        )

else:

    st.info(
        "Not enough suitable columns "
        "to generate visualizations."
    )
    
    
# ==================================================
# AI BUSINESS INSIGHTS
# ==================================================

st.divider()

st.header("💡 Business Insights")

st.write(
    "Automatically generated observations "
    "from your dataset."
)


insights = generate_insight_summary(df)

for insight in insights:

    st.info(
        f"💡 {insight}"
    )


st.subheader(
    "🏆 Top & Bottom Performers"
)

performance_insights = (
    find_top_bottom_performers(df)
)

for insight in performance_insights:

    st.success(
        f"📊 {insight}"
    )


st.subheader(
    "📈 Trend Analysis"
)

trend_insights = detect_trends(df)

for insight in trend_insights:

    st.warning(
        f"📈 {insight}"
    )
    
# =========================
# MISTRAL AI INSIGHTS
# =========================

st.divider()

st.header("🤖 AI Business Insights")

st.write(
    "Mistral AI analyzes the dataset and "
    "generates business-focused insights."
)

if st.button("✨ Generate AI Insights"):

    with st.spinner(
        "Mistral AI is analyzing your dataset..."
    ):

        ai_insights = generate_ai_insights(df)

    st.markdown(ai_insights)

st.subheader("📋 Executive Summary")

if st.button("📋 Generate Executive Summary"):

    with st.spinner(
        "Generating executive summary..."
    ):

        summary = generate_executive_summary(df)

    st.success(summary)
    
# =========================
# AI RECOMMENDATIONS
# =========================

st.divider()

st.header("🎯 AI Recommendations")

st.write(
    "Generate actionable recommendations "
    "based on the uploaded dataset."
)

if st.button("🎯 Generate Recommendations"):

    with st.spinner(
        "Mistral AI is generating recommendations..."
    ):

        recommendations = (
            generate_recommendations(df)
        )

    st.markdown(recommendations)
    
    # ==================================================
# CHAT WITH DATASET
# ==================================================

st.divider()

st.header("💬 Chat With Your Dataset")

st.write(
    "Ask questions about your uploaded dataset "
    "using natural language."
)

st.markdown("**Try asking:**")

example_questions = [
    "Which category performs best?",
    "What is the average sales?",
    "Which region has the highest revenue?",
    "What are the strongest performing products?"
]

for example in example_questions:

    st.caption(f"• {example}")


question = st.text_input(
    "Ask a question",
    placeholder="Example: Which category has the highest sales?"
)


if st.button("💬 Ask AI") and question:

    with st.spinner(
        "Mistral AI is analyzing your dataset..."
    ):

        answer = ask_dataset_question(
            df,
            question
        )

    st.markdown("### 🤖 AI Answer")

    st.info(answer)
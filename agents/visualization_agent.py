import pandas as pd
import plotly.express as px


def generate_charts(df):

    charts = []

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns.tolist()

    categorical_columns = df.select_dtypes(
        include="object"
    ).columns.tolist()

    datetime_columns = df.select_dtypes(
        include=["datetime", "datetimetz"]
    ).columns.tolist()


    # Line chart

    if datetime_columns and numeric_columns:

        fig = px.line(
            df,
            x=datetime_columns[0],
            y=numeric_columns[0],
            title=(
                f"{numeric_columns[0]} Over Time"
            )
        )

        charts.append(fig)


    # Bar chart

    if categorical_columns and numeric_columns:

        category = categorical_columns[0]
        metric = numeric_columns[0]

        grouped = (
            df.groupby(category)[metric]
            .sum()
            .reset_index()
            .sort_values(
                metric,
                ascending=False
            )
            .head(10)
        )

        fig = px.bar(
            grouped,
            x=category,
            y=metric,
            title=f"{metric} by {category}"
        )

        charts.append(fig)


    # Histogram

    if numeric_columns:

        column = numeric_columns[0]

        fig = px.histogram(
            df,
            x=column,
            title=f"{column} Distribution"
        )

        charts.append(fig)


    # Scatter

    if len(numeric_columns) >= 2:

        fig = px.scatter(
            df,
            x=numeric_columns[0],
            y=numeric_columns[1],
            title=(
                f"{numeric_columns[1]} "
                f"vs {numeric_columns[0]}"
            )
        )

        charts.append(fig)


    return charts
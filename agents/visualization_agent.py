import plotly.express as px


def generate_charts(df):

    charts = []

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns.tolist()

    categorical_columns = df.select_dtypes(
        include="object"
    ).columns.tolist()


    # =========================
    # CATEGORY BAR CHART
    # =========================

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


    # =========================
    # SECOND CATEGORY
    # =========================

    if (
        len(categorical_columns) >= 2
        and numeric_columns
    ):

        category = categorical_columns[1]
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


    # =========================
    # HISTOGRAM
    # =========================

    if numeric_columns:

        column = numeric_columns[0]

        fig = px.histogram(
            df,
            x=column,
            title=f"{column} Distribution"
        )

        charts.append(fig)


    # =========================
    # SCATTER
    # =========================

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
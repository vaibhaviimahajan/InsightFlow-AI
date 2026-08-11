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
    # DISTRIBUTION
    # =========================

    for column in numeric_columns[:3]:

        fig = px.histogram(
            df,
            x=column,
            title=f"{column} Distribution",
            marginal="box"
        )

        charts.append(fig)


    # =========================
    # SCATTER
    # =========================

    if len(numeric_columns) >= 2:

        x_column = numeric_columns[0]
        y_column = numeric_columns[1]

        fig = px.scatter(
            df,
            x=x_column,
            y=y_column,
            title=(
                f"{y_column} vs {x_column}"
            ),
            trendline="ols"
        )

        charts.append(fig)


    return charts
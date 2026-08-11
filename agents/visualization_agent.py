import pandas as pd


def detect_chart_types(df):

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

    if datetime_columns and numeric_columns:

        charts.append({
            "type": "line",
            "x": datetime_columns[0],
            "y": numeric_columns[0]
        })

    if categorical_columns and numeric_columns:

        charts.append({
            "type": "bar",
            "x": categorical_columns[0],
            "y": numeric_columns[0]
        })

    if numeric_columns:

        charts.append({
            "type": "histogram",
            "column": numeric_columns[0]
        })

    if len(numeric_columns) >= 2:

        charts.append({
            "type": "scatter",
            "x": numeric_columns[0],
            "y": numeric_columns[1]
        })

    return charts
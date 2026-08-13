import pandas as pd


def generate_insight_summary(df):

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns.tolist()

    categorical_columns = df.select_dtypes(
        include="object"
    ).columns.tolist()

    insights = []

    if numeric_columns:

        for column in numeric_columns[:5]:

            total = df[column].sum()
            average = df[column].mean()
            maximum = df[column].max()
            minimum = df[column].min()

            insights.append({
                "metric": column,
                "total": round(total, 2),
                "average": round(average, 2),
                "maximum": round(maximum, 2),
                "minimum": round(minimum, 2)
            })

    return insights
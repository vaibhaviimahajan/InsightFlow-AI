import pandas as pd


def generate_insight_summary(df):

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns.tolist()

    insights = []

    for column in numeric_columns[:5]:

        total = df[column].sum()
        average = df[column].mean()
        maximum = df[column].max()
        minimum = df[column].min()

        insights.append(
            f"{column} has a total of "
            f"{total:,.2f} with an average of "
            f"{average:,.2f}. "
            f"The highest value is "
            f"{maximum:,.2f}, while the lowest "
            f"value is {minimum:,.2f}."
        )

    return insights
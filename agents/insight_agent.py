import pandas as pd


def generate_insight_summary(df):

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns.tolist()

    insights = []

    for column in numeric_columns[:5]:

        total = df[column].sum()
        average = df[column].mean()

        insights.append(
            f"{column} generated a total of "
            f"{total:,.2f} with an average of "
            f"{average:,.2f}."
        )

    return insights


def find_top_bottom_performers(df):

    categorical_columns = df.select_dtypes(
        include="object"
    ).columns.tolist()

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns.tolist()

    results = []

    if not categorical_columns:
        return results

    if not numeric_columns:
        return results

    category = categorical_columns[0]
    metric = numeric_columns[0]

    grouped = (
        df.groupby(category)[metric]
        .sum()
        .sort_values(ascending=False)
    )

    if len(grouped) > 0:

        top_category = grouped.index[0]
        top_value = grouped.iloc[0]

        bottom_category = grouped.index[-1]
        bottom_value = grouped.iloc[-1]

        results.append(
            f"{top_category} is the top-performing "
            f"{category} with {top_value:,.2f} "
            f"in total {metric}."
        )

        results.append(
            f"{bottom_category} is the lowest-performing "
            f"{category} with {bottom_value:,.2f} "
            f"in total {metric}."
        )

    return results
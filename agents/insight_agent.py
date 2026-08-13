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

    if not categorical_columns or not numeric_columns:
        return results

    category = categorical_columns[0]
    metric = numeric_columns[0]

    grouped = (
        df.groupby(category)[metric]
        .sum()
        .sort_values(ascending=False)
    )

    if len(grouped) > 0:

        results.append(
            f"Top {category}: "
            f"{grouped.index[0]} "
            f"({grouped.iloc[0]:,.2f})"
        )

        results.append(
            f"Lowest {category}: "
            f"{grouped.index[-1]} "
            f"({grouped.iloc[-1]:,.2f})"
        )

    return results


def detect_trends(df):

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns.tolist()

    results = []

    for column in numeric_columns:

        if len(df) < 2:
            continue

        first_half = (
            df[column]
            .iloc[:len(df) // 2]
            .mean()
        )

        second_half = (
            df[column]
            .iloc[len(df) // 2:]
            .mean()
        )

        if first_half == 0:
            continue

        change = (
            (second_half - first_half)
            / abs(first_half)
        ) * 100

        if change > 5:

            results.append(
                f"{column} increased by "
                f"{change:.1f}% between the first "
                f"and second half of the dataset."
            )

        elif change < -5:

            results.append(
                f"{column} decreased by "
                f"{abs(change):.1f}% between the first "
                f"and second half of the dataset."
            )

        else:

            results.append(
                f"{column} remained relatively stable "
                f"across the dataset."
            )

    return results
def generate_category_analysis(df):

    categorical_columns = df.select_dtypes(
        include="object"
    ).columns

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns

    results = {}

    if len(numeric_columns) == 0:
        return results

    metric = numeric_columns[0]

    for column in categorical_columns:

        if df[column].nunique() <= 50:

            analysis = (
                df.groupby(column)[metric]
                .agg(
                    ["sum", "mean", "count"]
                )
                .sort_values(
                    "sum",
                    ascending=False
                )
                .round(2)
            )

            results[column] = analysis

    return results
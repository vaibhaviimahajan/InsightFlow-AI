import pandas as pd


def generate_summary(df):

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns.tolist()

    categorical_columns = df.select_dtypes(
        include="object"
    ).columns.tolist()

    summary = {
        "total_rows": len(df),
        "total_columns": len(df.columns),
        "numeric_columns": numeric_columns,
        "categorical_columns": categorical_columns,
        "missing_values": int(
            df.isnull().sum().sum()
        ),
        "duplicate_rows": int(
            df.duplicated().sum()
        )
    }

    return summary


def generate_kpis(df):

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns

    kpis = {}

    for column in numeric_columns:

        kpis[column] = {
            "sum": float(df[column].sum()),
            "mean": float(df[column].mean()),
            "min": float(df[column].min()),
            "max": float(df[column].max())
        }

    return kpis


def generate_statistics(df):

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns

    if len(numeric_columns) == 0:
        return pd.DataFrame()

    statistics = df[numeric_columns].describe().T

    return statistics.round(2)


def generate_correlations(df):

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns

    if len(numeric_columns) < 2:
        return pd.DataFrame()

    correlation_matrix = (
        df[numeric_columns]
        .corr()
        .round(2)
    )

    return correlation_matrix


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

    primary_metric = numeric_columns[0]

    for column in categorical_columns:

        if df[column].nunique() <= 50:

            analysis = (
                df.groupby(column)[primary_metric]
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
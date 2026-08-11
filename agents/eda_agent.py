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
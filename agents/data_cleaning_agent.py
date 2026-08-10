import pandas as pd


def detect_cleaning_issues(df):
    report = {
        "duplicate_rows": int(df.duplicated().sum()),
        "missing_values": int(df.isnull().sum().sum()),
        "columns_with_missing": int(
            df.isnull().any().sum()
        ),
        "total_columns": int(df.shape[1]),
        "total_rows": int(df.shape[0])
    }

    return report


def remove_duplicates(df):
    cleaned_df = df.drop_duplicates().copy()

    removed_rows = len(df) - len(cleaned_df)

    return cleaned_df, removed_rows
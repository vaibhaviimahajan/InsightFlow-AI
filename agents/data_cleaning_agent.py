import pandas as pd


def detect_cleaning_issues(df):

    report = {
        "duplicate_rows": int(
            df.duplicated().sum()
        ),

        "missing_values": int(
            df.isnull().sum().sum()
        ),

        "columns_with_missing": int(
            df.isnull().any().sum()
        ),

        "total_columns": int(
            df.shape[1]
        ),

        "total_rows": int(
            df.shape[0]
        )
    }

    return report


def remove_duplicates(df):

    cleaned_df = df.drop_duplicates().copy()

    removed_rows = (
        len(df) - len(cleaned_df)
    )

    return cleaned_df, removed_rows


def handle_missing_values(df):

    cleaned_df = df.copy()

    numeric_columns = (
        cleaned_df
        .select_dtypes(include="number")
        .columns
    )

    categorical_columns = (
        cleaned_df
        .select_dtypes(include="object")
        .columns
    )

    for column in numeric_columns:

        if cleaned_df[column].isnull().any():

            cleaned_df[column] = (
                cleaned_df[column]
                .fillna(
                    cleaned_df[column].median()
                )
            )

    for column in categorical_columns:

        if cleaned_df[column].isnull().any():

            cleaned_df[column] = (
                cleaned_df[column]
                .fillna("Unknown")
            )

    return cleaned_df


def standardize_categories(df):

    cleaned_df = df.copy()

    categorical_columns = (
        cleaned_df
        .select_dtypes(include="object")
        .columns
    )

    for column in categorical_columns:

        cleaned_df[column] = (
            cleaned_df[column]
            .astype(str)
            .str.strip()
            .str.title()
        )

    return cleaned_df


def clean_dataset(df):

    original_rows = len(df)

    cleaned_df, removed_duplicates = (
        remove_duplicates(df)
    )

    cleaned_df = handle_missing_values(
        cleaned_df
    )

    cleaned_df = standardize_categories(
        cleaned_df
    )

    cleaning_report = {

        "original_rows": original_rows,

        "final_rows": len(cleaned_df),

        "duplicates_removed": removed_duplicates,

        "missing_values_remaining": int(
            cleaned_df.isnull()
            .sum()
            .sum()
        )
    }

    return cleaned_df, cleaning_report
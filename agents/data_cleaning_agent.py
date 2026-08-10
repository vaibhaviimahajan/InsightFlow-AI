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

    filled_values = 0

    for column in numeric_columns:

        missing_count = (
            cleaned_df[column]
            .isnull()
            .sum()
        )

        if missing_count > 0:

            cleaned_df[column] = (
                cleaned_df[column]
                .fillna(
                    cleaned_df[column].median()
                )
            )

            filled_values += missing_count

    for column in categorical_columns:

        missing_count = (
            cleaned_df[column]
            .isnull()
            .sum()
        )

        if missing_count > 0:

            cleaned_df[column] = (
                cleaned_df[column]
                .fillna("Unknown")
            )

            filled_values += missing_count

    return cleaned_df, filled_values


def standardize_categories(df):

    cleaned_df = df.copy()

    categorical_columns = (
        cleaned_df
        .select_dtypes(include="object")
        .columns
    )

    standardized_columns = []

    for column in categorical_columns:

        original_values = (
            cleaned_df[column]
            .astype(str)
        )

        cleaned_df[column] = (
            original_values
            .str.strip()
            .str.title()
        )

        if not original_values.equals(
            cleaned_df[column]
        ):

            standardized_columns.append(
                column
            )

    return (
        cleaned_df,
        standardized_columns
    )


def clean_dataset(df):

    original_rows = len(df)

    original_missing = int(
        df.isnull().sum().sum()
    )

    original_duplicates = int(
        df.duplicated().sum()
    )

    # Remove duplicates
    cleaned_df, removed_duplicates = (
        remove_duplicates(df)
    )

    # Handle missing values
    cleaned_df, filled_values = (
        handle_missing_values(
            cleaned_df
        )
    )

    # Standardize categories
    cleaned_df, standardized_columns = (
        standardize_categories(
            cleaned_df
        )
    )

    cleaning_report = {

        "original_rows": original_rows,

        "final_rows": len(cleaned_df),

        "duplicates_removed":
            removed_duplicates,

        "missing_values_found":
            original_missing,

        "missing_values_filled":
            filled_values,

        "missing_values_remaining":
            int(
                cleaned_df
                .isnull()
                .sum()
                .sum()
            ),

        "standardized_columns":
            standardized_columns,

        "original_duplicates":
            original_duplicates
    }

    return cleaned_df, cleaning_report
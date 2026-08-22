def drop_cols(df: pd.DataFrame, cols: list[str]):
    """
    Drop specified columns from the DataFrame.
    """
    return df.drop(cols, axis=1, inplace=True)
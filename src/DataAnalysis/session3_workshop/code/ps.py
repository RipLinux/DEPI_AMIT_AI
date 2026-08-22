
import pandas as pd

def get_chk_dtype(df: pd.DataFrame):
    """
    Get the data types and unique values of each column in the DataFrame.
    """
    dtypes = df.dtypes
    nunique = df.nunique()
    return pd.DataFrame({'Dtypes': dtypes, 'Unique Values': nunique}).T
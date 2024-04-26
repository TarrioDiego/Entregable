import pandas as pd

def transform_coincap(df : pd.DataFrame) -> pd.DataFrame:
    # Realizo la transformacion de los datos
    df.drop(columns='maxSupply', inplace=True)
    return df

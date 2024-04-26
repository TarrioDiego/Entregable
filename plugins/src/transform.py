import pandas as pd
from constants import COLUMNS 

def transform(df : pd.DataFrame) -> pd.DataFrame:
    # Realizo la transformacion de los datos
    df.drop(columns='Roi', inplace=True)
    for campo in COLUMNS:
        df[campo] = pd.to_datetime(df[campo])
    return df

import json
import pandas as pd
import psycopg2


def load(df : pd.DataFrame):
    with open('credentials.json') as f:
        credentials = json.load(f)
        dbname = credentials['dbname']
        host = credentials['host']
        port = credentials['port']
        user = credentials['user']
        password = credentials['password']

    # Establecer la conexión con la base de datos Redshift
    conn = psycopg2.connect(
        dbname = dbname,
        user = user,
        password = password,
        host = host,
        port = port
    )

    # Carga de los datos en mi tabla de redshift
    df.to_sql('coins_data', conn, if_exists='append')

    # Cerrar la conexion
    conn.close()



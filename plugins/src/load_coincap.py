import json
import pandas as pd
import psycopg2


def load_coincap(df : pd.DataFrame):
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

    # Crear la tabla en Redshift si no existe
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS coinscap_data (
        id VARCHAR(50),  
        rank INTEGER, 
        symbol VARCHAR(50),
        name VARCHAR(255),  
        supply NUMERIC,  
        marketCapUsd NUMERIC,  
        volumeUsd24Hr NUMERIC,  
        priceUsd NUMERIC, 
        changePercent24Hr NUMERIC, 
        vwap24Hr NUMERIC,  
        explorer VARCHAR(255)
    );
    """
    # Crear un cursor para ejecutar consultas
    cur = conn.cursor()

    
    # Ejecutar la consulta para crear la tabla
    cur.execute(create_table_query)

    # Confirmar la transacción y cerrar la conexión
    conn.commit()
    cur.close()
   

    # Carga de los datos en mi tabla de redshift
    df.to_sql('coinscap_data', conn, if_exists='append')

    # Cerrar la conexion
    conn.close()

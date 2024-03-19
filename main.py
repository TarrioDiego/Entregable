import requests
import pandas as pd
import json
import psycopg2
from constants import Ids_moneda


# Definir la URL del endpoint de la API de CoinGecko
url = 'https://api.coingecko.com/api/v3/coins/markets'

# Parámetros de la solicitud
params = {
    'vs_currency': 'usd',  # Moneda de referencia (en este caso, dólares estadounidenses)
    'order': 'market_cap_desc',  # Ordenar por capitalización de mercado descendente
    'per_page': 100,  # Número de resultados por página (en este caso, 100)
    'page': 1,  # Página de resultados (en este caso, la primera página)
    'ids': Ids_moneda

}

# Realizar la solicitud a la API
response = requests.get(url,params=params)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Obtener los datos de la respuesta en formato JSON
    data = response.json()
    # Crear un DataFrame de pandas a partir de los datos
    df = pd.DataFrame(data)
   
else:
    # Si la solicitud no fue exitosa, imprimir el código de estado
    print('Error:', response.status_code)
    print('response text: ', response.text)


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

# Crear un cursor para ejecutar consultas
cur = conn.cursor()

# Definir la consulta SQL para crear la tabla
create_table_query = """
CREATE TABLE coins_data (
    ID VARCHAR(255) PRIMARY KEY,
    Symbol VARCHAR(255),
    Name VARCHAR(255),
    Image VARCHAR(255),
    Current_Price DECIMAL,
    Market_Cap DECIMAL,
    Market_Cap_Rank INT,
    Fully_Diluted_Valuation DECIMAL,
    Total_Volume DECIMAL,
    High_24h DECIMAL,
    Low_24h DECIMAL,
    Price_Change_24h DECIMAL,
    Price_Change_Percentage_24h DECIMAL,
    Market_Cap_Change_24h DECIMAL,
    Market_Cap_Change_Percentage_24h DECIMAL,
    Circulating_Supply DECIMAL,
    Total_Supply DECIMAL,
    Max_Supply DECIMAL,
    Ath DECIMAL,
    Ath_Change_Percentage DECIMAL,
    Ath_Date DATE,
    Atl DECIMAL,
    Atl_Change_Percentage DECIMAL,
    Atl_Date DATE,
    Last_Updated TIMESTAMP
);
"""


# Ejecutar la consulta para crear la tabla
cur.execute(create_table_query)

# Confirmar la transacción 
conn.commit()


# Realizo la transformacion de los datos
df.drop(columns='Roi', inplace=True)
columns = ['Ath_Date', 'Atl_Date', 'Last_Updated']
for campo in columns:
    df[campo] = pd.to_datetime(df[campo])


# Carga de los datos en mi tabla de redshift
df.to_sql('coins_data', conn, if_exists='append')

# Cerrar la conexion
cur.close()
conn.close()


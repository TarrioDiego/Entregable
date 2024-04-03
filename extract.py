import pandas as pd
import requests
from constants import IDS_MONEDA



def extract() -> pd.DataFrame:
    # Definir la URL del endpoint de la API de CoinGecko
    url = 'https://api.coingecko.com/api/v3/coins/markets'

    # Parámetros de la solicitud
    params = {
        'vs_currency': 'usd',  # Moneda de referencia (en este caso, dólares estadounidenses)
        'order': 'market_cap_desc',  # Ordenar por capitalización de mercado descendente
        'per_page': 100,  # Número de resultados por página (en este caso, 100)
        'page': 1,  # Página de resultados (en este caso, la primera página)
        'ids': IDS_MONEDA

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
    return df
   
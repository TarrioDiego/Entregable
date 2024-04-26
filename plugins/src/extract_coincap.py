import requests
import pandas as pd
from constants import IDS_MONEDA

def extract_coincap() -> pd.DataFrame:
    # URL base de la API de CoinCap
    base_url = 'https://api.coincap.io/v2/assets'

    # Construir los parámetros de la solicitud
    params = {
        'ids': IDS_MONEDA  # Lista de identificadores de activos (IDs) separados por comas
    }

    # Realizar la solicitud a la API con los parámetros
    response = requests.get(base_url, params=params)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Obtener los datos de la respuesta en formato JSON
        data = response.json()
        # Extraer la lista de activos (criptomonedas) de los datos
        assets = data['data']
        # Crear un DataFrame de pandas a partir de los datos de los activos
        df = pd.DataFrame(assets)
        
        # Imprimir el DataFrame para visualizarlo
        print(df)
    else:
        # Si la solicitud no fue exitosa, imprimir el código de estado
        print('Error:', response.status_code)
        print('response text: ', response.text)
        # Retornar un DataFrame vacío en caso de error
        df = pd.DataFrame()

    return df

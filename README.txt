OBJETIVO
Este proyecto consiste en un script en Python que realiza solicitudes a la API de CoinGecko 
para obtener datos sobre criptomonedas y los carga en un DataFrame de Pandas, para poder realizar un analisis 
de las distintas monedas y sus caracteristicas en el mercado,para luego aplicar transformacion y poder realizar 
la carga a una base de datos en Redshift.

PASOS A SEGUIR
Clonar el repositorio 
git clone <url_del_repositorio>

Instalar librerias usadas
pip install -r requirements.txt

Reemplazar los datos de tu conexion a redshift en el main.py
(linea 51 a 55)

Ejecutar el codigo
python main.py
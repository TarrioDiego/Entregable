# Proyecto de Dockerización para Análisis de Criptomonedas

## OBJETIVO
Este proyecto consiste en dockerizar un script en Python que realiza solicitudes a la API de CoinGecko y a la API CoinCap para obtener datos sobre criptomonedas y cargarlos en un DataFrame de Pandas. El objetivo principal es facilitar el análisis de las distintas monedas y sus características en el mercado. Una vez obtenidos los datos, se aplicarán transformaciones para prepararlos y luego se cargarán en una base de datos en Redshift.
Además, incluirá un mecanismo de alerta por correo electrónico para notificar eventos específicos, como cambios en los precios de las criptomonedas. El sistema estará automatizado utilizando DAGs (Directed Acyclic Graphs) en Airflow, ejecutándose periódicamente para mantener los datos actualizados y proporcionar insights en tiempo real.

## PASOS A SEGUIR
**Clonar el repositorio**
> git clone <url_del_repositorio>

A partir de los archivos
'docker-compose.yaml'
'.env'
vamos a levantar Airflow.

**Reemplazar los datos de tu conexion a redshift en credentials.json**

**Correr el setup de Airflow**
>docker compose up airflow-init


**Inicializar Airflow**
>docker compose up

**Acceder a la interfaz en tu navegador**
'localhost:8000'


import textwrap
from datetime import datetime, timedelta


from plugins.src.extract import extract
from plugins.src.transform import transform
from plugins.src.load import load

from plugins.src.extract_coincap import extract_coincap
from plugins.src.transform_coincap import transform_coincap
from plugins.src.load_coincap import load_coincap

from plugins.src.send_mail import send_email

#from airflow.models.dag import DAG
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


with DAG(
    "tutorial",
    # These args will get passed on to each operator
    # You can override thme on a per-task basis during operator initialization
    default_args={
        "depends_on_past": False,
        "email":["airflow@eample.com"],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5)  
    },

    description = "A simple tutorial DAG",
    # schedule = timedelta(days=1),
    schedule_interval='@hourly',
    start_date = datetime(2024, 2 , 1),
    catchup = False,
    tags = ["example"],
) as dag:
    
    def etl_func():
        data = extract()
        data = transform()
        load(data)
    
    
    def etl2_func():
        data = extract_coincap()
        data = transform_coincap()
        load_coincap(data)

    
    def fail_safe_email():
        # Obtener los datos
        data = extract()
        # Obtener el precio actual de Bitcoin
        bitcoin_price = data[data['id'] == 'bitcoin']['current_price'].iloc[0]
        # Definir el rango de precios para la alerta
        lower_threshold = 40000
        upper_threshold = 50000
        # Verificar si el precio de Bitcoin está fuera del rango
        if bitcoin_price < lower_threshold or bitcoin_price > upper_threshold:
            # Enviar alerta por correo electrónico
            sender_email = "your_email@gmail.com"
            sender_password = "your_password"
            receiver_email = "recipient_email@example.com"
            subject = "Alerta: Precio de Bitcoin fuera del rango"
            body = f"El precio actual de Bitcoin es {bitcoin_price}. ¡Está fuera del rango de {lower_threshold} a {upper_threshold}!"
            send_email(sender_email, sender_password, receiver_email, subject, body)


    etl = PythonOperator(task_id="execute_the_etl", python_callable=etl_func)

    etl2 = PythonOperator(task_id="execute_the_etl2", python_callable=etl2_func)

    enviar_resultado = PythonOperator(task_id="send_result", python_callable=fail_safe_email)

    [etl,etl2] >> enviar_resultado


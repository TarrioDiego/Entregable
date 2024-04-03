# Seleccion del lenguaje y version.
FROM python:3.11  

RUN mkdir /app

# COPY <nombre_conector> /app/
COPY . /app/


# Se agrega el driver del ODBC, se setea en 'Y' los terminos y condiciones del driver y luego se ejecuta
# COPY storage /app/storage
WORKDIR /app

# Instalo dependencias de python
RUN pip install -r requirements.txt

# Se ejecuta el archivo main.py mediante consola ## Solo puede haber un CMD statement por Dockerfile ##
CMD ["python", "main.py"]




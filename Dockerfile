# Seleccion del lenguaje y version.

FROM apache/airflow:2.8.4
COPY requirements.txt .
RUN pip install -r requirements.txt
ENTRYPOINT [ "/usr/bin/dumb-init", "--", "/entrypoint"]
CMD []





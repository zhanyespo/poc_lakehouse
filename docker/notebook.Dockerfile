FROM jupyter/datascience-notebook:python-3.11

USER root

RUN pip install --no-cache-dir \
    duckdb>=0.10.2 \
    deltalake \
    s3fs \
    boto3 \
    psycopg2-binary

USER jovyan

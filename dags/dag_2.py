from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
from sql_statements import sql_dict

with DAG(
        dag_id='2_select_values',
        start_date=datetime(2022, 9, 22),
        catchup=False,
        schedule_interval='@once',
        tags=['dag_2']
) as dag:
    task1 = PostgresOperator(
        task_id='copy_el_usd', postgres_conn_id='my_db', autocommit=True,
        sql=sql_dict['copy_el_usd'])

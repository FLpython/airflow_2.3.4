from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
from sql_statements import sql_dict
from airflow.operators.trigger_dagrun import TriggerDagRunOperator


with DAG(
        dag_id='1_insert_values',
        # default_args=default_args,
        description='creates_table',
        start_date=datetime(2022, 9, 22),
        catchup=False,
        schedule_interval='@once',
        tags=['dag_1']
) as dag:
    trigger_target = TriggerDagRunOperator(
        task_id='trigger_dag2',
        trigger_dag_id='2_create_table',
        reset_dag_run=True,
        wait_for_completion=True
    )

    task1 = PostgresOperator(
        task_id='insert_values', postgres_conn_id='my_db', autocommit=True,
        sql=sql_dict['insert_values'])
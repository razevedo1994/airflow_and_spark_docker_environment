from airflow import DAG
from pathlib import Path
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator


default_args = {
    "owner": "Rodrigo Azevedo",
    "start_date": datetime(2022, 9, 16),
    "retries": 2,
    "retry_delay": timedelta(seconds=10),
}

with DAG(
    Path(__file__).stem,
    default_args=default_args,
    catchup=False,
    schedule_interval="0 11 * * *",
    max_active_runs=1,
    concurrency=3,
) as dag:

    start = DummyOperator(task_id="Begin")

    spark = SparkSubmitOperator(
        task_id="teste_spark",
        application="/opt/airflow/dags/scripts/spark.py",
        conn_id="spark_conn",
    )

    end = DummyOperator(task_id="Ending")

    start >> spark >> end

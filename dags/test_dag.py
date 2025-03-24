from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# DAG 기본 설정
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 24),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# DAG 정의
with DAG(
    dag_id='my_first_dag',
    default_args=default_args,
    description='My first DAG in Airflow!',
    schedule_interval=timedelta(days=1),  # 매일 실행
    catchup=False,
) as dag:

    def print_hello():
        print("Hello, Airflow!")

    # Task 생성
    task_1 = PythonOperator(
        task_id='say_hello',
        python_callable=print_hello,
    )

    task_1  # DAG 실행 흐름 정의 (단일 Task)


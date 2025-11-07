# ~/airflow/dags/glue_redshift_etl_dag.py
from datetime import datetime
from airflow import DAG

# Try imports in order of provider versions/paths until one works
OperatorClass = None
_import_errors = []

try:
    # preferred in many newer provider versions
    from airflow.providers.amazon.aws.operators.glue_job import GlueJobOperator
    OperatorClass = GlueJobOperator
except Exception as e:
    _import_errors.append(("glue_job.GlueJobOperator", repr(e)))

if OperatorClass is None:
    try:
        # older style location / name (many 2.x provider releases)
        from airflow.providers.amazon.aws.operators.glue import AwsGlueJobOperator
        OperatorClass = AwsGlueJobOperator
    except Exception as e:
        _import_errors.append(("glue.AwsGlueJobOperator", repr(e)))

if OperatorClass is None:
    try:
        # alternative older name (some older providers used this)
        from airflow.providers.amazon.aws.operators.glue import GlueJobOperator as GlueJobOperatorAlt
        OperatorClass = GlueJobOperatorAlt
    except Exception as e:
        _import_errors.append(("glue.GlueJobOperatorAlt", repr(e)))

# If none found, raise ImportError with helpful debug info
if OperatorClass is None:
    raise ImportError(
        "No compatible Glue operator found in apache-airflow-providers-amazon. "
        "Tried: {}\nInstall a compatible provider (e.g. pip install "
        "'apache-airflow-providers-amazon>=9.4.0')".format(", ".join(n for n, _ in _import_errors))
    )


default_args = {
    'owner': 'sameer',
    'depends_on_past': False,
    'start_date': datetime(2025, 11, 6),
    'retries': 0,
}

with DAG(
    dag_id='glue_redshift_etl_dag',
    default_args=default_args,
    description='Trigger Glue ETL job (red) to load into Redshift — universal import',
    schedule_interval=None,
    catchup=False,
    tags=['glue', 'redshift', 'etl'],
) as dag:

    run_glue_job = OperatorClass(
        task_id='run_glue_job',
        job_name='red',  # ← your Glue job name (exact)
        script_args={
            '--TempDir': 's3://aws-glue-assets-969385807464-eu-north-1/temporary/',
            '--job-bookmark-option': 'job-bookmark-disable',
        },
        region_name='eu-north-1',
        aws_conn_id='aws_default',
        wait_for_completion=True,
    )

    run_glue_job
# ~/airflow/dags/glue_redshift_etl_dag.py
from datetime import datetime
from airflow import DAG

# Try imports in order of provider versions/paths until one works
OperatorClass = None
_import_errors = []

try:
    # preferred in many newer provider versions
    from airflow.providers.amazon.aws.operators.glue_job import GlueJobOperator
    OperatorClass = GlueJobOperator
except Exception as e:
    _import_errors.append(("glue_job.GlueJobOperator", repr(e)))

if OperatorClass is None:
    try:
        # older style location / name (many 2.x provider releases)
        from airflow.providers.amazon.aws.operators.glue import AwsGlueJobOperator
        OperatorClass = AwsGlueJobOperator
    except Exception as e:
        _import_errors.append(("glue.AwsGlueJobOperator", repr(e)))

if OperatorClass is None:
    try:
        # alternative older name (some older providers used this)
        from airflow.providers.amazon.aws.operators.glue import GlueJobOperator as GlueJobOperatorAlt
        OperatorClass = GlueJobOperatorAlt
    except Exception as e:
        _import_errors.append(("glue.GlueJobOperatorAlt", repr(e)))

# If none found, raise ImportError with helpful debug info
if OperatorClass is None:
    raise ImportError(
        "No compatible Glue operator found in apache-airflow-providers-amazon. "
        "Tried: {}\nInstall a compatible provider (e.g. pip install "
        "'apache-airflow-providers-amazon>=9.4.0')".format(", ".join(n for n, _ in _import_errors))
    )


default_args = {
    'owner': 'sameer',
    'depends_on_past': False,
    'start_date': datetime(2025, 11, 6),
    'retries': 0,
}

with DAG(
    dag_id='glue_redshift_etl_dag',
    default_args=default_args,
    description='Trigger Glue ETL job (red) to load into Redshift — universal import',
    schedule_interval=None,
    catchup=False,
    tags=['glue', 'redshift', 'etl'],
) as dag:

    run_glue_job = OperatorClass(
        task_id='run_glue_job',
        job_name='red',  # ← your Glue job name (exact)
        script_args={
            '--TempDir': 's3://aws-glue-assets-969385807464-eu-north-1/temporary/',
            '--job-bookmark-option': 'job-bookmark-disable',
        },
        region_name='eu-north-1',
        aws_conn_id='aws_default',
        wait_for_completion=True,
    )

    run_glue_job


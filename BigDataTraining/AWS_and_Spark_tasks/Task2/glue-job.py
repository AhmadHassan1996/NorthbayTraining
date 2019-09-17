"""Runs a glue job to run the file stored in s3 bucket."""

import boto3

if __name__ == "__main__":
    GLUE_CLIENT = boto3.client('glue', 'us-east-1')

    try:
        GLUE_JOB = GLUE_CLIENT.create_job(
            Name='task2-glue-ahmad',
            Role='GlueSecret',
            Command={
                'Name': 'pythonshell',
                'ScriptLocation': 's3://task2-s3-bucket-ahmad/code-file.py',
                'PythonVersion': '3'
            },
            DefaultArguments={
                '--extra-py-files': 's3://task2-s3-bucket-ahmad/pymysql-0.9.3-py3.6.egg'
            },
        )
    finally:
        JOB_RUN = GLUE_CLIENT.start_job_run(
            JobName='task2-glue-ahmad'
        )

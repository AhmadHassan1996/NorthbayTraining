"""Creates an s3 bucket and stores two files in it."""

import boto3

if __name__ == "__main__":
    S3_CLIENT = boto3.client('s3')
    S3_NAME = S3_CLIENT.create_bucket(Bucket='task2-s3-bucket-ahmad')

    with open('code-file.py', 'rb') as data:
        S3_CLIENT.upload_fileobj(
            data,
            'task2-s3-bucket-ahmad',
            'code-file.py'
        )

    with open('template.yaml', 'rb') as data:
        S3_CLIENT.upload_fileobj(
            data,
            'task2-s3-bucket-ahmad',
            'template.yaml'
        )

    with open('pymysql-0.9.3-py3.6.egg', 'rb') as data:
        S3_CLIENT.upload_fileobj(
            data,
            'task2-s3-bucket-ahmad',
            'pymysql-0.9.3-py3.6.egg'
        )

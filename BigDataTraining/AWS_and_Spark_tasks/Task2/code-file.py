"""Code to access an RDS instance."""

import base64
import ast
import pymysql
import boto3
from botocore.exceptions import ClientError

if __name__ == "__main__":
    CLIENT = boto3.client(
        service_name='secretsmanager',
        region_name='us-east-1'
    )

    try:
        GET_SECRET_VALUE_RESPONSE = CLIENT.get_secret_value(
            SecretId='dbInfo'
        )
    except ClientError as error:
        raise error
    else:
        if 'SecretString' in GET_SECRET_VALUE_RESPONSE:
            SECRET = GET_SECRET_VALUE_RESPONSE['SecretString']
        else:
            SECRET = base64.b64decode(GET_SECRET_VALUE_RESPONSE['SecretBinary'])

    SECRET = ast.literal_eval(SECRET)

    try:
        CONNECTION = pymysql.connect(
            host=SECRET['host'],
            user=SECRET['username'],
            password=SECRET['password'],
            port=SECRET['port'],
            database=SECRET['db']
        )
    finally:
        CURSOR = CONNECTION.cursor()
        CURSOR.execute('SELECT * FROM cars')

        for result in CURSOR.fetchall():
            print(result)

        CONNECTION.close()

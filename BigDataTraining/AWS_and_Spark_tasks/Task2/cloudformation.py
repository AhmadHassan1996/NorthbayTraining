"""Creates a cloudformation stack using yaml template."""

import boto3

if __name__ == "__main__":
    CLOUDFORM_CLIENT = boto3.client('cloudformation', 'us-east-1')
    CLOUDFORM_NAME = CLOUDFORM_CLIENT.create_stack(
        StackName='taqtest1',
        TemplateURL='https://task2-s3-bucket-ahmad.s3.amazonaws.com/template.yaml'
    )

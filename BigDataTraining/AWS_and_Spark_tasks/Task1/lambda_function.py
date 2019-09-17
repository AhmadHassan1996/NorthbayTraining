"""Lambda function to be accessed by APIGateway."""

def lambda_handler(event):
    """Returns string with 'Hello ' and the given name in event."""
    return 'Hello ' + event['queryParams']['name']

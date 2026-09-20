import json
from datetime import datetime, timezone


def lambda_handler(event, context):

    response = {
        "statusCode": 200,
        "message": "Hello from Lambda!",
        "environment": "AWS",
        "deployment": "GitHub Actions",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

    print("Lambda executed successfully")
    print(json.dumps(response))

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }
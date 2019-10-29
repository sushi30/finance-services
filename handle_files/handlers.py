import os

import boto3


def submit(event, context):
    print(event)
    file = event["file"]
    rid = context.aws_request_id.replace("-")
    boto3.resource("s3").object(os.getenv("S3_BUCKET"), "pending/" + rid).put(file)
    return {"statusCode": 202, "body": rid}


def retrieve(event, context):
    rid = event["body"]
    s3_object = boto3.resource("s3").object(os.getenv("S3_BUCKET"), "ready/" + rid)
    obj = s3_object.get()["Body"].read()
    obj.delete()
    return {"statusCode": 200, "Body": obj}

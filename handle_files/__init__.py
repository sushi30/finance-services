import boto3


def handler(event, context):
    file = event["file"]
    rid = context.aws_request_id.replace("-")
    boto3.resource("s3").object("files/" + rid).put(file)

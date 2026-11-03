import boto3
import json

def lambda_handler(event, context):
    s3= boto3.client("ec2")
    

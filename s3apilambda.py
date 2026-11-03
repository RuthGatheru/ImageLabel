import json
import boto3

client = boto3.client('s3')

def lambda_handler (event,context):
    bucket = event['bucket']
    key = event['key']

    response = client.get_object(
    Bucket= bucket,
    Key= key)

    data_bytes = response['Body'].read()
    data_string = data_bytes.decode('UTF-8')
    data_dict = json.loads(data_string)
    print(data_dict)

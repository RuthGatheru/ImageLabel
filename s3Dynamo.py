import json
import boto3

client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event,context):
    response = client.get_object(
    Bucket='aws-s3-dynamo-bucket',
    Key='string'
)
    #convert from streaming data to byte
    json_data = response["Body"]
    print(json_data)
    print(type(json_data))
    #convert from streaming bytes to string
    data_string = json_data.decode('UTF-8')
    print(data_string)
    print(type(data_string))
#convet from json string to dictionary

    data_dict = json.loads(data_string)
    print(data_dict)
    print(type(data_dict))

    table = dynamodb.Table('RetailsalesNyathigi')
    table.put_item (
        Item = data_dict
    )

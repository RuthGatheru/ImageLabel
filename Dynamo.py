import json
import boto3

client = boto3.client('dynamodb')

def lambda_handler(event, context):
    response = client.create_table(
        #creating the dynamo db table

    AttributeDefinitions=[
        {
            'AttributeName': 'CustomerID',
            'AttributeType': 'S'
        },

        {
            'AttributeName': 'Product',
            'AttributeType': 'S'
        },
    ],
    TableName='RetailSalesGatheru',
    KeySchema=[
        {
            'AttributeName': 'CustomerID',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'Product',
            'KeyType': 'RANGE'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
    )
    print(response)

#adding items to the table in dynamo db
result = client.put_item(
  
    TableName='RetailSalesGatheru',
    Item={
        'CustomerID': {
            'S': '001'
        },
    
        'Product': {
            'S': 'Mangoes'
        },
        'Quantity': {
            'N': '100'
        },
        'Address': {
            'S': '1909 Prestige Tranquil'
        }
        }
    )  
print (result)
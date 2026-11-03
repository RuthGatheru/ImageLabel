import json
import boto3

client = boto3.client('rekognition')
s3 = boto3.client('s3')

def lambda_handler(event, context):
#retrueve the pictures from s3
    response = s3.get_object(
        Bucket='image-reko-s3',
        Key='image.jpeg'
        )

    image = response['Body'].read()
    #label the image using amazon rekognition 

    image_labels = client.detect_labels(
        Image={
            'S3Object': {
                'Bucket': 'image-reko-s3',
                'Name': 'image.jpeg'
            }
            },
            MaxLabels=5,
            MinConfidence=90
    )

    print(image_labels)

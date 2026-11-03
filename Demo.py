import boto3
import json

client = boto3.client("ec2")

 #creating an Ec2 Instance
def lambda_handler(event, context):
    response = client.run_instances(
        ImageId = "string",
        InstaceType = "t2.micro",
        MaxCount = 1,
        MinCount = 1
        )
    print(response['Instances'][0]["InstanceId"])

 #stopping an Ec2 Instnace
def lambda_handler(event, context):
    stopEc2 = client.stop_instances(
        InstanceIds = ["string"])
    print(stopEc2)

 #starting an Ec2 Instance
def lambda_handler(event, context):
    startEc2 = client.start_instances(
        InstanceIds = ["string"]
    )
    print(startEc2)
import json
import boto3

s3 = boto3.client('s3')
polly = boto3.client('polly')

def lambda_handler(event, context):
    #retrieve the text from s3 bucket
    response = s3.get_object(
    Bucket='my-textfile',
    Key='textfile.txt'
    )

    text = response["Body"].read()
    #convert from streaming bytes to string
    text_bytes = text.decode('UTF-8').strip()

    #send the text to amazon polly
    result = polly.synthesize_speech(
    OutputFormat='mp3',
    Text= text_bytes,
    VoiceId = 'Joanna')

    #read the audio
    audio = result['AudioStream'].read()

    #upload the audio to the destination  bucket 
    s3.put_object(
    Bucket='my-audiofile',
    Key="speech.mp3",
    Body=audio,
    ContentType="audio/mpeg"
)
    print("Audio saved to the destination S3 bucket!")
import boto3
import random
import time
from datetime import datetime

AWS_REGION = 'us-east-1'

client = boto3.client('logs', region_name = AWS_REGION)

messages = ['App Created', 'App Runing', 'No Response Found', "Request Sent"] #Sample log messages to use

response = client.create_log_stream(
    logGroupName = 'New_Log_Group',
    logStreamName = 'New_App_Logs' # Name of the log stream where the logs will be stored
)

seq_token = None


for i in range(10):  #Using range(10) to print just 10 log messages
    log_event = {
        'logGroupName' : 'New_Log_Group',
        'logStreamName' : 'New_App_Logs',
        'logEvents' : [
            {
                'timestamp' : int(round(time.time() * 1000)),
                #random.randint picks a random integer between 0 and 3 and that is used to choose which log message to print
                #Example: First it picks 0, then it'll be messages[0] and the App Created message will be printed out
                'message' : messages[random.randint(0, 3)] 
            },
        ],
    }

    if seq_token:
        log_event['sequenceToken'] = seq_token

    response = client.put_log_events(**log_event) #To send all the logs to the log stream that is created

    seq_token = response['nextSequenceToken'] #sequenceToken is the response obtained from the previous log event
    time.sleep(1)

print("Successfully generated and added the logs.")
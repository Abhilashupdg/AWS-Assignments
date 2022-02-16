#Importing boto3 module
import boto3
#Importing json to display the output that the log group is created in json format
import json

AWS_REGION = 'us-east-1' #The region in which I'm running AWS

client = boto3.client('logs', region_name=AWS_REGION)
retention_period_in_days = 30 #How long to retain the log group

#Creating a New Log Group
log_group = 'New_Log_Group' #Name of the log group
response = client.create_log_group(
    logGroupName = log_group,
    tags = {
        'Type' : 'Demo',
        'Frequency' : '30 seconds',
        'Environment' : 'Development',
        'RetentionPeriod' : str(retention_period_in_days)
    }
)

#Setting how long the log group should be retained
response = client.put_retention_policy(logGroupName = log_group, retentionInDays = retention_period_in_days)
print(json.dumps(response, indent=4)) #Printing out the details of the log group
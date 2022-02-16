import boto3

client = boto3.client('s3')

response = client.create_bucket(
    ACL='private',
    Bucket='botobucket220121',
    #CreateBucketConfiguration={
        #'LocationConstraint': 'us-east-1'
    #},
)

print(response)
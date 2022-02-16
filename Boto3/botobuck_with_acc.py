import boto3

client = boto3.client('s3')

response = client.put_bucket_accelerate_configuration(
    Bucket='botobucket220121', #the bucket for which the tranfer acceleration has to be enabled
    AccelerateConfiguration={
        'Status': 'Enabled'    #setting the status to enabled so that transfer acceleration for this bucket works
    },
    ExpectedBucketOwner='779395302932' #the user id in which the bucket is present
)

print(response)


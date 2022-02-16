import json
import csv
import boto3

def lambda_handler(event, context):
    region : 'us-east-1'
    record_list = [] 
    
    try:
        s3 = boto3.client('s3')
        
        dynamodb = boto3.client('dynamodb')
        bucket = event['Records'][0]['s3']['bucket']['name'] #to get the name of the bucket
        key = event['Records'][0]['s3']['object']['key'] #to get the name of the csv file that has been uploaded
        
        print('Bucket: ', bucket, 'Key: ', key)
        
        csv_file = s3.get_object(Bucket = bucket, Key=key)
        
        record_list = csv_file['Body'].read().decode('utf-8').split('\n') #the records in the csv file are read
        
        csv_reader = csv.reader(record_list, delimiter = ',', quotechar = '"') 
        
        for row in csv_reader: #adding column names for the records in the file
            food_name = row[0]
            scientific_name = row[1]
            group = row[2]
            sub_group = row[3]
            
            print('Food Name: ', food_name, 'Scientific Name: ', scientific_name, 'Group: ', group, 'Sub Group: ', sub_group)
            
            # moving all the records from the csv file to the table called 'food_names' that was created
            add_to_db = dynamodb.put_item(
                TableName = 'food_names',
                Item = {
                    'food_name' : {'S': str(food_name)},
                    'scientific_name' : {'S': str(scientific_name)},
                    'group' : {'S': str(group)},
                    'sub_group' : {'S': str(sub_group)},
                }
                
                )
            print('Successfuly added all the records to the table.')
        
    except Exception as e:
        print(str(e))
        
    return {
        'statusCode': 200,
        'body': json.dumps('Transfer Success')
    }

import json
import boto3
from boto3.dynamodb.conditions import Key, Attr


client = boto3.resource('dynamodb')
table = client.Table('scientific-food-name') #the table from which to query 


def lambda_handler(event, context):
    food_name = event['key1']
    print('The name of the food is : ', event['key1'])
    response = table.query(
        KeyConditionExpression = Key("food_name").eq(event['key1']) 
        )
    
    item = response['Items']
    scientific_name = item[0]['scientific_name']
    print('The scientific name of {} is {}.'.format(event['key1'], scientific_name))
    
    return {
        'statusCode': 200,
        'body': json.dumps('Successful in running the code.')
    }


import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

client = boto3.resource('dynamodb')
table = client.Table('scientific-food-name') #the table from which to query


def lambda_handler(event, context):
    
    response = table.scan(FilterExpression = Attr('group').eq('Vegetables'))
    
    item = response['Items']
    print('The vegetable food group and the food names: ' , item)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Successful in running the code.')
    }


    


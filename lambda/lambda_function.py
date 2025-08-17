import os
import boto3
import json
from decimal import Decimal

table_name = os.environ['TABLE_NAME']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        response = table.update_item(
            Key={'id': 'counter'},
            UpdateExpression='SET #v = if_not_exists(#v, :start) + :inc',
            ExpressionAttributeNames={'#v': 'views'},
            ExpressionAttributeValues={':inc': 1, ':start': 0},
            ReturnValues='UPDATED_NEW'
        )
        views = response['Attributes']['views']
        if isinstance(views, Decimal):
            views = int(views)
        
        return {
            'statusCode': 200,
            'body': json.dumps({'views': views}),
            'headers': {'Content-Type': 'application/json'}
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'headers': {'Content-Type': 'application/json'}
        }

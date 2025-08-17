import boto3
import json
from decimal import Decimal

def lambda_handler(event, context):
    try:
        dynamodb = boto3.resource('dynamodb', region_name='eu-east-1')
        print("Connecting to table: pageviewresume in region eu-north-1")

        table = dynamodb.Table('pageviewresume')

        response = table.update_item(
            Key={'id': 'counter'},
            UpdateExpression='SET #v = if_not_exists(#v, :start) + :inc',
            ExpressionAttributeNames={
                '#v': 'views'
            },
            ExpressionAttributeValues={
                ':inc': 1,
                ':start': 0
            },
            ReturnValues='UPDATED_NEW'
        )

        views = response['Attributes']['views']
        if isinstance(views, Decimal):
            views = int(views)

        return {
            'statusCode': 200,
            'body': json.dumps({'views': views}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }

    except Exception as e:
        print("ERROR:", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }

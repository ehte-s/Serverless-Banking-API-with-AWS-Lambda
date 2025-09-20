import json
import boto3

def lambda_handler(event, context):
    # Get account ID from the web request
    account_id = event['pathParameters']['accountId']
    
    # Look up balance in database
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('BankAccounts')
    
    response = table.get_item(Key={'accountId': account_id})
    
    if 'Item' in response:
        balance = response['Item']['balance']
        return {
            'statusCode': 200,
            'body': json.dumps({'accountId': account_id, 'balance': float(balance)})
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps({'error': 'Account not found'})
        }

import boto3

dynamodb_resource = boto3.resource('dynamodb')
users_table = dynamodb_resource.Table('SocialNetworkUsers')

def lambda_handler(event, context):
    uid = event['requestContext']['authorizer']['lambda']['uid']

    users_table.put_item(
        Item={ 'userId': uid }, 
        ConditionExpression='userId <> :uid', 
        ExpressionAttributeValues={ ':uid': uid }
    )
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        }
    }

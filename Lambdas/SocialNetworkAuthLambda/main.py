import os
import firebase_admin
from firebase_admin import auth

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'firebase_keys.json'

firebase_admin.initialize_app()

def lambda_handler(event, context):
    auth_token = event['headers']['authtoken']
    if auth_token == None:
        return { 
            'isAuthorized': False,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            }
        }
    
    try:
        decoded_token = auth.verify_id_token(auth_token)
    except Exception as e:
        return { 
            'isAuthorized': False,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            }
        }

    uid = decoded_token['uid']
    return {
        'isAuthorized': True,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'context': { 'uid': uid }
    }

# Live Product
https://www.open-forumz.com

# Installation

## 1. Firebase
1. Generate admin SDK private key: Firebase -> Project Settings -> Service accounts -> Generate new private key -> Rename to firebase_keys.json

## 2. DyanmoDB
1. Create a DynamoDB table called "SocialNetworkUsers", with a string partition key called "userId"

## 3. Lambda
1. Create the appropriate Lambdas (python3.11) and Lambda Layers
2. Upload the firebase_keys.json to all Lambdas
3. Provide the appropriate permissions to your Lambdas (e.g. DynamoDB Full Access)

## 4. API Gateway
1. Create a HTTP API in Amazon Api Gateway called "social-network-api"
2. Create the following paths and associate the correct Lambdas:
- POST /register -> RegisterLambda
3. Create authorizers for all the previously specified paths
- Identity source for the authorizers: $request.header.AuthToken
4. Navigate to the CORS tab and configure it as such:
- Access-Control-Allow-Origin: *
- Access-Control-Allow-Headers: *
- Access-Control-Allow-Methods: *
- Access-Control-Expose-Headers: <leave empty>
- Access-Control-Max-Age: 300 Seconds
- Access-Control-Allow-Credentials: NO
5. Production only: Custom Domain Names -> Create -> api.<your-domain> -> Select the appropriate certificate -> Create -> Then navigate to API Mappings -> Configure API Mappings -> Link with your API
6. Production only: Navigate to Amazon Route53 -> Hosted Zones -> Select your hosted zone -> Create an alias A record to your API Gateway

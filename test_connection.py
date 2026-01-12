import boto3

session = boto3.Session(profile_name='TestUser6')
s3 = session.client('s3')

response = s3.list_buckets()

print('Connected Buckets:')

for bucket in response['Buckets']:
    print(bucket['Name'])

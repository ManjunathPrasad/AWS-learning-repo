import boto3

s3 = boto3.client('s3')

bucket_name = 'my-cf-s3-demo-bucket-123'

# s3.create_bucket(
#     Bucket=bucket_name,
#     CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'}
# )

s3.upload_file(
    'sample.txt',
    bucket_name,
    'sample.txt'
)

print("Bucket created and file uploaded successfully")

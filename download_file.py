import boto3

s3 = boto3.client('s3')
bucket_name = 'my-cf-s3-demo-bucket-123'

# List objects
objects = s3.list_objects_v2(Bucket=bucket_name)
for obj in objects.get('Contents', []):
    print(obj['Key'])

# Download file
s3.download_file(bucket_name, 'sample.txt', 'downloaded.txt')

# Delete file
# s3.delete_object(Bucket=bucket_name, Key='sample.txt')

print("List, download, and delete operations completed")

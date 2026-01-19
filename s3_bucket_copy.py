import boto3
from botocore.exceptions import ClientError

SOURCE_BUCKET = "my-boto3-demo-bucket-jan-13"
DEST_BUCKET = "my-boto3-demo-bucket-jan-19"
REGION = "ap-south-1"

s3 = boto3.client("s3", region_name=REGION)

def ensure_bucket_exists(bucket_name):
    try:
        s3.head_bucket(Bucket=bucket_name)
        print(f"Bucket exists: {bucket_name}")
    except ClientError as e:
        error_code = e.response["Error"]["Code"]
        if error_code in ("404", "NoSuchBucket"):
            print(f"Creating bucket: {bucket_name}")
            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={
                    "LocationConstraint": REGION
                }
            )
            print("Bucket created")
        else:
            raise



def copy_bucket_contents():
    response = s3.list_objects_v2(Bucket=SOURCE_BUCKET)

    if "Contents" not in response:
        print("Source bucket is empty")
        return

    for obj in response["Contents"]:
        copy_source = {
            "Bucket": SOURCE_BUCKET,
            "Key": obj["Key"]
        }

        s3.copy_object(
            CopySource=copy_source,
            Bucket=DEST_BUCKET,
            Key=obj["Key"]
        )

        print(f"Copied: {obj['Key']}")


# -------- MAIN --------
ensure_bucket_exists(DEST_BUCKET)
copy_bucket_contents()

print("Bucket copy completed")

import boto3
import botocore

client = boto3.client('s3')
s3 = boto3.resource('s3')

buckets = client.list_buckets()

for bucket in buckets['Buckets']:
    if(bucket['Name']=="awspersonalbucketpeternguyen"):
        continue
    s3_bucket = s3.Bucket(bucket['Name'])
    print(f"buckets currently getting deleted: {bucket}")
    s3_bucket.objects.all().delete()
    s3_bucket.objects_versions.delete()
    s3_bucket.delete()
   

import boto3

#Retrieves the list of existing buckets
s3 = boto3.client('s3')
response = s3.list_buckets()

#Outputs the bucket names
print("Existing Bucket")
for bucket in response['Bucket']:
    print(f' {bucket["Name"]}')

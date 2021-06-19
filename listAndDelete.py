import boto3

#Retrieves the list of existing buckets
s3 = boto3.client('s3')
s3Resource = boto3.resource('s3')


response = s3.list_buckets()
#print(type(response))

#List to collect all bucket names
lst = list()

#Outputs the bucket names
print("Existing Bucket")
for bucket in response['Buckets']:
    #print(f' {bucket["Name"]}')
    lst.append(bucket["Name"])

#print(lst)

def deletelistofbuckets(lst):
    for bucket in lst:
        s3_bucket = s3Resource.Bucket(bucket)
        s3_bucket.objects.all().delete()
        print(f'Deleting all objects in {bucket}')

deletelistofbuckets(lst)

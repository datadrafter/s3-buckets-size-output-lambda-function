import boto3

def lambda_handler(event,context):
    destination_bucket = "your-destination-bucket-for-output"
    #create a client to interact with S3
    s3 = boto3.client('s3')

    #get the list of all s3 buckets within an environment
    buckets = s3.list_buckets()['Buckets']

    #Open a new output file for writing
    output_file = open('/tmp/bucket_size.txt', 'w')

    #iterate over the buckets and get their sizes
    for bucket in buckets:
        bucket_name = bucket['Name']

        bucket_size = 0
        response = s3.list_objects_v2(Bucket=bucket_name)
        bucket_size+=obj['Size']

        #write the name and size of the bucket to the text file we opened
        output_file.write(f'{bucket_name}: {bucket_size}')

    output_file.close()

    #upload the file to s3
    s3.upload_file('/tmp/bucket_size.txt', destination_bucket, bucket_size.txt)
    
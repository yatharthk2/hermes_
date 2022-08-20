from secrets import access_key, secret_access_key

import boto3

  #file path to upload
def add_to_S3(file_name):

    client = boto3.client('s3',
                            aws_access_key_id = access_key,
                            aws_secret_access_key = secret_access_key)
    bucket = 'bots'
    store_as = 'bots/' + str(bot.botname) + str(file) 
    client.upload_file(file_name, bucket, store_as)



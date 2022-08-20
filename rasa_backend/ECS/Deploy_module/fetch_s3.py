
from secrets import access_key, secret_access_key

import boto3
import os
client = boto3.client('s3',
                        aws_access_key_id = access_key,
                        aws_secret_access_key = secret_access_key)
bucket_name = 'bots'
save_as = None #pth to don\wnlaod 
path_to_download = 'bot/' + str(bot.name) + str(file) 
client.download_file(bucket_name, path_to_download, save_as)


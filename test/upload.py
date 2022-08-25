access_key = 'AKIAYAPVILXZIAVZ3UN2'
secret_access_key = '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'
import boto3

client = boto3.client('s3',
                            aws_access_key_id = access_key,
                            aws_secret_access_key = secret_access_key)




client.download_file('yatharthk', 'h4_bot.tar.gz', 'test/h4_bot.tar.gz')
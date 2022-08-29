from decouple import config


import boto3
from flask import Flask,jsonify
import os



access_key = config('access_key')
secret_access_key = config('secret_access_key')



app = Flask(__name__)
@app.route("/<name>", methods=['GET', 'POST'])
def train(name):
    client = boto3.client('s3',
                            aws_access_key_id = access_key,
                            aws_secret_access_key = secret_access_key)
    bucket_name = 'yatharthk'
    save_as = '{}.tar.gz'.format(name) 
    path_to_download ='{}.tar.gz'.format(name) 
    client.download_file(bucket_name, save_as, path_to_download)
    os.system("rasa run --model {}.tar.gz".format(name))
    return jsonify({"status":"success"})

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8005))
    app.run(debug=True, port=port,host="0.0.0.0")    


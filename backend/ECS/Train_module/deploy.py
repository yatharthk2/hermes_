from time import clock_getres
from flask import Flask,jsonify
import os
from fetch_mongo import *
import boto3
from decouple import config
global_init()
access_key = config('access_key')
secret_access_key = config('secret_access_key')
app = Flask(__name__)

@app.route("/<name>", methods=['GET', 'POST'])
def deploy(name):
        temp_bot=get_bot_details(name)
        #os.system("cd data")
        temp_bot_NLU = temp_bot.NLU
        print(temp_bot_NLU)
        temp_bot_Domain = temp_bot.Domain
        temp_bot_story = temp_bot.Story
        temp_bot_Rules = temp_bot.Rules
        
        files_s=[{"name":temp_bot_NLU,"type":"data/nlu.yml"},{"name":temp_bot_Domain,"type":"domain.yml"},{"name":temp_bot_story,"type":"data/story.yml"},{"name":temp_bot_Rules,"type":"data/rules.yml"}]
        for i in files_s:
                f = open(i["type"], "w")
                f.write(str(i["name"]))
                f.close()
                
        os.system("rasa train --fixed-model-name /models/{}.gz".format(name))
        client = boto3.client('s3',
                            aws_access_key_id = access_key,
                            aws_secret_access_key = secret_access_key)
        file_name="./models/{}.tar.gz".format(name)
        bucket = 'yatharthk'
        store_as = '{}.tar.gz'.format(name)  
        client.upload_file(file_name, bucket, store_as)
        return jsonify({"status":"success"})
    
    
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    app.run(debug=True, port=port,host="0.0.0.0")    
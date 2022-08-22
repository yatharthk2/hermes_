from flask import Flask,jsonify
import os
from fetch_mongo import get_bot_details,global_init
import boto3
global_init()
access_key = 'AKIAQSW32ZL55362L35W'
secret_access_key = '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'
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
        temp_bot_Form = temp_bot.Form
        files_s=[{"name":temp_bot_NLU,"type":"NLU.yml"},{"name":temp_bot_Domain,"type":"Domain.yml"},{"name":temp_bot_story,"type":"Story.yml"},{"name":temp_bot_Rules,"type":"Rules.yml"},{"name":temp_bot_Form,"type":"Form.yml"}]
        for i in files_s:
                f = open(i["type"], "w")
                f.write(i["name"])
                f.close()
                
        os.system("rasa train --fixed-model-name ./models/{}.gz".format(name))
        client = boto3.client('s3',
                            aws_access_key_id = access_key,
                            aws_secret_access_key = secret_access_key)
        file_name="./models/{}.gz".format(name)
        bucket = 'bots'
        store_as = 'bots/' + str(name)  
        client.upload_file(file_name, bucket, store_as)
        return jsonify({"status":"success"})
    
    
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, port=port)
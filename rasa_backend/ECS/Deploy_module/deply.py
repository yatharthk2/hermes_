from flask import Flask,jsonify
import os
# from fetch_mongo import get_bot_details,global_init
import boto3
global_init()
access_key = 'AKIAQSW32ZL55362L35W'
secret_access_key = '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'
app = Flask(__name__)

@app.route("/<name>", methods=['GET', 'POST'])
def deploy(name):
        client = boto3.client('s3',
                        aws_access_key_id = access_key,
                        aws_secret_access_key = secret_access_key)
        
        bucket_name = 'bots'
        save_as = None #pth to don\wnlaod 
        path_to_download = 'bot/' + str(bot.name) + str(file) 
        client.download_file(bucket_name, path_to_download, save_as)
        # s3 ke path variables set karne baki hai ,, wo tu kar dena 

        os.system("rasa run --enable-api --cors '*' --model-path ./models/{}.gz --endpoint http://localhost:5005".format(name))

        




        # temp_bot=get_bot_details(name)
        # #os.system("cd data")
        # temp_bot_NLU = temp_bot.NLU
        # print(temp_bot_NLU)
        # temp_bot_Domain = temp_bot.Domain
        # temp_bot_story = temp_bot.Story
        # temp_bot_Rules = temp_bot.Rules
        # temp_bot_Form = temp_bot.Form
        # f = open("NLU.yml", "a")
        # f.write(str(temp_bot_NLU))
        # f.close()
        # s="echo '{}' > NLU.yml".format(temp_bot_NLU)
        # #os.system(s)
        # # os.system("echo '{}' > stories.yml".format(temp_bot_story))
        # # os.system("echo '{}' > rules.yml".format(temp_bot_Rules))
        # # #os.system("cd ..")
        # # os.system("echo '{}' > domain.yml".format(temp_bot_Domain))
        # # os.system("echo '{}' > forms.yml".format(temp_bot_Form))
        
        # os.system("rasa train --fixed-model-name ./models/{}.gz".format(name))
        # client = boto3.client('s3',
        #                     aws_access_key_id = access_key,
        #                     aws_secret_access_key = secret_access_key)
        # file_name="./models/{}.gz".format(name)
        # bucket = 'bots'
        # store_as = 'bots/' + str(name)  
        # client.upload_file(file_name, bucket, store_as)
        # return jsonify({"status":"success"})
    
    
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, port=port)
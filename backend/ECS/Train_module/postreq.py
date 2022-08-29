import requests
dictToSend = {'botname':'zippy'}
res = requests.get('http://localhost:5000/', json=dictToSend)
print ('response from server:',res.text)

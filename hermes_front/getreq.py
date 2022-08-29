# importing the requests library
import requests
  
# api-endpoint
URL = "http://h-388555080.us-east-1.elb.amazonaws.com"
botname="zippy"
requests.get(f"{URL}/{botname}")
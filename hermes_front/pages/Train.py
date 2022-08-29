import streamlit as st

from mongoengine import connect
import streamlit.components.v1 as components
from chalicelib.mongo_code.data.mongo_setup import global_init
from chalicelib.mongo_code import program_hosts
import webbrowser
train = st.button(label="Train")
deploy= st.button(label="Deploy")
send= st.button(label="Send")

if train:
    # Hit train URL AWS
    pass

if send:
    global_init()
    program_hosts.run()
    
if deploy:
    #hit deploy URL on AWS
    pass
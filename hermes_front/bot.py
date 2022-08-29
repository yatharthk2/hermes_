import streamlit as st
import pandas as pd
import numpy as np
import json

st.sidebar.markdown("# SIH 2022")



email=st.text_input(label="Email")
orgname=st.text_input(label="Org Name")
botname=st.text_input(label="Bot Name")
emailDict={"email":email,"orgName":orgname,"botName":botname}

access=st.button(label="Access")
if access:
    with open('email.json', 'w') as fp:
        json.dump(emailDict, fp)
import streamlit as st # rules.py
import random
import json

f = open("data.json")
names = []
data = json.load(f)
for i in data:
    names.append(i)

f2 = open("dataDomain.json")
actions = []
data2 = json.load(f2)
for i in data2:
    actions.append(i)

# for i in range(0, len(names)):
#     dropdown = st.selectbox("Please Select", names, key=i)
#     drop_list.append(dropdown)


rule = st.text_input(label="Enter rule")
intent_dropdown = st.selectbox("Intent Name", names)
action_dropdown = st.selectbox("Action Name", actions)


submit = st.button(label="submit")
if submit:
    examplesF = f"""version: \"3.1\"
rules:
- rule: {rule}
  steps:
  - intent: {intent_dropdown}
  - action: {action_dropdown}
"""
    file = open("rulesExample.yml", "w")
    file1=open("data/rules.yml","w")
    
    file.write(examplesF)
    file1.write(examplesF)
    file1.close()
    file.close()
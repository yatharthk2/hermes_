# import streamlit as st
# import random
# import string
# from pages import intents


# import json
  
# # Opening JSON file
# f = open('data.json')
# names=[]
# # returns JSON object as 
# # a dictionary
# data = json.load(f)
# for i in data:
#     names.append(i)

# examples=[]
# if 'n_rows' not in st.session_state:
#     st.session_state.n_rows = 1



# for i in range(len(names)):
#     #add text inputs here
#     examples.append(st.text_input(label=f"{names[i]}", key=i))
#     st.markdown("""---""")

# domainDict={}

# for key in names:
#     for value in examples:
#         value1=value.replace("\n","")
#         domainDict[key] = value1
#         examples.remove(value)
#         break

# print(names)
# domainF=f"""version: \"3.1\"
# intents:"""


# submit = st.button(label="submit")
# if submit:
#     for i in names:
#         domainF+=f"""
#     - {i}"""

#     domainF+=f"""
# responses:
# """

#     for i in domainDict:
#         domainF+=f"""  {i}:
#     - text: "{domainDict[i]}"
# """

#     file=open("domainExample.yml","w")
#     file.write(domainF)
#     file.close()

import streamlit as st # domain.py
import random
import string
from pages import intents


import json

# Opening JSON file
f = open("data.json")
names = []
# returns JSON object as
# a dictionary
data = json.load(f)
for i in data:
    names.append(i)

examples = []
if "n_rows" not in st.session_state:
    st.session_state.n_rows = 1


for i in range(len(names)):
    # add text inputs here
    examples.append(st.text_input(label=f"{names[i]}", key=i))
    st.markdown("""---""")

domainDict = {}

for key in names:
    for value in examples:
        value1 = value.replace("\n", "")
        domainDict[key] = value1
        examples.remove(value)
        break

print(names)
domainF = f"""version: \"3.1\"
intents:"""


submit = st.button(label="submit")
if submit:
    for i in names:
        domainF += f"""
    - {i}"""

    domainF += f"""
responses:
"""

    for i in domainDict:
        domainF += f"""  {i}:
    - text: "{domainDict[i]}"
"""

    file = open("domain.yml", "w")

    file.write(domainF)
    file.close()

    with open("dataDomain.json", "w") as fp:
        json.dump(domainDict, fp)
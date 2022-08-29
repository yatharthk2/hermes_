# import streamlit as st
# import random
# import string
# names=[]
# examples=[]
# if 'n_rows' not in st.session_state:
#     st.session_state.n_rows = 1

# add = st.button(label="add")
# remove=st.button(label="remove")

# if add:
#     st.session_state.n_rows += 1
#     st.experimental_rerun()
# if remove:
#     st.session_state.n_rows -= 1
#     st.experimental_rerun()

# for i in range(st.session_state.n_rows):
#     #add text inputs here
#     names.append(st.text_input(label="Intent Name", key=i))
#     examples.append(st.text_area(label="Example", key=i))
#     st.markdown("""---""")

# intentDict={}

# for key in names:
#     for value in examples:
#         value1=value.replace("\n","\n        - ")
#         intentDict[key] = [value1]
#         examples.remove(value)
#         break

# print(names)
# examplesF=f"""version: \"3.1\"
# nlu:"""

# # print(names)
# # print(examples)

# submit = st.button(label="submit")
# if submit:
#     for i in intentDict:
#         examplesF+=f"""
#     - intent: {i}
#       examples: |
#         - {intentDict[i][0]}
#     """
#     file=open("nluExample.yml","w")
#     file.write(examplesF)
#     file.close()
    
#     import json

#     with open('data.json', 'w') as fp:
#         json.dump(intentDict, fp)

import streamlit as st # intents.py
import random
import string

names = []
examples = []
if "n_rows" not in st.session_state:
    st.session_state.n_rows = 1

add = st.button(label="add")
remove = st.button(label="remove")

if add:
    st.session_state.n_rows += 1
    st.experimental_rerun()
if remove:
    st.session_state.n_rows -= 1
    st.experimental_rerun()

for i in range(st.session_state.n_rows):
    # add text inputs here
    names.append(st.text_input(label="Intent Name", key=i))
    examples.append(st.text_area(label="Example", key=i))
    st.markdown("""---""")

intentDict = {}

for key in names:
    for value in examples:
        value1 = value.replace("\n", "\n        - ")
        intentDict[key] = [value1]
        examples.remove(value)
        break

print(names)
examplesF = f"""version: \"3.1\"
nlu:"""

# print(names)
# print(examples)

submit = st.button(label="submit")
if submit:
    for i in intentDict:
        examplesF += f"""
    - intent: {i}
      examples: |
        - {intentDict[i][0]}
    """
    file = open("nluExample.yml", "w")
    file1=open("data/nlu.yml","w")
    file.write(examplesF)
    file1.write(examplesF)
    file.close()
    file1.close()

    import json

    with open("data.json", "w") as fp:
        json.dump(intentDict, fp)
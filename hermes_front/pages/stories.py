# import streamlit as st # stories.py
# import json


# f = open("data.json")
# names = []
# data = json.load(f)
# for i in data:
#     names.append(i)

# f2 = open("dataDomain.json")
# actions = []
# data2 = json.load(f2)
# for i in data2:
#     actions.append(i)


# if "n_rows" not in st.session_state:
#     st.session_state.n_rows = 1

# add = st.button(label="add")
# remove = st.button(label="remove")

# text_story=[]
# intent_dropdown=[]
# action_dropdown=[]
# if add:
#     st.session_state.n_rows += 1
#     st.experimental_rerun()
# if remove:
#     st.session_state.n_rows -= 1
#     st.experimental_rerun()
# for i in range(st.session_state.n_rows):
#     text_story.append(st.text_input(label="Enter your story name:",key=i))
#     intent_dropdown.append(st.selectbox("Intent Name", names,key=i))
#     action_dropdown.append(st.selectbox("Action Name", actions,key=i))
#     st.markdown("""---""")
# submit = st.button(label="submit")


# if submit:
#     examplesF = f"""version: \"3.1\"

# stories:

# - story: {text_story}
#   steps:
#   - intent: {intent_dropdown}
#   - action: {action_dropdown}
# """
#     file = open("storiesExample.yml", "w")
#     file.write(examplesF)
#     file.close()
    
import streamlit as st # stories.py
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


if "n_rows" not in st.session_state:
    st.session_state.n_rows = 1

add = st.button(label="add")
remove = st.button(label="remove")

text_story=[]
intent_dropdown=[]
action_dropdown=[]
if add:
    st.session_state.n_rows += 1
    st.experimental_rerun()
if remove:
    st.session_state.n_rows -= 1
    st.experimental_rerun()
for i in range(st.session_state.n_rows):
    text_story.append(st.text_input(label="Enter your story name:",key=i))
    intent_dropdown.append(st.selectbox("Intent Name", names,key=i))
    action_dropdown.append(st.selectbox("Action Name", actions,key=i))
    st.markdown("""---""")
submit = st.button(label="submit")

storiesDict={}

for key in text_story:
    for value in intent_dropdown:
        for value2 in action_dropdown:
            storiesDict[key] = [value,value2]
            intent_dropdown.remove(value)
            action_dropdown.remove(value2)

print(storiesDict) 

examplesF = f"""version: \"3.1\"
stories:"""

if submit:
    for i in storiesDict:
        examplesF+=f"""
    - story: {i}
      steps:
      - intent: {storiesDict[i][0]}
      - action: {storiesDict[i][1]}
"""
    file = open("storiesExample.yml", "w")
    file1=open("data/stories.yml","w")
    file1.write(examplesF)
    file1.close()
    file.write(examplesF)
    file.close()
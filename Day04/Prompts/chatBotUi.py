from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

import streamlit as st

## title
st.title("ChatBot Tool")

if "model" not in st.session_state:
    st.session_state['model'] = ChatGoogleGenerativeAI(model="gemini-1.5-flash") 

## initialize the session state for messages
if "messages" not in st.session_state:
    st.session_state["messages"] = []

## update interface with previous messages:

for message in st.session_state['messages']:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])




## create a chat interface
if prompt := st.chat_input("Enter your message"):
    st.session_state['messages'].append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)
        

    with st.chat_message("assistant"):
        client = st.session_state['model']
        response = client.invoke(st.session_state['messages'])
        st.markdown(response.content)
        response_content = response.content

    st.session_state['messages'].append({"role": "assistant", "content": response_content})
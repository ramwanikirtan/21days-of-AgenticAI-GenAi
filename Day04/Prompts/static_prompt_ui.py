from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

st.header("Chat Tool")
user_prompt = st.text_input("Enter your prompt")

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

if st.button("Generate"):
    st.text("Generating response...")
    if user_prompt:
        response = llm.invoke(user_prompt)
        st.write(response.content)
        st.text("Response generated successfully!")
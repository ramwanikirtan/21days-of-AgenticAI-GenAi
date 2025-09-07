from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt
load_dotenv()


model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

st.header("Summarizer tool")

paper_input = st.selectbox(
    "Select a research paper",options=[
    "Attention Is All You Need",
    "Generative Adversarial Nets",
    "Auto-Encoding Variational Bayes",
    "ArcMemo: Abstract Reasoning Composition with Lifelong LLM Memory",
    "Psychologically Enhanced AI Agents",
]
)


style_input = st.selectbox(
    "Select a style",options=[
    "Formal",
    "Informal",
    "Concise",
    "Detailed",
    "Technical",
    "Simplified"
]
)

length_input = st.selectbox(
    "Select summary length",options=[
    "Short",
    "Medium",
    "Long"
]
)

## template

prompt_template = load_prompt('prompt_template.json')

### why we didnt use f string instead of promp_template when fstring works same


# adv 1: default validatio using advance feature like validate_true
# adv 2 : Reusability,  save template as json
# adv 3 : Tightly coupled with Langchain ecosystem



## filling the place holders

prompt = prompt_template.invoke({
    'paper_input': paper_input,
    "style_input": style_input,
    "length_input": length_input
})



if st.button("Generate Summary"):
    result = model.invoke(prompt)
    st.text("Generating summary...")
    st.write(result.content)
    
from langchain_core.prompts import ChatPromptTemplate

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()


chat_template = ChatPromptTemplate([  
    ("system","You are a helpful {domain} experts."),
    ("human","explain in simple words about {topic}")
])

model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash")
prompt = chat_template.invoke({"domain":"cricket","topic":"ipl"})
response = model.invoke(prompt)

print(response.content)
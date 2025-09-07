from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash")

messages = [
    SystemMessage(content="You are a help Assistant in healthcare profession"),
    HumanMessage(content="what should i do in headache")
]


response = model.invoke(messages)

messages.append(AIMessage(content=response.content))
print(messages)
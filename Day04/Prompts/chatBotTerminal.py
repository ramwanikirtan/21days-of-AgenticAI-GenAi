from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from dotenv import load_dotenv
load_dotenv()


model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash")

chat_messages = [
    SystemMessage(content="You are a helpful Ai assistant.")    
]

while True:
    user_input = input("you:")
    if user_input.lower() == 'exit':
        print("Exiting the chat. Goodbye!")
        break
    chat_messages.append(HumanMessage(content=user_input))
    response = model.invoke(chat_messages)
    chat_messages.append(AIMessage(content=response.content))
    print("Bot:", response.content)

print(chat_messages)

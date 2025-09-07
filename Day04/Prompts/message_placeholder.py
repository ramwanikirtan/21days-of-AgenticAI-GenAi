from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

## chat_template

chat_template = ChatPromptTemplate([
    ("system","you are helpful customer support agent."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human","{query}")
])

chat_history = []
## load chat history

with open ("chat_history.txt") as file:
    chat_history.extend(file.readlines())


### prompt

prompt = chat_template.invoke({"chat_history":chat_history,"query":"where is my refund?"})

print(prompt)
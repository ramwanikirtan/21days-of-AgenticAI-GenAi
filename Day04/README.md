
# Day 4: Deep Dive into Prompt Engineering & Conversational AI with LangChain, Streamlit, and Google Gemini

## 📚 What I Studied in Depth

### 1. The `invoke()` Function in LangChain
- Explored how `invoke()` is the core method to send prompts/messages to LLMs.
- Learned the difference between passing a single static string (for single-turn), a formatted prompt (for dynamic/static), and a list of message objects (for multi-turn chat).

### 2. Single-Turn Static Messages
- Used `invoke("your prompt")` to send a single, unchanging prompt to the model.
- Example: `static_prompt_ui.py` lets you enter a prompt and get a direct response.

### 3. Dynamic Static Messages with PromptTemplate
- Built prompts using `PromptTemplate` for parameterized, reusable prompt structures.
- Example: `dynamic_prompt_ui.py` uses a template to fill in paper title, style, and length, then sends the result to the model.
- Learned why PromptTemplate is better than f-strings for validation, reusability, and integration with LangChain.

### 4. Multi-Turn Static Messages with ChatPromptTemplate
- Studied how to use `ChatPromptTemplate` to create a fixed sequence of messages (system, user, etc.) for the model.
- Understood the structure and use-case for static multi-turn conversations.

### 5. Multi-Turn Dynamic Messages with MessagePlaceholder
- Used `MessagePlaceholder` to allow dynamic insertion of user/AI messages into the chat history.
- Realized this is essential for real conversational memory and context.

### 6. Streamlit Chatbot UI (`chatBotUi.py`)
- Built a UI that collects all user/assistant messages in `st.session_state["messages"]`.
- Learned to pass the full message history to `invoke()` for context-aware, multi-turn chat.
- Understood the importance of message formatting (list of dicts for chat models).

### 7. Advanced Terminal Chatbot with Memory (`chatBotTerminal.py`)
- Used `HumanMessage`, `AIMessage`, and `SystemMessage` from LangChain to build a terminal chatbot with persistent memory.
- Each turn, appended new messages to the chat history and passed the entire list to `invoke()`.
- Saw how this enables advanced memory, context, and system instructions in a simple terminal app.

---
## 🌱 What I Learned (My Day 4 Journey)

- The difference between static, dynamic, single-turn, and multi-turn prompts—and when to use each.
- How to use `PromptTemplate` for safe, reusable, and validated prompt engineering.
- How to use `ChatPromptTemplate` and `MessagePlaceholder` for advanced, multi-turn conversational flows.
- The importance of message types: HumanMessage, AIMessage, SystemMessage for structuring chat history.
- How to build both web (Streamlit) and terminal chatbots with real memory and context.
- Debugging: Why passing the wrong type (e.g., list vs. string) to `invoke()` causes errors, and how to fix it.
- The value of session state and message history for real conversational AI.

This day gave me a deep, practical understanding of prompt engineering, LLM invocation patterns, and how to architect both simple and advanced chatbots using LangChain and Streamlit.

---
## 🛠️ How to Run the Demos

1. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
2. **Set up your API key:**
   - Create a `.env` file in the project root:
     ```env
     GOOGLE_API_KEY=your_google_api_key_here
     ```
3. **Run the Streamlit UIs:**
   ```sh
   streamlit run Day04/Prompts/static_prompt_ui.py
   streamlit run Day04/Prompts/dynamic_prompt_ui.py
   streamlit run Day04/Prompts/chatBotUi.py
   ```
4. **Run the advanced terminal chatbot:**
   ```sh
   python Day04/Prompts/chatBotTerminal.py
   ```

---
## 🔍 File Guide

- `static_prompt_ui.py`: Single-turn, static prompt demo (Streamlit)
- `dynamic_prompt_ui.py`: Dynamic prompt with PromptTemplate (Streamlit)
- `prompt_generator.py` & `prompt_template.json`: Custom prompt template definition and usage
- `chatBotUi.py`: Multi-turn, context-aware chatbot UI (Streamlit)
- `chatBotTerminal.py`: Advanced terminal chatbot with memory using HumanMessage, AIMessage, SystemMessage

---
This day was a deep exploration of prompt engineering, LLM invocation, and building both web and terminal conversational agents with real memory and context.

## 🌱 What I Learned (My Day 4 Journey)

- I learned how to use Streamlit to build a real-time chat interface that feels modern and interactive.
- I discovered how to connect Google Gemini (via LangChain) to my own app, and what it takes to get API keys working securely.
- I understood the difference between single-turn and multi-turn chat: sending just one message vs. sending the whole conversation for better context.
- I practiced managing session state in Streamlit, so my chatbot remembers the conversation as I chat.
- I saw how important it is to format the chat history correctly—passing a list vs. a string can break the model!
- I learned to debug errors by reading stack traces and updating my code to match what the model expects.
- I realized that building with LLMs is as much about UI/UX as it is about the backend model.

This day helped me connect the dots between frontend (Streamlit), backend (LangChain, Gemini), and the real-world challenges of building conversational AI.

# Day 4: Building a Conversational AI Chatbot with Streamlit & LangChain (Google Gemini)


**`chatBotUi.py`** is a Streamlit app that lets you chat with Google Gemini (via LangChain). It demonstrates:

- Real-time, multi-turn conversation: The app keeps track of all your messages and sends the full chat history to the model for context-aware responses.
- Clean, interactive UI: Uses Streamlit's chat components for a modern look and feel.
- Session state: Remembers your conversation as long as the app is running.

## 🛠️ Step-by-Step: Run It Yourself

1. **Install dependencies:**
   ```sh
   pip install streamlit langchain-google-genai python-dotenv
   ```
2. **Set up your API key:**
   - Create a `.env` file in the project root:
     ```env
     GOOGLE_API_KEY=your_google_api_key_here
     ```
3. **Start the chatbot app:**
   ```sh
   streamlit run Day04/Prompts/chatBotUi.py
   ```

## 💡 Key Concepts

- **Multi-turn context:** Instead of sending just the latest message, the app joins all previous messages so the AI can respond with full context—just like a real conversation.
- **Session state:** Streamlit's `st.session_state` keeps your chat history alive between messages.
- **API security:** Sensitive keys are loaded from `.env` (never hard-coded).

## 📝 Reflection & Next Steps

- Try changing the model or prompt style to see how responses change.
- Experiment with how much history you send—does it improve or confuse the AI?
- Think about how you could add features: avatars, message timestamps, or even voice input!

---
This day is about hands-on learning: not just building a chatbot, but understanding how modern conversational AI apps are structured and deployed.

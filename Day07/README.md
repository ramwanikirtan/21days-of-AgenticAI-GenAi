# Day 7: Building Custom Runnable Chains and Fake LLMs in Python

## 🚀 Technologies & Concepts Used
- **Python OOP**: Abstract Base Classes, method overriding, and custom class design
- **LangChain Patterns**: Inspired by LangChain's Runnable, LLM, PromptTemplate, and OutputParser interfaces
- **Custom LLM Simulation**: Created a `FakeLLM` to mimic LLM responses for testing and prototyping
- **Prompt Engineering**: Built a `FakePromptTemplate` for dynamic prompt formatting
- **Composable Chains**: Designed `RunnableConnector` to chain together prompt templates, LLMs, and parsers
- **Output Parsing**: Implemented a simple `Stroutparser` to extract string responses

## 🧠 What I Learned
- How to design and implement a modular, composable chain-of-runnables system (like LangChain) from scratch
- The importance of type consistency: ensuring each step in a chain returns the correct type (dict vs. str)
- How to simulate LLM behavior for rapid prototyping and testing without API calls
- How to build and connect custom prompt templates, LLMs, and output parsers
- How to debug and fix common issues in chain composition (e.g., TypeError with str.format and dict unpacking)
- The value of abstract base classes for enforcing method signatures and design patterns

## 🛠️ Key Components
- **Runnable (ABC)**: Abstract base class for all chainable components
- **FakeLLM**: Simulates an LLM by returning random canned responses
- **FakePromptTemplate**: Formats prompts using Python's string formatting and input variables
- **RunnableConnector**: Chains multiple runnables, passing output of one as input to the next
- **Stroutparser**: Extracts the 'response' field from LLM output
- **FakeLLMChain**: (Optional) A simple chain for prompt → LLM → response

## 📝 Example Chain
```python
# Create components
llm = FakeLLM()
parser = Stroutparser()
template1 = FakePromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)
template2 = FakePromptTemplate(
    template='Explain the following joke {response}',
    input_variables=['response']
)
# Build chains
chain1 = RunnableConnector([template1, llm])
chain2 = RunnableConnector([template2, llm, parser])
final_chain = RunnableConnector([chain1, chain2])
# Run the chain
final_chain.invoke({'topic': 'cricket'})
```

## 🐍 How to Run
1. Open `langchain_fake_llm.ipynb` in VS Code or Jupyter
2. Run all cells to see the chain in action
3. Experiment with your own templates, LLMs, and chain compositions

## ⚡ Troubleshooting
- If you see `TypeError: str.format() argument after ** must be a mapping, not str`, check that every prompt template receives a dict, not a string
- Use print statements to debug the type and value of data passed between runnables

---
This day was a deep dive into the architecture of LLM chains-building the foundation for more advanced agentic and compositional AI systems.
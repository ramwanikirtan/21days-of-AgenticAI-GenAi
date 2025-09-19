# Day 06: Advanced Chain Composition in LangChain

---

## 🚀 Overview
Day 06 focused on mastering **advanced chain composition patterns** in LangChain, including:
- **Simple Chains**
- **Sequential Chains**
- **Conditional Chains**
- **Parallel Chains**

I explored how to build, combine, and orchestrate LLM-powered workflows using these patterns, leveraging both OpenAI and Google Gemini models, prompt templates, and output parsers.

---

## 🛠️ Technologies & Concepts Used
- **LangChain Core**: `PromptTemplate`, `StrOutputParser`, `PydanticOutputParser`, `RunnableParallel`, `RunnableBranch`, `RunnableLambda`
- **LLM Providers**: `ChatOpenAI`, `ChatGoogleGenerativeAI` (Gemini)
- **Python OOP**: For custom logic and output validation
- **Pydantic**: For structured output parsing
- **dotenv**: For environment variable management

---

## 📚 What I Learned

### 1. Simple Chains
- Chained a `PromptTemplate` → LLM → `StrOutputParser` for basic text generation.
- Used Google Gemini (`gemini-1.5-flash`) for creative fact generation.
- Visualized chain graphs using `grandalf`.

### 2. Sequential Chains
- Built multi-step pipelines where the output of one step feeds into the next.
- Used multiple prompt templates and chained them with an LLM and output parser.
- Example: Generate advancements on a topic, then summarize them in bullet points.

### 3. Conditional Chains
- Used `RunnableBranch` to route inputs dynamically based on LLM output.
- Implemented sentiment classification with `PydanticOutputParser` and generated context-aware responses.
- Demonstrated how to branch logic for positive/negative feedback using prompt templates and LLMs.

### 4. Parallel Chains
- Leveraged `RunnableParallel` to run multiple LLM chains concurrently.
- Combined outputs (e.g., notes and Q&A) and merged them into a single document.
- Used both OpenAI and Gemini models in parallel for diverse outputs.

---

## 🧩 Key Code Patterns
```python
# Example: Parallel Chain
from langchain.schema.runnable import RunnableParallel

parallel_chain = RunnableParallel(
    notes=prompt1 | model1 | parser,
    quiz=prompt2 | model2 | parser
)

result = parallel_chain.invoke({"text": "Your input text here"})
```

---

## 🌟 Takeaways
- **Chain composition** enables modular, scalable, and flexible LLM workflows.
- **Conditional and parallel execution** unlocks advanced use cases (e.g., feedback routing, multi-output generation).
- **Prompt engineering** and **output parsing** are critical for reliable, structured results.
- **LangChain's abstractions** make it easy to experiment with complex LLM pipelines.

---

## 📂 Files in This Module
- `simplechains.ipynb`: Basic prompt → LLM → parser chain
- `sequentialchain.ipynb`: Multi-step sequential pipeline
- `conditionalChain.ipynb`: Sentiment-based branching and response
- `parallelChain.ipynb`: Parallel LLM chains and output merging

---

## 📝 Reflections
This day deepened my understanding of how to orchestrate LLMs for real-world, production-grade workflows. I now feel confident designing both simple and complex chains, and see how these patterns can be extended for agentic and autonomous AI systems.

---

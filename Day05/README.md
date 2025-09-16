# Day 5: Structured Outputs, Output Parsers, and Pydantic in LangChain

## What I Learned

- How to use LangChain's output parsers, including StrOutputParser for raw string output and structured output with Pydantic models.
- The difference between static type hints (TypedDict) and runtime validation (Pydantic BaseModel).
- How to use HuggingFace and Google Gemini (GemAI) models with LangChain for both text generation and structured outputs.
- How to debug and resolve common issues: missing API keys, unsupported structured output, and kernel restarts in notebooks.
- The importance of running all cells and saving outputs for GitHub rendering.

## Key Concepts & Demos

### 1. StrOutputParser
- Returns the raw model output as a string (no parsing or validation).
- Useful for simple pipelines or when you want the model's response verbatim.

### 2. PydanticOutputParser
- Enforces structured output using Pydantic models.
- Validates and parses model output into Python objects with type safety.
- Raises errors for invalid or missing fields.

### 3. TypedDict vs. Pydantic
- TypedDict: Type hints only, no runtime validation.
- Pydantic: Full runtime validation, type coercion, and error reporting.

### 4. HuggingFace & Google Gemini Integration
- How to use HuggingFaceEndpoint and ChatGoogleGenerativeAI with LangChain.
- How to set up API keys in .env and load them in code.

### 5. Troubleshooting
- How to fix ModuleNotFoundError by installing missing packages.
- How to resolve NotImplementedError for structured output by upgrading packages or using supported models.
- How to ensure outputs are saved in notebooks for GitHub display.

## How to Run

1. Install dependencies:
   ```sh
   pip install langchain langchain-google-genai pydantic python-dotenv
   ```
2. Set up your `.env` file with required API keys (OpenAI, Google, HuggingFace, etc.).
3. Open and run the notebooks in `Day05/Structured_outputs/WithStructureLLMs/`.
4. For scripts, run them from the project root or the correct subfolder.

## Example: Pydantic Structured Output
```python
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

class Review(BaseModel):
    summary: str = Field(...)
    sentiment: str = Field(...)

model = ChatOpenAI(method="function_calling")
structured_model = model.with_structured_output(Review)
result = structured_model.invoke("The product is great!")
print(result.summary, result.sentiment)
```

---
This day focused on robust data validation, output parsing, and integrating multiple LLM providers with LangChain for both research and production use.

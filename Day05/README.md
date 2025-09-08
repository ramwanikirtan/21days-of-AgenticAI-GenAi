# Day 5: Structured Outputs with Pydantic and TypedDict in Python

## What I Learned

- The difference between Python's `TypedDict` (type hints, no runtime validation) and Pydantic's `BaseModel` (runtime validation, type coercion, and error reporting).
- How to use Pydantic for data validation, default values, optional fields, and type coercion.
- How Pydantic enforces strict types (e.g., string vs. int) and validates formats (e.g., email addresses with `EmailStr`).
- How to debug and interpret Pydantic validation errors.
- The importance of re-running all cells after installing new packages in Jupyter/VS Code notebooks.

## Key Concepts & Demos

### 1. TypedDict (Static Type Hints)
- Used for type hinting dictionaries, but does not enforce types at runtime.
- Example: You can assign a string to an int field and no error is raised.

### 2. Pydantic BaseModel (Runtime Validation)
- Enforces types and validates data at runtime.
- Raises errors for invalid types or formats (e.g., wrong email format).
- Supports default values and optional fields.
- Coerces types when possible (e.g., string to int).

### 3. Pydantic with EmailStr
- Demonstrated how to use `EmailStr` for email validation.
- Shows how invalid emails raise validation errors.

### 4. Common Errors and Debugging
- ModuleNotFoundError: No module named 'pydantic' — fixed by installing pydantic in the notebook environment.
- ValidationError: Raised when data does not match the model's type or format requirements.
- Kernel restarts: Always re-run all cells after installing new packages.

## How to Run

1. Open the notebook `Day05/Structured_outputs/WithStructureLLMs/pydantic-demo.ipynb` in VS Code or Jupyter.
2. If you see a module error, install pydantic in the notebook environment and restart the kernel.
3. Run all cells from the top to see type validation, coercion, and error handling in action.

## Example Code

```python
from pydantic import BaseModel, EmailStr
from typing import Optional

class Student(BaseModel):
    name: str = "kirtan"
    age: Optional[int] = None
    email: EmailStr

student = Student(email="kirtan@gmail.com")
print(student.name)
print(student.age)
print(student.email)
```

## Troubleshooting
- If you get a module error, install pydantic in the notebook (not just in your system Python).
- If you get a validation error, check your data types and formats.
- Always re-run all cells after installing or updating packages.

---
This day focused on robust data validation and type safety in Python using Pydantic, and how it compares to static type hints with TypedDict.

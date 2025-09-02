# Day 2: Pydantic in Python

This folder contains my Day 2 project focused on learning and practicing Pydantic for data validation and modeling in Python.

## Why Pydantic?
Pydantic is a powerful library for data validation and settings management using Python type annotations. It ensures that data is structured, correct, and safe to use in your applications. Unlike regular Python classes or dataclasses, Pydantic automatically validates input data, provides clear error messages, and supports complex nested models. This makes it ideal for:
- Building robust APIs and data pipelines
- Preventing bugs caused by invalid or unexpected data
- Simplifying code for data validation and transformation
- Generating schemas for documentation and interoperability

## What I Learned
- **Pydantic Models:** How to create models using `BaseModel` for structured and validated data.
- **Type Annotations:** Using Python type hints to define model fields and ensure correct data types.
- **Validation:** Automatic type validation and error handling for incorrect or missing data.
- **Optional Fields:** Adding optional fields with default values using `Optional` from the `typing` module.
- **Nested Models:** Building complex data structures with nested models for hierarchical data.
- **Field Customization:** Using `Field` for constraints (min/max length, value ranges), default values, and descriptions.
- **Data Classes vs. Pydantic Models:** Compared Python `dataclass` (no validation) with Pydantic models (strict validation).
- **List Fields:** Defining fields as lists and handling type casting.
- **Model Schema:** Generating JSON schema for models using `.model_json_schema()`.

## Key Techniques & Examples
- Creating models with required and optional fields
- Validating and type casting input data
- Handling errors and exceptions for invalid data
- Using nested models for structured data
- Customizing fields with constraints and descriptions
- Comparing dataclasses and Pydantic models for validation

## How to Use
- Explore `intro.ipynb` for step-by-step code examples and explanations
- Run the notebook cells to see validation, error handling, and model creation in action

## Resources
- [Pydantic Documentation](https://docs.pydantic.dev/latest/)
- [Real Python: Pydantic](https://realpython.com/python-data-classes/#pydantic-data-validation)

---

This project helped me master robust data validation and modeling in Python using Pydantic.

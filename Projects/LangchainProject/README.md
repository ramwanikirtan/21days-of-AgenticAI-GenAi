# Documentation Similarity Project

## Project Overview
This project focuses on building a documentation similarity system using LangChain and machine learning techniques. The goal is to compare and retrieve similar documents or text passages based on their semantic meaning, which is useful for search, recommendation, and knowledge management tasks.

## Approach and Workflow

### 1. Data Preparation
- Collected a set of documents or text passages to be compared.
- Preprocessed the text (cleaning, normalization) to ensure consistent input for embeddings.

### 2. Embedding Generation
- Used LangChain's embedding models to convert text into high-dimensional vector representations.
- Functions used:
  - `from langchain.embeddings import OpenAIEmbeddings, HuggingFaceEmbeddings`
  - Initialized the embedding model (e.g., OpenAI, HuggingFace, or other supported models).
  - Example:
    ```python
    from langchain.embeddings import HuggingFaceEmbeddings
    embedder = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector = embedder.embed_query("Sample document text")
    ```
- Each document was transformed into a vector using the embedding model.

### 3. Similarity Computation
- Applied cosine similarity to measure the closeness between document vectors.
- Used scikit-learn's `cosine_similarity` function:
  ```python
  from sklearn.metrics.pairwise import cosine_similarity
  similarity_score = cosine_similarity([vector1], [vector2])[0][0]
  ```
- Compared the query/document vector with all other document vectors to find the most similar ones.

### 4. Retrieval and Ranking
- Ranked documents based on their similarity scores.
- Retrieved the top-N most similar documents for a given query.
- Displayed results with similarity percentages for better interpretability.

## Key Functions and Libraries Used
- `langchain.embeddings.OpenAIEmbeddings` and `langchain.embeddings.HuggingFaceEmbeddings` for vectorization.
- `sklearn.metrics.pairwise.cosine_similarity` for similarity calculation.
- Python standard libraries for data handling and preprocessing.

## Machine Learning Concepts Applied
- **Embeddings:** Used to capture semantic meaning of text.
- **Cosine Similarity:** Measures the angle between two vectors, providing a normalized similarity score between -1 and 1.
- **Vector Search:** Enables efficient retrieval of similar documents.

## Resources and References
- [LangChain Documentation](https://python.langchain.com/docs/)
- [HuggingFace Embeddings](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
- [Scikit-learn Cosine Similarity](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html)
- YouTube tutorials on semantic search and vector databases

## Summary
This project demonstrates how to combine LangChain's embedding capabilities with classic machine learning techniques to build a robust documentation similarity system. The approach is modular and can be extended to larger datasets or integrated with vector databases for production use.

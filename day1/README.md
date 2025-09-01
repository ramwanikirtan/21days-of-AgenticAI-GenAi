# Day 1: NumPy & Pandas – In-Depth Learning

Welcome to my Day 1 journey, where I explored the foundations and advanced features of NumPy and Pandas for data science and analysis.

## NumPy
NumPy is a powerful library for numerical computing in Python. Here’s what I studied:

### Key Concepts
- **Array Creation:** Using `np.array`, `np.zeros`, `np.ones`, `np.arange`, and `np.linspace` to create arrays of different shapes and values.
- **Array Manipulation:** Reshaping arrays with `.reshape()`, flattening with `.ravel()`, and stacking arrays with `np.vstack`/`np.hstack`.
- **Mathematical Operations:** Element-wise operations, broadcasting, aggregation (`sum`, `mean`, `std`), and universal functions (`np.exp`, `np.sqrt`).
- **Indexing & Slicing:** Accessing and modifying array elements using slicing, boolean indexing, and fancy indexing.
- **Random Module:** Generating random numbers with `np.random` for simulations and experiments.

### Tips & Tricks
- Use broadcasting to perform operations on arrays of different shapes without explicit loops.
- Prefer vectorized operations for speed and efficiency.
- Use `np.where` for conditional logic on arrays.
- Always check array shapes before performing operations to avoid errors.

---

## Pandas
Pandas is the go-to library for data manipulation and analysis. Here’s what I covered:

### Key Concepts
- **DataFrame Creation:** Building DataFrames from dictionaries, lists, and CSV files using `pd.DataFrame` and `pd.read_csv`.
- **Data Selection:** Selecting rows/columns with `.loc`, `.iloc`, and boolean masks.
- **Data Cleaning:** Handling missing data with `.isnull()`, `.dropna()`, and `.fillna()`.
- **Data Transformation:** Applying functions with `.apply()`, renaming columns, and changing data types.
- **Aggregation & Grouping:** Using `.groupby()` for grouped analysis and aggregation functions (`sum`, `mean`, `count`).
- **Merging & Joining:** Combining DataFrames with `.merge()`, `.join()`, and `.concat()`.
- **Visualization:** Quick plotting with `.plot()` for data exploration.

### Tips & Tricks
- Use `.info()` and `.describe()` to quickly understand your data.
- Chain methods for concise and readable data transformations.
- Use `.value_counts()` to analyze categorical data.
- Always handle missing data before analysis to avoid skewed results.
- Use `.groupby()` for powerful grouped operations and insights.

---

## What I Practiced
- Created and manipulated arrays and DataFrames.
- Cleaned and transformed real-world datasets.
- Performed statistical analysis and visualized results.
- Applied best practices for efficient data workflows.

---

## Resources
- [NumPy Documentation](https://numpy.org/doc/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Real Python: NumPy](https://realpython.com/numpy-array-programming/)
- [Real Python: Pandas](https://realpython.com/pandas-python-explore-dataset/)

---

This day set a strong foundation for data science and AI projects. I’m excited to build on these skills in the coming days!

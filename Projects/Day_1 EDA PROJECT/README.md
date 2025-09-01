# Day 1 Project: Diwali Sales Analysis (EDA)

This project documents my in-depth Exploratory Data Analysis (EDA) of Diwali sales data, focusing on practical data science techniques and learnings.

## What I Learned
- **Data Import & Cleaning:** Used Pandas to load CSV data, handle missing values, and clean inconsistent entries.
- **Data Types & Conversion:** Checked and converted column data types for accurate analysis.
- **Descriptive Statistics:** Applied `.describe()`, `.info()`, and `.value_counts()` to summarize data and understand distributions.
- **Grouping & Aggregation:** Leveraged `.groupby()` and aggregation functions (`sum`, `mean`, `count`) to analyze sales by city, gender, and product category.
- **Data Visualization:** Created bar charts, histograms, and pie charts using Matplotlib and Seaborn to visualize sales trends, top products, and customer segments.
- **Business Insights:** Interpreted results to find best-selling products, high-value customers, and seasonal trends.

## Tips & Tricks
- Always inspect data with `.head()`, `.tail()`, and `.sample()` for quick checks.
- Use `.isnull().sum()` to find missing values fast.
- Visualize grouped data for clearer insights (e.g., sales by city).
- Combine Pandas and Seaborn for powerful, readable plots.
- Document findings and code for reproducibility.

## How to Run
- Open `Diwali_sales_Analysis.ipynb` in Jupyter Notebook.
- Run cells step-by-step to follow the EDA workflow and see visualizations.

## Resources
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Seaborn Documentation](https://seaborn.pydata.org/)

---

This project helped me master core EDA skills and extract actionable insights from real-world sales data.

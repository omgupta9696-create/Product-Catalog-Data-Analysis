# Product Catalog Data Analysis 📊

## Project Overview

This is a beginner-friendly **Data Analytics project using Python, Pandas, and Matplotlib**.

The project analyzes a product catalog to understand product categories, brands, pricing, product costs, ratings, and profit. The analysis includes data cleaning, basic statistical analysis, filtering, grouping, and data visualization.

## Dataset

The dataset contains **1,175 product records** across **15 product categories**.

Main columns used in the project:

- `Product_id` – Unique product ID
- `Product_name` – Product name
- `Product_category` – Product category
- `Product_subcategory` – Product subcategory
- `Brand` – Product brand
- `Supplier` – Product supplier
- `Unit_price` – Selling/unit price
- `Product_cost` – Product cost
- `Product_rating` – Product rating
- `Profit` – Calculated as `Unit Price - Product Cost`

## Tools & Technologies

- **Python**
- **Pandas** – Data cleaning and analysis
- **Matplotlib** – Data visualization
- **Jupyter Notebook / VS Code / Python IDE**
- **Git & GitHub** – Project version control

## Project Workflow

```text
Raw Dataset
     ↓
Data Cleaning
     ↓
Exploratory Data Analysis
     ↓
Profit Calculation
     ↓
Data Visualization
     ↓
Business Insights
```

## Data Cleaning

The project cleans the column names by removing extra spaces and standardizing the format. Missing product ratings are filled with a value of `3.0`.

The cleaned dataset is then saved as `product_DA.csv`.

## Analysis Performed

The project answers the following questions:

1. Find the number of products in each category and identify the category with the highest number of products.
2. Find the top 5 brands based on the number of products.
3. Calculate the average, minimum, and maximum unit price.
4. Find the 10 most expensive products.
5. Calculate the average unit price and average product cost for each category.
6. Calculate profit using:
   `Profit = Unit Price - Product Cost`
7. Find the 10 products with the highest profit.
8. Find products with a rating greater than 4.
9. Visualize the number of products in each category.
10. Visualize the relationship between unit price and product cost.
11. Visualize average profit by product category.

## Visualizations

### 1. Number of Products in Each Category

![Number of Products in Each Category](Number%20of%20Products%20in%20Each%20Category.png)

This chart compares the number of products available in each category.

### 2. Unit Price vs Product Cost

![Unit Price vs Product Cost](Uniit%20price%20vs%20Product%20cost.png)

The scatter plot shows a strong positive relationship between unit price and product cost. In this dataset, the correlation is approximately **0.98**.

### 3. Average Profit by Category

![Average Profit by Category](Average%20Profit%20by%20Each%20Category.png)

This chart compares the average calculated profit across product categories.

## Key Findings

Based on the dataset analysis:

- **Sports & Outdoors** has the highest number of products with **91 products**.
- **Electronics** has the highest average profit among the categories, at approximately **317.75**.
- **Jewelry** has the second-highest average profit, at approximately **260.20**.
- The average unit price is approximately **245.52**.
- The minimum unit price is **6.31**, while the maximum is **1,482.95**.
- The relationship between unit price and product cost is strongly positive, with a correlation of approximately **0.98**.
- The most frequently occurring brand in the dataset is **Williams-Sonoma**, with **19 products**.

## Project Structure

```text
Product-Catalog-Data-Analysis/
│
├── product_catalog_DA.csv
├── product_DA.csv
├── code.py
├── graph.py
│
├── Number of Products in Each Category.png
├── Uniit price vs Product cost.png
├── Average Profit by Each Category.png
│
└── README.md
```

## How to Run the Project

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### Step 2: Open the project folder

```bash
cd Product-Catalog-Data-Analysis
```

### Step 3: Install required libraries

```bash
pip install pandas matplotlib
```

### Step 4: Run the data analysis code

```bash
python code.py
```

This performs data cleaning and the main analysis.

### Step 5: Run the visualization code

```bash
python graph.py
```

This generates the charts used in the project.

## Skills Demonstrated

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Data Manipulation
- Data Aggregation
- GroupBy
- Filtering
- Sorting
- Handling Missing Values
- Profit Calculation
- Statistical Analysis
- Data Visualization
- Python Programming
- Pandas
- Matplotlib

## Conclusion

This project demonstrates a basic end-to-end data analysis workflow using a product catalog dataset. It shows how raw data can be cleaned, analyzed, and converted into useful visual insights for understanding products, pricing, costs, and profitability.

---

## Author

**Om Gupta**

PGDM | Aspiring Data Analyst

### Connect

- GitHub: `Add your GitHub profile link`
- LinkedIn: `Add your LinkedIn profile link`

# First we import the data 

import pandas as pd
df=pd.read_csv("product_catalog_DA.csv")

# Cleaning the Data

df.columns=df.columns.str.strip().str.capitalize().str.replace(" ", "_")
print(df)
df.to_csv("product_DA.csv",index=False)  

print(df.info())
print(df.describe())
df["Product_rating"]=df["Product_rating"].fillna(3.0)
print(df.isna().sum())

#  Questions

# 1  Find the number of products in each category and identify the category with the highest number of products.
print(df["Product_category"].value_counts())

# 2. Find the top 5 brands based on the number of products they have.
print(df["Brand"].value_counts().head(5))

# 3. Calculate the average, minimum, and maximum Unit Price of all products.
print("Average Unit Price:", df["Unit_price"].mean())
print("Minimum Unit Price:", df["Unit_price"].min())
print("Maximum Unit Price:", df["Unit_price"].max())

# 4. Find the 10 most expensive products and display their Product Name, Brand, Category, and Unit Price.
most_expensive_products = df.nlargest(10, "Unit_price")
print(most_expensive_products[["Product_name", "Brand", "Product_category", "Unit_price"]])

# 5. Calculate the average Unit Price and average Product Cost for each category.
print(df.groupby("Product_category")[["Unit_price", "Product_cost"]].mean())

# 6. Create a new Profit column using: Profit = Unit Price − Product Cost. Then find the 10 products with the highest profit.
df["Profit"] = df["Unit_price"] - df["Product_cost"]
highest_profit_products = df.nlargest(10, "Profit")
print(highest_profit_products[["Product_name", "Brand", "Product_category", "Profit"]])

# 7. Find all products with a Product Rating greater than 4 and display their Product Name, Category, Unit Price, and Rating.
high_rated_products = df[df["Product_rating"] > 4]
print(high_rated_products[["Product_name", "Product_category", "Unit_price", "Product_rating"]])



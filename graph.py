import pandas as pd
df=pd.read_csv("product_DA.csv")
print(df)

import matplotlib.pyplot as plt

# 8. Create a bar chart showing the number of products in each category. Add a suitable title and axis labels.
k=df["Product_category"].value_counts()
plt.barh(k.index,k.values)
plt.title("Number of Products in Each Category")
plt.xlabel("Product category")
plt.ylabel("Number of Products")
plt.show()

# # 9. Create a scatter plot showing Unit Price vs Product Cost. Add a title, axis labels, and grid, then observe the relationship between them.
plt.scatter(df["Unit_price"], df["Product_cost"])
plt.title("Unit price vs Product cost")
plt.xlabel("Unit price")
plt.ylabel("Product cost")
plt.grid(True)
plt.show()

# creating profit column
df["Profit"] = df["Unit_price"] - df["Product_cost"]
print(df)

# 10. Create a bar chart showing the average Profit for each category and write 2–3 observations based on the chart.
avg_profit = df.groupby("Product_category")["Profit"].mean()
plt.barh(avg_profit.index, avg_profit.values)
plt.title("Average Profit by Category")
plt.xlabel("Product Category")
plt.ylabel("Average Profit")
plt.show()

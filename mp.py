import pandas as pd

data = pd.read_excel(r"C:\mini project\Retail Sales Data Set (1).xlsx")

print(data.head())
print("\n===== TOTAL SALES =====")
print(data["Total Amount"].sum())

print("\n===== TOTAL QUANTITY =====")
print(data["Quantity"].sum())

print("\n===== SALES BY PRODUCT CATEGORY =====")
print(data.groupby("Product Category")["Total Amount"].sum())

print("\n===== SALES BY GENDER =====")
print(data.groupby("Gender")["Total Amount"].sum())

print("\n===== SALES BY AGE GROUP =====")
print(data.groupby("Age Group")["Total Amount"].sum())
import matplotlib.pyplot as plt

# Product Category Chart
category_sales = data.groupby("Product Category")["Total Amount"].sum()

plt.figure(figsize=(6,4))
category_sales.plot(kind="bar")
plt.title("Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

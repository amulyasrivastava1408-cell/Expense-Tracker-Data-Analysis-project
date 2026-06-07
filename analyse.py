print("EXPENSE TRACKER DATA ANALYSIS PROJECT")

import pandas as pd 
df = pd.read_csv("expense.csv")
print(df)

print(df.head(0))

# check the column category
food_df = df[df["Category"] == "Food"]
print(food_df)
print((df["Category"] == "Food").sum())
print(df.head())
print(df.info())
print(df.describe())

# Total Income

income = df[df["Type"] == "Income"]["Amount"].sum()
print("Total Income:", income)

# Total Expense 
expense = df[df["Type"] == "Expense"]["Amount"].sum()
print("Total Expense:", expense)

# Expense by Category

category_expense = (
    df[df["Type"] == "Expense"]
    .groupby("Category")["Amount"]
    .sum()
)

print(category_expense)

# Number of Transactions per Category

print(df["Category"].value_counts())

# Highest Expense

expenses = df[df["Type"] == "Expense"]

highest = expenses.loc[expenses["Amount"].idxmax()]

print(highest)

# Lowest Expense

lowest = expenses.loc[expenses["Amount"].idxmin()]

print(lowest)

# Payment Method Usage

print(df["Payment_Method"].value_counts())


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("expense.csv")

category_expense = (
    df[df["Type"] == "Expense"]
    .groupby("Category")["Amount"]
    .sum()
)

category_expense.plot(kind="bar", color="skyblue")

plt.title("Expense by Category")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.tight_layout()
plt.show()

# Pie chart of Expense 

category_expense.plot(
    kind="pie",
    autopct="%1.1f%%",
    figsize=(8,8)
)

plt.title("Expenses by Category")
plt.ylabel("")
plt.show()
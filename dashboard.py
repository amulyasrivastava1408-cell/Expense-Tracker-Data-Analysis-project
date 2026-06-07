import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Page title
st.title("💰 Expense Tracker Dashboard")

# Load data
df = pd.read_csv("expense.csv")

# Show raw data
st.subheader("Dataset")
st.dataframe(df)

# Income, Expense, Savings
income = df[df["Type"] == "Income"]["Amount"].sum()
expense = df[df["Type"] == "Expense"]["Amount"].sum()
savings = income - expense

col1, col2, col3 = st.columns(3)

col1.metric("Total Income", f"${income:,.2f}")
col2.metric("Total Expense", f"${expense:,.2f}")
col3.metric("Savings", f"${savings:,.2f}")

# Expense by Category
st.subheader("Expense by Category")

category_expense = (
    df[df["Type"] == "Expense"]
    .groupby("Category")["Amount"]
    .sum()
)

st.bar_chart(category_expense)

# Pie Chart
st.subheader("Expense Distribution")

fig, ax = plt.subplots(figsize=(6, 6))

ax.pie(
    category_expense,
    labels=category_expense.index,
    autopct="%1.1f%%"
)

st.pyplot(fig)

# Payment Methods
st.subheader("Payment Methods")

payment_counts = df["Payment_Method"].value_counts()

st.bar_chart(payment_counts)
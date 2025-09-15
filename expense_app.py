import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

# File to store expenses
FILE_NAME = "expenses.csv"

# Create file if not exists
if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=["Date", "Category", "Amount"])
    df.to_csv(FILE_NAME, index=False)

# Load data
def load_data():
    return pd.read_csv(FILE_NAME)

# Save data
def save_data(date, category, amount):
    new_entry = pd.DataFrame([[date, category, amount]], columns=["Date", "Category", "Amount"])
    new_entry.to_csv(FILE_NAME, mode="a", header=False, index=False)

# ---------------- Web App ---------------- #
st.set_page_config(page_title="Expense Tracker", page_icon="💰")

st.title("💰 Personal Expense Tracker")

menu = st.sidebar.radio("Menu", ["Add Expense", "View Summary"])

if menu == "Add Expense":
    st.header("➕ Add a New Expense")

    category = st.selectbox("Category", ["Food", "Travel", "Shopping", "Bills", "Other"])
    amount = st.number_input("Amount (₹)", min_value=1.0, step=10.0)
    date = st.date_input("Date", datetime.today())

    if st.button("Add Expense"):
        save_data(date, category, amount)
        st.success(f"✅ Added {amount} in {category} on {date}")

elif menu == "View Summary":
    st.header("📊 Expense Summary")

    df = load_data()

    if df.empty:
        st.warning("⚠️ No expenses found yet!")
    else:
        st.write("### All Expenses")
        st.dataframe(df)

        total = df["Amount"].sum()
        st.metric("Total Spent", f"₹{total}")

        category_sum = df.groupby("Category")["Amount"].sum()

        st.write("### Category-wise Spending")
        st.bar_chart(category_sum)

        fig, ax = plt.subplots()
        category_sum.plot(kind="pie", autopct="%1.1f%%", ax=ax)
        ax.set_ylabel("")
        st.pyplot(fig)

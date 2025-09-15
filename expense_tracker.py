import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

# File to store expenses
FILE_NAME = "expenses.csv"

# Create file with headers if not exists
if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=["Date", "Category", "Amount"])
    df.to_csv(FILE_NAME, index=False)

def add_expense(category, amount):
    """Add a new expense"""
    date = datetime.now().strftime("%Y-%m-%d")
    new_entry = pd.DataFrame([[date, category, amount]], columns=["Date", "Category", "Amount"])
    new_entry.to_csv(FILE_NAME, mode="a", header=False, index=False)
    print(f"✅ Added {amount} in {category} on {date}")

def show_summary():
    """Show total and category-wise expenses"""
    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("⚠️ No expenses found yet!")
        return

    print("\n📊 Expense Summary:")
    print(f"Total Spent: ₹{df['Amount'].sum()}")

    # Category-wise total
    category_sum = df.groupby("Category")["Amount"].sum()
    print("\nCategory-wise spending:")
    print(category_sum)

    # Plot pie chart
    category_sum.plot(kind="pie", autopct="%1.1f%%", figsize=(5, 5))
    plt.title("Expense Breakdown")
    plt.ylabel("")  # Hide ylabel
    plt.show()

# ---- MENU ----
while True:
    print("\n==== Personal Expense Tracker ====")
    print("1. Add Expense")
    print("2. View Summary")
    print("3. Exit")
    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        cat = input("Enter category (Food, Travel, Shopping, etc.): ")
        amt = float(input("Enter amount: "))
        add_expense(cat, amt)

    elif choice == "2":
        show_summary()

    elif choice == "3":
        print("👋 Goodbye! Keep tracking your expenses.")
        break

    else:
        print("❌ Invalid choice! Try again.")

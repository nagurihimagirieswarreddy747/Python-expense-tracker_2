import json
import os

# Load expenses
if os.path.exists("expenses.json"):
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except:
        expenses = []
else:
    expenses = []

# Save expenses
def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Highest Expense")
    print("5. Lowest Expense")
    print("6. Category Total")
    print("7. Search by Category")
    print("8. Delete Expense")
    print("9. Update Expense")
    print("10. Exit")

    choice = input("\nEnter your choice: ")

    # Add Expense
    if choice == "1":
        try:
            amount = int(input("Enter amount: "))
        except:
            print("Invalid amount, numbers only pettali")
            continue

        if amount > 0:
            print("Valid amount")
            category = input("Enter category: ")
            description = input("Enter description: ")

            expense = {
                "amount": amount,
                "category": category,
                "description": description
            }

            expenses.append(expense)
            save_expenses()
            print("Expense added successfully")
        else:
            print("Invalid amount")

    # View Expenses
    elif choice == "2":
        if not expenses:
            print("No expenses found")
        else:
            for i, expense in enumerate(expenses, 1):
                print(f"{i}. {expense}")

    # Total Expenses
    elif choice == "3":
        total_amount = 0

        for expense in expenses:
            total_amount += expense["amount"]

        print("Total amount:", total_amount)

    # Highest Expense
    elif choice == "4":
        if not expenses:
            print("No expenses found")
        else:
            highest_expense = expenses[0]

            for expense in expenses:
                if expense["amount"] > highest_expense["amount"]:
                    highest_expense = expense

            print("Highest expense:", highest_expense)

    # Lowest Expense
    elif choice == "5":
        if not expenses:
            print("No expenses found")
        else:
            lowest_expense = expenses[0]

            for expense in expenses:
                if expense["amount"] < lowest_expense["amount"]:
                    lowest_expense = expense

            print("Lowest expense:", lowest_expense)

    # Category Total
    elif choice == "6":
        search_category = input("Enter category: ")
        category_total = 0
        category_count = 0

        for expense in expenses:
            if expense["category"].lower() == search_category.lower():
                category_total += expense["amount"]
                category_count += 1

        print("Category total:", category_total)
        print("Number of expenses:", category_count)

    # Search by Category
    elif choice == "7":
        search_category = input("Enter category: ")
        found = False

        for expense in expenses:
            if expense["category"].lower() == search_category.lower():
                print(expense)
                found = True

        if not found:
            print("Expense not found")

    # Delete Expense
    elif choice == "8":
        target_description = input("Enter description to delete: ")
        found = False

        for expense in expenses:
            if expense["description"].lower() == target_description.lower():
                expenses.remove(expense)
                found = True
                break

        if found:
            save_expenses()
            print("Expense deleted successfully")
        else:
            print("Expense not found")

    # Update Expense - BUG FIX CHESINA PART
    elif choice == "9":
        update_target = input("Enter description to update: ")
        updated = False

        for expense in expenses:
            if expense["description"].lower() == update_target.lower():
                try:
                    new_amount = int(input("Enter new amount: "))
                except:
                    print("Invalid amount, numbers only pettali")
                    break

                if new_amount > 0:
                    print("Valid amount")
                    expense["amount"] = new_amount
                    expense["category"] = input("Enter new category: ")
                    expense["description"] = input("Enter new description: ")
                    updated = True
                else:
                    print("Invalid amount")
                break

        if updated:
            save_expenses()
            print("Expense updated successfully")
        else:
            print("Expense not found")

    # Exit
    elif choice == "10":
        save_expenses()
        print("Expenses saved. Thank you!")
        break

    else:
        print("Invalid choice")

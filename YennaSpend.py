expenses = []

while True:
    print("\n===== 💐 Welcome to YennaSpend 💸 =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Edit Expense")
    print("5.Delete Expense")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))

        expense = {
            "category": category,
            "amount": amount
        }

        expenses.append(expense)
        print("✅ Expense added!")

    elif choice == "2":
        if not expenses:
            print("No expenses found.")
        else:
            print("\n--- Your Expenses ---")

            for i, expense in enumerate(expenses, 1):
                print(f"{i}. {expense['category']} - ₹{expense['amount']}")

    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)
        print(f"💰 Total Spending: ₹{total}")
    elif choice == "4":
            if not expenses:
                print("No expenses found.")
            else:
                print("\n--- Your Expenses ---")
                for i, expense in enumerate(expenses, 1):
                    print(f"{i}. {expense['category']} - ₹{expense['amount']}")
    
                try:
                    index = int(input("Enter expense number to edit: ")) - 1
                    if 0 <= index < len(expenses):
                        new_category = input(f"New category (leave blank to keep '{expenses[index]['category']}'): ")
                        new_amount = input(f"New amount (leave blank to keep ₹{expenses[index]['amount']}): ")
                        if new_category.strip():
                            expenses[index]["category"] = new_category
                        if new_amount.strip():
                            expenses[index]["amount"] = float(new_amount)
    
                        print("✏️ Expense updated!")
                    else:
                        print("❌ Invalid expense number.")
                except ValueError:
                    print("❌ Please enter a valid number.")
    
    elif choice == "5":
            if not expenses:
                print("No expenses found.")
            else:
                print("\n--- Your Expenses ---")
                for i, expense in enumerate(expenses, 1):
                    print(f"{i}. {expense['category']} - ₹{expense['amount']}")
    
                try:
                    index = int(input("Enter expense number to delete: ")) - 1
                    if 0 <= index < len(expenses):
                        removed = expenses.pop(index)
                        print(f"🗑️ Deleted: {removed['category']} - ₹{removed['amount']}")
                    else:
                        print("❌ Invalid expense number.")
                except ValueError:
                    print("❌ Please enter a valid number.")
    elif choice == "6":
        print("👋 Thank you! Have a great day🫶")
        break

    else:
        print("❌ Invalid choice!")
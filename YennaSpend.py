expenses = []

while True:
    print("\n===== 💐 Welcome to YennaSpend 💸 =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Exit")

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
        print("👋 Thank you! Have a great day🫶")
        break

    else:
        print("❌ Invalid choice!")
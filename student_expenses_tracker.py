
# Student Expenses Tracker

def load_expenses():
    expenses = []

    try:
        file = open("expenses.txt", "r")

        for line in file:
            data = line.strip().split(",")

            if len(data) == 3:
                expenses.append([
                    data[0], data[1], float(data[2])
                ])

        file.close()

    except FileNotFoundError:
        pass

    return expenses


def save_expenses(expenses):
    file = open("expenses.txt", "w")

    for expense in expenses:
        file.write(
            expense[0] + "," + expense[1] + ","
            + str(expense[2]) + "\n"
        )

    file.close()


def add_expense(expenses):
    name = input("Enter expense name: ")
    category = input("Enter category: ")

    try:
        amount = float(input("Enter amount (Rs.): "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        expenses.append([name, category, amount])
        save_expenses(expenses)

        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid amount.")


def view_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    print("\n--- All Expenses ---")

    for expense in expenses:
        print("Name:", expense[0])
        print("Category:", expense[1])
        print("Amount: Rs.", expense[2])
        print("--------------------")


def total_expenses(expenses):
    total = 0

    for expense in expenses:
        total = total + expense[2]

    print("Total expenses: Rs.", total)


def search_category(expenses):
    category = input("Enter category to search: ")
    found = False

    for expense in expenses:
        if expense[1].lower() == category.lower():
            print(
                expense[0], "-", expense[1],
                "- Rs.", expense[2]
            )
            found = True

    if not found:
        print("No expenses found in this category.")


def main():
    expenses = load_expenses()

    while True:
        print("\n===== STUDENT EXPENSES TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Calculate Total Expenses")
        print("4. Search by Category")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            total_expenses(expenses)

        elif choice == "4":
            search_category(expenses)

        elif choice == "5":
            print("Thank you for using Student Expenses Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


main()
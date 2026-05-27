Income = []
Expense = []
while True:
    print("--- Budgeting Menu ---\n")
    budgeting_choice = int(input("What do you wish to do?\n1. Add new Income/Expene\n2. Remove existing Income/Expense\n3. View\n4. Back to main menu\n\nChoice: "))
    if budgeting_choice == 1:
        addition_choice = int(input("What would you like to add?\n1. Income\n2. Expense\n3. Back to main menu\n\nChoice: "))
        if addition_choice == 1:
            income_type = input("Enter income type:\n")
            income_value = int(input("Enter amount of income:\n"))
            income_dictonary  = {
                "Type" : income_type,
                "Amount" : income_value
            }
            Income.append(income_dictonary)
            print("New expense is added!")
        elif addition_choice == 2:
            Expense.append(float(input("Enter the amount of expense: ")))
            print("Adding new expense...")
        else:
            break
    elif budgeting_choice == 2:
        budget_removing_choice = int(input("What would you like to remove?\n1. Income\n2. Expense\n3. Back to main menu\n\nChoice: "))
        if addition_choice == 1:
            for i, income in enumerate(Income):
                print(f"Index {i}: {income}")
            income_removing_choice = int(input("Enter the index of the income to remove: "))
            Income.pop(income_removing_choice)
            print("Income removed.")
        elif addition_choice == 2:
            for i, expense in enumerate(Expense):
                print(f"Index {i}: {expense}")
            expense_removing_choice = int(input("Enter the index of the expense to remove: "))
            Expense.pop(expense_removing_choice)
            print("Expense removed.")
        else:
            break
    elif budgeting_choice == 3:
        view_choice = int(input("What do you wish to view?\n1. History\n2. Calender\n3. Back to main menu\n\nChoice: "))
        if view_choice == 1:
            income_history = None
        elif view_choice == 2:
            print("On the way")
        elif view_choice == 3:
            break
        else:
            print("Error: Please enter a valid choice!")
    elif budgeting_choice == 4:
        break
    else:
        print("Error: Please enter a valid choice!")
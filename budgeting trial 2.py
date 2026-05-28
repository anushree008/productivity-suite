import datetime
Income = []
Expense = []
Budget = []
total_income = 0
total_exppense = 0
total_budget = 0
while True:
    print("--- Budgeting Menu ---")
    budgeting_choice = int(input("What do you wish to do?\n1. Add new Income/Expense/Monthly budegt\n2. Remove existing Income/Expense/Budget\n3. View\n4. Back to main menu\n\nChoice: "))
    match budgeting_choice:
        case 1:
            addition_choice = int(input("What would you like to add?\n1. Income\n2. Expense\n3. Monthly budget\n4. Back to main menu\n\nChoice: "))
            match addition_choice:
                case 1:
                    income_type = input("Enter income type:\n")
                    income_value = float(input("Enter amount of income:\n"))
                    income_date = datetime(input("Enter the date in the format (dd:MM:yy):\n"))
                    income_dictonary  = {
                        "Type" : income_type,
                        "Amount" : income_value,
                        "Date" : income_date
                    }
                    Income.append(income_dictonary)
                    print("New income is added!")
                case 2:
                    expense_type = input("Enter expense type:\n")
                    expense_value = float(input("Enter the amount of expense:\n"))
                    expense_date = datetime(input("Enter the date in the format (dd:MM:yy):\n"))
                    expense_dictonary = {
                        "Type" : expense_type,
                        "Amount" : expense_value,
                        "Date" : expense_date
                    }
                    Expense.append(expense_dictonary)
                    print("New expense is added!")
                case 3:
                    budget_type = input("Enter budget type:\n")
                    budget_amount = float(input("Enter the montly budget you would like to set:\n"))
                    budget_dictonary = {
                        "Type" : budget_type,
                        "Amount" : budget_amount
                    }
                    Budget.append(budget_dictonary)
                    print("The montly budget is set!")
                case 4:
                    break
                case _:
                    print("Error: Please enter a valid choice!")
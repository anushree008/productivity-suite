import datetime
Income = []
Expense = []
Budget = []
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
                    income_date = datetime.datetime.strptime(input("Enter the date in the format (dd:MM:yy):\n"),"%d:%m:%y")
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
                    expense_date = datetime.datetime.strptime(input("Enter the date in the format (dd:MM:yy):\n"),"%d:%m:%y")
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
        case 2:
            budget_removing_choice = int(input("What would you like to remove?\n1. Income\n2. Expense\n3. Back to main menu\n\nChoice: "))
            match budget_removing_choice:
                case 1:
                    for i, income in enumerate(Income):
                        print(f"Index {i}: {income}")
                    #removing the specific index
                    income_removing_choice = int(input("Enter the index of the income to remove: "))
                    Income.pop(income_removing_choice)
                    print("Income removed.")
                case 2:
                    for i, expense in enumerate(Expense):
                        print(f"Index {i}: {expense}")
                    expense_removing_choice = int(input("Enter the index of the expense to remove: "))
                    Expense.pop(expense_removing_choice)
                    print("Expense removed.")
                case 3:
                    break
                case _:
                    print("Error: Please enter a valid choice!")
        case 3:
            view_choice = int(input("What do you wish to view?\n1. History\n2. Calender\n3. Back to main menu\n\nChoice: "))
            match view_choice:
                case 1:
                    history_choice = int(input("What do you wish to view?\n1. Montly expenses\n2. Income summary\n3. Expense summary\n4. Budget list\n5. Back to main menu\n\nChoice: "))
                    total_income = 0
                    total_expense = 0
                    total_budget = 0
                    for i in Income:
                        total_income += i["Amount"]
                    for i in Expense:
                        total_expense += i["Amount"]
                    for i in Budget:
                        total_budget += i["Amount"]
                    match history_choice:
                        case 1:
                            print(f"Your total income was {total_income}.\nYour total expense was {total_expense}.")
                            if total_expense > total_budget:
                                print(f"Budget was exceeded by {total_expense - total_budget}.")
                            else:
                                print(f"You managed to stay within the budget by {total_budget - total_expense}.")
                        case 2:
                            print(f"Income summary:\n{Income}\n")
                        case 3:
                            print(f"Expense summary:\n{Expense}\n\n")
                        case 4:
                            for i, budget in enumerate(Budget):
                                print(f"{i}: {budget}")
                        case 5:
                            break
                        case _:
                            print("Error: Please enter a valid choice!")
                case 2:
                    print("Onthe way!")
                case 3:
                    break
                case _:
                    print("Error: Please enter a valid choice!")
        case 4:
            break
        case _:
            print("Error: Please enter a valid choice!")
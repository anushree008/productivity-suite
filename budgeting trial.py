import datetime
Income = []
Expense = []
Budget = []
total_income = 0
total_expense = 0
total_budget = 0
#keeping the loop running
while True:
    print("--- Budgeting Menu ---\n")
    budgeting_choice = int(input("What do you wish to do?\n1. Add new Income/Expense/Monthly budegt\n2. Remove existing Income/Expense/Budget\n3. View\n4. Back to main menu\n\nChoice: "))
    if budgeting_choice == 1:
        #adding values
        addition_choice = int(input("What would you like to add?\n1. Income\n2. Expense\n3. Monthly budget\n4. Back to main menu\n\nChoice: "))
        if addition_choice == 1:
            #dictonary for income to save multiple values in a single list
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
        elif addition_choice == 2:
            #dictonary for expense to save multiple values in a single list
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
        elif addition_choice == 3:
            budget_type = input("Enter budget type:\n")
            budget_amount = float(input("Enter the montly budget you would like to set:\n"))
            budget_dictonary = {
                "Type" : budget_type,
                "Amount" : budget_amount
            }
            Budget.append(budget_dictonary)
            print("The montly budget is set!")
        else:
            break
    elif budgeting_choice == 2:
        #removing values
        budget_removing_choice = int(input("What would you like to remove?\n1. Income\n2. Expense\n3. Back to main menu\n\nChoice: "))
        if addition_choice == 1:
            #adding indexes to list to indentify values in the list 
            for i, income in enumerate(Income):
                print(f"Index {i}: {income}")
            #removing the specific index
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
            for i in Income:
                total_income += i["Amount"]
            for i in Expense:
                total_expense += i["Amount"]
            for i in Budget:
                total_budget += i["Amount"]
            print(f"Your total income was {total_income}.\nYour total expense was {total_expense}.")
            print(f"Income summary:\n{Income}\n\nExpense summary:\n{Expense}\n\n")
            if total_expense > total_budget:
                print(f"Budget was exceeded by {total_expense - total_budget}.")
            else:
                print(f"You managed to stay within the budget by {total_budget - total_expense}.")
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
import time
import datetime
import calendar
import customtkinter

#calendar logic
def open_calendar(productivity_manager, budget_manager, focus_sessions):
    Calendar = customtkinter.CTk()
    Calendar.title("Calendar")
    Calendar.geometry("311x300")
    current_month = datetime.date.today().month
    current_year = datetime.date.today().year
    calendar_frame = customtkinter.CTkFrame(Calendar)
    calendar_frame.grid(row=2, column=0, columnspan=7)

    def open_day(day):
        day_window = customtkinter.CTkToplevel(Calendar)
        day_window.title(f"{day} {calendar.month_name[current_month]} {current_year}")
        day_window.geometry("400x500")
        selected_date = datetime.date(current_year, current_month, day)

        customtkinter.CTkLabel(day_window, text=f"{day} {calendar.month_name[current_month]} {current_year}", font=("Arial", 16)).pack(pady=10)

        # focus sessions
        customtkinter.CTkLabel(day_window, text="Focus Sessions:", font=("Arial", 14)).pack(anchor="w", padx=10)
        day_sessions = [s for s in focus_sessions if s["Date"] == selected_date]
        if day_sessions:
            for s in day_sessions:
                customtkinter.CTkLabel(day_window, text=f"  {s['Minutes']} minutes").pack(anchor="w", padx=20)
        else:
            customtkinter.CTkLabel(day_window, text="  No focus sessions.").pack(anchor="w", padx=20)

        # tasks
        customtkinter.CTkLabel(day_window, text="Tasks:", font=("Arial", 14)).pack(anchor="w", padx=10, pady=(10,0))
        if productivity_manager.tasks:
            for task in productivity_manager.tasks:
                customtkinter.CTkLabel(day_window, text=f"  {task['Name']} | {task['Category']} | Difficulty: {task['Difficulty']}").pack(anchor="w", padx=20)
        else:
            customtkinter.CTkLabel(day_window, text="  No tasks.").pack(anchor="w", padx=20)

        # income
        customtkinter.CTkLabel(day_window, text="Income:", font=("Arial", 14)).pack(anchor="w", padx=10, pady=(10,0))
        day_income = [i for i in budget_manager.income if i["Date"].date() == selected_date]
        if day_income:
            for i in day_income:
                customtkinter.CTkLabel(day_window, text=f"  {i['Type']} | {i['Amount']}").pack(anchor="w", padx=20)
        else:
            customtkinter.CTkLabel(day_window, text="  No income.").pack(anchor="w", padx=20)

        # expenses
        customtkinter.CTkLabel(day_window, text="Expenses:", font=("Arial", 14)).pack(anchor="w", padx=10, pady=(10,0))
        day_expense = [e for e in budget_manager.expense if e["Date"].date() == selected_date]
        if day_expense:
            for e in day_expense:
                customtkinter.CTkLabel(day_window, text=f"  {e['Type']} | {e['Amount']}").pack(anchor="w", padx=20)
        else:
            customtkinter.CTkLabel(day_window, text="  No expenses.").pack(anchor="w", padx=20)

    def prev_month():
        nonlocal current_month, current_year
        current_month -= 1
        if current_month == 0:
            current_month = 12
            current_year -= 1
        update_calendar()

    def next_month():
        nonlocal current_month, current_year
        current_month += 1
        if current_month == 13:
            current_month = 1
            current_year += 1
        update_calendar()

    prev_button = customtkinter.CTkButton(Calendar, text="<", width=30, command=prev_month)
    prev_button.grid(row=0, column=0)
    next_button = customtkinter.CTkButton(Calendar, text=">", width=30, command=next_month)
    next_button.grid(row=0, column=6)
    month_label = customtkinter.CTkLabel(Calendar, text="", font=("Arial", 20))
    month_label.grid(row=0, column=0, columnspan=7, pady=10)

    def update_calendar():
        for widget in calendar_frame.winfo_children():
            widget.destroy()
        month_label.configure(text=f"{calendar.month_name[current_month]} {current_year}")
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for column, day in enumerate(days):
            customtkinter.CTkLabel(calendar_frame, text=day).grid(row=0, column=column, padx=5)
        month_days = calendar.monthcalendar(current_year, current_month)
        for row_num, week in enumerate(month_days):
            for column_num, day in enumerate(week):
                if day == 0:
                    customtkinter.CTkLabel(calendar_frame, text="").grid(row=row_num+1, column=column_num)
                else:
                    customtkinter.CTkButton(calendar_frame, text=str(day), width=40, height=40,
                        command=lambda d=day: open_day(d)).grid(row=row_num+1, column=column_num, padx=2, pady=2)

    update_calendar()
    Calendar.mainloop()

#focus logic
class FocusTimer:
    def __init__(self, min):
        self.time_left = min * 60
        self.minutes = min
        self.is_running = False

    def start_countdown(self):
        self.is_running = True
        while self.time_left >= 0:
            min, sec = divmod(self.time_left, 60)
            print(f"Time remaining: {min:02d}:{sec:02d}")
            time.sleep(1)
            self.time_left -= 1
        self.is_running = False
        print("Time's up! Great job focusing.")

#productivity logic
class ProductivityManager:
    def __init__(self):
        self.tasks = []

    def run_menu(self):
        while True:
            print("\n--- Productivity Menu ---\n")
            productivity_choice = int(input("What do you wish to do?\n1. Add new task\n2. Remove existing task\n3. View existing tasks\n4. Back to main menu\n\nChoice: "))
            match productivity_choice:
                case 1:
                    self.add_task()
                case 2:
                    self.remove_task()
                case 3:
                    self.view_tasks()
                case 4:
                    break
                case _:
                    print("Error: Please enter a valid number!")

    def add_task(self):
        task_name = input("Task name:\n")
        task_type = input("Category name:\n")
        task_difficulty = int(input("Task difficulty (1-5):\n"))
        while not 1 <= task_difficulty <= 5:
            print("Error please enter a valid number!")
            task_difficulty = int(input("Task difficulty (1-5):\n"))
        tasks_dictionary = {
            "Name": task_name,
            "Category": task_type,
            "Difficulty": task_difficulty
        }
        self.tasks.append(tasks_dictionary)
        print("Saved.")

    def remove_task(self):
        if not self.tasks:
            print("No tasks to remove.")
            return
        for i, task in enumerate(self.tasks):
            print(f"{i}: {task['Name']}")
        task_removing_choice = int(input("Enter the number of the task to remove: "))
        if 0 <= task_removing_choice < len(self.tasks):
            self.tasks.pop(task_removing_choice)
            print("Task removed.")
        else:
            print("Error: Please enter a valid number!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks yet.")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i}: {task['Name']} | Category: {task['Category']} | Difficulty: {task['Difficulty']}")

#budget logic
class BudgetManager:
    def __init__(self):
        self.income = []
        self.expense = []
        self.budget = []

    def run_menu(self):
        while True:
            print("\n--- Budgeting Menu ---")
            budgeting_choice = int(input("What do you wish to do?\n1. Add new Income/Expense/Monthly budget\n2. Remove existing Income/Expense/Budget\n3. View\n4. Back to main menu\n\nChoice: "))
            match budgeting_choice:
                case 1:
                    self.add()
                case 2:
                    self.remove()
                case 3:
                    self.view()
                case 4:
                    break
                case _:
                    print("Error: Please enter a valid choice!")

    def add(self):
        addition_choice = int(input("What would you like to add?\n1. Income\n2. Expense\n3. Monthly budget\n4. Back\n\nChoice: "))
        match addition_choice:
            case 1:
                income_type = input("Enter income type:\n")
                income_value = float(input("Enter amount of income:\n"))
                income_date = datetime.datetime.strptime(input("Enter the date (dd:mm:yy):\n"), "%d:%m:%y")
                self.income.append({"Type": income_type, "Amount": income_value, "Date": income_date})
                print("New income added!")
            case 2:
                expense_type = input("Enter expense type:\n")
                expense_value = float(input("Enter the amount of expense:\n"))
                expense_date = datetime.datetime.strptime(input("Enter the date (dd:mm:yy):\n"), "%d:%m:%y")
                self.expense.append({"Type": expense_type, "Amount": expense_value, "Date": expense_date})
                print("New expense added!")
            case 3:
                budget_type = input("Enter budget type:\n")
                budget_amount = float(input("Enter the monthly budget:\n"))
                self.budget.append({"Type": budget_type, "Amount": budget_amount})
                print("Monthly budget set!")
            case 4:
                return
            case _:
                print("Error: Please enter a valid choice!")

    def remove(self):
        budget_removing_choice = int(input("What would you like to remove?\n1. Income\n2. Expense\n3. Back\n\nChoice: "))
        match budget_removing_choice:
            case 1:
                if not self.income:
                    print("No income to remove.")
                    return
                for i, income in enumerate(self.income):
                    print(f"{i}: {income['Type']} | {income['Amount']}")
                income_removing_choice = int(input("Enter the index to remove: "))
                if 0 <= income_removing_choice < len(self.income):
                    self.income.pop(income_removing_choice)
                    print("Income removed.")
                else:
                    print("Error: Please enter a valid number!")
            case 2:
                if not self.expense:
                    print("No expenses to remove.")
                    return
                for i, expense in enumerate(self.expense):
                    print(f"{i}: {expense['Type']} | {expense['Amount']}")
                expense_removing_choice = int(input("Enter the index to remove: "))
                if 0 <= expense_removing_choice < len(self.expense):
                    self.expense.pop(expense_removing_choice)
                    print("Expense removed.")
                else:
                    print("Error: Please enter a valid number!")
            case 3:
                return
            case _:
                print("Error: Please enter a valid choice!")

    def view(self):
        view_choice = int(input("What do you wish to view?\n1. History\n2. Back\n\nChoice: "))
        match view_choice:
            case 1:
                total_income = sum(i["Amount"] for i in self.income)
                total_expense = sum(i["Amount"] for i in self.expense)
                total_budget = sum(i["Amount"] for i in self.budget)
                print(f"\nTotal income: {total_income}")
                print(f"Total expenses: {total_expense}")
                if total_budget > 0:
                    if total_expense > total_budget:
                        print(f"Budget exceeded by {total_expense - total_budget}.")
                    else:
                        print(f"Within budget by {total_budget - total_expense}.")
                print(f"\nIncome: {self.income}")
                print(f"Expenses: {self.expense}")
            case 2:
                return
            case _:
                print("Error: Please enter a valid choice!")

#main menu
def main():
    productivity_manager = ProductivityManager()
    budget_manager = BudgetManager()
    focus_sessions = []

    while True:
        print("\n1. Timer\n2. Tasks\n3. Budget\n4. Calendar\n5. Quit")
        activity_choice = int(input("Choice: "))
        match activity_choice:
            case 1:
                print("\n--- Timer Menu ---\n")
                minutes = int(input("Enter the number of minutes for the timer: "))
                timer = FocusTimer(minutes)
                timer.start_countdown()
                focus_sessions.append({
                    "Date": datetime.date.today(),
                    "Minutes": minutes
                })
            case 2:
                productivity_manager.run_menu()
            case 3:
                budget_manager.run_menu()
            case 4:
                open_calendar(productivity_manager, budget_manager, focus_sessions)
            case 5:
                print("Goodbye!")
                break
            case _:
                print("Error: Please enter a valid choice!")

main()
import json
import datetime
class saving():
    def __init__(self):
        try:
            with open("/Users/anushreegovilkar/Documents/SRHIC/UG08/productivity-suite/productivity_data.json", "r") as f:
                data = json.load(f)
                self.tasks = data["tasks"]
                self.income = data["income"]
                self.expense = data["expense"]
                self.budget = data["budget"]
                self.focus_sessions = data["focus_sessions"]
                self.points = data["points"]
                self.last_budget_check_month = data["last_budget_check_month"]

                #converting the dates from string to date format
                for i in self.income:
                    i["Date"] = datetime.datetime.strptime(i["Date"], "%d:%m:%y")

                for i in self.expense:
                    i["Date"] = datetime.datetime.strptime(i["Date"], "%d:%m:%y")
        except:
            self.tasks = []
            self.income = []
            self.expense = []
            self.budget = []
            self.focus_sessions = []
            self.points = 0
            self.last_budget_check_month = datetime.date.today().month

    def save_data(self):
        with open("/Users/anushreegovilkar/Documents/SRHIC/UG08/productivity-suite/productivity_data.json", "w") as f:
            
            #converting data back to string to save in json file
            income_to_save = []
            for i in self.income:
                new_entry_income = dict(i)  # makes a copy of the dictionary, not the same one
                new_entry_income["Date"] = datetime.datetime.strftime(new_entry_income["Date"], "%d:%m:%y")
                income_to_save.append(new_entry_income)
                    
            expense_to_save = []    
            for i in self.expense:
                new_entry_expense = dict(i)
                new_entry_expense["Date"] = datetime.datetime.strftime(new_entry_expense["Date"], "%d:%m:%y")
                expense_to_save.append(new_entry_expense)

            data = {
                "tasks": self.tasks,
                "income": income_to_save,
                "expense": expense_to_save,
                "budget": self.budget,
                "focus_sessions": self.focus_sessions,
                "points": self.points
                }
            json.dump(data, f)

test = saving()
test.income.append({"Type": "Job", "Amount": 500, "Date": datetime.datetime.strptime("08:07:26", "%d:%m:%y")})
test.save_data()
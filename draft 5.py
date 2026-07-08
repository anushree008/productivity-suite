import time
import datetime
import calendar
import customtkinter
import threading
import json

class App(customtkinter.CTk):
    # defining the window
    def __init__(self):
        super().__init__()
        self.title("Productivity Suite")
        self.geometry("800x600")

        # data
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

        # layout
        self.sidebar = customtkinter.CTkFrame(self, width=150)
        self.sidebar.pack(side="left", fill="y", padx=10, pady=10)
        self.main_frame = customtkinter.CTkFrame(self)
        self.main_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # sidebar buttons
        customtkinter.CTkLabel(self.sidebar, text="Menu", font=("Arial", 18)).pack(pady=20)
        customtkinter.CTkButton(self.sidebar, text="Timer", command=self.show_timer).pack(pady=5, padx=10, fill="x")
        customtkinter.CTkButton(self.sidebar, text="Tasks", command=self.show_tasks).pack(pady=5, padx=10, fill="x")
        customtkinter.CTkButton(self.sidebar, text="Budget", command=self.show_budget).pack(pady=5, padx=10, fill="x")
        customtkinter.CTkButton(self.sidebar, text="Calendar", command=self.show_calendar).pack(pady=5, padx=10, fill="x")

        # points display in sidebar
        customtkinter.CTkLabel(self.sidebar, text="Points", font=("Arial", 14)).pack(pady=(30, 0))
        self.points_label = customtkinter.CTkLabel(self.sidebar, text="⭐ 0", font=("Arial", 20))
        self.points_label.pack(pady=5)

        self.show_timer()
        self.check_budget_month()

    # closing the window
    def clear_main(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    # ── BUDGET MONTH CHECK ─────────────────────────────────
    def check_budget_month(self):
        today = datetime.date.today()
        # check if month has changed since last check
        if today.month != self.last_budget_check_month:
            # get last month's expenses and budget
            last_month = self.last_budget_check_month
            last_year = today.year if today.month != 1 else today.year - 1
            total_expense = sum(
                e["Amount"] for e in self.expense
                if e["Date"].month == last_month and e["Date"].year == last_year
            )
            total_budget = sum(b["Amount"] for b in self.budget)
            if total_budget > 0:
                if total_expense <= total_budget:
                    self.add_points(100)
                    self.show_points_popup("🎉 Stayed within budget last month! +100 points")
                else:
                    self.add_points(-50)
                    self.show_points_popup("❌ Exceeded budget last month! -50 points")
            self.last_budget_check_month = today.month
        # check again every hour
        self.after(3600000, self.check_budget_month)

    # ── POINT SYSTEM ─────────────────────────────────────────
    # adding points
    def add_points(self, amount):
        self.points += amount
        self.points_label.configure(text=f"⭐ {self.points}")

    # message window for points 
    def show_points_popup(self, message):
        popup = customtkinter.CTkToplevel(self)
        popup.title("Points Update")
        popup.geometry("300x100")
        customtkinter.CTkLabel(popup, text=message, font=("Arial", 14)).pack(pady=20, padx=10)
        customtkinter.CTkButton(popup, text="OK", command=popup.destroy).pack()

    # ── TIMER ──────────────────────────────────────────────
    def show_timer(self):
        self.clear_main()
        customtkinter.CTkLabel(self.main_frame, text="Focus Timer", font=("Arial", 20)).pack(pady=20)

        self.timer_display = customtkinter.CTkLabel(self.main_frame, text="00:00", font=("Arial", 48))
        self.timer_display.pack(pady=20)

        input_frame = customtkinter.CTkFrame(self.main_frame)
        input_frame.pack(pady=10)
        customtkinter.CTkLabel(input_frame, text="Minutes:").pack(side="left", padx=5)
        self.timer_input = customtkinter.CTkEntry(input_frame, width=80)
        self.timer_input.pack(side="left", padx=5)

        customtkinter.CTkButton(self.main_frame, text="Start", command=self.start_timer).pack(pady=10)
        self.timer_status = customtkinter.CTkLabel(self.main_frame, text="")
        self.timer_status.pack(pady=5)

        self.timer_running = False

    def start_timer(self):
        if self.timer_running:
            return
        try:
            minutes = int(self.timer_input.get())
        except ValueError:
            self.timer_status.configure(text="Please enter a valid number!")
            return
        self.timer_running = True
        self.time_left = minutes * 60
        self.timer_minutes = minutes
        self.timer_status.configure(text="Timer running...")
        threading.Thread(target=self.run_timer, daemon=True).start()

    def run_timer(self):
        while self.time_left >= 0:
            mins, secs = divmod(self.time_left, 60)
            self.timer_display.configure(text=f"{mins:02d}:{secs:02d}")
            time.sleep(1)
            self.time_left -= 1
        self.timer_running = False

        # points: 2 points per 10 mins, only if at least 10 mins
        earned = (self.timer_minutes // 10) * 2
        if earned > 0:
            self.add_points(earned)
            self.timer_status.configure(text=f"Time's up! Great job! +{earned} points")
        else:
            self.timer_status.configure(text="Time's up! (Minimum 10 mins for points)")

        self.focus_sessions.append({
            "Date": datetime.date.today(),
            "Minutes": self.timer_minutes,
            "Points": earned
        })

    # ── TASKS ──────────────────────────────────────────────
    def show_tasks(self):
        self.clear_main()
        customtkinter.CTkLabel(self.main_frame, text="Tasks", font=("Arial", 20)).pack(pady=20)

        form = customtkinter.CTkFrame(self.main_frame)
        form.pack(pady=10, padx=20, fill="x")

        customtkinter.CTkLabel(form, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.task_name_input = customtkinter.CTkEntry(form, width=120)
        self.task_name_input.grid(row=0, column=1, padx=5, pady=5)

        customtkinter.CTkLabel(form, text="Category:").grid(row=0, column=2, padx=5, pady=5)
        self.task_category_input = customtkinter.CTkEntry(form, width=120)
        self.task_category_input.grid(row=0, column=3, padx=5, pady=5)

        customtkinter.CTkLabel(form, text="Difficulty (1-5):").grid(row=1, column=0, padx=5, pady=5)
        self.task_difficulty_input = customtkinter.CTkEntry(form, width=80)
        self.task_difficulty_input.grid(row=1, column=1, padx=5, pady=5)

        customtkinter.CTkLabel(form, text="Deadline (dd:mm:yy, optional):").grid(row=1, column=2, padx=5, pady=5)
        self.task_deadline_input = customtkinter.CTkEntry(form, width=120)
        self.task_deadline_input.grid(row=1, column=3, padx=5, pady=5)

        customtkinter.CTkButton(form, text="Add Task", command=self.add_task).grid(row=2, column=3, padx=5, pady=5)

        self.task_status = customtkinter.CTkLabel(self.main_frame, text="")
        self.task_status.pack()

        self.task_list_frame = customtkinter.CTkScrollableFrame(self.main_frame)
        self.task_list_frame.pack(fill="both", expand=True, padx=20, pady=10)
        self.refresh_task_list()

    def add_task(self):
        name = self.task_name_input.get()
        category = self.task_category_input.get()
        try:
            difficulty = int(self.task_difficulty_input.get())
        except ValueError:
            self.task_status.configure(text="Difficulty must be a number!")
            return
        if not 1 <= difficulty <= 5:
            self.task_status.configure(text="Difficulty must be between 1 and 5!")
            return
        if not name:
            self.task_status.configure(text="Please enter a task name!")
            return

        # optional deadline
        deadline = None
        deadline_str = self.task_deadline_input.get()
        if deadline_str:
            try:
                deadline = datetime.datetime.strptime(deadline_str, "%d:%m:%y").date()
            except ValueError:
                self.task_status.configure(text="Invalid deadline format! Use dd:mm:yy")
                return

        self.tasks.append({
            "Name": name,
            "Category": category,
            "Difficulty": difficulty,
            "Deadline": deadline,
            "Done": False,
            "Done_date": None
        })
        self.task_name_input.delete(0, "end")
        self.task_category_input.delete(0, "end")
        self.task_difficulty_input.delete(0, "end")
        self.task_deadline_input.delete(0, "end")
        self.task_status.configure(text="Task saved!")
        self.refresh_task_list()

    def refresh_task_list(self):
        for widget in self.task_list_frame.winfo_children():
            widget.destroy()
        if not self.tasks:
            customtkinter.CTkLabel(self.task_list_frame, text="No tasks yet.").pack()
            return
        for i, task in enumerate(self.tasks):
            row = customtkinter.CTkFrame(self.task_list_frame)
            row.pack(fill="x", pady=3)
            status = "✓" if task["Done"] else "✗"
            deadline_str = f" | Due: {task['Deadline']}" if task["Deadline"] else ""
            customtkinter.CTkLabel(row, text=f"{status} {task['Name']} | {task['Category']} | Difficulty: {task['Difficulty']}{deadline_str}").pack(side="left", padx=10)
            if not task["Done"]:
                customtkinter.CTkButton(row, text="Done", width=60, command=lambda i=i: self.mark_done(i)).pack(side="right", padx=5)
            customtkinter.CTkButton(row, text="Remove", width=70, command=lambda i=i: self.remove_task(i)).pack(side="right", padx=5)

    def mark_done(self, index):
        task = self.tasks[index]
        task["Done"] = True
        task["Done_date"] = datetime.date.today()

        # points based on difficulty
        base_points = task["Difficulty"] * 10

        if task["Deadline"] is None:
            # no deadline, full points
            earned = base_points
            msg = f"Task done! +{earned} points"
        elif task["Done_date"] <= task["Deadline"]:
            # on time, full points
            earned = base_points
            msg = f"Task done on time! +{earned} points"
        else:
            # late, half points rounded down
            earned = base_points // 2
            msg = f"Task done late! +{earned} points (half)"

        self.add_points(earned)
        self.task_status.configure(text=msg)
        self.refresh_task_list()

    def remove_task(self, index):
        self.tasks.pop(index)
        self.refresh_task_list()

    # ── BUDGET ─────────────────────────────────────────────
    def show_budget(self):
        self.clear_main()
        customtkinter.CTkLabel(self.main_frame, text="Budget", font=("Arial", 20)).pack(pady=20)

        form = customtkinter.CTkFrame(self.main_frame)
        form.pack(pady=10, padx=20, fill="x")

        customtkinter.CTkLabel(form, text="Type:").grid(row=0, column=0, padx=5, pady=5)
        self.budget_type_input = customtkinter.CTkEntry(form, width=120)
        self.budget_type_input.grid(row=0, column=1, padx=5, pady=5)

        customtkinter.CTkLabel(form, text="Amount:").grid(row=0, column=2, padx=5, pady=5)
        self.budget_amount_input = customtkinter.CTkEntry(form, width=100)
        self.budget_amount_input.grid(row=0, column=3, padx=5, pady=5)

        customtkinter.CTkLabel(form, text="Date (dd:mm:yy):").grid(row=1, column=0, padx=5, pady=5)
        self.budget_date_input = customtkinter.CTkEntry(form, width=120)
        self.budget_date_input.grid(row=1, column=1, padx=5, pady=5)

        customtkinter.CTkButton(form, text="Add Income", command=self.add_income).grid(row=1, column=2, padx=5, pady=5)
        customtkinter.CTkButton(form, text="Add Expense", command=self.add_expense).grid(row=1, column=3, padx=5, pady=5)

        customtkinter.CTkLabel(form, text="Monthly Budget:").grid(row=2, column=0, padx=5, pady=5)
        self.monthly_budget_input = customtkinter.CTkEntry(form, width=120)
        self.monthly_budget_input.grid(row=2, column=1, padx=5, pady=5)
        customtkinter.CTkButton(form, text="Set Budget", command=self.set_budget).grid(row=2, column=2, padx=5, pady=5)

        self.budget_status = customtkinter.CTkLabel(self.main_frame, text="")
        self.budget_status.pack()
        self.budget_summary = customtkinter.CTkLabel(self.main_frame, text="")
        self.budget_summary.pack(pady=5)

        self.budget_list_frame = customtkinter.CTkScrollableFrame(self.main_frame)
        self.budget_list_frame.pack(fill="both", expand=True, padx=20, pady=10)
        self.refresh_budget_list()

    def set_budget(self):
        try:
            amount = float(self.monthly_budget_input.get())
        except ValueError:
            self.budget_status.configure(text="Invalid amount!")
            return
        self.budget = [{"Amount": amount}]
        self.monthly_budget_input.delete(0, "end")
        self.budget_status.configure(text=f"Monthly budget set to {amount}!")
        self.refresh_budget_list()

    def add_income(self):
        try:
            amount = float(self.budget_amount_input.get())
            date = datetime.datetime.strptime(self.budget_date_input.get(), "%d:%m:%y")
        except ValueError:
            self.budget_status.configure(text="Invalid amount or date format!")
            return
        self.income.append({"Type": self.budget_type_input.get(), "Amount": amount, "Date": date})
        self.budget_status.configure(text="Income added!")
        self.clear_budget_inputs()
        self.refresh_budget_list()

    def add_expense(self):
        try:
            amount = float(self.budget_amount_input.get())
            date = datetime.datetime.strptime(self.budget_date_input.get(), "%d:%m:%y")
        except ValueError:
            self.budget_status.configure(text="Invalid amount or date format!")
            return
        self.expense.append({"Type": self.budget_type_input.get(), "Amount": amount, "Date": date})
        self.budget_status.configure(text="Expense added!")
        self.clear_budget_inputs()
        self.refresh_budget_list()

    def clear_budget_inputs(self):
        self.budget_type_input.delete(0, "end")
        self.budget_amount_input.delete(0, "end")
        self.budget_date_input.delete(0, "end")

    def refresh_budget_list(self):
        for widget in self.budget_list_frame.winfo_children():
            widget.destroy()
        total_income = sum(i["Amount"] for i in self.income)
        total_expense = sum(e["Amount"] for e in self.expense)
        total_budget = sum(b["Amount"] for b in self.budget)
        self.budget_summary.configure(text=f"Income: {total_income} | Expenses: {total_expense} | Balance: {total_income - total_expense} | Monthly Budget: {total_budget}")
        if not self.income and not self.expense:
            customtkinter.CTkLabel(self.budget_list_frame, text="No entries yet.").pack()
            return
        for i, item in enumerate(self.income):
            row = customtkinter.CTkFrame(self.budget_list_frame)
            row.pack(fill="x", pady=3)
            customtkinter.CTkLabel(row, text=f"[Income] {item['Type']} | {item['Amount']} | {item['Date'].strftime('%d/%m/%y')}").pack(side="left", padx=10)
            customtkinter.CTkButton(row, text="Remove", width=70, command=lambda i=i: self.remove_income(i)).pack(side="right", padx=5)
        for i, item in enumerate(self.expense):
            row = customtkinter.CTkFrame(self.budget_list_frame)
            row.pack(fill="x", pady=3)
            customtkinter.CTkLabel(row, text=f"[Expense] {item['Type']} | {item['Amount']} | {item['Date'].strftime('%d/%m/%y')}").pack(side="left", padx=10)
            customtkinter.CTkButton(row, text="Remove", width=70, command=lambda i=i: self.remove_expense(i)).pack(side="right", padx=5)

    def remove_income(self, index):
        self.income.pop(index)
        self.refresh_budget_list()

    def remove_expense(self, index):
        self.expense.pop(index)
        self.refresh_budget_list()

    # ── CALENDAR ───────────────────────────────────────────
    def show_calendar(self):
        self.clear_main()
        self.current_month = datetime.date.today().month
        self.current_year = datetime.date.today().year

        top = customtkinter.CTkFrame(self.main_frame)
        top.pack(pady=10)
        customtkinter.CTkButton(top, text="<", width=30, command=self.prev_month).pack(side="left", padx=5)
        self.month_label = customtkinter.CTkLabel(top, text="", font=("Arial", 20))
        self.month_label.pack(side="left", padx=20)
        customtkinter.CTkButton(top, text=">", width=30, command=self.next_month).pack(side="left", padx=5)

        self.cal_frame = customtkinter.CTkFrame(self.main_frame)
        self.cal_frame.pack(pady=10)
        self.refresh_calendar()

    def prev_month(self):
        self.current_month -= 1
        if self.current_month == 0:
            self.current_month = 12
            self.current_year -= 1
        self.refresh_calendar()

    def next_month(self):
        self.current_month += 1
        if self.current_month == 13:
            self.current_month = 1
            self.current_year += 1
        self.refresh_calendar()

    def refresh_calendar(self):
        for widget in self.cal_frame.winfo_children():
            widget.destroy()
        self.month_label.configure(text=f"{calendar.month_name[self.current_month]} {self.current_year}")
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for col, day in enumerate(days):
            customtkinter.CTkLabel(self.cal_frame, text=day, width=50).grid(row=0, column=col, padx=2, pady=2)
        month_days = calendar.monthcalendar(self.current_year, self.current_month)
        for row_num, week in enumerate(month_days):
            for col_num, day in enumerate(week):
                if day == 0:
                    customtkinter.CTkLabel(self.cal_frame, text="", width=50).grid(row=row_num+1, column=col_num)
                else:
                    customtkinter.CTkButton(self.cal_frame, text=str(day), width=50, height=40,
                        command=lambda d=day: self.open_day(d)).grid(row=row_num+1, column=col_num, padx=2, pady=2)

    def open_day(self, day):
        selected_date = datetime.date(self.current_year, self.current_month, day)
        day_window = customtkinter.CTkToplevel(self)
        day_window.title(f"{day} {calendar.month_name[self.current_month]} {self.current_year}")
        day_window.geometry("400x500")

        customtkinter.CTkLabel(day_window, text=f"{day} {calendar.month_name[self.current_month]} {self.current_year}", font=("Arial", 16)).pack(pady=10)

        scroll = customtkinter.CTkScrollableFrame(day_window)
        scroll.pack(fill="both", expand=True, padx=10, pady=10)

        # focus
        customtkinter.CTkLabel(scroll, text="Focus Sessions:", font=("Arial", 14)).pack(anchor="w", pady=(10,0))
        day_sessions = [s for s in self.focus_sessions if s["Date"] == selected_date]
        if day_sessions:
            for s in day_sessions:
                customtkinter.CTkLabel(scroll, text=f"  {s['Minutes']} mins | +{s['Points']} points").pack(anchor="w", padx=10)
        else:
            customtkinter.CTkLabel(scroll, text="  None").pack(anchor="w", padx=10)

        # tasks
        customtkinter.CTkLabel(scroll, text="Tasks Completed:", font=("Arial", 14)).pack(anchor="w", pady=(10,0))
        day_tasks = [t for t in self.tasks if t["Done"] and t["Done_date"] == selected_date]
        if day_tasks:
            for t in day_tasks:
                customtkinter.CTkLabel(scroll, text=f"  ✓ {t['Name']} | Difficulty: {t['Difficulty']}").pack(anchor="w", padx=10)
        else:
            customtkinter.CTkLabel(scroll, text="  None").pack(anchor="w", padx=10)

        # income
        customtkinter.CTkLabel(scroll, text="Income:", font=("Arial", 14)).pack(anchor="w", pady=(10,0))
        day_income = [i for i in self.income if i["Date"].date() == selected_date]
        if day_income:
            for i in day_income:
                customtkinter.CTkLabel(scroll, text=f"  {i['Type']} | {i['Amount']}").pack(anchor="w", padx=10)
        else:
            customtkinter.CTkLabel(scroll, text="  None").pack(anchor="w", padx=10)

        # expenses
        customtkinter.CTkLabel(scroll, text="Expenses:", font=("Arial", 14)).pack(anchor="w", pady=(10,0))
        day_expense = [e for e in self.expense if e["Date"].date() == selected_date]
        if day_expense:
            for e in day_expense:
                customtkinter.CTkLabel(scroll, text=f"  {e['Type']} | {e['Amount']}").pack(anchor="w", padx=10)
        else:
            customtkinter.CTkLabel(scroll, text="  None").pack(anchor="w", padx=10)

app = App()
app.mainloop()
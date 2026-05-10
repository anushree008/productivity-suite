#timer logic
import time
class FocusTimer:
    def __init__ (self,min):
        self.time_left =  min * 60
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
            print("\n--- Productivity Menu ---")
            choice = int(input("What do you wish to do?\n1. Add new task\n2. Remove existing task\n3. View existing tasks\n4. Back to main menu\n\nChoice: "))
            if choice == 1:
                self.add_task()
            elif choice == 2:
                self.remove_task()
            elif choice == 3:
                self.view_tasks()
            elif choice == 4:
                break 
            else:
                print("Error: Please enter a valid number!")

    def add_task(self):
        task_name = input("Task name:\n")
        task_type = input("Category name:\n")
        task_difficulty = int(input("Task difficulty (1-5):\n"))
        tasks_dictionary = {
            "Name" : task_name,
            "Category" : task_type,
            "Difficulty" :task_difficulty
        }
        self.tasks.append(tasks_dictionary)

    def remove_task(self):
        for index, task in enumerate(self.tasks):
            print(f"{index}: {task['Name']}")
        removing_choice = int(input("Enter the number of the task to remove: "))
        self.tasks.pop(removing_choice)
        print("Task removed.")

    def view_tasks(self):
        print(self.tasks)

#asking user for the activity they wish to do
class ActivityChoice:
    def __init__ (self,activity_choice):
        self.activity_choice = activity_choice
    def status(self):
        if self.activity_choice == "timer":
            user_choice = int(input("How many minutes? "))
            my_timer = FocusTimer(user_choice)
            my_timer.start_countdown()
        elif self.activity_choice == "productivity":
            manager = ProductivityManager()
            manager.run_menu()
        else:
            print("testing")

activity = input("What do you want to do?:\n")
my_choice = ActivityChoice(activity)
my_choice.status()
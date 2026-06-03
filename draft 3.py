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
            print("\n--- Productivity Menu ---\n")
            productivity_choice = int(input("What do you wish to do?\n1. Add new task\n2. Remove existing task\n3. View existing tasks\n4. Back to main menu\n\nChoice: "))
            if productivity_choice == 1:
                self.add_task()
            elif productivity_choice == 2:
                self.remove_task()
            elif productivity_choice == 3:
                self.view_tasks()
            elif productivity_choice == 4:
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
        for i, task in enumerate(self.tasks):
            print(f"{i}: {task['Name']}")
        task_removing_choice = int(input("Enter the number of the task to remove: "))
        self.tasks.pop(task_removing_choice)
        print("Task removed.")

    def view_tasks(self):
        print(self.tasks)
#asking user for the activity they wish to do
def main():
    while True:
        print("1. Timer\n2. Tasks\n3. Budget\n4. Quit")
        activity_choice = int(input("Choice: "))
        if activity_choice == 1:
            print("\n--- Timer Menu ---\n")
            timer = FocusTimer(int(input("Enter the number of minutes for the timer: ")))
            timer.start_countdown()
        elif activity_choice == 2:
            productivity_manager = ProductivityManager()
            productivity_manager.run_menu()
        elif activity_choice == 3:
            print("Budget feature coming soon!")
        elif activity_choice == 4:
            print("Goodbye!")
            break
        else:
            print("Error: Please enter a valid choice!")

main()
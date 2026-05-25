#getting stats
import json
#loading existing tasks 
try:
    with open("/Users/anushreegovilkar/Documents/SRHIC/UG08/portfolio/productivity data.txt", "r") as f:
        tasks = json.load(f)
except:
    tasks = []  #if file empty or doesn't exist
#loading exisiting completed tasks
try:
    with open("/Users/anushreegovilkar/Documents/SRHIC/UG08/portfolio/completed tasks.txt", "r") as f:
        completed_tasks = json.load(f)
except:
    completed_tasks = []
try:
    productivity_choice = int(input("what do you wish to do?\n1. Add new task.\n2. Remove existing task.\n3. Mark as completed\n4. View existing tasks.\n: "))
except ValueError:
    print("Error please enter a valid number!")
    productivity_choice = 0
if productivity_choice == 1:
    #add task
    task_name = input("Task name:\n")
    task_type = input("Category name:\n")
    task_difficulty = int(input("Task difficulty (1-5):\n"))
    while not 1 <= task_difficulty <= 5:
        print("Error please enter a valid number!")
        task_difficulty = int(input("Task difficulty (1-5):\n"))
    tasks_dictionary = {
        "Name" : task_name,
        "Category" : task_type,
        "Difficulty" : task_difficulty
    }
    tasks.append(tasks_dictionary)
    print("Saved.")
elif productivity_choice == 2:
    #remove task
    for index, task in enumerate(tasks):
        print(f"{index}: {task['Name']}")
    removing_choice = int(input("Enter the number of the task to remove: "))
    if 0 <= removing_choice < len(tasks):
        tasks.pop(removing_choice)
        print("Task removed.")
    else:
        print("Error please enter a valid number!")
elif productivity_choice == 3:
    #mark as completed
    for index, task in enumerate(tasks):
        print(f"{index}: {task['Name']}")
    mark_completed = int(input("Enter the number of the task to mark as completed: "))
    if 0 <= mark_completed < len(tasks):
        completed_tasks.append(tasks[mark_completed])
        tasks.pop(mark_completed)
        print("Task marked as completed.")
    else:
        print("Error please enter a valid number!")
elif productivity_choice == 4:
    #view tasks
    print(tasks)
else:
    print("Error please enter a valid number!")
#saving difficulties to file
difficulties = [task["Difficulty"] for task in tasks]
print(f"Difficulties: {difficulties}")
with open("/Users/anushreegovilkar/Documents/SRHIC/UG08/portfolio/productivity data.txt", "w") as f:
    json.dump(tasks, f)
#saving completed tasks to file
with open("/Users/anushreegovilkar/Documents/SRHIC/UG08/portfolio/completed tasks.txt", "w") as f:
    json.dump(completed_tasks, f)
#display completed tasks
print(f"Completed tasks: {completed_tasks}")
#defining tasks
tasks = []

#choice for action
productivity_choice = int(input("what do you wish to do?\n1. Add new task.\n2.Remove existing task.\n3.View existing tasks.\n: "))

#getting tasks
task_name = input("Task name:\n")
task_type = input("Catogory name:\n")
task_difficulty = int(input("Task difficulty (1-5):\n"))
tasks_dictonary = {
    "Name" : task_name,
    "Catogory" : task_type,
    "Difficulty" :task_difficulty
}
tasks.append(tasks_dictonary)
#display tasks
print(tasks)

#to print tasks with index numbers
for index, task in enumerate(tasks):
    print(f"{index}: {task['Name']}")
removing_choice = int(input("Enter the number of the task to remove: "))
tasks.pop(removing_choice)
#validation
print("Task removed.")
print(tasks)
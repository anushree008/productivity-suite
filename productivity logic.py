#defining tasks
tasks = []
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
tasks = []
task_name = input("Task name:\n")
task_type = input("Catogory name:\n")
task_difficulty = int(input("Task difficulty (1-5):\n"))
tasks_dictonary = {
    "name" : task_name,
    "type" : task_type,
    "difficulty" :task_difficulty
}
tasks.append(tasks_dictonary)
#opening the file
productivity_data_appened = open("/Users/anushreegovilkar/Documents/SRHIC/UG08/portfolio/productivity data.txt","a")
#defining tasks
tasks = []
#choice for action
productivity_choice = int(input("what do you wish to do?\n1. Add new task.\n2.Remove existing task.\n3.View existing tasks.\n: "))
if productivity_choice == 1:
    #getting tasks
    task_name = input("Task name:\n")
    task_type = input("Category name:\n")
    task_difficulty = int(input("Task difficulty (1-5):\n"))
    tasks_dictonary = {
        "Name" : task_name,
        "Category" : task_type,
        "Difficulty" :task_difficulty
    }
    tasks.append(tasks_dictonary)
    #display tasks
    print("saved")
elif productivity_choice == 2:
    #to print tasks with index numbers
    for index, tasks in enumerate(tasks):
        print(f"{index}: {tasks['Name']}")
    removing_choice = int(input("Enter the number of the task to remove: "))
    tasks.pop(removing_choice)
    #validation
    print("Task removed.")
elif productivity_choice == 3:
    productivity_data_read = open("/Users/anushreegovilkar/Documents/SRHIC/UG08/portfolio/productivity data.txt","r")
    print(productivity_data_read.read())
else:
    print("Error please entr a valid number!")
#adding list to file
for i in tasks:
    productivity_data_appened.write(str(i)+"\n")
productivity_data_read = open("/Users/anushreegovilkar/Documents/SRHIC/UG08/portfolio/productivity data.txt","r")
#print(productivity_data_read.read())
tasks.append(productivity_data_read.read())
print(tasks)
tasks = []

def addTask():
    task = input("Enter the task to be added: ")
    tasks.append(task)
    print(f"Task '{task}' is added in the list")

def deleteTask():
    task = input("Enter the task to be deleted: ")
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' is deleted from the list")
    else:
        print(f"Task '{task}' not found in the list")

def listTasks():
    print("Tasks in the list:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def markTask():
    task = input("Enter the task to mark as done/not done: ")
    if task in tasks:
        index = tasks.index(task)
        if "[Done]" in tasks[index]:
            tasks[index] = tasks[index].replace("[Done]", "")
            print(f"Task '{task}' marked as Not Done")
        else:
            tasks[index] += " [Done]"
            print(f"Task '{task}' marked as Done")
    else:
        print(f"Task '{task}' not found in the list")
def renameTask():
    old_task = input("Enter the task to rename: ")
    if old_task in tasks:
        new_task = input("Enter the new name for the task: ")
        index = tasks.index(old_task)
        tasks[index] = new_task
        print(f"Task '{old_task}' renamed to '{new_task}'")
    else:
        print(f"Task '{old_task}' not found in the list")

while True:
    print("\n***To Do List****")
    print("1. Add a new task")
    print("2. Delete an existing task")
    print("3. List the tasks")
    print("4. Mark a task as done/not done")
    print("5. Rename a task")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    if choice == "1":
        addTask()
    elif choice == "2":
        deleteTask()
    elif choice == "3":
        listTasks()
    elif choice == "4":
        markTask()
    elif choice == "5":
        renameTask()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")

Tasks = []

def add_task():
    description = input("Enter task description:")
    due_date = input("Enter due date:")
    priority = input("Enter the priority in numbers:")

    task_dict = {"Description": description, "Due date": due_date, "Priority": priority, "Status": "Incomplete"}
    Tasks.append(task_dict)
    print("Task added successfully!")

def update_status():
    a = int(input("Enter the serial number of the task you want to update: ")) - 1
    b = input("Enter 'y' if the task is completed, enter 'n' if the task is incomplete: ")
    if 0 <= a < len(Tasks):
        if b == "y":
            Tasks[a]["Status"] = "Completed"
        else:
            Tasks[a]["Status"] = "Incomplete"
        print("Status updated successfully!!")
    else:
        print("Task not found with the specified serial number")

def update_task():
    a = int(input("Enter the serial number of the task you want to update: ")) - 1
    if 0 <= a < len(Tasks):
        d = input("Enter the new task description:")
        b = input("Enter the new due date:")
        c = input("Enter priority:")
        Tasks[a]["Description"] = d
        Tasks[a]["Due date"] = b
        Tasks[a]["Priority"] = c
        print("Task updated successfully!!")
    else:
        print("Task not found with the specified serial number")

def remove_task():
    a = int(input("Enter the serial number of the task you want to remove: ")) - 1
    if 0 <= a < len(Tasks):
        del Tasks[a]
        print("Task removed successfully!!")
    else:
        print("Task not found with the specified serial number")

print("\nOptions:")
print("1. Add Task")
print("2. Display Tasks")
print("3. Update Status")
print("4. Update Task")
print("5. Remove Task")
print("6. Exit")

while True:
    choice = input("Enter your choice:")

    if choice == "1":
        add_task()
    elif choice == "2":
        if Tasks:
            for index, element in enumerate(Tasks, start=1):
                print(f"Task {index}:")
                for key, value in element.items():
                    print(f"{key}: {value}")
        else:
            print("No tasks.")
    elif choice == "3":
        update_status()
    elif choice == "4":
        update_task()
    elif choice == "5":
        remove_task()
    elif choice == "6":
        print("Exiting from the app")
        break
    else:
        print("Invalid choice")

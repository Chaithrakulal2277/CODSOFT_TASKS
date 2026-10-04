tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, 1):
                print(i, task)

    elif choice == "3":
        num = int(input("Enter task number: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1] = input("Enter new task: ")
            print("Task updated.")
        else:
            print("Invalid task number.")

    elif choice == "4":
        num = int(input("Enter task number: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            print("Task deleted.")
        else:
            print("Invalid task number.")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
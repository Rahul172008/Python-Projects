tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task Added Successfully!")

    elif choice == 2:
        print("\nYour Tasks:")
        for task in tasks:
            print("-", task)

    elif choice == 3:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
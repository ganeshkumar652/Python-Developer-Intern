# ---------------- Load existing tasks ----------------
tasks = []

# Try reading the file and load tasks
try:
    file = open("tasks.txt", "r")
    for line in file:
        tasks.append(line.strip())
    file.close()
except FileNotFoundError:
    # Create empty file if it doesn't exist
    open("tasks.txt", "w").close()


# ---------------- Main Loop ----------------
while True:
    print("\n----- TO-DO APP -----")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # ---------- Add task ----------
    if choice == "1":
        task = input("Enter the new task: ")
        tasks.append(task)

        # Save tasks to file
        file = open("tasks.txt", "w")
        for t in tasks:
            file.write(t + "\n")
        file.close()

        print("Task added!")

    # ---------- Remove task ----------
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")

            try:
                num = int(input("Enter task number to remove: "))
                if 1 <= num <= len(tasks):
                    removed_task = tasks.pop(num - 1)

                    # Update file
                    file = open("tasks.txt", "w")
                    for t in tasks:
                        file.write(t + "\n")
                    file.close()

                    print("Removed:", removed_task)
                else:
                    print("Invalid number.")
            except ValueError:
                print("Enter a valid number.")

    # ---------- View tasks ----------
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")

    # ---------- Exit ----------
    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please choose 1-4.")

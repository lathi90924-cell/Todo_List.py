tasks = []
next_id = 1


def add_task():
    global next_id

    description = input("Enter task description: ").strip()

    if description == "":
        print("Task description cannot be empty!")
        return

    task = {
        "id": next_id,
        "description": description,
        "status": "Pending"
    }

    tasks.append(task)
    next_id += 1
    print("Task added successfully!")


def view_tasks():
    if len(tasks) == 0:
        print("No tasks available!")
    else:
        print("\n===== YOUR TASKS =====")
        for task in tasks:
            print("ID:", task["id"])
            print("Task:", task["description"])
            print("Status:", task["status"])
            print("----------------------")


def update_task():
    try:
        task_id = int(input("Enter task ID to update: "))

        for task in tasks:
            if task["id"] == task_id:
                new_description = input(
                    "Enter new task description: "
                ).strip()

                if new_description == "":
                    print("Task description cannot be empty!")
                    return

                task["description"] = new_description
                print("Task updated successfully!")
                return

        print("Task ID not found!")

    except ValueError:
        print("Please enter a valid numeric ID!")


def complete_task():
    try:
        task_id = int(input("Enter task ID to complete: "))

        for task in tasks:
            if task["id"] == task_id:
                if task["status"] == "Pending":
                    task["status"] = "Completed"
                    print("Task marked as completed!")
                else:
                    print("Task is already completed!")
                return

        print("Task ID not found!")

    except ValueError:
        print("Please enter a valid numeric ID!")


def delete_task():
    try:
        task_id = int(input("Enter task ID to delete: "))

        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                print("Task deleted successfully!")
                return

        print("Task ID not found!")

    except ValueError:
        print("Please enter a valid numeric ID!")


def main():
    while True:
        print("\n===== TODO APPLICATION =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            complete_task()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            print("Thank you for using TODO Application!")
            break
        else:
            print("Invalid choice! Enter a number from 1 to 6.")


if __name__ == "__main__":
    main()

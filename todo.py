tasks=[]

def show_mean():
    print("Mean of the tasks:")
    print("1.Add Tasks")
    print("2.Remove Tasks")
    print("3.view tasks")
    print("4.Show Mean")    
    print("5.Exit")
    print("6.Clear Tasks")  

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):  # Display each task with a number
            print(f"{index}. {task}")

def remove_task():
    view_tasks()  # Show the current list of tasks
    if tasks:
        try:
            task_num = int(input("Enter the task number to remove: "))  # Ask user for the task number
            if 1 <= task_num <= len(tasks):  # Validate input
                removed_task = tasks.pop(task_num - 1)  # Remove the task from the list
                print(f'Task "{removed_task}" removed successfully!')
            else:
                print("Invalid task number. Try again.")
        except ValueError:
            print("Please enter a valid number.")
while True:
    show_mean()  # Display menu options
    choice = input("Choose an option (1-4): ")  # Get user choice

    if choice == "1":
        add_task()  # Call add_task function
    elif choice == "2":
        view_tasks()  # Call view_tasks function
    elif choice == "3":
        remove_task()  # Call remove_task function
    elif choice == "4":
        print("Goodbye! Exiting the program.")  # Exit message
        break  # Exit the loop
    else:
        print("Invalid choice. Please try again.")  # Error handling

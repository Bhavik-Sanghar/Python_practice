# Simple Command-Line To-Do List

tasks = []

while True:
    print("\n--- MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    
    opt = input("Select an option (1-4): ")
    
    if opt == '1':
        task = input('Enter Task: ')
        tasks.append(task)  
        print("Task Added Successfully !!")
        
    elif opt == '2':
        if not tasks:
            print("No tasks in the list.")
        else:
            print("\nCurrent Tasks:")
            for index, task in enumerate(tasks, 1):
                print(f"{index}. {task}")
                
    elif opt == '3':
        if not tasks:
            print("No tasks to remove.")
        else:
            task_to_remove = input("Enter the name of the task to remove: ")
            if task_to_remove in tasks:
                tasks.remove(task_to_remove)
                print("Task removed successfully.")
            else:
                print("Task not found.")
                
    elif opt == '4':
        print("Exiting...")
        break
        
    else:
        print("Invalid option. Please try again.")
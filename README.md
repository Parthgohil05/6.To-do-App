# Task Management App

## Overview

The Task Management App is a simple command-line tool for managing a list of tasks. You can add, update, delete, and view tasks through an interactive interface. This app helps you keep track of your tasks for the day efficiently.

## Features

- **Add Tasks**: Add new tasks to your task list.
- **Update Tasks**: Update existing tasks with new details.
- **Delete Tasks**: Remove tasks from your list.
- **View Tasks**: View all tasks in your list.
- **Exit**: Exit the application.

## How to Use

1. **Start the Application**: When you run the application, you will be greeted with a welcome message.

2. **Initial Task Entry**:
    - The app will prompt you to enter the number of tasks you want to add initially.
    - Enter the tasks one by one as prompted.

3. **Task Management Menu**:
    - After entering the initial tasks, you will see a menu with the following options:
        1. Add
        2. Update
        3. Delete
        4. View
        5. Exit

4. **Perform Operations**:
    - **Add a Task**: Enter `1` and then the name of the new task to add it to your list.
    - **Update a Task**: Enter `2`, then provide the name of the task you want to update, followed by the new task details.
    - **Delete a Task**: Enter `3`, then provide the name of the task you want to delete.
    - **View Tasks**: Enter `4` to see all tasks currently in your list.
    - **Exit**: Enter `5` to exit the application.

5. **Invalid Operations**:
    - If you enter an invalid operation number, the app will prompt you to enter a valid operation.

## Example

```python
def task():
    task = []
    print("-----Welcome To the Task Management App-----")
    
    total_task = int(input("Enter how many tasks you want to add: "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i}: ")
        task.append(task_name)
        
    print(f"Today's Tasks are\n{task}")
    
    while True:
        operation = int(input("Enter \n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit: "))
        if operation == 1:
            new_task = input("Enter the task you want to add: ")
            task.append(new_task)
            print(f"Task {new_task} has been successfully added.")
            
        elif operation == 2:
            update_task = input("Enter the task name you want to update: ")
            if update_task in task:
                new_task1 = input("Enter new task: ")
                index = task.index(update_task)
                task[index] = new_task1
                print(f"Task {new_task1} has been successfully updated.")
        
        elif operation == 3:
            delete_value = input("Enter the task you want to delete: ")
            if delete_value in task:
                ind = task.index(delete_value)
                del task[ind]
                print(f"Task {delete_value} has been successfully deleted.")
                
        elif operation == 4:
            print(f"Total tasks: {task}")
        
        elif operation == 5:
            print("Your app is closing...")
            break 
        
        else:
            print("Enter a valid operation.")

if __name__ == "__main__":
    task()
```

## Notes

- Ensure you have Python installed to run the application.
- This app runs in the command-line interface and requires user input for managing tasks.

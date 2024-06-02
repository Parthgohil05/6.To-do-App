def task():
    task = []
    print("-----Welcome To the Task Management App-----")
    
    total_task=int(input("Enter How many task you want to add ="))
    for i in range(1,total_task+1):
        task_name= input(f"Enter the task{i} =")
        task.append(task_name)
        
    print(f"Today's Tasks are\n{task}")
    
    while True:
        operation = int(input("Enter \n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit"))
        if operation == 1:
            new_task = input("Enter task you want to add =")
            task.append(new_task)
            print(f" Task {new_task} has been successfully added..")
            
        elif operation == 2:
            update_task = input("Enter the task name you want to update =")
            if update_task in task:
                new_task1 = input("Enter new Task =")
                index = task.index(update_task)
                task[index]=new_task1
                print(f"Updated Task {new_task1} has been Successfully Updated..")
        
        elif operation == 3:
            delete_value = input("Enter task that you want to Delete =")
            if delete_value in task:
                ind = task.index(delete_value)
                del task[ind]
                print(f"Deleted Task {delete_value} has been Successfully Deleted..")
                
        elif operation == 4:
            print(f"Total Task : {task}")
        
        elif operation == 5:
            print("Your App is Closing..")  
            break 
        
        else:
            print("Enter Vaild opration..")
            
if __name__=="__main__":
    task()
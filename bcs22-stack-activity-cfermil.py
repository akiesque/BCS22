# Create a task manager in python using stack with basic functionalities:
#  (classes, methods, lists, loops, input-handling in python )
#  - add tasks with a title and descriptiom
#  - mark tasks as completed
#  - display the list of tasks along with status
#  - exit option to exit the task manager
#  push in your gitHub account and paste the URL in our SB- lab
#  bcs21-stack-activity-ffernandez.py

import time
import sys
    
def ctc(): 
    sys.stdout.write("\u001b[2J") #clears the text.
    time.sleep(.3)
        
class Task:
    def __init__(self, title, desc):
        self.title = title
        self.description = desc
        self.status = "Uncomplete"
    
class TaskManager(Task):
        
    def __init__(self):
        self.tasklist = []
    
    def add_task(self, title, description):
        task = Task(title, description)
        self.tasklist.append(task)
    
    def mark_as_completed(self):
        task_index = int(input("Please enter the task number to be completed: "))
        if self.tasklist[task_index-1] in self.tasklist:
            self.tasklist[task_index-1].status = "Complete"
            print(f"\nTask [{task_index}] has been completed.\n Well done!\n")
        else:
            print(f'Task {task_index} does not exist.')  
        
    def display_tasks(self):
        if self.tasklist:
            print("All Tasks")
            for i, task in enumerate(self.tasklist, 1):
                print(f'{i}. {task.title} | Status: {task.status}\n Description: {task.description}\n')
        else:
            print('There are no Current Tasks.') 


task_manager = TaskManager()

while True:
    print('\nWelcome to the Task Manager! \n\n1. Add Task\n2. Complete Task\n3. Display Tasks\n4. Exit')
    choice = input('Select Option: ') 

    if choice == '1':
        title = input('Enter Task Title: ')
        desc = input('Enter Task Description: ')
        task_manager.add_task(title, desc)
        ctc()
        print("A new task has been added! Press [3] to check all tasks.\n")

    elif choice == '2':
        task_manager.mark_as_completed()

    elif choice == '3':
        task_manager.display_tasks()

    elif choice == '4':
        print("Thank you for visiting the Task Manager. Have a good day!")
        break

    else:
        print('Please Select an Option.')
    

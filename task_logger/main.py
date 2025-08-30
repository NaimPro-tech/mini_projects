from task import Task
from task_manager import TaskManager
from validation import get_task
import csv
from datetime import datetime


csv_path = "/home/npro/mini projects/task_logger/task_file.csv"
print("=====Welcome to Task Logger=====")

manager = TaskManager(csv_path)
try:
    while True:
        
        print("*****Menu*****")
        print("\n1.Add New Task\n2.Remove a Task\n3.Update a Task\n4.View All Task\n5.Search Task\n6.Exit")
        choice = int(input("Enter an option(1-5): "))

        if choice == 1:
            task = get_task()
            if task:
                manager.save_task(task)
            else:
                print("Invalid Input.")

        elif choice == 2:
            t_no = int(input("Enter a task no to remove: "))
            manager.remove_task(t_no)
            print("Remove Successfully")

        elif choice == 3:
            t_no = int(input("Enter task id to update: "))
            t = str(input('Enter your task: '))
            a_info = input("Enter Additional information: ")
            t_dt = input("Enter date & time(format= d-m-y H:M:S am/pm): ")
            
            if t_dt.strip():
                try:
                    t_dt = datetime.strptime(t_dt, "%d-%m-%Y %I:%M:%S %p")
                except ValueError:
                    print("Invalid Time Format. Keeping previous date & time")
            else:
                t_dt = None

            manager.update_task(t_no, t, a_info, t_dt)
            print("Task update completed")

        elif choice == 4:
            print("Task List")
            tasks = manager.task_list()
            print(tasks)
            
        elif choice == 5:
            while True:
                try:
                    print("1.Search with task id\n2.Search with task\n3.Search with Additional Info\n4.Search with date\n5.Exit")
                    search_el = input("Enter keyword to search: ").strip()

                    if not search_el:
                        print("You have to enter a field to search.")
                    
                    elif search_el == str(1):
                        task_id = input("Search with task id: ")
                        tasks = manager.search_task(task_id=task_id)
                        print(tasks)

                    elif search_el == str(2):
                        task = input("Search with Task: ")
                        tasks = manager.search_task(task=task)
                        print(tasks)

                    elif search_el == str(3):
                        info = input("Search with additional info: ")
                        tasks = manager.search_task(info=info)
                        print(tasks)

                    elif search_el == str(4):
                        task_datetime = input("Search with date(format: d-m-y): ")
                        tasks = manager.search_task(task_datetime=task_datetime)
                        print(tasks)
                    
                    elif search_el == str(5):
                        print("Existing")
                        break

                except Exception as e:
                    print(f"Error: {e}")


        elif choice == 6:
            print("Existing...")
            break
        else:
            print("Invalid Input. Please Try again")
except Exception:
    raise ValueError("Invalid Option")

finally:
    print("Thanks for using our system.")
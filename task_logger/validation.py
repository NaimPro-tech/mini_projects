from task import Task
from datetime import datetime

def get_task():
    try:    
        task_no = input("Enter task id: ").strip()
        if not task_no:
            raise ValueError("Task id cannot be empty.")
        t_no = int(task_no)

        t = input("Enter your Task: ").strip()
        if not t:
            raise ValueError("Task cannot be empty.")
        
        a_info = input("Enter additional info: ").strip()
        if not a_info:
            raise ValueError("Additional information cannot be empty.")
        
        raw_date = input("Enter task date & time(format= d-m-y H:M:S am/pm): ").strip()
        if not raw_date:
            raise ValueError("Date Time cannot be empty.")
        t_dt = datetime.strptime(raw_date, "%d-%m-%Y %I:%M:%S %p")

        return Task(t_no, t, a_info, t_dt)
    except ValueError as e:
        print(f"Invalid Input: {e}")
        return None
    
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None
    
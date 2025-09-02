from task import Task
from datetime import datetime
import csv
import os

class TaskManager:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def remove_task(self, task_id):
        task = []
        deleted = False
        with open(self.file_path, mode="r") as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                if row[0] == str(task_id):
                    deleted = True
                    continue
                else:
                    task.append(row)

        with open(self.file_path, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(task)
        if deleted:
            print("Deleted Successfully.")
        else:
            print("Task not found.")
                    

    def update_task(self, task_id, task=None, additional_info=None, task_datetime=None):
        updated_list = []
        updated = False
        with open(self.file_path, mode="r") as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:  
                    if row[0] == str(task_id):
                        if task: row[1] = task
                        if additional_info: row[2] = additional_info
                        if task_datetime: row[3] = task_datetime
                        updated = True
                    updated_list.append(row)
                    
        if updated:
            with open(self.file_path, mode="w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(header)
                writer.writerows(updated_list)
        
        if not updated:
            raise ValueError("Task not found") 
        
        return updated
        
    def task_list(self):
        try:    
            with open(self.file_path, mode="r") as f:
                reader = csv.reader(f)
                next(reader, None)
                return [row for row in reader]
        except Exception:
            raise ValueError("No Task Found")


    def search_task(self, task_id=None, task = None, info = None, task_datetime = None):
        results = []
        try:    
            with open(self.file_path, mode="r") as f:
                reader = csv.reader(f)
                next(reader, None)
                for row in reader:
                    if task_id is not None and row[0] == str(task_id):
                        results.append(row)
                    elif task is not None and row[1].strip().lower() == str(task).strip().lower():
                        results.append(row)
                    elif info is not None and row[2].strip().lower() == str(info).strip().lower():
                        results.append(row)
                    elif task_datetime is not None:                        
                        try:
                            # full date time parse from csv
                            row_datetime = datetime.strptime(row[3], "%d-%m-%Y %I:%M:%S %p")
                            # only date parse from user input
                            search_date = datetime.strptime(task_datetime, "%d-%m-%Y").date()

                            if row_datetime.date() == search_date:
                                results.append(row)
                        except ValueError as ve:
                            # for debugging paring issue
                            print(f"Date parse error: {ve}")

        except Exception:
            raise ValueError("Task is invalid.")
        
        if not results:
            raise ValueError("Task not Found")
              
        return results  

    
    def save_task(self, task):
        if isinstance(task, Task):
            task_id = task.task_id
            task_name = task.task
            task_info = task.info
            date_time = task.task_datetime
        else:
            task_id, task_name, task_info, date_time = task

        if not isinstance(task_id, int):
            raise ValueError("Task id must be integer")
        
        exists = os.path.exists(self.file_path)
        if exists:
            with open(self.file_path, mode="r") as f:
                reader = csv.reader(f)
                next(reader, None)
                for row in reader:
                    if int(row[0]) == task_id:
                        print("You can't override a task.")
                        print("You can update old task with new one.\nPlease choose update.")
                        return

        with open(self.file_path, mode="a", newline="") as f:
            writer = csv.writer(f)
            if not exists:
                writer.writerow(["Task Id", "Task", "Info", "Date & Time"])
            writer.writerow([task_id, task_name, task_info, date_time.strftime("%d-%m-%Y %I:%M:%S %p")])
            print("New task added successfully.")

if __name__ == "__main__":
    manager = TaskManager("/home/npro/mini projects/task_logger/task_file.csv")
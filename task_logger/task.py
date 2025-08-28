class Task:
    def __init__(self, task_id, task, info, task_datetime):
        self.task_id = task_id
        self.task = task
        self.info = info
        self.task_datetime = task_datetime

    def __str__(self):
        return f"<Task Details: {self.task_id}, {self.task}, {self.info}, {self.task_datetime}>"
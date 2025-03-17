from task import Task
from storage import Storage

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.storage = Storage()
    
    def add_task(self, title: str, status: str = "Offen"):
        self.tasks.append(Task(title, status))
        self.storage.save_tasks(self.tasks)
    
    def get_tasks(self):
        return self.tasks
    
    def remove_task(self, title: str):
        self.tasks = [task for task in self.tasks if task.title != title]
        self.storage.save_tasks(self.tasks)

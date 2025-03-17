import json
from task import Task

class Storage:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
    
    def save_tasks(self, tasks):
        with open(self.filename, "w") as file:
            json.dump([{ "title": t.title, "status": t.status } for t in tasks], file)
    
    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                return [Task(item["title"], item["status"]) for item in data]
        except FileNotFoundError:
            return []
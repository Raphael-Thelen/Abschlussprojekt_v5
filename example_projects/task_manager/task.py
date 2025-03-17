class Task:
    def __init__(self, title: str, status: str):
        self.title = title
        self.status = status
    
    def update_status(self, new_status: str):
        self.status = new_status

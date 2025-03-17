from task_manager import TaskManager
from storage import Storage

def main():
    manager = TaskManager()
    storage = Storage()
    
    # Lade bestehende Aufgaben
    manager.tasks = storage.load_tasks()
    
    manager.add_task("Dokumentation schreiben", "Offen")
    manager.add_task("Unit-Tests implementieren", "In Bearbeitung")
    
    # Speichere Aufgaben nach der Änderung
    storage.save_tasks(manager.get_tasks())
    
    print("Aktuelle Aufgaben:")
    for task in manager.get_tasks():
        print(f"- {task.title} [{task.status}]")

if __name__ == "__main__":
    main()
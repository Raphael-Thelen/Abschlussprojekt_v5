import unittest
from task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def test_add_task(self):
        manager = TaskManager()
        manager.add_task("Test-Aufgabe")
        self.assertEqual(len(manager.get_tasks()), 1)
    
    def test_remove_task(self):
        manager = TaskManager()
        manager.add_task("Test-Aufgabe")
        manager.remove_task("Test-Aufgabe")
        self.assertEqual(len(manager.get_tasks()), 0)

if __name__ == "__main__":
    unittest.main()
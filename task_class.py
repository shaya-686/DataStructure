import json


class Task:

    def __init__(self, number, description, state):
        self.number = number
        self.description = description
        self.state = state

    def print_task(self):
        print(f"Task info: number - {self.number}, description - {self.description}, state - {self.state}")


class TaskTracker:
    tasks_file = 'tasks.json'

    def __init__(self):
        self.tasks = {}

    def add_task(self, task: Task):
        if task.number in self.tasks:
            raise ValueError("Task is already exists")
        self.tasks[task.number] = {"description": task.description, "state": task.state}

    def remove_task(self, task_number):
        if task_number not in self.tasks:
            raise ValueError("Task not found")
        del self.tasks[task_number]

    def save(self):
        with open(self.tasks_file, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def load(self):
        with open(self.tasks_file, 'r') as file:
            dct = json.load(file)
            self.tasks = dct

    def print_info(self):
        print(self.tasks)


task1 = Task("111", "Some desc for task1", "NEW")
task2 = Task("222", "Some desc for task2", "CANCEL")
task3 = Task("333", "Some desc for task3", "NEW")

tasks = TaskTracker()
tasks.add_task(task1)
tasks.add_task(task2)
tasks.add_task(task3)

tasks.save()
tasks.load()
tasks.print_info()

tasks.remove_task("111")
tasks.save()
tasks.load()
tasks.print_info()



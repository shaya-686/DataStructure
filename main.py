from queue import Queue


# queue = Queue()
# queue.put(1)
# queue.put(2)
# queue.put(3)
#
# print(queue.get())
# print(queue.get())
# print(queue.get())
# print(queue.empty())

class BankQueue:
    def __init__(self):
        self.queue = Queue()

    def put_client(self, client):
        self.queue.put(client)

    def serve_next_client(self):
        if self.queue.empty():
            raise IndexError("No elements in queue")
        else:
            client = self.queue.get()
            print(f"Serve client {client}")

    def number_clients(self):
        return self.queue.qsize()

    def is_empty_queue(self):
        return self.queue.empty()

    def print_clients(self):
        temp_queue = Queue()
        while not self.queue.empty():
            client = self.queue.get()
            print(client, end=' <- ')
            temp_queue.put(client)
        print()
        self.queue = temp_queue


bank_queue = BankQueue()
bank_queue.put_client("Mary")
bank_queue.put_client("Kate")
bank_queue.print_clients()
bank_queue.serve_next_client()
bank_queue.put_client("Nick")
bank_queue.print_clients()
bank_queue.serve_next_client()
bank_queue.serve_next_client()
print(bank_queue.is_empty_queue())


#Tasts
from queue import PriorityQueue
# queue = PriorityQueue()
# queue.put((1, "John"))
# queue.put((2, "Max"))
# queue.put((3, "Kate"))
# queue.put((2, "Sonya"))
# queue.put((-1, "John1"))
# queue.put((-3, "Kate1"))
# queue.put((-2, "Sonya1"))

# while not queue.empty():
#     priority, client = queue.get()
#     print(client, priority)

class TaskSolver:
    def __init__(self):
        self.queue = PriorityQueue()

    def add_task(self, priority, task):
        self.queue.put((priority, task))

    def solve_next_task(self):
        if self.queue.empty():
            print("No tasks")
            return

        priority, task = self.queue.get()
        print(f"Solve task {task}")

solver = TaskSolver()
solver.add_task(2, "Task1")
solver.add_task(1, "Task2")
solver.add_task(3, "Task3")
solver.solve_next_task()
solver.solve_next_task()
solver.solve_next_task()

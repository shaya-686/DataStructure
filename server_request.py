import random
from queue import PriorityQueue
import uuid
from datetime import datetime
import time


class Client:
    def __init__(self, phone, priority):
        if not isinstance(priority, int):
            raise ValueError("The priority should be int")
        self.phone = phone
        self.priority = priority

    def __str__(self):
        return f'Client info: phone - {self.phone}, priority - {self.priority}'


class ClientRequest:
    def __init__(self, client: Client):
        self.uuid = uuid.uuid4()
        self.client = client
        self.create_date = datetime.now()
        self.start_date = None
        self.end_date = None

    def __str__(self):
        return (f'Request info: uuid - {self.uuid}, created date - {self.create_date}, start date - {self.start_date}, '
                f'end date - {self.end_date},{self.client}')


class RequestQueue:
    def __init__(self):
        self.queue = PriorityQueue()
        self.stat_queue = PriorityQueue()

    def add_request(self, request: ClientRequest):
        request.start_date = datetime.now()
        self.queue.put((request.client.priority, request))

    def get_request(self):
        if self.queue.empty():
            raise IndexError("Queue is empty")
        priority, request = self.queue.get()
        request.end_date = datetime.now()
        print(f"Get {request.uuid} with {priority} priority")
        self.stat_queue.put((priority, request))

    def print_queue(self):
        temp_queue = PriorityQueue()
        print("Original queue: ")
        while not self.queue.empty():
            priority, request = self.queue.get()
            print(str(request.uuid) + ": " + str(priority), end='\n')
            temp_queue.put((priority, request))
        print()
        self.queue = temp_queue

    def print_stat(self):
        temp_queue = PriorityQueue()
        print("Statistic queue: ")
        while not self.stat_queue.empty():
            priority, request = self.stat_queue.get()
            print(str(request.uuid) + ": " + "start date - " + str(request.start_date) + "end date - " + str(request.end_date)
                  + ", " + "priority - " + str(priority), end='\n')
            temp_queue.put((priority, request))
        print()
        self.stat_queue = temp_queue

    def is_empty(self):
        return self.queue.empty()

    def queue_size(self):
        return self.queue.qsize()


clients = []
rq = RequestQueue()
for i in range(1, 5):
    client = Client("380777777" + f"{i}", random.randint(1111, 9999))
    print(client)
    clients.append(client)
print()

for i in range(len(clients)):
    request = ClientRequest(clients[i])
    rq.add_request(request)

rq.print_queue()
time.sleep(3)
while rq.queue_size() > 2:
    rq.get_request()

print()
rq.print_stat()

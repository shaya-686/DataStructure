class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, text):
        self.queue.append(text)

    def dequeue(self):
        if len(self.queue) == 0:
            raise IndexError("No items in queue")
        deleted_element = self.queue.pop(0)
        return deleted_element

    def peek(self):
        if len(self.queue) == 0:
            raise IndexError("No items in queue")
        text = self.queue[-1]
        print(f"First element in queue: {text}")

    def is_empty(self):
        return len(self.queue) == 0

    def show(self):
        print("Queue: ", self.queue)


q = Queue()
q.enqueue("test1")
q.enqueue("test3")
q.enqueue("test2")
q.show()
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
q.enqueue("test5")
q.peek()
q.enqueue("test4")
q.show()

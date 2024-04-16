class PriorityQueue:
    def __init__(self):
        self.queue = []

    def insert_with_priority(self, priority, text):
        self.queue.append((priority, text))
        self.queue.sort(key=lambda x: x[0], reverse=True)

    def pull_highest_priority_element(self):
        if len(self.queue) == 0:
            raise IndexError("No items in queue")
        highest_priority_element = self.queue.pop()
        return highest_priority_element

    def peek(self):
        priority, text = self.queue[-1]
        print(f"Priority: {priority}, text: {text}")

    def is_empty(self):
        return len(self.queue) == 0

    def show(self):
        print("Queue: ", self.queue)


q = PriorityQueue()
q.insert_with_priority(1, "test1")
q.insert_with_priority(3, "test3")
q.insert_with_priority(2, "test2")
q.show()
print(q.pull_highest_priority_element())
print(q.is_empty())
q.peek()
q.show()

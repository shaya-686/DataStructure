# stack = []
#
# stack.append(1)
# stack.append(2)
# stack.append(3)
#
# print(f'{stack=}')
# print(f'Pop last element:  {stack.pop()}')
# print(f'{stack=}')


# from collections import deque
# from queue import LifoQueue
#
# stack = deque()
# stack.append(1)
# stack.append(2)
# stack.append(3)
#
# print(f'{stack=}')
# print(f'Pop last element:  {stack.pop()}')
# print(f'{stack=}')
#
# stack = LifoQueue()
# stack.put(1)
# stack.put(2)
# stack.put(3)
#
# print(f'{stack=}')
# print(f'Pop last element:  {stack.get()}')
# print(f'{stack=}')


class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        self.size += 1
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            raise IndexError('stack is empty')
        self.size -= 1
        data = self.head.data
        self.head = self.head.next
        return data

    def get_size(self):
        return self.size

    def print(self):
        node = self.head

        while node:
            print(node.data, end="->")
            node = node.next

    def peek(self):
        if self.head is None:
            raise IndexError('stack is empty')
        return self.head.data


stack = Stack()
stack.append(1)
stack.append(2)
stack.append(3)

stack.print()
print(f'Pop last element:  {stack.pop()}')
print(f'Pop last element:  {stack.peek()}')
stack.print()



# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     def __str__(self):
#         return f'{self.data} -> {self.next}'
#
#
# # node1 = Node(12)
# # node2 = Node(99)
# # node3 = Node(37)
# # node1.next = node2
# # node2.next = node3
# # print(node1)
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def __str__(self):
#         return f'{self.head}'
#
#     def append(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#
#         tail = self.head
#         while tail.next is not None:
#             tail = tail.next
#
#         tail.next = new_node


# my_list = LinkedList()
# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
# my_list.append(4)
# my_list.append(5)
# print(my_list)

# Double linked list

# class Node1:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None
#
#     def __str__(self):
#         return f'{self.data} -> {self.next}'
#
#
# class DoubleLinkedList:
#     def __init__(self):
#         self.head = None
#
#     def __str__(self):
#         return f'{self.head}'
#
#     def append(self, data):
#         new_node = Node1(data)
#         if self.head is None:
#             self.head = new_node
#             return
#
#         tail = self.head
#         while tail.next is not None:
#             tail = tail.next
#
#         tail.next = new_node
#         new_node.prev = tail
#
#
# my_list = DoubleLinkedList()
# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
# my_list.append(4)
# my_list.append(5)
# print(my_list)


# passangers
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return f'{self.data} -> {self.next}'


class BoardingQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail

        self.tail = new_node

    def move_forward(self, data):
        # find node with data
        node = self.head
        while node is not None and node.data != data:
            node = node.next

        if node is None:
            print('Passanger not in queue')
            return

        red = node.prev
        green = node
        blue = node.next
        black = node.next.next  # blue.next

        # change links to head
        red.next, green.next, blue.next = blue, black, green

        # change links to tail
        green.prev, blue.prev, black.prev = blue, red, green

    def print(self):
        node = self.head
        while node is not None:
            print(node.data, end='->')
            node = node.next


my_list = BoardingQueue()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.print()


my_list.move_forward(2)
print('\n')
my_list.print()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return f'{self.data} -> {self.next}'


class Numbers:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        return f'{self.head}'

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail

        self.tail = new_node

    def delete(self, data):
        node = self.head
        while node is not None:
            if node.data == data:
                node.prev.next = node.next
                return
            node = node.next
        if node is None:
            print('Number not in queue')
            return

    def find_number(self, data):
        node = self.head
        while node is not None:
            if node.data == data:
                return True
            else:
                node = node.next
        if node is None:
            return False

    def change_number(self, data, new_data):
        node = self.head
        while node is not None:
            if node.data == data:
                node.data = new_data
                return
            else:
                node = node.next
        if node is None:
            print('Number not in queue')
            return

    def print(self):
        node = self.head
        while node is not None:
            print(node.data, end='->')
            node = node.next
        print('\n')


number = Numbers()
while True:
    print("\nMenu:")
    print("1. Add new element")
    print("2. Delete element")
    print("3. Print list")
    print("4. Check if number exist")
    print("5. Change number")
    print("6. Exit")

    choice = input("Choose the option: ")

    if choice == '1':
        num = input("Enter the number to add: ")
        number.append(num)
        number.print()
    elif choice == '2':
        num = input("Enter the number to delete: ")
        number.delete(num)
        number.print()
    elif choice == '3':
        print("List info:")
        number.print()
    elif choice == '4':
        num = input("Enter the number to find: ")
        if number.find_number(num):
            print("Number found")
        else:
            print("Number not found.")
    elif choice == '5':
        old_num = input("Enter number for search: ")
        new_num = input("Enter new number: ")
        number.change_number(old_num, new_num)
        number.print()
    elif choice == '6':
        print("Bye!")
        break
    else:
        print("Unknown operation!")

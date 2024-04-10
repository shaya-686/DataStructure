class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Number:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_unique(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        node = self.head
        while node.next:
            if node.data == data:
                raise ValueError("Number is already exists")
            else:
                node = node.next
        if node.data == data:
            raise ValueError("Number is already exists")
        self.tail.next = new_node
        node.prev = self.tail
        self.tail = new_node

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
            return

        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def remove_all(self, data):
        if self.head is None:
            raise ValueError("List is empty")
        if self.head.data == data and self.head.next is None:
            self.head = None
            return
        node = self.head
        while node.next:
            if node.data == data:
                if node == self.head:
                    self.head = node.next
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev
            node = node.next
        if node.data == data:
            node.prev.next = None
            self.tail = node.prev

    def find_number(self, data):
        node = self.head
        while node is not None:
            if node.data == data:
                return True
            else:
                node = node.next
        return False

    def print(self, desc=True):
        if desc:
            node = self.head
            while node:
                print(node.data, end='->')
                node = node.next
        else:
            node = self.tail
            while node:
                print(node.data, end='->')
                node = node.prev

    def change_number(self, data, new_data, multi=False):
        node = self.head
        while node is not None:
            if node.data == data:
                node.data = new_data
                if not multi:
                    return
            else:
                node = node.next


number = Number()
try:
    while True:
        print("\nMenu:")
        print("1. Add new number")
        print("2. Remove all number entries")
        print("3. Print list")
        print("4. Check if number exist")
        print("5. Change number")
        print("6. Exit")

        choice = input("Choose the option: ")

        if choice == '1':
            option = int(input("Enter '1' to add the unique number or '2' to add number without control: "))
            num = input("Enter the number to add: ")
            if option == 1:
                number.append_unique(num)
            elif option == 2:
                number.append(num)
            else:
                print("Incorrect option")
        elif choice == '2':
            num = input("Enter the number to remove: ")
            number.remove_all(num)
        elif choice == '3':
            option = int(input("Enter '1' to print list in desc order or '2' in asc order: "))
            print("List info:")
            if option == 1:
                number.print()
            elif option == 2:
                number.print(desc=False)
            else:
                print("Incorrect option")
        elif choice == '4':
            num = input("Enter the number to find: ")
            if number.find_number(num):
                print("Number found")
            else:
                print("Number not found.")
        elif choice == '5':
            old_num = input("Enter number for search: ")
            new_num = input("Enter new number: ")
            option = int(input("Enter '1' to change first number entry or '2' to change all number entries: "))
            if option == 1:
                number.change_number(old_num, new_num)
            elif option == 2:
                number.change_number(old_num, new_num, multi=True)
            else:
                print("Incorrect option")
        elif choice == '6':
            print("Bye!")
            break
        else:
            print("Unknown operation!")
except ValueError as e:
    print("Message: ", e)
except Exception as e:
    print("Message: ", e)

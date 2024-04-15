class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self, max_size=None):
        self.head = None
        self.size = 0
        self.max_size = max_size

    def push(self, data):
        if self.max_size and self.size == self.max_size:
            raise OverflowError("Stack is full")
        if self.max_size and self.size < self.max_size or self.max_size is None:
            node = Node(data)
            if self.head is None:
                self.head = node
            else:
                node.next = self.head
                self.head = node
            self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError("Stack is empty")
        node = self.head
        self.head = node.next
        self.size -= 1
        return node.data

    def print(self):
        if self.head is None:
            raise IndexError("Stack is empty")
        node = self.head

        while node:
            print(node.data, end="->")
            node = node.next

    def get_size(self):
        return self.size

    def set_max_size(self, new_size):
        if new_size >= self.size:
            self.max_size = new_size
        else:
            raise IndexError("Stack size is bigger than max stack size")

    def get_max_size(self):
        return self.max_size

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        if self.max_size:
            return self.size == self.max_size
        else:
            return self.size != 0

    def clear(self):
        self.head = None
        self.size = 0

    def peek(self):
        if self.head is not None:
            return self.head.data
        else:
            raise IndexError("Stack is empty")


stack = Stack()
try:
    while True:
        print("\nMenu:")
        print("1. Set stack size")
        print("2. Add new item to stack")
        print("3. Remove item from stack")
        print("4. Show stack")
        print("5. Check if stack is empty")
        print("6. Check if stack is full (for stack without fixed size will return 'TRUE' if stack has even one)"
              "element")
        print("7. Clear stack")
        print("8. Get last stack element")
        print("9. Exit")

        choice = input("Choose the option: ")

        if choice == '1':
            size = int(input("Enter stack size: "))
            stack.set_max_size(size)
        elif choice == '2':
            item = input("Enter new stack item: ")
            stack.push(item)
            stack.print()
        elif choice == '3':
            print(stack.pop())
        elif choice == '4':
            stack.print()
        elif choice == '5':
            if stack.is_empty():
                print("Stack is empty")
            else:
                print("Stack is not empty")
        elif choice == '6':
            if stack.get_max_size():
                if stack.is_full():
                    print("Stack is full")
                else:
                    print("Stack isn't full")
            else:
                if stack.is_full():
                    print("Stack has even one element")
                else:
                    print("Stack is empty")
        elif choice == '7':
            stack.clear()
        elif choice == '8':
            print("Last stack element: ", stack.peek())
        elif choice == '9':
            print("Bye!")
            break
        else:
            print("Unknown operation!")
except IndexError as e:
    print("Message: ", e)
except OverflowError as e:
    print("Message: ", e)
except Exception as e:
    print("Message: ", e)
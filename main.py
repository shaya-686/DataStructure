# calculator
example = '3 + ( 4 * 2 ) - 5 - ( 4 * 2 ) + 10'


def infix_to_postfix(text):
    priority = {'+': 1, '-': 1, '*': 2, '/': 2, '(': -100}
    characters = text.split()
    stack = []
    result = ''

    for char in characters:
        if char.isdigit():
            result += ' ' + char

        elif char == '(':
            stack.append(char)

        elif char == ')':
            while stack[-1] != '(':
                result += ' ' + stack.pop()

            stack.pop()

        else:
            while stack and priority[stack[-1]] >= priority[char]:
                result += ' ' + stack.pop()

            stack.append(char)

    result += ' ' + ' '.join(stack)

    return result


print(infix_to_postfix(example))


def calculate(text):
    stack = []
    operators = ['+', '-', '*', '/']
    characters = text.split()
    result = 0
    for char in characters:
        if char.isdigit():
            stack.append(char)
        elif char in operators:
            first_number = int(stack.pop())
            second_number = int(stack.pop())
            if char == '+':
                result = first_number + second_number
            elif char == '-':
                result = second_number - first_number
            elif char == '*':
                result = first_number * second_number
            elif char == '/':
                result = first_number / second_number
            stack.append(result)
    return stack


print(calculate(infix_to_postfix(example)))


# pages
class Webpage:
    def __init__(self):
        self.pages = []

    def add_page(self, data):
        self.pages.append(data)
        print(f"Added new page: {data}")

    def move_to_last(self):
        if len(self.pages) == 0:
            print("History is empty")
        else:
            last_page = self.pages.pop()
            print(f"Last visited page: {last_page}")

    def view_history(self):
        print(f'Pages history: ', self.pages)


page = Webpage()
page.add_page('first')
page.add_page('second')
page.add_page('third')
page.move_to_last()
page.view_history()

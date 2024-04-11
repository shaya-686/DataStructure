example = '3 + 4 * ( 2 - 5 )'


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

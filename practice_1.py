examples = ["()", "[[()]]", "{[}]}", "[{()}]", "((()))"]


def naive(text):
    num_type1 = 0
    num_type2 = 0
    num_type3 = 0

    for char in text:
        if char == '(':
            num_type1 += 1
        elif char == '{':
            num_type2 += 1
        elif char == '[':
            num_type3 += 1

        if char == ')':
            if num_type1 == 0:
                return False
            else:
                num_type1 -= 1

        if char == '}':
            if num_type2 == 0:
                return False
            else:
                num_type2 -= 1

        if char == ']':
            if num_type3 == 0:
                return False
            else:
                num_type3 -= 1
    return num_type1 == 0 and num_type2 == 0 and num_type3 == 0


def check_with_stack(example):
    stack = []
    for char in example:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if len(stack) == 0:
                return False
            if stack.pop() + char not in ['()', '{}','[]']:
                return False

    return len(stack) == 0


for example in examples:
    print(f'{example} - {check_with_stack(example)}')

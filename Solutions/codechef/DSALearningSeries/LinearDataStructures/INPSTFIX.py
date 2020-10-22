precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
t = int(input())
for _ in range(t):
    n = int(input())
    infix_expression = list(input())
    stack = []
    expression = []
    for operand in infix_expression:
        if operand == '(':
            stack.append('(')
        elif operand in precedence.keys():
            while len(stack) > 0 and stack[-1] != '(' and precedence.get(operand) <= precedence.get(stack[-1]):
                expression.append(stack.pop())
            stack.append(operand)
        elif operand == ')':
            while len(stack) > 0 and stack[-1] != '(':
                expression.append(stack.pop())
            stack.pop()
        else:
            expression.append(operand)

    while (len(stack) > 0):
        if (stack[-1] != '('):
            expression.append(stack.pop())

    str = ''
    for item in expression:
        str += item

    print(str)

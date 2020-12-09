character = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3,'(':0}

def infix_to_postfix(t:int,inexpression,n:int):

    for _ in range(t):

        infix_expression = inexpression
        stack = []
        str = ''
        for operand in infix_expression[0:n]:
            if operand in character:
                str += operand
            elif operand == '(':
                stack.append('(')
            elif operand == ')':
                while len(stack) > 0 and stack[-1] != '(':
                    str += stack.pop()
                stack.pop()
            else:
                    while len(stack) != 0 and stack[-1] != '(' and  precedence.get(stack[-1]) >= precedence.get(operand):
                        str += stack.pop()
                    stack.append(operand)


        while (len(stack) > 0):
            str += stack.pop()
        print(str)
        return str

def evaluvator(stack) :
     if len(stack) > 0:
        return precedence.get(stack[-1])
     else:
        return 0


if __name__ == "__main__":
    t = int(input())
    inexpression = list(input())
    n = int(input())
    try:
       infix_to_postfix(t, inexpression, n)
    except Exception:
        pass


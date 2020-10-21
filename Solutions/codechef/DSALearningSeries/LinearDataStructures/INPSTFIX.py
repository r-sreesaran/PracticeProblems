#https://www.codechef.com/LRNDSA02/problems/INPSTFIX




t = int(input())

for _ in range(t):
    n = int(input())
    infix_expression = list(input())
    stack = []
    for operand in infix_expression:
        if operand=='(':
            stack.append('(')

        elif operand=='+':
            while stack[-1] != '(' and stack[-1] != '+':
                print(stack.pop())
            stack.append('+')

        elif operand=='-':
            while stack[-1] != '(' and stack[-1] != '+' and stack[-1] != '-' :
                  print(stack.pop())
            stack.append('-')


        elif operand=="*":
            while stack[-1] != '(' and stack[-1] != '+' and stack[-1] != '-'  and stack[-1] !='*':
                  print(stack.pop())
            stack.append('*')

        elif operand == "/":
            while stack[-1] != '(' and stack[-1] != '+' and stack[-1] != '-' and stack[-1] != '*' and stack[-1]=='/':
                print(stack.pop())
            stack.append('/')

        elif operand == '^':
            stack.append('^')

        elif operand ==')':

            while stack[-1]!='(' :
                print(stack.pop())
                if(len(stack)==0):
                    break

            if(len(stack)>0 and stack[-1]=='('):
              stack.pop()

        else:
            print(operand)

while(len(stack)>0):
    if(stack[-1]!='('):
        print(stack.pop())
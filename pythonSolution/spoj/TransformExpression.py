#https://www.spoj.com/problems/ONP/
operands =['+','-','*','/','^','(',')']
postfix=[]
def operandvalue(operand)->int:
    if(operand=='+'):
        return 1 
    if(operand=='-'):
        return 2 
    if(operand=='*'):
        return 3 
    if(operand=='/'):
        return 4 
    if(operand=='^'):
        return 5
    if(operand=='('):
        return 6


t = int(input())
for t in range(t):
 expression = list(input())


 for c in  expression:
    if(c not in operands):
      print(c,end="")
    elif(c is '('):
      postfix.append(c) 
    elif(c is ')'):
       for c1 in reversed(postfix) :
           if c1 != '(': 
             print(postfix.pop(),end="")
           else:
             postfix.pop()
             break
    else:
        if not postfix:
            postfix.append(c)
        elif int(operandvalue(postfix[-1])) > int(operandvalue(c)) :
             if(postfix[-1]!='('):
                print(postfix.pop(),end="")
             postfix.append(c)
        else:
            postfix.append(c)

 print()
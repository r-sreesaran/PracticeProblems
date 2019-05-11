#https://www.spoj.com/problems/ANARC09A/

while(True):
    n=list(input().rstrip())
    stack=list()
    if(n[0]!='-'):
        for e in n:
            if(e=='{'):
                stack.append(e)
            elif(e=='}' and stack):
                stack.pop()
            else:
                stack.append('}')
        print(stack)
        b=0
        pair = False
        for i in range(0,len(stack)-1,2):
            if(stack): 
              if(stack[i]=='{' and stack[i+1]=='{'):
                b+=1
              elif(stack[i]=='}' and stack[i+1]=='}'):
                 b+=1
              else:
                   pair=True  

        if(pair==True):
          b=+2
        print(b)
    else:
        break
#https://www.spoj.com/problems/ANARC09A/
no=1
while(True):
    n=list(input().strip())
    stack=[]
    if(n[0]!='-'):
        for e in n:
            if(e=='{'):
                stack.append(e)
            elif(e=='}' and stack):
                if(stack[-1]=='{'):
                 stack.pop()
                else:
                    stack.append('}')
            elif(e=='}' and not stack):
                stack.append('}')
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
        if(len(stack)%2!=0):
           b+=1
        print(str(no)+'. '+ str(b))
        no+=1
    else:
        break
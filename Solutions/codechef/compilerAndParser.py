#https://www.codechef.com/problems/COMPILER
n = int(input())

for _ in range(n):
    letters = list(input())
    pair=0
    open=0
    close=0

    for i in range(len(letters)):
        if( letters[i] is '>'):
          close+=1
        elif(letters[i] is '<'):
           open+=1
        if(open-close==0):
            pair=i+1
        elif(close>open):
            break;    

    print(pair)

    

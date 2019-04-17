#https://www.codechef.com/problems/COMPILER
n = int(input())

for _ in range(n):
    letters = list(input())
    pair=0
    open=0

    for i in letters:
        if( i is '>' and open >=1):
          open-=1
          pair+=1
        elif(i is '<'):
           open+=1
    print(pair*2)

    

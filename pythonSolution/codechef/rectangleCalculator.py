#https://www.codechef.com/problems/STICKS
t = int(input())
for i in range(t):
    options = int(input())
    sizes = list(map(int,input().split(" ")))
    possiblevalues = []
    l=b=0
    for j in sizes:
        if (sizes.count(j) >=2 and j not in possiblevalues):
            if(l<j):
                b=l
                l=j
            elif(b<j):
                b=j
            possiblevalues.append(j)
    if  len(possiblevalues)<2 or l==b:
        print(-1)
    else: 
        print (l*b)

     

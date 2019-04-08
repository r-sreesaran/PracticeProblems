#https://www.codechef.com/problems/STICKS
t = int(input())
for i in range(t):
    n = int(input())
    values = list(map(int,input().split(" ")))
    values.sort(reverse=True)
    while i<len(values)-2 and count < 2:
        if(values[i]==values[i+1]):
           area = area*values[i]
           i=i+2
           count=count+1   
        else:
            i=i+1 
    if(count<2):
        print -1 
    else:
        print(area) 
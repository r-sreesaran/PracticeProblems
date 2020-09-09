#https://www.codechef.com/problems/STICKS
t = int(input())
for i in range(t):
    n = int(input())
    values = list(map(int,input().split(" ")))
    values.sort(reverse=True)
    j=0
    count=0
    area=1
    while j<len(values)-1 and count < 2:
        if(values[j]==values[j+1]):
           area = area*values[j]
           j=j+2
           count=count+1   
        else:
            j=j+1 
    if(count<2):
        print(-1) 
    else:
        print(area)
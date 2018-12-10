t = int(input())


for j in range(t):
    value = []
    for a in range(100):
        value.append('yes')
    M,x,y= map(int,input().split())
    val = x*y
    h = list(map(int, input().split()))
    for i in range(0,M):
        for k in range(h[i]-val-1,h[i]+val):
            if(k>-1 and k<100):
               value[k]='no'
    print(value.count('yes'))
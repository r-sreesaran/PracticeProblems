t = int(input())
for k in range(0,t):
    n = int(input())
    values = list(map(int,input()))
    i=0
    for i in range(n-2,0,-1):
        if values[i]<values[i+1]:
           break

    if (i == 0):
        print(-1)
        break

    j=0
    for j in range(i+1,n):
        if (values[j] < values[i]):
            break

    values[j-1], values[i] = values[i], values[j-1]
    values = values[0:i+1] + sorted(values[i + 1:])
    print(values)



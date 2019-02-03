t = int(input())
for k in range(0,t):
    n = int(input())
    values = list(map(int,input()))
    i=0;
    for i in range(n,0,-1):
        if values[i]<values[i+1]:
           break
        elif (i==2):
              i=-1
              break


    if (i == -1):
        print(-1)
        break

    j = i + 1
    for j in range(n):
        if (values[j] < values[i]):
            break

    values[j], values[i] = values[i], values[j]
    values = values[0:i + 1] + sorted(values[i + 1:])
    print(values)



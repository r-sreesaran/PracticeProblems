t=int(input())
for i in range(t):
    n= int(input())
    values = list(map(int,input().split()))
    iteration = sum(values) - n*min(values)
    print(iteration)



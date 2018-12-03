t=int(input())
for i in range(t):
    X,C=map(int,input().split())
    L=list(map(int,input().split()))
    if(C>=sum(L)):
        print("Yes")
    else:
        print("No")
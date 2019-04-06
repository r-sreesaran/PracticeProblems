t=int(input())
for i in range(t):
    X,Y,K,N=map(int,input().split())
    a="";
    for j in range(N):
        P,C=map(int,input().split())
        if (X - Y <=P and K>=C):
            a="LuckyChef"
        else:
             if(a!="LuckyChef"):
              a="UnluckyChef"
    print(a)

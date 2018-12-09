t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    dict = list(map(str,input().split()))
    value=[]
    for j in range(k):
        l,*m = input().split()
        for t in range(len(dict)):
            if dict[t] in m:
                value[t]='YES'
    for v in range(len(dict)):
        if(value[v]=='YES'):
            print("YES ",end='')
        else:
             print("NO ",end='')


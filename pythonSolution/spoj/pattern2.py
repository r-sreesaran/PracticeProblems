#https://www.spoj.com/problems/CPTTRN2/

t=int(input())
for i in range(t):
    c, r = map(int, input().split())
    for j in range(c):
        for k in range(r):
            if(k==0 or j==0 or j==c-1 or k == r-1):
                print("*",end="")
            else:
                print(".",end="")
        print()
    print()

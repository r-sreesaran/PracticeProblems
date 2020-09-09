#https://www.spoj.com/problems/CPTTRN4/
t=int(input())
for i in range(t):
    r, c, h, w = map(int, input().split())
    h = h + 1
    w= w+1
    for k in range(r*h+1):
        for j in range(c*w+1):
            if(k%h==0 or j%w==0):
                print("*",end="")
            else:
                print(".",end="")
        print()
    print()
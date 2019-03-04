#https://www.spoj.com/problems/CPTTRN5/
t = int(input())
for i in range(t):
    r, c, s = map(int, input().split())
    s = s + 1
    for k in range(r*s+1):
        for j in range(c*s+1):
            if(k%s==0 or j%s==0):
                print("*",end="")
            else:
                if (int((k + j) / s) % 2 == 0)):
                    print()


                print()
    print()

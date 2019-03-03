#https://www.spoj.com/problems/CPTTRN3/
t=int(input())
for i in range(t):
    r, c = map(int, input().split())
    for k in range(r*3+1):
        for j in range(c*3+1):
            if(k==0 or j==0 or j%3==0 or k%3==0 or k%3 ==0 or j%3==0  ):
                print("*",end="")
            else:
                print(".",end="")
        print()
    print()
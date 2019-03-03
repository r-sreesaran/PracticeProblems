#https://www.spoj.com/problems/CPTTRN1/

'''
*
.
*

*.*.
.*.*
*.*.
.*.*

*.*.*
.*.*.
'''

n = int(input())
for i in range(n):
    r,c = list(map(int,input().split()))
    temp=["*","."]
    for j in range(r):
         for k in range(c):
              print(temp[k%2],end='')
         print()
         temp[0],temp[1]=temp[1],temp[0]
    print()

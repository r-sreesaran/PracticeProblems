#https://www.codechef.com/certification/data-structures-and-algorithms/prepare#foundation
#https://www.codechef.com/problems/NXTBIG

n = int(input())

for i in range(n):
    l = int(input())
    no = list(map(int,input().split(' ')))
    for j in reversed(range(l)):

      print(no[0])
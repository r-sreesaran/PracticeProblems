#https://www.codechef.com/LRNDSA02/problems/STFOOD

t = int(input())

for _ in range(t):

   n = int(input())
   maxv = []
   for _ in range(n):
       s,p,v = map(int,input().split(" "))
       maxv.append(p//(s+1)*v)
   print(max(maxv))
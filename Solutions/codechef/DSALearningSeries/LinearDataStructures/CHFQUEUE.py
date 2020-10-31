# https://www.codechef.com/LRNDSA02/problems/CHFQUEUE
n,k = map(int,input().split(" "))
a = list(input().split(" "))
product =1
for i in range(n):
    for j in range(i+1,n):
        if(a[i]>a[j]):
          product *= (j-i+1)
          product %= 1000000007
          break
print(product)

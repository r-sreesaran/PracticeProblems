# https://www.codechef.com/LRNDSA02/problems/CHFQUEUE

# n = 5000
# k = 2
# arr = []
# for i in range(5000):
#     if(i%2==0):
#         arr.append(1)
#     else:
#         arr.append(2)

n,k = map(int,input().split(" "))
arr = list(input().split(" "))
product =1
for i in range(n):
    for j in range(i+1,n):
        if(arr[i]>arr[j]):
          product *= (j-i+1)
          product %= 1000000007
          break
print(product)


#n, k = map(int, input().split())
# arr = list(map(int, input().split()))

# chf = []
# prod = 1
#
# n = 1
# for i in arr:
#     while len(chf)>0 and chf[-1][0]>i:
#         val,ind=chf.pop()
#         prod*=n-ind+1
#         prod%=1000000007
#     chf.append((i,n))
#     n += 1
# print(prod%1000000007)

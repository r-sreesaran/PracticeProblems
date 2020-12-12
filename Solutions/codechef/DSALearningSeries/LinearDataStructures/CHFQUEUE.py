# https://www.codechef.com/LRNDSA02/problems/CHFQUEUE

# o(n^2) solution brute force
n,k = map(int,input().split(" "))
# The running time of the program exceeds due to type conversion from str to integer
# Need to understand how the types are getting converted.
arr = list(input().split(" "))

product =1
for i in range(n):
    for j in range(i+1,n):
        if(arr[i]>arr[j]):
          product *= (j-i+1)
          product %=  1000000007
          break
print(product)

# o(n) solution
stack = []
product = 1
index = []
mod=10**9+7
for i in range(n):
    while len(stack)!=0 and stack[-1]> arr[i]:
        product *=  (i+1-index.pop()+1)
        product %=  mod
        stack.pop()

    stack.append(arr[i])
    index.append(i+1)
print(product)




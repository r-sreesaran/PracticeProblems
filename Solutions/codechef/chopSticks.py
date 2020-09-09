#https://www.codechef.com/problems/TACHSTCK
n,d = map(int,input().split(" "))
numbers=[0]*n
arb=[0]*n
for i in range(n):
    numbers[i]=int(input())

numbers.sort()

i=0
j=1
for k in range(n-1):
        if(arb[k]!=1 and arb[k+1]!=1 and abs(numbers[k]-numbers[k+1])<=d):
               arb[k] = arb[k+1] = 1
        

print(arb.count(1)//2)


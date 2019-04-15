#https://www.codechef.com/problems/TACHSTCK
n,d = map(int,input().split(" "))
numbers=[0]*n
arb=[0]*n
for i in range(n):
    numbers[i]=int(input())
    if(i>0):
        if(abs(numbers[i-1]-numbers[i])<=d and arb[i]!=1 and arb[i-1]!=1):
            arb[i]=arb[i-1]=1

for i in range(n):
    for j in range(i,n):
        if(arb[i]!=1 and arb[j]!=1 and abs(numbers[i]-numbers[j])<=d):
            arb[i] = arb[j] = 1


print(arb.count(1)/2)


#https://www.spoj.com/problems/STPAR/


while(True):
 n = int(input())
 if(n==0):
    break
 sequence=list(map(int,input().split()))
 k=1
 orderedList=[0]*n
 for i in range(n):
    if(k==sequence[i]):
        orderedList[k-1]=sequence[i]
        k+=1
 
 for j in reversed(range(n)):
    if(k==sequence[j]):
        orderedList[k-1]=sequence[j]
        k+=1
 if(k-1==n):
    print("yes")
 else:
    print("no")




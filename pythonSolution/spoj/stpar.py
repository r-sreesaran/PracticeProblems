#https://www.spoj.com/problems/STPAR/


while(True):
 n = int(input())
 if(n==0):
    break
 sequence=list(map(int,input().split()))
 status=True
 k=1
 tempList=[]
 for e in sequence:
     while bool(len(tempList)) and tempList[-1]==k:
         k=k+1
         tempList.pop()

     if(e==k):
         k=k+1

     elif bool(len(tempList)) and e>tempList[-1]:
         print("no")
         status=False
         break
     else:
         tempList.append(e)

 if status:
  print("yes")

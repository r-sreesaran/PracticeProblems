t = int(input())
for i in range(t) :
   a = int(input())
   val = list(map(int,input().rstrip().split(" ")))
   nextval = -1
   for j in reversed(range(a)):
       if(val[j-1]<val[j] and j>=1):
           nextval = j
           val[j-1],val[j]=val[j],val[j-1]
           break
   for k in reversed(range(a)):
        if(k>=nextval):
   if(nextval!=-1):
    list1 = val[0:nextval+1]
    list2 = val[nextval+1:a]
    list2.sort()
    no=list1+list2
    print(no)
   else:
    print(-1)     

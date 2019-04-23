#https://www.spoj.com/problems/JNEXT/
t = int(input())

for k in range(t):
 n = int(input())
 no = list(map(int,input().split(" ")))
 i=n-1
 diff = 1
 found = False
 while((not found) and i>0):
     if(i-diff>0 and diff<n):
        if(no[i-diff]<no[i]):
            no[i],no[i-diff]=no[i-diff],no[i]
            found=True
            break
        if(i==1):
            diff=diff+1
            i=n-1
     i=i-1

 if(found==True):
    list1 = no[0:i]
    list2 = no[i:n]
    list2.sort()
    no=list1+list2
    no=''.join(str(x) for x in no)
    print(no)

 else:
    print(-1)



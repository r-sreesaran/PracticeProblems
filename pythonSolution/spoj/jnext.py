#https://www.spoj.com/problems/JNEXT/
t = int(input())
diff = 1 
found = False

for k in range(t):
 n = int(input())
 no = list(map(int,input().split(" ")))
 i=n-1
 while((not found) and diff<n):
     if(i-diff>0):
        if(no[i-diff]>no[i]):
            no[i],no[i-diff]=no[i-diff],no[i]
            found=True
            break
        if(i==1):
            diff=diff+1
            i=n-1
 i=i-1

 if(found==True):
    list1 = no[0:i+1]
    list2 = no[i+1:n]
    list2.sort()
    no=list1+list2
    print(no)
else:
    print(-1)
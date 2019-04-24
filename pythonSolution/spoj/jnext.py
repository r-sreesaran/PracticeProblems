#https://www.spoj.com/problems/JNEXT/
t = int(input())

for k in range(t):
 n = int(input())
 no = list(map(int,input().split(" ")))
 i=n-1
 found = True
 while i > 0 and no[i - 1] >= no[i]:
        i -= 1
 if i <= 0:
    found=False
          
 if(found==True):
    j = len(no) - 1
    while no[j] <= no[i - 1]:
        j -= 1
    no[i - 1], no[j] = no[j], no[i - 1]

    list1 = no[0:i]
    list2 = no[i:n]
    list2.sort()
    no=list1+list2
    no=''.join(str(x) for x in no)
    print(no)

 else:
    print(-1)



def sort(alist):
    n = len(alist)
    for i in range(n):
        for j in range(i,n):
            if(alist[i]<alist[j]):
                alist[i],alist[j]=alist[j],alist[i]
    print(alist)
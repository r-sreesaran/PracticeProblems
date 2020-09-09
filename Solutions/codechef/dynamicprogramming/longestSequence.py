LS = list(map(int,input().split(" ")))
n = len(LS)
for i in range(0,n-1):
     LS[i]=1
     for j in range(0,i-1):
          if (a[i] >  a[j] and LS[i]<LS[j]):
              LS[i] = LS[j]+1

for i in range(0,n-1):
      if (largest < LS[i]):
          largest = LS[i]

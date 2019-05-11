#https://www.spoj.com/problems/HISTOGRA/
#This solution takes o(n^2) running time


n=[-1]
while(n[0]!=0):
    n=list(map(int,input().split()))
    a=0
    if(n[0]!=0):
      length = n[0]
      i=1
      m=0
      while(i<=length):
           j=1
           while(j+i<=length):
              l=min(n[j:i+j+1])
              a = l*(i+1)
              if(m<a):
                   m=a
              j+=i
           i+=1
      print(m)
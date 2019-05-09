#https://www.spoj.com/problems/HISTOGRA/

n=-1
while(n!=0):
    n=list(map(int,input().split(" ")))
    if(n!=0):
      length = n[0]
      i=1
      max=0
      while(i<=length-1):
           j=1
           while(j+i<n):
              l=max(n[j:i+j+1])
              a = l*i
              if(a>max):
                   a=max
              j+=i
        i+=1

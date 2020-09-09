
def prob(n):
      count = [0]*(n+1)
      count[1]=1
      count[2]=2

      if n == 1: return 1
      if n == 2: return 2

      for i in range(3,n+1):
          count[i] = count[i-1]+count[i-2]

      return count[n]

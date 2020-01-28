class sample:

  count = []
  def prob(n):
    global  count
    if n == 1: return 1
    if n == 2: return 2

    if count[n]!=0: return count[n]
    else:
        count[n] = prob(n-1)+prob(n-2)
        return count[n]

  def climbStairs(n):
    global count
    count = [0]*(n+1)
    return sample.prob(n)
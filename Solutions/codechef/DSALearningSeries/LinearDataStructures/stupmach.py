#https://www.codechef.com/LRNDSA02/problems/STUPMACH

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int,input().split(" ")))
    l =n
    total = 0
    try:
        remove =s.index(0)
        s= s[:remove]
        l = len(s)
    except:
        pass

    while l>1:
      minv = min(s)
      total = total + (l * minv)
      s = [v-minv for v in s ]
      remove = s.index(0)
      s = s[:remove]
      l = len(s)

    try:
      total = total + s[0]
    except:
        pass

    print(total)
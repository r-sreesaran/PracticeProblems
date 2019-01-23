n = int(input())
c = set(range(1,101))
for _ in range(n):
    a = set()
    m,sp,t = map(int, input().split())
    M = list(map(int, input().split()))
    for i in range(m):
        b = set(range(M[i]-(sp*t),M[i]+(sp*t)+1))
        a = a.union(b)
        a = a.intersection(c)
    print(100-len(a))
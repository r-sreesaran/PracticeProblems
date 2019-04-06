for _ in range(int(input())):
    t = int(input())
    con = list(map(int,input()))
    n= con.count(1)
    print(int((n*(n+1))/2))
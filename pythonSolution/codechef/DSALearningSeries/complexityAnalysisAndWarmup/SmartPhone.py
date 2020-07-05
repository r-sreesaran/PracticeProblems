try:
    n = int(input())
    no = list()
    for _ in range(n):
        no.append(int(input()))

    no.sort(reverse=True)
    for i in range(len(no)):
        no[i] = no[i] * (i + 1)
    no.sort()
    print(no[-1])
except:
    pass

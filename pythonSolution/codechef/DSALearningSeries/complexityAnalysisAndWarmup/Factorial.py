# factorial using memorization
a = int(input())
fact_values = []
divisble = []
fact_values.append(1)

def fact(n, start=1):

    for i in range(start, n + 1):
        fact_values.append(fact_values[i-1] * i)


for _ in range(a):
    n = int(input())
    try:
        value = fact_values[n]
    except IndexError:
       fact(n,len(fact_values)+1)
    print(fact_values[n-1])

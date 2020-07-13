# factorial using memorization
a = int(input())
fact_values = []
divisble = []
fact_values.append(1)
fact_values.append(1)

def fact(n, start=2):

    for i in range(start, n + 1):
        fact_values.append(fact_values[i-1] * i)

def divisibility(temp,no):
    if(no%10==0):
        temp = temp+1
        temp = divisibility(temp, int(no / 10))
    else:
        return temp

    return  temp

for _ in range(a):
    n = int(input())
    try:
        value = fact_values[n]
    except IndexError:
       fact(n,len(fact_values))
    print(divisibility(0,fact_values[n]))

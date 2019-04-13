from typing import List

no1=[1,9,3,7,0,7,7,2,1] 
no2=[7,6,1,8,3,8,2,5,7,2,8,7]
result=[]
carryover=0
def multiply(num1: List[int], num2: List[int]):
    sign = -1 if(num1[0]<0) ^ (num2[0]<0) else 1

    result = [0] * (len(num1) + len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i+j+1] += num1[i] * num2[j]
            result[i+j] += result[i+j+1] // 10
            result[i+j+1] %= 10
    result = result[next((i for i, x in enumerate(result)
    if x !=0 ), len(result)): ] or [0]
    return [sign * result[0]] + result[1:]
result= multiply(no1,no2)
print(result)
        
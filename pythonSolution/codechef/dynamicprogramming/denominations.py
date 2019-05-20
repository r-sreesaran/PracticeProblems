import math

denominations = [1,3,5]
sum = 13
minimum = [sum]*100
minimum[0]=0


for i in range(1,sum+1): 
    for d in denominations:
        if(d<=i and minimum[i-d]+1< minimum[i]):
            minimum[i] = minimum[i-d]+1

print(minimum[sum])

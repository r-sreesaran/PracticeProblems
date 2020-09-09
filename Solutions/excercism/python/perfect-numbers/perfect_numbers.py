import math

def classify(number):
    factors = []

    if(number <=0):
        raise ValueError("Disibility error")

    for no in range(1,number):
       if number % no == 0: factors.append(no)

    if sum(factors) ==  number :
        return "perfect"

    elif sum(factors) > number :
        return "abundant"

    else :
        return "deficient"

def is_armstrong_number (number):
    sum = 0
    pow = len(str(number))
    for no in str(number):
        sum += int(no) ** pow
    return sum == number

def is_armstrong_number_listComprehension (number):
    pow = len(str(number))
    sum((int(no) ** pow) for no in str(number))
    return sum == number

def find_the_sum (number):
    numbers=[]
    for position,no in enumerate(str(number)):
         numbers.append([position+1,int(no)])
    sum = 0
    for position,no in numbers:
        sum += no**position
    return  sum==number

def convert(number):
    result = ""
    if (number%3 == 0):
        result = result+"Pling"
    if (number % 5 == 0):
        result = result+"Plang"
    if (number % 7 == 0):
        result = result+"Plong"
    if(number%7!=0 and number % 5!=0 and number%3!=0):
        result = f"{number}"
    return result

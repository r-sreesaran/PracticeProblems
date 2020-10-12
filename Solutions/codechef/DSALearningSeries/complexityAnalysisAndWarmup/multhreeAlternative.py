def multiple1(no_of_digits,d0,d1):
 #t = int(input())
 #for _ in range(t):
    #no_of_digits,d0,d1 = list(map(int,input().split(" ")))
    sum = d0+d1
    dk =  sum % 10
    for _ in range(no_of_digits-3):
        sum += dk
        dk = sum%10

    sum += dk
    #print("yes") if  sum%3==0 else print("No")
    return "YES" if sum % 3 == 0 else "NO"
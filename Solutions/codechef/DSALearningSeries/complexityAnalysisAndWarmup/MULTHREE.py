#https://www.codechef.com/LRNDSA01/problems/MULTHREE

# t = int(input())
# for _ in range(t):
#     no_of_digits,d0,d1 = list(map(int,input().split(" ")))
#     sum = d0+d1
#     dk =  sum % 10
#     for _ in range(no_of_digits-3):
#         sum =+ dk
#         dk = sum%10
#
#     sum += dk
#     print("yes") if  sum%3==0 else print("No")


# This is the wrong implementation assuming the repetition will start after three numbers

# t = int(input())
# for _ in range(t):
#     no_of_digits,d0,d1 = list(map(int,input().split(" ")))
#     digits = []
#     dk = d0+d1
#     total = dk+d0+d1
#     Sum = total
#     for _ in range(4):
#         dk = Sum%10
#         Sum += dk
#         digits.append(dk)
#     Sum = sum(digits)
#
#     if no_of_digits <=2 :
#         Sum = d0+d1
#     elif no_of_digits-3 <=7 :
#         Sum = total + sum(digits[0:no_of_digits-3])
#     else :
#         if (no_of_digits - 3) % 4 == 0:
#             Sum = total + Sum * ((no_of_digits - 3) // 4)
#
#         else:
#             Sum = Sum *( (no_of_digits - 3) // 4)
#             Sum = total + Sum + sum(digits[:(no_of_digits - 3) %4 ])
#
#
#     print("YES") if Sum % 3 == 0 else print("NO")

def multiple(no_of_digits:int,d0:int,d1:int):
 #t = int(input())
 #for _ in range(t):
    #no_of_digits,d0,d1 = list(map(int,input().split(" ")))
    #no_of_digits -=2
    digits = []
    dk = d0+d1
    Sum =dk
    digits.append(d1)
    digits.append(d0)
    for _ in range(10):
       dk = Sum%10
       Sum += dk
       digits.append(dk)



    if no_of_digits<10:

       #print("YES") if Sum % 3 == 0 else print("NO")
       return  "YES" if Sum % 3 == 0 else "NO"
       #continue

    else:
      t0 = d0%2
      t1 = d1%2

      if ((t1==0 and t0%2==0) or (t1!=0 and t0!=0)):
          no_of_digits -= 2
          no_of_sets = no_of_digits//4
          remainder = no_of_digits%4
          Sum =  sum(digits[0:2]) + ((no_of_sets * 20) if digits[3]!=0 else 0) + sum(digits[2:2+remainder])
      else:
          no_of_digits -= 3
          no_of_sets = no_of_digits // 4
          remainder = no_of_digits % 4
          Sum = sum(digits[0:3]) +( (no_of_sets * 20) if digits[3]!=0 else 0 ) + sum(digits[3:3+remainder])

    #print("YES") if Sum % 3 == 0 else print("NO")
    return "YES" if Sum % 3 == 0 else "NO"



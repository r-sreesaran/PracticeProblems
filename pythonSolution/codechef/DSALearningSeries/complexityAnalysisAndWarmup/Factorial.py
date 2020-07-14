# factorial using memorization
# tip https://brilliant.org/wiki/trailing-number-of-zeros/

a = int(input())

def find_no_of_zeros(n):
   count=0;
   intial = 5;
   if(n<5):
       return 0;
   while (intial < n):
      count =  count + int(n/intial)
      intial= intial * 5
   return count

for _ in range(a):
    n = int(input())
    print(find_no_of_zeros(n))



#fact_values.append(1)
#  fact_values.append(1)

# def fact(n, start=2):
#
#     for i in range(start, n + 1):
#         fact_values.append(fact_values[i-1] * i)

#Traceback (most recent call last):
#  File "./prog.py", line 29, in <module>
#  File "./prog.py", line 17, in divisibility
#  File "./prog.py", line 17, in divisibility
#  File "./prog.py", line 17, in divisibility
#  [Previous line repeated 994 more times]
#  File "./prog.py", line 15, in divisibility
# RecursionError: maximum recursion depth exceeded in comparison


# def divisibility(temp,no):
#     if(no%10==0):
#         temp = temp+1
#         temp = divisibility(temp, int(int(no) // int(10)))
#     else:
#         return temp
#
#     return  temp

# def divisibility(no):
#     str(no)


# https://www.codechef.com/LRNDSA02/problems/ZCO12001

l = int(input())
items = list(input().split(" "))

max_depth = 0
max_depth_pos = 0
length_vector = [0]
symbols = []
depth = 0
max_length = 0
max_length_pos = 0

for i in range(l):
    if items[i] == '1':
        symbols.append((i,"1"))
        depth +=1
        if(depth>max_depth):
            max_depth = depth
            max_depth_pos = i+1


    elif items[i]== '2':
        symbols.pop(len(symbols)-1)
        depth -=1
        if(depth ==0):
            length_vector.append((i+1))

for i in range(len(length_vector)-1):
    if(length_vector[i+1]-length_vector[i]>max_length):
        max_length = length_vector[i+1]-length_vector[i]
        max_length_pos = length_vector[i]+1


print(max_depth,max_depth_pos,max_length,max_length_pos)


# N = int(input())
# braces = list(map(int, input().split()))
# nesting_depth, nesting_depth_index, max_elements_index, max_elements, stack_cnt = 0, 0, 0, 0, 0
# stack = []
#
# for i in range(N):
#     if braces[i] == 1:
#         stack.append(i)
#         stack_cnt += 1
#         if stack_cnt > nesting_depth:
#             nesting_depth = stack_cnt
#             nesting_depth_index = i + 1
#     elif braces[i] == 2:
#         stack_cnt -= 1
#         starting_index = stack.pop()
#         if len(stack) == 0:
#             if i - starting_index > max_elements:
#                 max_elements = i + 1 - starting_index
#                 max_elements_index = starting_index + 1
#
# print(nesting_depth, nesting_depth_index, max_elements, max_elements_index)

# Test cases
# 14
# 1 1 2 1 2 1 2 2 1 1 1 2 2 2
# 3 11 8 1



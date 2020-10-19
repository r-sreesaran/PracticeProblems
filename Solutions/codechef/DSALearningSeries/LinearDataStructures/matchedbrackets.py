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
            max_depth_pos = i-1

    elif items[i]== '2':
        symbols.pop(len(symbols)-1)
        depth -=1
        if(depth ==0):
            length_vector.append((i+1))

for i in range(len(length_vector)-1):
    if(length_vector[i+1]-length_vector[i]>max_length):
        max_length = length_vector[i+1]-length_vector[i]
        max_length_pos = length_vector[i]+1


print(str(max_depth)+" "+str(max_depth_pos)+" "+str(max_length_pos)+" "+str(max_length))



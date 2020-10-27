#https://www.codechef.com/LRNDSA02/problems/NOTALLFL
# t = int(input())
# for _ in range(t):
#     n,k=map(int,input().split(" "))
#     cakeslist = list(map(int,input().split(" ")))
#     cakes_frequency = {}
#     cakes_frequency_list = []
#
#     prev_cake  = cakeslist.pop(0)
#     cake_count = 1
#     for cake in cakeslist:
#         if prev_cake == cake :
#             cake_count += 1
#         else:
#             cakes_frequency_list.append((prev_cake, cake_count))
#             prev_cake = cake
#             cake_count =1
#     cakes_frequency_list.append((prev_cake, cake_count))
#
#     prev = cakes_frequency_list[0]
#     next_pointer = 0
#
#     count = 0
#     #count = prev[1]
#     cakes_types = []
#     # cakes_types.append(prev[0])
#     max_count = count;
#     prev_pointer = 0
#     prev_continue = True
#
#     while next_pointer<len(cakes_frequency_list) and prev_pointer <len(cakes_frequency_list):
#
#         if(prev_continue==True):
#           next = cakes_frequency_list[next_pointer]
#           cakes_types.append(next[0])
#           count += next[1]
#
#         if(len(set(cakes_types))<k):
#             if(count>max_count):
#                 max_count=count
#             prev_continue = True
#
#         else:
#             count -= prev[1]
#             cakes_types.pop(0)
#             prev_pointer+=1
#             prev = cakes_frequency_list[prev_pointer]
#             next_pointer -=1
#             prev_continue = False
#
#         next_pointer += 1
#
#     print(max_count)

# The above solution exceeds the prescribed time limit

# TODO Add explanation how the current algorithm is better than the previous one
# TODO Add pictorial representation how the solution works
# TODO Add Big O(n) for both solutions

t = int(input())
for _ in range(t):
    n,k=map(int,input().split(" "))
    cakeslist = list(map(int,input().split(" ")))
    count = []
    l,r,maxv,nflav = 0,0,0,0;

    for i in range(k+1):
        count.append(0)

    while True:

        while r<n and nflav<k:
            if count[cakeslist[r]]==0:
                nflav +=1
            count[cakeslist[r]] += 1
            if nflav<k:
                maxv = max(maxv,r-l+1)
            r+=1

        if r==n:
            break

        while l<=r and nflav==k:
            if count[cakeslist[l]]==1:
                nflav -=1
            count[cakeslist[l]] -=1
            l+=1
    print(maxv)


# ------------------
# 1
# 9 3
# 1|2|2|2|2|2|2|3|3|
# ------------------
#
# The following is the input and output here must be 8,
# The longest subsequence can contain length of max of two different flavours of cake
# To calculate this, we iterate over the list, so its basically takes time just O(n)
# But to do this there should be two pointers one referring to the lowest starting element and another to the current location
# l and r are used as locaters.
# count is a array that will store the maximum value of each and every element
# As we move to the next element, the max no of flavours selected might be affected.
# Due to which the nflav will become equal to k
# using which we can run a while loop to remove the elements from list
# And since l is pointing to the starting element we can subtract it from value saved in count array
# the difference of l and r at any point will give maximum length.
# using this we can get the maximum subsequence.
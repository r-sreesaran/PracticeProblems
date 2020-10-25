#https://www.codechef.com/LRNDSA02/problems/NOTALLFL
t = int(input())
for _ in range(t):
    n,k=map(int,input().split(" "))
    cakeslist = list(map(int,input().split(" ")))
    cakes_frequency = {}
    cakes_frequency_list = []

    prev_cake  = cakeslist.pop(0)
    cake_count = 1
    for cake in cakeslist:
        if prev_cake == cake :
            cake_count += 1
        else:
            cakes_frequency_list.append((prev_cake, cake_count))
            prev_cake = cake
            cake_count =1
    cakes_frequency_list.append((prev_cake, cake_count))

    prev = cakes_frequency_list[0]
    next_pointer = 0

    count = 0
    #count = prev[1]
    cakes_types = []
    # cakes_types.append(prev[0])
    max_count = count;
    prev_pointer = 0
    prev_continue = True

    while next_pointer<len(cakes_frequency_list) and prev_pointer <len(cakes_frequency_list):

        if(prev_continue==True):
          next = cakes_frequency_list[next_pointer]
          cakes_types.append(next[0])
          count += next[1]

        if(len(set(cakes_types))<k):
            if(count>max_count):
                max_count=count
            prev_continue = True

        else:
            count -= prev[1]
            cakes_types.pop(0)
            prev_pointer+=1
            prev = cakes_frequency_list[prev_pointer]
            next_pointer -=1
            prev_continue = False

        next_pointer += 1

    print(max_count)

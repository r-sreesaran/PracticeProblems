#https://www.codechef.com/LRNDSA02/problems/PSHOT

t = int(input())
for _ in range(t):
    n = int(input())
    goals = [int(x) for x in input()]


    combinations = []
    sa = 0
    sb = 0
    ra = n
    rb = n
    for i in range(0,n*2,2):
        #combinations.append((goals[i],goals[i+1]))



        if goals[i]==1:
            sa +=1
        ra = ra - 1

        if sa - sb > rb or sb - sa > ra :
            print(i + 1)
            break

        if goals[i+1]==1:
            sb+=1
        rb =rb -1


        if sb - sa > ra or sa - sb > rb:
            print((i + 2))
            break

        elif i==(n*2)-2:
            print(n*2)





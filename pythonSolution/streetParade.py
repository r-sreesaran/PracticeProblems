'''
10



no
5
1 3 4 2 5
no
4
4 2 3 1
no
1 2 10 5 4 3 9 8 7 6
yes
4 1 5 3 2
no
5
3 1 2 5 4
yes
5
5 1 2 4 3
0
'''

lane=[];
state=True
need = 1
size = int(input())
if(size!=0):
    order = list(map(int,input().split(" ")))
    for i in range(size):
        while not lane and lane[-1] == need:
            need+=1
            lane.pop()
        if(order[i]==need):
            need=+1
        elif not lane and lane[-1]<order[i]:
            state = False
            break
        else:
            lane.append(order[i])
    if(state):
       print ("yes")
    else:
       print ("no")




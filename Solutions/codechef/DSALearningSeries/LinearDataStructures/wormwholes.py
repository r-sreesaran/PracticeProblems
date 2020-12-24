#https://www.codechef.com/LRNDSA02/problems/ZCO12002

n,x,y = map(int,input().split(" "))
contest = []
for _ in range(n):
    s,e = map(int,input().split(" "))
    contest.append([s,e])
v = list(map(int,input().split(" ")))
w = list(map(int,input().split(" ")))

v.sort();
w.sort();
min_time = 1000000;

for i in range(n):
    s,e = contest[i][0],contest[i][1]
    start_time = 0;
    end_time = 0;
    for j in range(x):
        if (v[j]<=s):
           start_time = v[j]
        else:
           break;
    for j in range(y):
        if(w[j]>=e):
            end_time = w[j]
            break;
    time = end_time - start_time +1
    if(time<min_time and time > 0):
        min_time = time

print(min_time)

#Binary search
def find_nearpoint(time,wormwholes,len_wormwholes):
    start = 0
    end = len_wormwholes-1
    mid = start + end / 2
    if(time<=wormwholes[mid]):
        end = mid
    else:
        start = mid+1



# print(n,x,y)
# print(contest)
# print(v,w)




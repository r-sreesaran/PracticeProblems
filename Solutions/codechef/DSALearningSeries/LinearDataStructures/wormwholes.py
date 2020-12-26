#https://www.codechef.com/LRNDSA02/problems/ZCO12002

#Binary search
def find_nearpoint(time,wormwholes,len_wormwholes,start_wormhole):
    start = 0
    end = len_wormwholes-1

    while start<=end:
      mid = start + int((end - start) / 2)
      if(time==wormwholes[mid]):
        return wormwholes[mid]
      elif(wormwholes[mid]<time):
        start  = mid+1
      else :
        end = mid-1

    if start_wormhole:
        return wormwholes[mid] if time> wormwholes[mid] else wormwholes[mid-1]
    else:
        return wormwholes[mid] if time< wormwholes[mid] else wormwholes[mid+1]

def find_mintime(v,w,x,y,contest):
    v.sort();
    w.sort();
    min_time = 1000000;
    for i in range(n):
        s, e = contest[i][0], contest[i][1]
        if (s>=v[0] and e<=w[-1]):

         start_time = find_nearpoint(s, v, x,True);
         end_time = find_nearpoint(e, w, y,False);
         time = end_time - start_time + 1
         if (time < min_time and time > 0):
            min_time = time

    print(min_time)


# Naive implementation o(n^2)
# for i in range(n):
#     s,e = contest[i][0],contest[i][1]
#     start_time = 10000;
#     end_time = 0;
#     for j in range(x):
#         if (v[j]<=s):
#            start_time = v[j]
#            break;
#     for j in range(y):
#         if(w[j]>=e):
#             end_time = w[j]
#             break;
#     time = end_time - start_time +1
#     if(time<min_time and time > 0):
#         min_time = time


if __name__ == "__main__":
    n, x, y = map(int, input().split(" "))
    contest = []
    for _ in range(n):
        s, e = map(int, input().split(" "))
        contest.append([s, e])
    v = list(map(int, input().split(" ")))
    w = list(map(int, input().split(" ")))
    find_mintime(v,w,x,y,contest)
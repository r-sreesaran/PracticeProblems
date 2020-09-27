#https://www.codechef.com/LRNDSA01/problems/LADDU

import enum

class Point(enum.Enum):
   CONTEST_WON = 300
   TOP_CONTRIBUTOR = 300
   CONTEST_HOSTED = 50
   INDIAN = 200
   NON_INDIAN = 400

activities = int(input())
for t in range(activities):
    total = 0
    n,nationality = map(str,input().split(""))
    total = 0

    for item in range(n):
        no = 0;
        print(item)
        l1 = map(str,input().split(" "))
        if len(l1)>1:
            no = int(l1[1])
            if l1[0]=='CONTEST_WON' and no<20 :
                total = total + 20 - no


        total = total + Point.l1[0] + no[0]
    print(int(total/Point.nationality))







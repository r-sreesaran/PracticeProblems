#https://www.codechef.com/LRNDSA01/problems/LADDU
#
# import enum
#
# class Point(enum.Enum):
#    CONTEST_WON = 300
#    TOP_CONTRIBUTOR = 300
#    CONTEST_HOSTED = 50
#    INDIAN = 200
#    NON_INDIAN = 400
#    BUG_FOUND = 0
#
# activities = int(input())
# for t in range(activities):
#     total = 0
#     n,nationality = map(str,input().split(" "))
#     n = int(n)
#
#     for item in range(n):
#         l1 = list(map(str,input().split(" ")))
#         if len(l1)>0:
#
#             if l1[0]==Point.CONTEST_WON.name :
#                 no = int(l1[1])
#                 total += Point.CONTEST_WON.value + (20 -no if  no <=20 else 0)
#             if l1[0] ==Point.CONTEST_HOSTED.name :
#                 total += Point.CONTEST_HOSTED.value
#             if l1[0] == Point.TOP_CONTRIBUTOR.name:
#                 total += Point.TOP_CONTRIBUTOR.value
#             if l1[0] == Point.BUG_FOUND.name:
#                 total += int(l1[1])
#
#     print(int(total/Point[nationality].value))

activities = int(input())
for t in range(activities):
    total = 0
    n,nationality = map(str,input().split(" "))
    n = int(n)
    total = 0

    for item in range(n):
        no = 0;
        l1 = list(map(str,input().split(" ")))
        if len(l1)>0:

            if l1[0]=="CONTEST_WON" :
                no = int(l1[1])
                total += 300 + (20 -no if  no <=20 else 0)
            if l1[0] =="CONTEST_HOSTED" :
                total += 50
            if l1[0] == "TOP_CONTRIBUTOR":
                total += 300
            if l1[0] == "BUG_FOUND":
                total += int(l1[1])

    print(total// (200 if nationality == "INDIAN" else 400))

#https://www.codechef.com/LRNDSA02/problems/ZCO15004

no_of_points  = int(input())

points = []
for _ in range(no_of_points):
    (x,y) = map(int,input().split(" "))
    points.append((x,y))


# Adding arbitary points
for _ in range(500):
    points.append((_,500))

points.append((0,100000))

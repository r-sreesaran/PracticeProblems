#https://www.codechef.com/LRNDSA02/problems/ZCO15004
# video tutorial is https://www.youtube.com/watch?v=XC8PHFDuVD0&list=PLi0ZM-RCX5nsjTRrJVndL0jdJkIhKvGOJ&index=4&ab_channel=CodeChef

no_of_points  = int(input())

points = []
for _ in range(no_of_points):
    (x,y) = map(int,input().split(" "))
    points.append((x,y))


# Adding arbitary points
for _ in range(500):
    points.append((_,500))

points.append((0,100000))

points = sorted(points,key=1)
points_with_pos = []
pos=0
for point in points:
   points_with_pos.append((point[0],point[1],pos))
   pos=+1

points = points_with_pos
rightside_points_finder = [points(0)]
rightside_points = len(points)*[0]
position =0

# The tuple will have three points namely the x,y co-cordinate, the position

for point in points:


    starting_point = point[0]
    # comparing the y position
    if rightside_points_finder[-1][1] > starting_point[1]:
       current_point = rightside_points.pop()
       # setting the max point till rectangle can be drawn
       rightside_points[current_point[3]]=starting_point[0]


















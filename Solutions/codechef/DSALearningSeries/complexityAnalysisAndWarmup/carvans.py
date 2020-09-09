try:
   t = int(input())
   for _ in range(t):
    cars = int(input())
    cars_speed = list(map(int, input().split(" ")))
    cars_in_maxspeed = 1
    max_speed = cars_speed[0]
    for pos in range(1, len(cars_speed)):
        if (max_speed > cars_speed[pos] ):
            cars_in_maxspeed += 1
            max_speed = cars_speed[pos]
    print(cars_in_maxspeed)
except:
    pass
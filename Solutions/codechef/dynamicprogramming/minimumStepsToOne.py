n=12
minimum = [0]*(n+1)
minimum[1] =0
minimum[2] = minimum[3] = 1

for i in range(4,n+1):
     minimum[i] = minimum[i-1]+1
     if(i%2==0):
         minimum[i] =  min(minimum[i],minimum[int(i/2)]+ 1)
     elif(i%3==0):
         minimum[i] =  min(minimum[i],minimum[int(i/2)]+ 1)

print(minimum[n])           
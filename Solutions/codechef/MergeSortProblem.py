#https://www.codechef.com/problems/MRGSRT
def snapshot(left,right,n,depth):
    mid = int((left + right)/2)
    if(mid>=n):
        right=mid
    else:
        left=mid+1
    print(left,right)
    depth = depth+1
    if(left==right):
        if(left==n):
          print(depth)
          
    else:
        snapshot(left,right,n,depth)

k = raw_input().split(" ")
k = int(k)

for i in range(k):
    values = list(map(int,input().split(" ")))
    left = values[0], right = values[1] 
    if(values[0] <= values[2] <= values[1]):
       print(values[0],values[1])
        
    else: 
       print(-1)


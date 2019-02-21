tc = int(input())
for i in range(0,tc):
 len = int(input())
 number = list(map(int,input().split()))
 i=0
 exchange = True
 for i in range(len-1,0,-1):
  if(number[i]>number[i-1]):
   number[i],number[i-1] = number[i-1],number[i]
   exchange = False
   break;

  if(exchange):
   print("no")
  else:
    newlist = number(0,i)
    newlist.append(number(i,len-1).sort())
    print(newlist)







 
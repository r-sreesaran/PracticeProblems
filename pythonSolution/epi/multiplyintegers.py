no1=[1,2,3] 
no2=[3,2,1]
result=[]
carryover=0

for i in reversed(range(len(no1)-1)):
    ans = no1[i] * no2[i]
    if(ans<10):
       result.append(ans+carryover)
    else:
        result.append(ans%10)
        carryover = int(ans/10)
print(result)
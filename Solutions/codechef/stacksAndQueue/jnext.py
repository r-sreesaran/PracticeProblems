#https://www.codechef.com/certification/data-structures-and-algorithms/prepare#foundation
#https://www.codechef.com/problems/NXTBIG

def process():
    n = int(input())
    temp=[]

    for k in range(n):
      l = int(input())
      data = list(map(int,input().split(' ')))
      temp.append("".join([str(j) for j in data]))
      temp.append(biggest_number(data,l))

    for i in temp:
        print(i)

def biggest_number(no:list, l:int):

     placeholder =0
     for j in reversed(range(1,l)):
         if no[j-1]< no [j]:
             placeholder=j
             break

     if placeholder ==0 :
       return "NO NXTBIG"

     ans = no[:placeholder-1]
     pending = no[placeholder:]
     value = no[placeholder-1]
     pending.sort()
     length =  len(pending)
     i =0
     while i<length and value >= pending[i]:
           i =i +1
     ans.append(pending[i])
     pending[i] = value
     ans.extend(pending)
     return ''.join([str(j) for j in ans])

process()

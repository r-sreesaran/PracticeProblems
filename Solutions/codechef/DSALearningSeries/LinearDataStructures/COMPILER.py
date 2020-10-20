#https://www.codechef.com/LRNDSA02/problems/COMPILER

# t = int(input())
# for _ in range(t):
#     branceslist = list(input())
#     openbraces = []
#     count =0
#     expression = 0
#     if(branceslist[0]=='>'):
#         print(0)
#         continue
#
#     for e in range(len(branceslist)):
#         if branceslist[e]=='<':
#             openbraces.append(branceslist[e])
#             #expression +=1
#
#
#         else:
#             if len(openbraces)!=0:
#                 openbraces.pop(len(openbraces)-1)
#                 count +=1
#             else:
#                 break
#
#
#     if(len(openbraces)==0):
#       print(count*2)
#     else:
#         print(0)


t = int(input())
for _ in range(t):
    branceslist = list(input())
    openbraces = []
    count =0
    maincount = 0
    if(branceslist[0]=='>'):
        print(0)
        continue

    for e in range(len(branceslist)):
        if branceslist[e]=='<':
            openbraces.append(branceslist[e])
            #expression +=1


        else:
            if len(openbraces)!=0:
                openbraces.pop(len(openbraces)-1)
                count +=1
                if (len(openbraces)==0):
                   maincount = maincount + count*2
                   count =0


            else:
                break


    if(len(openbraces)!=0 and maincount ==0):
      print(0)
    else:
        print(maincount)

# Better solution

# cook your dish here
t = int(input())
#<><<<><><><<<><>><<<>><>><

for i in range(t):
    s = input()
    su = 0
    ans = 0
    count = 0
    for c in s:
        if c == "<":
            su+=1
        else:
            su-=1
            if su==0:
                ans=count+1
            elif su<0:
                break
        count+=1
    print(ans)


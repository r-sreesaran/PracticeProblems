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

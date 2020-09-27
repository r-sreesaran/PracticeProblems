#https://www.codechef.com/LRNDSA01/problems/CONFLIP
# The no of test cases

# testcases = int(input())
#
# for t in range(testcases):
#     games = int(input())
#     for g in range(games):
#         I,N,Q = map(int,input().split(" "))
#         initial = N * [I]
#         for count in range(N):
#             if count%2==0 :
#              initial[count]  = 2  if initial[count] == 1 else  1
#         print(initial.count(Q))


#https://www.codechef.com/LRNDSA01/problems/CONFLIP
# The no of test cases

testcases = int(input())

for t in range(testcases):
    games = int(input())
    for g in range(games):
        I,N,Q = map(int,input().split(" "))
        if N%2==0:
            print(int(N/2))
        else:
            if I==1:
                print(int(N/2) if Q==1 else int(N/2+1))
            else:
                print(int(N/2)+1 if Q==1 else int(N/2))



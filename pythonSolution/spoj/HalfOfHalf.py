#https://www.spoj.com/problems/STRHH/
n = int(input())
for i in range(n):
    word = list(input().strip())
    length  = len(word)
    print(word[0],end='')
    if(length>4):
        for j in range(2,int(length/2),2):
            print(word[j],end='')
    print("")
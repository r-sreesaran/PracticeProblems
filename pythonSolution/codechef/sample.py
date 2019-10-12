# https://www.codechef.com/problems/LAPIN

n = int(input())
string=[]

for i in range(n):
    string.append(input())


for i in string:
    length = len(i)
    if (length % 2 == 0):
        firstHalf = int(length / 2)
        secondHalf = firstHalf
    else:
        firstHalf = int(length / 2)
        secondHalf = firstHalf + 1
    string1 = ''.join(list(i)[0:firstHalf])
    string2 = ''.join(list(i)[secondHalf:length+1])
    print(('NO','YES') [string1 in string2])

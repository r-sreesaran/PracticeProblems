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
    string1 = list(i)[0:firstHalf]
    string2 = list(i)[secondHalf:length+1]
    string1.sort()
    string2.sort()
    print(('NO','YES') [string1 == string2])

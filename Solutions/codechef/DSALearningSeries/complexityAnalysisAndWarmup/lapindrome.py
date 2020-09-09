# cook your dish here
n = int(input())
condition = "YES"
for _ in range(n):
    no = input()
    first_half_start = 0
    first_half_end = int(len(no) / 2)
    second_half_start = int(len(no) / 2) if len(no) % 2 == 0 else int(len(no) / 2) + 1
    second_half_end = len(no)
    string1 = no[first_half_start:first_half_end]
    string2 = no[second_half_start:second_half_end]

    if (string1 == string2):
        print("YES")
    elif(sorted(string1)==sorted(string2)):
        print("YES")
    else:
       print("NO")

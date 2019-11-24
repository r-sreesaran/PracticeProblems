import copy

n = " ".join(input()).split()
print(n)
def findPermutations(n):

    permute = n
    length = len(n)
    for i in range(length):
        for  j in range(i+1,length):
              temp = copy.deepcopy(permute)
              temp[i] = permute[j]
              temp[j] = permute[i]
              print(temp)
findPermutations(n)

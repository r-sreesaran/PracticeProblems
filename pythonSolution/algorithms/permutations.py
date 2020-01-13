
def permutations(original,prefix):
    if(not original):
        print(prefix)
    else:
        for i in range(len(original)):
            rem = original[0:i]+original[i+1:]
            permutations(rem,prefix+original[i])

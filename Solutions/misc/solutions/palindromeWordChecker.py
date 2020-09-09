

def checkStringIsPalindrome(string):
    palindromeTab={}
    found = True
    for e in string.replace(" ",""):
        if palindromeTab.get(e):
            palindromeTab[e]= palindromeTab[e]+1
        else:
            palindromeTab[e]=1

    for value in palindromeTab.values():

         if value %2 !=0:
             if found == True and value==1:
                found = False
             else:
                 return  False

    return True

# Read in the tokens one at a time
# If a token is an integer, write it into the output
# If a token is an operator, push it to the stack, if the stack is empty. If the stack is not empty, you pop entries with higher or equal priority and only then you push that token to the stack.
# If a token is a left parentheses '(', push it to the stack
# If a token is a right parentheses ')', you pop entries until you meet '('.
# When you finish reading the string, you pop up all tokens which are left there.
# Arithmetic precedence is in increasing order: '+', '-', '*', '/';

def InfxToPostFix():
    expression = list(map,input("Enter the expression"))
    for element in expression:



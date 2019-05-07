#https://www.spoj.com/problems/MMASS/

m = input().split(" ")
st = []
for e in m:
    if(e=='('):
       st.append(-1)
    elif(e=='H'):
        st.append(1)
    elif(e=='C'):
        st.append(12)
    elif(e=='O'):
        st.append(16)
    elif(e==')'):
        sum =0
        while (st[-1]!=-1):
            sum = sum + st.pop()
        st.pop()
        st.append(sum)
    elif(e>=2 and e<=9 ):
        no = st[-1]
        st.append(e*st.pop())
    
print(sum(st))    

    
        
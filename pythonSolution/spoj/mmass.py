#https://www.spoj.com/problems/MMASS/

m = list(map(str,input()))

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
        s =0
        while (st[-1]!=-1):
            s = s + st.pop()
        st.pop()
        st.append(s)
    elif(int(e)>=2 and int(e)<=9 ):
        no = st.pop()
        st.append(int(e)*no)
    
print(sum(st))    

    
        
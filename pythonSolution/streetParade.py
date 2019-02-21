
st=[];
state=True

while True:
 size = int(input())
 if(size!=0):
    a = list(map(int,input().split(" ")))
    i = 0
    k=0

    while(i<size):
        while not (not st) and st[-1] == k+1:
            k=k+1
            st.pop()
        if(a[i]!=k+1):
            st.append(a[i])
        else:
            k=k+1
        i=i+1
    while not (not st) and st[-1] == k+1:
        k = k +1
        st.pop()
    if(k==size):
        print("yes")
    else:
        print("no")
 else:
    break


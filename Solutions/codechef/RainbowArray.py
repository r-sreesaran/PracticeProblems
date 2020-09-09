for _ in range(int(input())):
	n=int(input())
	a=[int(x) for x in input().split()]
	if(a==a[::-1] and len(list(set(a)))==7 and a.count(1)>0 and a.count(2)>0 and a.count(3)>0 and a.count(4)>0 and a.count(5)>0 and a.count(6)>0 and a.count(7)>0):
		print("yes")
	else:
		print("no")


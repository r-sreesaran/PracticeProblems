import sys
for cs, s in enumerate(sys.stdin.readlines(), 1):
	if s[0] == '-': break
	n, cnt = 0, 0
	for c in s:
		if c == '{': n+= 1
		elif c == '}' and n==0: n+= 1; cnt+= 1
		elif c == '}' and n>0: n-= 1
	print('%d. %d' % (cs, n/2+cnt))
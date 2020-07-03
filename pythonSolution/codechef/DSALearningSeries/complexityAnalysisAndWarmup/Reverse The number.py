try:
  n = int(input())
  for _ in range(n):
     no = input()
     print(int(no[::-1]))
except Exception:
    pass
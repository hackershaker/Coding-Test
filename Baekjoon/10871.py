n, x = list(map(int, input().split(" ")))
A = list(map(int, input().split(" ")))

A = [k for k in A if k < x]
for num in A: print(num)
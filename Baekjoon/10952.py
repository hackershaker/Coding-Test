case = []
while True:
    a, b = list(map(int, input().split(" ")))
    if a == 0 and b == 0: break
    else: case.append((a,b))

for c in case:
    print(sum(c))
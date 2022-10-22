from itertools import combinations
n ,m = map(int, input().split(" "))
cardlist = list(map(int ,input().split(" ")))

answer = 0
for c in combinations(range(n), 3):
    temp = sum([cardlist[int(i)] for i in c])
    if temp == m:
        answer = m
        break
    elif temp < m:
        answer = max(answer, temp)
    else:
        continue
print(answer)
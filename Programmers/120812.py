from collections import Counter
def solution(array):
    c = Counter(array)
    c = list(sorted(c.items(), key=lambda x : (-x[1])))
    # print(c)
    answer = 0
    for x in c:
        if x[1] == c[0][1]: answer += 1
        if x[1] < c[0][1]: break
        if answer >= 2: return -1
    return c[0][0]

print(solution([1,1,2,2]))
print(solution([1,2,3,3,3,4]))
from itertools import combinations
def solution(number):
    answer = 0
    for c in combinations(range(len(number)), 3):
        if sum([number[int(i)] for i in c]) == 0:
            answer += 1
    return answer

print(solution([-2, 3, 0, 2, -5]))


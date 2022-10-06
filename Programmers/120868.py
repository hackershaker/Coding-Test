def solution(sides):
    answer = 0
    i = 0
    while True:
        if i >= sum(sides):
            break
        sides.append(i)
        if max(sides) * 2 < sum(sides):
            answer += 1
        i += 1
        sides.pop()
    return answer


print(solution([1, 2]))
print(solution([3, 6]))
print(solution([11, 7]))

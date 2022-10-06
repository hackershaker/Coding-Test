def solution(n):
    answer = 0
    # arr = [0, 1]

    a, b = 0, 1
    for i in range(n + 1):
        a, b = a + b, a
    answer = a

    if answer > 1000000007:
        return answer % 1000000007
    else:
        return answer


print(solution(1))

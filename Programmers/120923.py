def solution(num, total):
    answer = []
    n = int(total / num)
    if num % 2 == 1:
        answer.append(n)
        for i in range(1, int(num / 2) + 1):
            answer.append(n - i)
            answer.append(n + i)
    else:
        for i in range(int(num / 2)):
            answer.append(n - i)
            answer.append(n + 1 + i)

    return sorted(answer)


print(solution(3, 12), [3, 4, 5])
print(solution(4, 14), [2, 3, 4, 5])

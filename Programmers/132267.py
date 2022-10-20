def solution(a, b, n):
    answer = 0
    coke = 0
    empty = 0
    while True:
        coke = (n // a) * b
        empty += n % a
        answer += coke
        if coke + empty >= a:
            n = coke + empty
            empty = 0
            continue
        else:
            break

    return answer

print(solution(2,1,20), 19)
print(solution(3,1,20), 9)
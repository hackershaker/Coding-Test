def solution(n, stations, w):
    answer = 0
    minnum = 1

    for s in sorted(stations):
        print("minnum : ", minnum, "answer", answer)
        if s - w <= minnum:
            pass
        else:
            answer += -(-(s - w - minnum) // (2 * w + 1))

        minnum = s + w + 1
    if minnum <= n:
        answer += -(-(n - minnum + 1) // (2 * w + 1))
    print("minnum : ", minnum, "answer", answer)

    return answer


print(solution(11, [4, 11], 1), 3)
print(solution(16, [9], 2), 3)
print(solution(15, [1], 3), 2)

from functools import reduce


def solution(n):
    answer = []
    for i in range(n):
        answer.append([0] * (i + 1))

    k = 0
    r, c, curnum = 0, 0, 1
    while curnum <= n * (n + 1) / 2:
        while True:
            try:
                if answer[r][c] == 0:
                    answer[r][c] = curnum
                    r += 1
                    curnum += 1
                else:
                    r -= 1
                    break
            except:
                r -= 1
                break
        print(answer, r, c, curnum)
        c += 1

        while True:
            try:
                if answer[r][c] == 0:
                    answer[r][c] = curnum
                    c += 1
                    curnum += 1
                else:
                    c -= 1
                    break
            except:
                c -= 1
                break
        print(answer, r, c, curnum)
        r -= 1
        c -= 1

        while True:
            try:
                if answer[r][c] == 0:
                    answer[r][c] = curnum
                    r -= 1
                    c -= 1
                    curnum += 1
                else:
                    r += 1
                    c += 1
                    break
            except:
                break

        r += 1
        k += 1

        print(answer, r, c, curnum)

    answer = reduce(lambda x, y: x + y, answer)
    return answer


print(solution(4), [1, 2, 9, 3, 10, 8, 4, 5, 6, 7])
print(solution(5), [1, 2, 12, 3, 13, 11, 4, 14, 15, 10, 5, 6, 7, 8, 9])
# print(solution(6), [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11])

def solution(score):
    avg = []
    avgdic = {}
    for x in score:
        avg.append(sum(x) / 2)
    avg.sort(reverse=True)

    for i in range(len(avg)):
        if str(avg[i]) in avgdic.keys():
            continue
        avgdic[str(avg[i])] = i + 1

    for i in range(len(score)):
        score[i] = avgdic[str(sum(score[i]) / 2)]

    return score


print(
    solution(
        [[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]
    ),
    [4, 4, 6, 2, 2, 1, 7],
)
print(solution([[80, 70], [80, 80], [90, 90], [90, 100]]), [4, 3, 2, 1])
print(solution([[80, 70]]), [1])
print(solution([[70, 90], [80, 80], [90, 100], [90, 100]]), [3, 3, 1, 1])
print(solution([[0, 0], [80, 80], [20, 30], [90, 100]]), [4, 2, 3, 1])
print(solution([[0, 0], [0, 0], [0, 0], [90, 100]]), [2, 2, 2, 1])
print(
    solution([[14, 71], [24, 72], [13, 53], [72, 42], [45, 32], [12, 78], [45, 78]]),
    [4, 4, 6, 2, 2, 1, 7],
)

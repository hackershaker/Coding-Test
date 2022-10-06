from collections import Counter


def solution(arr):
    answer = []

    def quadPress(arr, answer=answer):
        if len(arr[0]) == 1:
            for ar in arr:
                answer += ar
            return
        line = int(len(arr) / 2)
        arrup = arr[:line]
        arrdown = arr[line:]

        arrul, arrur, arrdl, arrdr = [], [], [], []
        for ar in arrup:
            arrul.append(ar[:line])
            arrur.append(ar[line:])
        for ar in arrdown:
            arrdl.append(ar[:line])
            arrdr.append(ar[line:])

        arrsum = 0
        for ar in arr:
            arrsum += sum(ar)

        if arrsum == len(arr) ** 2:
            answer.append(1)
        elif arrsum == 0:
            answer.append(0)
        else:
            for division in arrul, arrur, arrdl, arrdr:
                quadPress(division)

    quadPress(arr)
    counter = Counter(answer)
    return [counter[0], counter[1]]


print(solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]))
print(
    solution(
        [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 1, 1, 1, 1],
            [0, 1, 0, 0, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1, 0, 0, 1],
            [0, 0, 0, 0, 1, 1, 1, 1],
        ]
    )
)
print(solution([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]))
print(solution([[1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]]))
print(solution([[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]]))
print(solution([[1]]))
print(solution([[1, 1], [1, 0]]))
print(solution([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]))

def solution2(sizes):
    sizes.sort(key=lambda x: (x[0], x[0] * x[1]))
    print((map(list, zip(*sizes))))
    widthcolumn = list(map(list, zip(*sizes)))[0]
    heightcolumn = list(map(list, zip(*sizes)))[1]

    while True:
        beforewcol = widthcolumn
        maxwidx = widthcolumn.index(max(widthcolumn))
        maxhidx = heightcolumn.index(max(heightcolumn))
        if heightcolumn[maxwidx] < max(widthcolumn) and max(widthcolumn) < max(
            heightcolumn
        ):
            temp = widthcolumn[maxwidx]
            widthcolumn[maxwidx] = heightcolumn[maxwidx]
            heightcolumn[maxwidx] = temp

        if widthcolumn[maxhidx] < max(heightcolumn) and max(heightcolumn) < max(
            widthcolumn
        ):
            temp = widthcolumn[maxhidx]
            widthcolumn[maxhidx] = heightcolumn[maxhidx]
            heightcolumn[maxhidx] = temp
        if beforewcol == widthcolumn:
            break

    print(widthcolumn, heightcolumn)
    return max(widthcolumn) * max(heightcolumn)


import math, copy
from itertools import permutations


def solution3(sizes):
    answer = math.inf

    widthcol = list(zip(*sizes))[0]
    heightcol = list(zip(*sizes))[1]

    for p in permutations(heightcol):
        print(p)

    return answer


def solution(sizes):
    for i in range(len(sizes)):
        if sizes[i][1] > sizes[i][0]:
            temp = [sizes[i][1], sizes[i][0]]
            sizes[i] = temp

    sizes.sort(key=lambda x: x[0])
    # print(sizes)

    cols = list(zip(*sizes))

    return max(cols[0]) * max(cols[1])


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))

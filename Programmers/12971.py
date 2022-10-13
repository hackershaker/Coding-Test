def solution2(sticker):
    answer = 0

    stack = [[[0], sticker[0]], [[1], sticker[1]]]
    while stack:
        order = stack.pop()
        # print(order)
        for i in [order[0][-1] + 2, order[0][-1] + 3]:
            if order[0][0] == 0 and i == len(sticker)-1: continue
            elif i >= len(sticker):
                answer = max(answer, order[1])
                continue
            else:
                stack.append([order[0] + [i], order[1] + sticker[i]])

    return answer

# Dynamic Programming
from collections import deque
def solution(sticker):
    answer = 0
    deq = deque(sticker)

    def getMaxValue(n, deq):
        idx = deq.index(n)
        if idx == 0:
            deq.rotate(1)
            deq[0], deq[1], deq[2] = -1, -1, -1
        elif idx == len(deq)-1:
            deq.rotate(-1)
            deq[-1], deq[-2], deq[-3] = -1, -1, -1
        else:
            deq[idx-1], deq[idx], deq[idx+1] = -1, -1, -1


print(solution2([14, 6, 5, 11, 3, 9, 2, 10]), 36)
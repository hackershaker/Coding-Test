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
    dic = {}
    deq = deque(sticker)

    def zerocut(i):
        if i < 0: return 0
        return i

    def getMaxValue(list):
        maxvalue = 0
        stack = []
        for i in range(len(list)):
            stack.append([list[i], list[i+2:]+list[:zerocut(i-1)]])

        while stack:
            print(stack)
            pops, lefts = stack[-1]
            if len(lefts) == 0:
                dic[tuple(stack[-1])] = pops
            elif len(lefts) == 1:
                dic[tuple(stack[-1])] = pops + lefts[0]
            elif len(lefts) == 2:
                dic[tuple(stack[-1])] = pops + max(lefts)
            else:
                pass

            try:
                dic[tuple(stack[-1])] = pops + dic[tuple(lefts)]
                max(maxvalue, dic[tuple(stack[-1])])
                stack.pop()
            except:
                for i in range(len(lefts)):
                    stack.append([lefts[i], lefts[i+2:]+lefts[:zerocut(i-1)]])

        return maxvalue

    for i in range(len(sticker)):
        if i == 0: answer = max(answer, sticker[0] + getMaxValue(sticker[2:-1]))
        elif i == len(sticker)-1: answer = max(answer, sticker[-1] + getMaxValue(sticker[1:-2]))
        else: answer = max(answer, sticker[i] + getMaxValue(sticker[i+2:]+sticker[:i-1]))
    print(dic)
    return answer

print(solution([14, 6, 5, 11, 3, 9, 2, 10]), 36)
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
def solution3(sticker):
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
            stack.append([list[zerocut(i-1):i+2], list[i+2:]+list[:zerocut(i-1)]])

        k = 0
        while stack:
            print(stack[-1])
            print(dic)
            pops, lefts = stack[-1]
            key = frozenset(pops+lefts)
            if dic.get(key, None):
                stack.pop()
                continue

            if len(key) < 2:
                dic[key] = max(key)
                stack.pop()
                continue
            if len(key) == 3:
                dic[key] = max(key[1], key[0]+key[2])
                stack.pop()
                continue
            
            for i in range(len(lefts)):
                stack.append([lefts[zerocut(i-1):i+2], lefts[i+2:]+lefts[:zerocut(i-1)]])

            if k > 20: break
            k+=1

        return dic[tuple(list)]

    for i in range(len(sticker)):
        if i == 0: answer = max(answer, sticker[0] + getMaxValue(sticker[2:-1]))
        elif i == len(sticker)-1: answer = max(answer, sticker[-1] + getMaxValue(sticker[1:-2]))
        else: answer = max(answer, sticker[i] + getMaxValue(sticker[i+2:]+sticker[:i-1]))
    print(dic)
    return answer

def solution(sticker):
    maxvalue = 0
    dic = {frozenset([i]): sticker[i] for i in range(len(sticker))}

    stack = [{i} for i in range(len(sticker))]
    while stack:
        part = stack.pop()

        isEnd = True
        for i in range(len(sticker)):
            if i in part or (i-1+len(sticker))%len(sticker) in part or i+1 in part: continue
            dic[frozenset(part|{i})] = dic[frozenset(part)] + sticker[i]
            stack.append(part|{i})
            isEnd = False
        
        if isEnd:
            maxvalue = max(maxvalue, dic[frozenset(part)])
    print(dic)
    return maxvalue


print(solution([14, 6, 5, 11, 3, 9, 2, 10]), 36)
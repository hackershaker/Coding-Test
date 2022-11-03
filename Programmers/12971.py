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

def solution4(sticker):
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

def solution(sticker):
    answer = 0
    totalsum = sum(sticker)
    prior = [(idx, value) for idx, value in enumerate(sticker)]
    prior.sort(key=lambda x: -x[1])

    stack = [[prior, 0, sticker, sum(sticker)]]
    while stack:
        part, s, stic, total = stack.pop()
        
        if total == 0:
            answer = max(answer, s)
            break
        
        # print(part, s, total, stic)
        maxinfo = part[0]

        idxs = getIdx(maxinfo[0], stic)
        tearSticker = stic[idxs[1]] + stic[idxs[0]] + stic[idxs[2]]
        center = stic[idxs[1]]
        # sticker[idxs[1]] , sticker[idxs[0]] , sticker[idxs[2]] = 0, 0, 0
        stack.append([deleteList(idxs,part), s + center, zeroSticker(idxs, stic),total - tearSticker])
        if stic[idxs[1]] <= stic[idxs[0]]+stic[idxs[2]]:
            subidxs = getIdx(idxs[0], part)
            tearSticker = stic[subidxs[1]] + stic[subidxs[0]] + stic[subidxs[2]]
            center = stic[subidxs[1]]
            # sticker[subidxs[1]] , sticker[subidxs[0]] , sticker[subidxs[2]] = 0, 0, 0
            stack.append([deleteList(subidxs,part), s + center, zeroSticker(subidxs, stic), total - tearSticker])

    return answer

def getIdx(idx, part):
    leftidx = (idx-1+len(part))%len(part)
    rightidx = (idx+1)%len(part)

    return leftidx, idx, rightidx

def deleteList(indexes, l):
    newlist = [x for x in l if x[0] not in indexes]
    return newlist

def zeroSticker(indexes, sticker):
    part = [sticker[i] if i not in indexes else 0 for i in range(len(sticker))]
    return part


print(solution([14, 6, 5, 11, 3, 9, 2, 10]), 36) # 6, 11, 9, 10
print(solution([14, 6, 9, 11, 10, 5, 11, 10]), 36) # 6, 11, 9, 10
print(solution([1, 3, 2, 5, 4]), 8) # 3, 5
print(solution([4,3,2,1,2,3,4]), 9) # 4, 2, 3
print(solution([4,3,2,1,3,2,4]), 10) # 4, 3, 3
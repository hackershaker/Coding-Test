from collections import defaultdict
from heapq import heappush, heappop
def solution(X, Y):
    answer = ''
    dicY = defaultdict(int)
    heap = []
    for number in str(Y):
        dicY[number] += 1

    for num in str(X):
        if dicY[num] != 0:
            heappush(heap, (-int(num), int(num)))
            dicY[num] -= 1
        else:
            continue
    # print(heap)
    
    if len(heap) == 0: return "-1"
    elif heap[0][1] == 0: return "0"
    else:
        while heap:
            answer += str(heappop(heap)[1])
        return answer


print(solution("100", "2345"), "-1")
print(solution("100", "203045"), "0")
print(solution("100", "123450"), "10")
print(solution("5525", "1255"), "552")
def solution2(gems):  # 시간초과
    gemkind = len(set(gems))
    print(gemkind)

    def ispossiDle(k):
        pos = False
        for i in range(0, len(gems) - k + 1):
            if len(set(gems[i : i + k])) == gemkind:
                answer.append([i + 1, i + k])
                pos = True
                break
        return pos

    start = 1
    end = len(gems)
    answer = []
    while True:
        print(start, end)
        if start == end:
            answer = []
            ispossible(start)
            break
        answer = []
        mid = int((start + end) / 2)

        if ispossible(mid):
            end = mid
        else:
            start = mid + 1
    print(answer)
    return answer[0]


# two-pointer 활용
from collections import deque


def solution3(gems):
    answer = []
    gemkind = len(set(gems))
    start, end = 0, 0

    deq = deque([gems[0]])
    sets = set(deq)
    while True:
        if len(sets) != gemkind:
            end += 1
            deq.append(gems[end])
            sets.add(gems[end])
        else:
            popattr = deq.popleft()
            if len(set(deq)) != gemkind:
                answer = [start + 1, end + 1]
                break
            else:
                start += 1
    return answer


from collections import deque, Counter


def solution(gems):  # 이진탐색 + sliding window
    answer = []
    l = len(set(gems))
    start, end = l, len(gems)
    bestidx = [0, len(gems) - 1]

    def windowSlide(k):
        deq = deque(gems[bestidx[0] : bestidx[0] + k])
        deqdic = dict(Counter(deq))
        idx = bestidx[0] + k - 1
        while True:
            # print(deq, deqdic)
            try:
                if len(deqdic) == l:
                    bestidx[0], bestidx[1] = idx - mid + 1, idx
                    return True, [idx + 2 - k, idx + 1]
                else:
                    for _ in range(l - len(set(deqdic))):
                        element = deq.popleft()
                        deqdic[element] -= 1
                        if deqdic[element] == 0:
                            deqdic.pop(element)
                        deq.append(gems[idx + 1])
                        try:
                            deqdic[gems[idx + 1]] += 1
                        except:
                            deqdic[gems[idx + 1]] = 1
                        idx += 1
            except:
                break
        return False, []

    while True:
        mid = int((start + end) / 2)
        # print(start, mid, end, bestidx)
        if start == end:
            _, answer = windowSlide(start)
            break
        isp, temp = windowSlide(mid)
        # print(isp, temp)
        if temp != []:
            answer = temp
        if isp:
            end = mid
        else:
            start = mid + 1

    return answer


import random, string

print(
    solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]),
    [3, 7],
)
print(solution(["B", "A", "B", "A", "C"]), [3, 5])
print(solution(["A", "E", "B", "A", "D"]), [2, 5])
print(solution(["C", "E", "B", "A", "D"]), [1, 5])
print(solution(["D", "C", "E", "B", "A", "D"]), [1, 5])
print(solution(["A", "A", "B", "A", "A", "C"]), [3, 6])
print(solution(["A", "C", "A", "B", "C", "B"]), [2, 4])
print(solution(["A", "C", "AB", "B", "C", "B"]), [1, 4])
print(solution(["A", "A", "A", "A", "A", "D"]), [5, 6])
print(solution(["A", "A", "A", "B", "B", "D"]), [3, 6])
print(solution(["A", "A", "A", "B", "B", "B"]), [3, 4])
print(solution(["A", "A", "A", "B", "B"]), [3, 4])
print(solution(["A", "B", "C", "A", "B", "C", "D"]), [4, 7])
print(solution(["C", "A", "A", "A", "A", "B"]), [1, 6])
print(solution(["A", "B", "C", "A", "D", "B", "E", "D", "C", "B", "A"]), [3, 7])
print(solution(["C"]), [1, 1])
print(solution(["C", "C"]), [1, 1])
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "ZZZ"]), [1, 3])
print(solution(["A", "B", "B", "B", "B", "B", "B", "C", "B", "A"]), [8, 10])
print(
    solution(["A", "A", "B", "B", "B", "B", "B", "C", "B", "A", "C", "B", "B", "A"]),
    [8, 10],
)

print(solution(["A"] * 50000 + ["B"] * 50000), [50000, 50001])
print(solution(["A", "B", "C"] * 33333 + ["B"]), [1, 3])
print(solution(["A", "B", "C"] * 33332 + ["A", "B", "C", "D"]), [99997, 100000])
print(
    solution(
        ["AAAAAAAAAA", "BBBBBBBBBB", "CCCCCCCCCC", "DDDDDDDDDD"] * 6249
        + ["EEEEEEEEEE", "FFFFFFFFFF", "GGGGGGGGGG", "HHHHHHHHHH"]
        + ["AAAAAAAAAA", "BBBBBBBBBB", "CCCCCCCCCC", "DDDDDDDDDD"] * 6250
    ),
    [99997, 100000],
)
print(
    solution(
        [
            "".join(random.choices(string.ascii_uppercase, k=random.randint(9, 10)))
            for _ in range(99995)
        ]
        + ["A", "B", "C", "D", "E"]
    ),
    [1, 100000],
)

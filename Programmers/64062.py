def solution2(stones, k):
    class segmentTree:
        def __init__(self, arr):
            self.arr = arr
            self.length = len(arr)
            self.dic = {}
            self.init(1, 0, len(arr) - 1)

        def init(self, node, start, end):
            mid = int((start + end) / 2)
            if start == end:
                self.dic[node] = self.arr[start]
                return self.dic[node]

            self.dic[node] = self.init(node * 2, start, mid) + self.init(
                node * 2 + 1, mid + 1, end
            )
            return self.dic[node]

        def getSum(self, start, end, node, left, right):
            mid = int((start + end) / 2)
            if right < start or end < left:
                return 0
            elif left <= start and end <= right:
                return self.dic[node]
            else:
                return self.getSum(start, mid, node * 2, left, right) + self.getSum(
                    mid + 1, end, node * 2 + 1, left, right
                )

        def update(self, start, end, node, idx, value):
            mid = int((start + end) / 2)
            if idx < start or idx > end:
                pass
            if start <= idx and idx <= end:
                self.dic[node] += value
                if self.dic[node] < 0:
                    self.dic[node] = 0
            if start == end:
                return

            return self.update(start, mid, node * 2, idx, value), self.update(
                mid + 1, end, node * 2 + 1, idx, value
            )

    answer = 0
    segTree = segmentTree(stones)
    l = len(stones)
    available = True
    while True:
        for i in range(l - k + 1):
            if segTree.getSum(0, l - 1, 1, i, i + k - 1) == 0:
                available = False
                break
        else:
            answer += 1

        if available == False:
            break

        for i in range(l):
            if stones[i] == 0:
                continue
            else:
                stones[i] -= 1
                segTree.update(0, l - 1, 1, i, -1)
        # print(stones)
        # print(segTree.dic)

    return answer


def solution3(stones, k):
    import sys

    sys.setrecursionlimit(10 ** 9)

    def leftsearch(stone, num, answer):
        if stone[0] - 1 >= 0 and stones[stone[0] - 1] <= num:
            answer += leftsearch((stone[0] - 1, stones[stone[0] - 1]), num, answer) + 1
            return answer
        else:
            return 0

    def rightsearch(stone, num, answer):
        if stone[0] + 1 <= len(stones) - 1 and stones[stone[0] + 1] <= num:
            answer = rightsearch((stone[0] + 1, stones[stone[0] + 1]), num, answer) + 1
            return answer
        else:
            return 0

    def search(stone, num, answer):
        answer += leftsearch(stone, num, answer)
        answer += rightsearch(stone, num, answer)
        return answer + 1

    sorts = sorted(enumerate(stones), key=lambda x: x[1])

    answer = 0
    for s in sorts:
        answer = search(s, s[1], answer)
        if answer >= k:
            answer = s[1]
            break
        else:
            answer = 0
    # print(search(stones[3], stones[3][1], 0))

    return answer


def solution(stones, k):
    def checkValid(people):
        num = 0
        for s in stones:
            if s < people:
                num += 1
            else:
                num = 0
            if num >= k:
                return False
        return True

    start = 0
    end = 200200000
    maxpeople = 0
    while True:
        # print(start, end)
        if start == end:
            break
        mid = int((start + end) / 2)
        if checkValid(mid) == False:
            end = mid
        else:
            maxpeople = max(maxpeople, mid)
            start = mid + 1

    return maxpeople


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3), 3)
print(solution([5, 2, 3, 4, 1], 4), 4)
print(solution([1, 3, 4, 6, 2, 4, 5], 2), 3)
print(solution([1, 2, 1, 1, 2, 1, 2], 2), 3)
print(solution([3, 3, 3, 3, 3], 2), 3)

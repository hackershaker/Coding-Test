import sys


class Solution:
    def __init__(self):
        self.n = int(sys.stdin.readline().strip())
        self.arr = list(map(int, sys.stdin.readline().strip().split(" ")))
        self.total = int(sys.stdin.readline().strip())

    def solution(self):
        if sum(self.arr) <= self.total:
            print(max(self.arr))
            return
        start, end = 1, self.total
        while start < end:
            mid = (start + end) // 2 + 1
            budget = sum([min(mid, x) for x in self.arr])
            if budget <= self.total:
                start = mid
            else:
                end = mid - 1
        print(start)


if __name__ == "__main__":
    s = Solution()
    s.solution()

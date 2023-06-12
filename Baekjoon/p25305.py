from heapq import heapify, heappop
import sys


class Solution:
    def __init__(self):
        self.n, self.k = map(int, sys.stdin.readline().strip().split(" "))
        self.score = map(int, sys.stdin.readline().strip().split(" "))

    def solution(self):
        heap = list(map(lambda x: -x, self.score))
        heapify(heap)
        for _ in range(self.k - 1):
            heappop(heap)
        print(-heap[0])


if __name__ == "__main__":
    s = Solution()
    s.solution()

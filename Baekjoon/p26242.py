from heapq import heappop, heappush
import sys


class Solution:
    def __init__(self):
        self.n, self.k = map(int, sys.stdin.readline().strip().split(" "))
        self.caught = list(map(int, sys.stdin.readline().strip().split(" ")))
        self.answer = []

    def solution(self):
        heap = []
        total = 0
        for karmon in self.caught:
            if len(heap) < self.k:
                heappush(heap, karmon)
                total += karmon
            else:
                if heap[0] < karmon:
                    total = total - heappop(heap) + karmon
                    heappush(heap, karmon)

            if len(heap) == self.k:
                self.answer.append(total)

        print(" ".join(map(str, self.answer)))


if __name__ == "__main__":
    s = Solution()
    s.solution()

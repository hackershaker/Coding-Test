from collections import deque
from heapq import heappop, heappush
import sys


class Solution:
    @classmethod
    def solution(cls):
        n, m = map(int, sys.stdin.readline().strip().split(" "))
        heap = []
        priority = list(map(int, sys.stdin.readline().strip().split(" ")))
        for prior in priority:
            heappush(heap, -prior)

        priority = deque(priority)
        answer = 0
        while priority:
            if -heap[0] == priority[0]:
                if m == 0:
                    print(answer + 1)
                    return
                heappop(heap)
                priority.popleft()
                answer += 1
                m -= 1
            else:
                priority.rotate(-1)
                m = m - 1 if m > 0 else len(priority) - 1


if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        Solution.solution()

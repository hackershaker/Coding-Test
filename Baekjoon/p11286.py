from heapq import heappop, heappush
import sys


class Solution:
    def solution(self):
        n = int(sys.stdin.readline().strip())
        heap = []
        for _ in range(n):
            x = int(sys.stdin.readline().strip())
            if not x:
                if not heap:
                    sys.stdout.write("0\n")
                    continue
                sys.stdout.write(str(heappop(heap)[1]) + "\n")
            else:
                heappush(heap, (abs(x), x))


if __name__ == "__main__":
    s = Solution()
    s.solution()

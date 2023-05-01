from collections import defaultdict
from heapq import heappop, heappush
import sys


class Solution:
    def solution(self):
        v, e = map(int, sys.stdin.readline().strip().split(" "))
        k = int(sys.stdin.readline().strip())
        dic = defaultdict(lambda: defaultdict(lambda: float("inf")))
        for _ in range(e):
            i, j, w = map(int, sys.stdin.readline().strip().split(" "))
            dic[i][j] = min(dic[i][j], w)

        visited = set()
        memo = defaultdict(lambda: float("inf"))
        memo[k] = 0
        stack = []
        heappush(stack, (memo[k], k))
        while stack:
            dis, node = heappop(stack)
            if node in visited:
                continue
            visited.add(node)
            for nextnode in dic[node]:
                if memo[nextnode] > memo[node] + dic[node][nextnode]:
                    memo[nextnode] = memo[node] + dic[node][nextnode]
                heappush(stack, (memo[nextnode], nextnode))

        for i in range(1, v + 1):
            sys.stdout.write(str(memo[i]).upper() + "\n")


if __name__ == "__main__":
    s = Solution()
    s.solution()

from collections import defaultdict, deque
import sys


class Solution:
    def __init__(self):
        self.n, self.m = map(int, sys.stdin.readline().strip().split(" "))
        self.dic = defaultdict(list)
        for _ in range(self.m):
            a, b = sys.stdin.readline().strip().split(" ")
            self.dic[a].append(b)
            self.dic[b].append(a)
        self.minBacon = float("inf")
        self.answer = 0

    def solution(self):
        for i in range(1, self.n + 1):
            result = 0
            stack = deque([(str(i), 0)])
            visited = set()
            while stack:
                node, distance = stack.popleft()
                visited.add(node)
                result += distance
                for nextnode in self.dic[node]:
                    if nextnode in visited:
                        continue
                    stack.append((nextnode, distance + 1))
                    visited.add(nextnode)
            if result < self.minBacon:
                self.minBacon = result
                self.answer = i
        print(self.answer)


if __name__ == "__main__":
    s = Solution()
    s.solution()

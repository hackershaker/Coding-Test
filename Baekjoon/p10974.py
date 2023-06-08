from collections import deque
import sys


class Solution:
    def __init__(self):
        self.n = int(sys.stdin.readline().strip())

    def solution(self):
        stack = deque([[i] for i in range(1, self.n + 1)])
        while stack:
            node = stack.popleft()
            if len(node) == self.n:
                print(" ".join(map(str, node)))
            for k in range(1, self.n + 1):
                if k not in node:
                    newnode = node + [k]
                    stack.append(newnode)


if __name__ == "__main__":
    s = Solution()
    s.solution()

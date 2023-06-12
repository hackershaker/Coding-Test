from collections import deque
import sys


class Solution:
    def solution(self):
        n, m = map(int, sys.stdin.readline().strip().split(" "))
        stack = deque([[i] for i in range(1, n + 1)])
        while stack:
            seq = stack.popleft()
            if len(seq) == m:
                print(" ".join(map(str, seq)))
                continue
            for i in range(1, n + 1):
                stack.append(seq + [i])


if __name__ == "__main__":
    s = Solution()
    s.solution()

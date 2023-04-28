import sys


class Solution:
    def solution(self):
        n = int(sys.stdin.readline().strip())
        for i in range(1, n + 1):
            print(" " * (n - i) + "*" * (2 * i - 1))
        for i in range(n + 1, 2 * n):
            print(" " * (i - n) + "*" * (2 * n - 1 - 2 * (i - n)))


if __name__ == "__main__":
    s = Solution()
    s.solution()

import sys


class Solution:
    def solution(self):
        n = int(sys.stdin.readline().strip())
        for i in range(1, n + 1):
            print("*" * i + " " * (2 * n - i * 2) + "*" * i)
        for i in range(n - 1, -1, -1):
            print("*" * i + " " * (2 * n - i * 2) + "*" * i)


if __name__ == "__main__":
    s = Solution()
    s.solution()

import sys


class Solution:
    def solution(self):
        n = int(sys.stdin.readline().strip())
        for i in range(1, 2 * n):
            if i <= n:
                sys.stdout.write(" " * (i - 1) + "*" * (2 * (n - i) + 1) + "\n")
            else:
                sys.stdout.write(" " * (2 * n - i - 1) + "*" * (2 * (i - n) + 1) + "\n")


if __name__ == "__main__":
    s = Solution()
    s.solution()

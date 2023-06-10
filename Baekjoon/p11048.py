import sys


class Solution:
    def __init__(self):
        self.n, self.m = map(int, sys.stdin.readline().strip().split(" "))
        self.maze = [
            list(map(int, sys.stdin.readline().strip().split(" ")))
            for _ in range(self.n)
        ]

    def solution(self):
        dp = [[0] * (self.m + 1) for _ in range(self.n + 1)]
        for i in range(1, self.n + 1):
            for j in range(1, self.m + 1):
                dp[i][j] = (
                    max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                    + self.maze[i - 1][j - 1]
                )
        print(dp[-1][-1])


if __name__ == "__main__":
    s = Solution()
    s.solution()

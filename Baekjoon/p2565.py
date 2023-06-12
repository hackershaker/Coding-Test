from pprint import pprint
import sys


class Solution:
    def __init__(self):
        self.n = int(sys.stdin.readline().strip())
        self.loc = [
            list(map(int, sys.stdin.readline().strip().split(" ")))
            for _ in range(self.n)
        ]
        self.pole = max(map(max, self.loc))

    def solution(self):
        dp = [[0] * (self.pole + 1) for _ in range(self.pole + 1)]
        for a, b in self.loc:
            dp[a][b] += 1
        for i in range(1, self.pole + 1):
            for j in range(1, self.pole + 1):
                dp[i][j] += max(dp[i - 1][j], dp[i][j - 1])
        print(self.n - dp[self.pole][self.pole])


if __name__ == "__main__":
    s = Solution()
    s.solution()

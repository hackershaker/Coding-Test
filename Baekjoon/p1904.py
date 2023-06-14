import sys


class Solution:
    def solution(self):
        n = int(sys.stdin.readline().strip())
        dp = [1,2]
        for _ in range(3, n + 1):
            dp.append((dp[- 1] + dp[- 2])%15746)
        print(dp[n-1])


if __name__ == "__main__":
    s = Solution()
    s.solution()

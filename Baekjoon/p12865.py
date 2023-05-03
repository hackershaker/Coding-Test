import sys


class Solution:
    def solution(self):
        n, k = map(int, sys.stdin.readline().strip().split(" "))
        items = [
            list(map(int, sys.stdin.readline().strip().split(" "))) for _ in range(n)
        ]  # [무게, 가치]

        dp = [0] * (k + 1)  # dp[i]: 배낭의 무게가 i 일때 가치의 최댓값
        for item in items:
            for i in range(k - item[0], -1, -1):
                dp[i + item[0]] = max(dp[i + item[0]], dp[i] + item[1])
            # print(dp)
        answer = max(dp)
        sys.stdout.write(str(answer) + "\n")


if __name__ == "__main__":
    s = Solution()
    s.solution()

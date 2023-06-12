class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        n = len(str(k))

        for i in range(len(s)):
            for j in range(i, -1, -1):
                if i-j+1 > n:
                    break
                target = s[j : i + 1]
                if target[0] != '0' and int(target) <= k:
                    dp[i + 1] += dp[j]
                else:
                    continue
        return dp[len(s)] % (10**9+7)

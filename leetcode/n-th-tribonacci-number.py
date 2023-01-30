# dp 이용



class Solution:
    def tribonacci(self, n: int) -> int:
        memo = [0,1,1]

        while len(memo) < n+1:
            memo.append(memo[-1]+memo[-2]+memo[-3])

        return memo[n]
from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}
        # 0:alice, 1:Bob
        def getMaxValue(info) -> tuple:
            if info in memo:
                return memo[info]
            who, m, start = info
            result = (0, 0)
            if start >= len(piles):
                memo[info] = result
                return result
            for i in range(1, min(2 * m + 1, len(piles) - start + 1)):
                stone = prefixSum[start + i] - prefixSum[start]
                dic = getMaxValue(((who + 1) % 2, max(i, m), start + i))
                if dic[who] + stone > result[who]:
                    result = [dic[0], dic[1]]
                    result[who] += stone
                    result = tuple(result)
            memo[info] = result
            return result

        prefixSum = [0]
        for pile in piles:
            prefixSum.append(prefixSum[-1] + pile)
        answer = getMaxValue((1, 1, 0))

        return answer[1]

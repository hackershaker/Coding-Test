from functools import lru_cache
from typing import List


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        @lru_cache(maxsize=None)
        def minimumCut(interval: tuple, cutIdx: tuple):
            if cutIdx[0] == cutIdx[1]:
                return interval[1] - interval[0]
            if cutIdx[0] > cutIdx[1]:
                return 0

            return (
                interval[1]
                - interval[0]
                + min(
                    [
                        minimumCut((interval[0], cuts[i]), (cutIdx[0], i - 1))
                        + minimumCut((cuts[i], interval[1]), (i + 1, cutIdx[1]))
                        for i in range(cutIdx[0], cutIdx[1] + 1)
                    ]
                )
            )

        cuts.sort()
        return minimumCut((0, n), (0, len(cuts) - 1))

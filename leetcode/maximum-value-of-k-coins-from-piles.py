from typing import Any, List


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        # O(kn)
        sumPiles: List[List[Any]] = [[0] for _ in range(len(piles) + 1)]
        for i in range(1, len(sumPiles)):
            for j in range(1, k + 1):
                if j <= len(piles[i - 1]):
                    sumPiles[i].append(sumPiles[i][j - 1] + piles[i - 1][j - 1])
                else:
                    sumPiles[i].append(sumPiles[i][j - 1])
        # O(kn)
        table = [[0 for j in range(k + 1)] for i in range(len(piles) + 1)]
        # table[i][j]: max value of sum when popped j element in first i stack
        # O(k^2*n)
        for i in range(1, len(table)):
            for j in range(1, k + 1):
                compareArray = [
                    table[i - 1][j - m] + sumPiles[i][m]
                    for m in range(min(j + 1, len(piles[i - 1]) + 1))
                ]
                table[i][j] = max(compareArray)

        return table[len(piles)][k]

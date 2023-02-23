from heapq import heappop, heappush


# Greedy Solution
class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        minimumCapital = []
        for profit, cost in zip(profits, capital):
            heappush(minimumCapital, (cost, profit))
        # print(minimumCapital)
        maximumProfit = []
        while k > 0:
            while minimumCapital:
                cost, profit = minimumCapital[0]
                if cost > w:
                    break
                cost, profit = heappop(minimumCapital)
                heappush(maximumProfit, (-profit, cost))
            # print(maximumProfit)
            if not maximumProfit:
                break
            p, _ = heappop(maximumProfit)
            w += -p
            k -= 1

        return w

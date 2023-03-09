from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, 10**13
        while start < end:
            mid = int((start + end) / 2)
            time = 0
            for pile in piles:
                time += ceil(pile / mid)

            if h < time:
                start = mid + 1
            else:
                end = mid
        return end

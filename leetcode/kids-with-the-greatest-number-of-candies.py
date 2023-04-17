class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxValue = max(candies)
        result = [candy+extraCandies >= maxValue for candy in candies]
        return result
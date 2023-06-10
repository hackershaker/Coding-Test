class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        start, end = 1, 10**9
        while start < end:
            mid = (start + end) // 2 + 1
            # print(start, mid, end)
            lowerBound, UpperBound = self.sumArray(n, index, mid), mid * n
            # print(lowerBound, UpperBound)
            if lowerBound <= maxSum <= UpperBound:
                start = mid
            elif UpperBound < maxSum:
                start = mid + 1
            else:
                end = mid - 1
        return start

    def sumArray(self, n, idx, value):
        k = max(value - idx - 1, 0)
        l = max(idx + 1 - value, 0)
        a = max(value - n + idx, 0)
        b = max(n - idx - value, 0)
        return (
            (value * (value + 1))
            - value
            - (k * (k + 1)) // 2
            + l
            - (a * (a + 1)) // 2
            + b
        )


s = Solution()
print(s.maxValue(4, 0, 4))

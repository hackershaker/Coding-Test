class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        prefixSum = [0]
        for sat in satisfaction:
            prefixSum.append(prefixSum[-1] + sat)
        # print(prefixSum)

        total = 0
        for i, sat in enumerate(satisfaction):
            total += (i + 1) * sat
        # print(total)

        maxLTC = total
        for i in range(len(prefixSum)):
            total -= prefixSum[-1] - prefixSum[i]
            maxLTC = max(maxLTC, total)

        return maxLTC

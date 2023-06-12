class Solution:
    def average(self, salary: List[int]) -> float:
        minV, maxV = 10**6, 1000
        total = 0
        for sal in salary:
            minV = min(minV, sal)
            maxV = max(maxV, sal)
            total += sal

        return (total - minV - maxV) / (len(salary) - 2)

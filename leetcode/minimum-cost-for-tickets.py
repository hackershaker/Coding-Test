from typing import List

# Using DP
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dic = {0: 0}

        for i in range(1, len(days) + 1):
            case1 = costs[0] + dic[i - 1]
            start, mid, end = 0, 0, len(days) - 1
            while start < end:
                mid = int((start + end) / 2)
                if days[i - 1] - days[mid] < 7:
                    end = mid
                else:
                    start = mid + 1
            case2 = costs[1] + dic[start]
            start, mid, end = 0, 0, len(days) - 1
            while start < end:
                mid = int((start + end) / 2)
                if days[i - 1] - days[mid] < 30:
                    end = mid
                else:
                    start = mid + 1
            case3 = costs[2] + dic[start]
            dic[i] = min(case1, case2, case3)

        return dic[len(days)]

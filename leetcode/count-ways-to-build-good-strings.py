from collections import defaultdict


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dic = defaultdict(int)
        dic[zero] += 1
        dic[one] += 1
        for i in range(1, high + 1):
            dic[i] += dic[i - one] + dic[i - zero]

        return sum([dic[k] for k in range(low, high + 1)]) % (10**9 + 7)

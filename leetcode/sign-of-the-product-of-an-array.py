from functools import reduce
from operator import mul


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        num = reduce(mul, nums, 1)
        if num > 0:
            return 1
        elif num < 0:
            return -1
        else:
            return 0

class Solution:
    def rob(self, nums: List[int]) -> int:
        dic = {0:0, 1:nums[0]}

        for i in range(2, len(nums)+1):
            dic[i] = max(nums[i-1]+dic[i-2], dic[i-1])

        return dic[len(nums)]
# brute force를 이용해 모든 경우의 수 계산
# 중복되는 경우의 수를 거르기 위해 set사용


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        temp = set()

        for i in range(len(nums)):
            newtemp = set()
            for subsequence in temp:
                if subsequence[-1] <= nums[i]:
                    newtemp.add(subsequence + (nums[i],))
                if len(subsequence) >= 2:
                    newtemp.add(subsequence)

            for j in range(i):
                if nums[j] <= nums[i]:
                    seq = (nums[j], nums[i])
                    if seq not in newtemp: newtemp.add(seq)
                
            temp = newtemp

        return [list(x) for x in temp]
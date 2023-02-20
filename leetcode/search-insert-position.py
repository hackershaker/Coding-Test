class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        while start < end:
            mid = int((start + end) / 2)

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:  # nums[mid] > target
                end = mid

        return start

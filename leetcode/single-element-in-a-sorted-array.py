class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1

        while start < end:
            mid = int((start + end) / 2)
            # start index and end index of same number pair
            # elementStart + 1 = elementEnd
            elementStart, elementEnd = 0, 0
            # find appropriate elementStart and elementEnd
            if mid != 0 and nums[mid - 1] == nums[mid]:
                elementStart = mid - 1
                elementEnd = mid
            elif mid != len(nums) - 1 and nums[mid] == nums[mid + 1]:
                elementStart = mid
                elementEnd = mid + 1
            else:
                return nums[mid]
            # if element number before elementStart is even
            # there is no single element
            # so set start to elementEnd
            if (elementStart - start) % 2 == 0:
                start = elementEnd + 1
            # otherwise there is single element before elementStart
            # so set end to elementStart
            else:
                end = elementStart - 1
        # after binary search, start and end meet at single element
        return nums[start]

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range((len(nums)) // 2 - 1, -1, -1):
            self.heapify(nums, i, len(nums))
        for i in range(len(nums) - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.heapify(nums, 0, i)
        return nums

    def heapify(self, array, index, end):
        largest = index
        leftChild = index * 2 + 1
        rightChild = index * 2 + 2
        if leftChild < end and array[largest] < array[leftChild]:
            largest = leftChild
        if rightChild < end and array[largest] < array[rightChild]:
            largest = rightChild
        if index != largest:
            array[largest], array[index] = array[index], array[largest]
            self.heapify(array, largest, end)

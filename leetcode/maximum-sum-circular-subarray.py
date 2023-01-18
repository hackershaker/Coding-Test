# 누적합, dp이용
# dic[n] : 인덱스 0 부터 n까지 부분합 중 가장 큰 값
# 원형으로 이어진 배열은 (전체 합 - 가장 작은 구간 합)으로 구한다.


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        prefixSum = [0] * len(nums)
        prefixSum[0] = nums[0]
        for i in range(1, len(nums)):
            prefixSum[i] = prefixSum[i-1] + nums[i]

        dic = {0:prefixSum[0]}
        minPrefixSum = prefixSum[0]
        maxPrefixSum = prefixSum[0]
        minArraySum = prefixSum[0]

        for i in range(1, len(prefixSum)):
            dic[i] = max(dic[i-1], prefixSum[i]-minPrefixSum)
            minPrefixSum = min(minPrefixSum, prefixSum[i])
            maxPrefixSum = max(maxPrefixSum, prefixSum[i])
            minArraySum = min(minArraySum, prefixSum[i] - maxPrefixSum)
            
        return max(dic[len(nums)-1], prefixSum[-1]-minArraySum)
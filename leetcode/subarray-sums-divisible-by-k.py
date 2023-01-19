# 누적합 이용
# 전 index의 누적합 중 k로 나누었을 때 나머지가 같은 것들을 select


from collections import defaultdict


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        answer = 0
        prefixSum = [0]*len(nums)
        prefixSum[0] = nums[0]
        for i in range(1, len(nums)): prefixSum[i] = prefixSum[i-1]+nums[i]

        dic = defaultdict(int)

        for pfsum in prefixSum:
            r = pfsum % k
            if r == 0: answer += 1
            answer += dic[r]
            dic[r] += 1
        
        return answer
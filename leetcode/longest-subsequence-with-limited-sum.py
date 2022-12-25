# 합에 순서 고려 안 해도 됨 따라서 정렬하고 뽑아도 똑같은 효과.
# nums를 정렬 후 누적합으로 바꿈
# queries를 반복문으로 돌면서 queries[i] 보다 작은 누적합 중
# 가장 큰 누적값 선정
# nums는 정렬되어 있으므로 이분탐색 이용


from typing import List
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()

        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        print(nums)
        answer = []

        for q in queries:
            start = 0; end = len(nums)-1
            while start < end:
                mid = int((start+end)/2)
                
                if nums[mid] <= q:
                    start = mid+1
                if q < nums[mid]:
                    end = mid-1
            
            answer.append(start)

        return answer
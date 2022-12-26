# 각 인덱스에서 최대로 갈 수 있는 값 구함
# 최대로 갈 수 있는 값을 end에 갱신
# 만약 end값이 현재 인덱스보다 작으면
# 현재 인덱스로 갈 수 있는 방법이 없다는 뜻이므로 False 리턴
# 만약 end 값이 마지막 인덱스이면 True 리턴


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        start, end = 0, 0

        for i in range(len(nums)):
            if end < i: return False
            else:
                end = max(end, i+nums[i])
            
            if end >= len(nums)-1: return True
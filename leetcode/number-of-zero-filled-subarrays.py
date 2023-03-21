class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        answer = 0
        subarrayLen = 0
        for n in nums:
            if n == 0:
                subarrayLen += 1
            else:
                if subarrayLen > 0:
                    answer += int(subarrayLen * (subarrayLen + 1) / 2)
                subarrayLen = 0
        if subarrayLen > 0:
            answer += int(subarrayLen * (subarrayLen + 1) / 2)
        return answer

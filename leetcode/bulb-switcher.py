class Solution:
    def bulbSwitch(self, n: int) -> int:
        answer = 0
        i = 1
        while i**2 <= n:
            answer += 1
            i += 1
        return answer

# str1의 모든 divisor string을 gcdCandidate에 저장
# str2가 gcdCandidate로 나누어지는지 검사
# 나눠지는 string 중 가장 긴 stirng 반환


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcdCandidate = set()
        temp = ''; i = 0
        for i in range(len(str1)):
            temp += str1[i]
            if self.isDivisible(str1, temp): gcdCandidate.add(temp)
            i += 1
        
        answer = ''
        for c in gcdCandidate:
            if self.isDivisible(str2, c):
                answer = c if len(c) > len(answer) else answer
        
        return answer

    def isDivisible(self, x, r):
        if len(x) % len(r) != 0: return False
        i = 0

        while i < len(x):
            if x[i:i+len(r)] != r: return False
            i += len(r)
        return True
from collections import defaultdict


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a","e","i","o","u"}
        start, end = 0, k-1
        vowelNum = defaultdict(int)
        for i in range(0, k):
            if s[i] in vowels:
                vowelNum[ s[i]]+=1

        result = sum(vowelNum.values())
        if result == k:
            return result
        
        answer = result
        while True:
            start += 1
            end += 1
            if end >= len(s):
                break
            if s[start-1] in vowels:
                vowelNum[s[start-1]] -= 1
                result -= 1
                if vowelNum[s[start-1]] == 0:
                    del vowelNum[s[start-1]]
            
            if s[end] in vowels:
                vowelNum[s[end]] += 1
                result += 1
            
            answer = max(answer, result)
        return answer

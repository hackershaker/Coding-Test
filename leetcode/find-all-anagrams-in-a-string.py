# 알파벳 26개 카운팅하여 판별


from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        answer = set(); count = 0
        sCount, pCount = [0]*26, [0]*26

        for char in p:
            pCount[ord(char)-ord('a')] += 1

        for schar, pchar in zip(sCount, pCount):
            if schar == pchar: count += 1

        for i in range(len(s)):
            rightIndex = ord(s[i]) - ord('a')
            
            # window left side
            if i >= len(p):
                leftIndex = ord(s[i-len(p)]) - ord('a')
                sCount[leftIndex] -= 1
                if sCount[leftIndex] == pCount[leftIndex]: count += 1
                if sCount[leftIndex] == pCount[leftIndex]-1: count -= 1
            
            # window right side
            sCount[rightIndex] += 1
            if sCount[rightIndex] == pCount[rightIndex]: count += 1
            if sCount[rightIndex] == pCount[rightIndex]+1: count -= 1
            print(count)
            if count == 26: answer.add(i-len(p)+1)

        print(answer)
        return answer
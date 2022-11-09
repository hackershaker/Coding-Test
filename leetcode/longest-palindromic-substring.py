from collections import deque
class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ''
        stack = deque([ [i,i, s[i]] for i in range(len(s)) ] + [ [i,i+1, s[i]+s[i+1]] for i in range(len(s)-1) if s[i] == s[i+1]])

        while stack:
            start, end, palindrome = stack.popleft()
            leftidx = start - 1
            rightidx = end + 1
            if leftidx >= 0 and rightidx < len(s) and s[leftidx] == s[rightidx]:
                stack.append([leftidx, rightidx, s[leftidx]+palindrome+s[rightidx]])
            else:
                answer = palindrome if len(palindrome) > len(answer) else answer
        
        return answer


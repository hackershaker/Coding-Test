class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if not stack or c != "*":
                stack.append(c)
            if c == "*" and stack[-1] != "*":
                stack.pop()
        
        answer = "".join(stack)
        return answer
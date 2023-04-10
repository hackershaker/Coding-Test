class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if not stack:
                stack.append(p)
            elif p == ")" and stack[-1] == "(":
                stack.pop()
            elif p == "}" and stack[-1] == "{":
                stack.pop()
            elif p == "]" and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(p)
        return True if len(stack)==0 else False
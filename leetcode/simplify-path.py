class Solution:
    def simplifyPath(self, path: str) -> str:
        pathlist = path.split("/")

        stack = []
        for p in pathlist:
            if not p:
                continue
            elif p == ".":
                continue
            elif p == "..":
                if len(stack) >= 1:
                    stack.pop()
            else:
                stack.append("/" + p)
        if not stack:
            stack.append("/")

        return "".join(stack)

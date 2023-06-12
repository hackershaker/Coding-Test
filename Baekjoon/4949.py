class Solution:
    def solution(self):
        while True:
            line = input()
            if line == ".":
                return
            stack = []
            for s in line:
                if s == "[" or s == "(":
                    stack.append(s)
                elif s == ")":
                    if len(stack) == 0 or stack[-1] != "(":
                        print("no")
                        break
                    else:
                        stack.pop()
                elif s == "]":
                    if len(stack) == 0 or stack[-1] != "[":
                        print("no")
                        break
                    else:
                        stack.pop()
                else:
                    continue
            else:
                print("yes") if len(stack) == 0 else print("no")


if __name__ == "__main__":
    s = Solution()
    s.solution()

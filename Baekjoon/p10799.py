import sys
class Solution:
    def solution(self):
        operation = sys.stdin.readline().strip()
        answer = 0
        stack = 0
        for i in range(len(operation)):
            if operation[i] == ")":
                if operation[i-1] == "(":
                    answer += stack
                else:
                    answer += 1
                    stack -= 1
            else:
                if operation[i+1] == "(":
                    stack += 1
        print(answer)


if __name__ == '__main__':
    s = Solution()
    s.solution()
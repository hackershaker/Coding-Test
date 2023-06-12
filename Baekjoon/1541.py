import sys


class Solution:
    def solution(self):
        expression = sys.stdin.readline().strip()
        expression = expression.split("-")

        answer = self.eval_custom(expression[0])
        for i in range(1, len(expression)):
            answer -= self.eval_custom(expression[i])

        print(answer)
        return answer

    def eval_custom(self, exp: str):
        exp = exp.split("+")
        answer = 0
        for num in exp:
            answer += int(num)
        return answer


if __name__ == "__main__":
    s = Solution()
    s.solution()

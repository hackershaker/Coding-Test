class Solution:
    def calculate(self, s: str) -> int:
        answer = 0
        tempop = '+'
        stack = []
        temp = '0'
        for op in s:
            if op.isnumeric():
                temp += op
            else:
                answer += self.tempOpConvert(tempop) * int(temp)
                temp = '0'
    
                if op == '+' or op == '-':
                    tempop = op
                if op == '(':
                    stack.extend([answer, tempop])
                    tempop = "+"
                    answer = 0
                if op == ')':
                    o = stack.pop()
                    lastAnswer = stack.pop()
                    answer = lastAnswer + self.tempOpConvert(o) * answer
            print(answer, stack)
        else:
            while stack:
                o = stack.pop()
                lastAnswer = stack.pop()
                answer = lastAnswer + self.tempOpConvert(o) * answer

            if temp: answer += self.tempOpConvert(tempop) * int(temp)

        return answer

    def tempOpConvert(self, tempop):
        return -1 if tempop == "-" else 1
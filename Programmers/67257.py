import re
from itertools import permutations
def solution(expression):
    answer = 0; operator = set()
    temp = re.findall("(\d*)([*\-+])", expression)
    temp.append(re.findall("(\d+)$", expression))
    exp = []
    for t in temp:
        for el in t:
            exp.append(el)
    for i in range(len(exp)):
        if i % 2 == 1: operator.add(exp[i])
        
    def calculate(op, expression):
        if len(op) == 0:
            return int(expression[0])
        while True:
            for j in range(1, len(expression), 2):
                if op[0] == expression[j]:
                    if op[0] == "+":
                        temp = int(expression[j-1]) + int(expression[j+1])
                        del expression[j+1]
                        del expression[j]
                        expression[j-1] = temp
                        break
                    if op[0] == "*":
                        temp = int(expression[j-1]) * int(expression[j+1])
                        del expression[j+1]
                        del expression[j]
                        expression[j-1] = temp
                        break
                    if op[0] == "-":
                        temp = int(expression[j-1]) - int(expression[j+1])
                        del expression[j+1]
                        del expression[j]
                        expression[j-1] = temp
                        break
            else:
                return calculate(op[1:], expression)

    for o in permutations(operator):
        # print(o)
        tempexp = exp[:]
        result = calculate(o, tempexp)
        # print(result, exp)
        answer = max(answer, abs(result))
    
    return answer

print(solution(	"100-200*300-500+20"))
print(solution("50*6-3*2"))
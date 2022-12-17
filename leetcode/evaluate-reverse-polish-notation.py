# stack 이용
# tokens의 원소를 하나씩 저장
# stack의 마지막 원소가 기호면 그 전 2개의 원소를 이용해 연산
# 연산 결과를 stack에 저장
# stack이 비면 반환
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if self.isInt(token):
                stack.append(int(token))
            else:
                b, a = stack.pop(), stack.pop()
                if token == "+": stack.append(a+b)
                elif token == "-": stack.append(a-b)
                elif token == "*": stack.append(a*b)
                else: stack.append(int(a/b))

        return stack[0]

    def isInt(self, x):
        try:
            x = int(x)
            return True
        except:
            return False
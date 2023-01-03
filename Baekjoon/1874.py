# pushNum = 마지막으로 push한 숫자
# 입력값이 들어왔을 때 pushNum보다 크면 
# 입력값까지 stack에 push 후 pop
# 작거나 같을 경우 stack 제일 위에 있는 값이 입력값과 같은지 검사
# print함수를 쓰면 느리므로 sys.stdout.write 함수를 쓸 것(개행 처리해주어야 함)


import sys


def solution():
    n = int(input())
    answer = []

    pushNum = 0
    stack = []
    for _ in range(n):
        k = int(input())

        if k > pushNum:
            for num in range(pushNum+1, k+1):
                stack.append(num)
                answer.append("+")
            pushNum = k

        if stack[-1] != k:
            return "NO"
        else:
            stack.pop()
            answer.append("-")

    return answer

if __name__=="__main__":
    print = sys.stdout.write
    answer = solution()

    if type(answer) == str:
        print(answer)
    else:
        for a in answer: print(a+"\n")
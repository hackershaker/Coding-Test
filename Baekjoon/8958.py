def solution(s):
    stack = []
    answer = 0
    for result in s:
        if result == "O":
            stack.append("O")
            answer += len(stack)
        else:
            stack = []
    print(answer)
    return answer

if __name__=="__main__":
    T = int(input())

    for _ in range(T):
        solution(input())
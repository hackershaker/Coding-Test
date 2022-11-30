from collections import deque
def solution():
    answer = 0
    n = int(input())
    stairs = [int(input()) for _ in range(n)]

    stack = deque([[[1], stairs[0]], [[2], stairs[1]]])
    while stack:
        steps, total= stack.popleft()
        print(steps, total)
        if steps[-1] > n: continue
        if steps[-1] == n:
            answer = max(answer, total)
            continue
        
        if len(steps) == 1 or (len(steps) > 2 and not(steps[-1] - steps[-2] == 1)):
            stack.append([steps[-2:] + [steps[-1]+1], total+stairs[steps[-1]]])
        if steps[-1]+2 <= n:
            stack.append([steps[-2:] + [steps[-1]+2], total+stairs[steps[-1]+1]])

    return answer

if __name__=="__main__":
    answer = solution()
    print(answer)